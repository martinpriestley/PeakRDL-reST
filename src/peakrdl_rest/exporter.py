"""PeakRDL ReStructuredText exporter."""

# TODO:
# - enum encoding as field reset value in table
# - Calculate how many leading 0's to put on addresses in a more
#   context-sensitive manner
# - Muti-page output??
# - Text fields that include RDL markup should really get translated to rst

__authors__ = [
    "Martin Priestley <martin@rainlabs.ai>",
]

import json

from functools import reduce
from operator import mul
from pathlib import Path
from typing import List, Optional, Union
from rstcloth import RstCloth

from systemrdl.messages import MessageHandler  # type: ignore
from systemrdl.node import (  # type: ignore
    AddressableNode,
    AddrmapNode,
    FieldNode,
    MemNode,
    Node,
    RegfileNode,
    RegNode,
    RootNode,
)
from systemrdl.rdltypes.user_enum import UserEnum

class RestExporter:

    def hex(self, value:int):
        return f"0x{value:0{self._max_hexwidth}X}"

    HEADING_STYLES = {
        1 : (True, "#"),
        2 : (True, "*"),
        3 : (False, "="),
        4 : (False, "-"),
        5 : (False, "^"),
        6 : (False, '"'),
        7 : (False, '~'),
        8 : (False, '='),
        9 : (False, '>'),
        10 : (False, '<'),
    }

    def _heading(self, level: int, title: str, label: Optional[str] =None):
        """Generate ReST heading for the given level"""
        if label:
            self.doc.ref_target(label)
            self.doc.newline()

        (overline, char) = self.HEADING_STYLES[level]

        self.doc.heading(text=title, char=char, overline=overline)
        self.doc.newline()

    def _node_label(self, node: Node):
        """Generate a unique label for a node for cross-referencing"""
        path = node.get_path(hier_separator='__', empty_array_suffix='')
        return "regmap__" + path

    def _node_name(self, node):
        suffix = ""
        if hasattr(node, "is_array"):
            if node.is_array:
                suffix = "[]"
        return node.inst_name + suffix

    def _node_heading(self, level: int, node: Node):
        node_type = self._get_node_type(node)
        node_name = self._node_name(node)
        title = f"{node_type} {node_name}"
        self._heading(level, title, label=self._node_label(node))

    def _addressable_info(self, node: AddressableNode, level: int):
        # If we're describing an array of registers, point at the [0] instance.
        # TODO - presumably this breaks with multidimensional arrays
        set_index = False
        if node.is_array and node.current_idx is None:
            node.current_idx = [0]
            set_index = True

        self.doc.field(name="Absolute Address", value=self.hex(node.absolute_address))
        self.doc.field(name="Base Offset", value=self.hex(node.raw_address_offset))
        if node.is_array and node.array_dimensions is not None:
            size = node.size * reduce(mul, node.array_dimensions, 1)
            self.doc.field(name="Size", value=self.hex(size))
        else:
            self.doc.field(name="Size", value=self.hex(node.size))

        if node.is_array:
            self.doc.field(name="Array Dimensions", value=str(node.array_dimensions))
            self.doc.field(name="Array Stride", value=self.hex(node.array_stride))
            self.doc.field(name="Total Size", value=self.hex(node.total_size))

        desc = node.get_property("desc")
        if desc is not None:
            self.doc.field(name="Description", value=desc)

        self.doc.newline()

        if set_index:
            node.current_idx = None

    def _get_node_type(self, node):
        if isinstance(node, AddrmapNode):
            return "AddressMap"
        elif isinstance(node, RegfileNode):
            return "Regfile"
        elif isinstance(node, MemNode):
            return "Memory"
        elif isinstance(node, RegNode):
            return "Register"
        elif isinstance(node, FieldNode):
            return "Field"

        logger.warning(f"Unknown node type {type(node)}")
        return "Node"

    def _convert_addrmap(self, node: AddressableNode, level: int):
        self._node_heading(level, node)
        self._addressable_info(node, level)

        # Table of direct children
        headers = ["Offset", "Identifier", "Name"]
        table = []
        for child in node.children(unroll=False):
            name = child.get_html_name() or ""
            ref = self._node_label(child)
            table.append([
                self.hex(child.raw_address_offset),
                f":ref:`{self._node_name(child)}<{ref}>`",
                name,
            ])

        if table:
            self.doc.table(headers, table)

        # Descend through child nodes
        for child in node.children(unroll=False):
            if isinstance(child, (AddrmapNode, RegfileNode, MemNode)):
                self._convert_addrmap(child, level+1)
            elif isinstance(child, RegNode):
                self._convert_reg(child, level+1)

    def _convert_reg(self, node: AddressableNode, level: int):
        self._node_heading(level, node)
        self._addressable_info(node, level)

        if self.do_bitfield_diagrams:
            self._bitfield_diagram(node)

        # Table of fields
        headers = ["Bits", "Identifier", "SW Access", "HW Access", "Reset", "Name"]
        table = []
        for field in node.fields():

            sw_access = field.get_property("sw").name
            if field.get_property("onread") is not None:
                access += ", " + field.get_property("onread").name
            if field.get_property("onwrite") is not None:
                access += ", " + field.get_property("onwrite").name

            hw_access = field.get_property("hw").name

            # Reset value is generally nothing or an int. If it's an int, it
            # might correspond to an enum value.
            reset = field.get_property("reset", default="-")
            if isinstance(reset, int):

                enum = field.get_property("encode")
                if enum:
                    for m in enum:
                        if m.value == reset:
                            reset = f"{hex(reset)} ({m.name})"
                            break
                else :
                    reset = hex(reset)

            # Fields only get a section to link to if they have a description or
            # enum. Otherwise, put a link to (but not from) the table for that
            # field, so external references have something to point to
            field_entry = self._node_name(field)
            label = self._node_label(field)
            if field.get_property("desc") or field.get_property("encode"):
                field_entry = f":ref:`{self._node_name(field)}<{label}>`"
            else:
                self.doc.ref_target(label)

            table.append([
                self._field_bits(field),
                field_entry,
                sw_access,
                hw_access,
                reset,
                field.get_property("name", default=""),
            ])

        self.doc.table(headers, table)

        # Field descriptions
        for field in node.fields():
            desc = field.get_property("desc")
            enum = field.get_property("encode")
            if desc or enum:
                self._node_heading(level+1, field)
            if desc:
                self.doc.content(desc)
                self.doc.newline()
            if enum:
                self._enum_table(enum)

    def _enum_table(self, enum: UserEnum):
        """Generate a table showing the encoding of an enum."""
        # TODO - enums and their members can have 'desc'
        headers = ["Enumeral", "Encoding", ""]
        table = []
        for m in enum:
            table.append([
                m.name,
                m.value,
                m.rdl_name,
            ])

        self.doc.content(f"{enum.type_name}:")
        self.doc.table(headers, table, indent=2)




    def _field_bits(self, field: FieldNode):
        if field.msb == field.lsb:
            return str(field.lsb)
        else:
            return f"{field.msb}:{field.lsb}"

    def _bitfield_type(self, field: FieldNode):
        """Pick a 'type' for a bitfield based on its access properties. A type
        just determines what colour the field is rendered in the bitfield
        diagram:

        0,1,2,8,9 : grey
        2 : red
        3 : green
        4 : cyan
        5 : peach
        6 : dark green
        7 : blue
        not specified: white with name, or grey with no name
        """

        cmap = {
            "none"    : {},
            "grey"    : {'type' : 1},
            "red"     : {'type' : 2},
            "green"   : {'type' : 3},
            "cyan"    : {'type' : 4},
            "peach"   : {'type' : 5},
            "dkgreen" : {'type' : 6},
            "blue"    : {'type' : 7},
        }

        sw_access = field.get_property("sw").name
        hw_access = field.get_property("hw").name

        if sw_access == 'r' and hw_access == 'r':
            return cmap["grey"]
        elif hw_access in ["rw", "w"]:
            return cmap["red"]
        elif sw_access == 'w':
            return cmap["green"]
        elif sw_access == 'rw':
            return cmap["cyan"]
        else:
            return cmap["none"]

    def _bitfield_diagram(self, reg: RegNode):
        """Use sphinxcontrib-bitfield to draw a bitfield diagram of a register"""

        nbits = reg.get_property("regwidth")
        bitfields = []

        for field in reg.fields(include_gaps=True):
            if isinstance(field, FieldNode):
                props = {
                    "name" : field.inst_name,
                    "bits" : field.get_property("fieldwidth"),
                }
                props.update(self._bitfield_type(field))
                bitfields.append(props)
            else:
                # This is a 'gap' where no fields are specified
                (hi, lo) = field
                bits = 1 + hi - lo
                bitfields.append({
                    "bits" : bits
                })

        self.doc.directive(
            name="bitfield",
            fields = [
                ("bits", str(nbits)),
                ("lanes", str(1)),
                ("fontsize", str(12)),
                ("caption", reg.inst_name),
            ],
            content=json.dumps(bitfields),
        )


    def export(
        self,
        node: Union[AddrmapNode, RootNode],
        output_path: str,
        bitfield_diagrams: bool =False,
    ):

        self.do_bitfield_diagrams = bitfield_diagrams

        # Get the top node.
        top = node.top if isinstance(node, RootNode) else node
        self._max_hexwidth = len(f"{top.size:X}")

        # Ensure proper format of the output path and that the directory exists.
        if not output_path.endswith(".rst"):
            raise ValueError("The output file is not ReST file.")
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)

        ofh = open(output_path, "w+")
        self.doc = RstCloth(ofh)
        self._convert_addrmap(top, 1)
        ofh.close()




