"""PeakRDL ReStructuredText exporter."""

# TODO:
# - ref labels for every node and field
# - Optional field diagrams using sphinxcontrib-bitfield
# - Text fields that include RDL markup should really get translated to rst

__authors__ = [
    "Martin Priestley <martin@rainlabs.ai>",
]

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

class RestExporter:

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

        (overline, char) = self.HEADING_STYLES[level]

        self.doc.heading(text=title, char=char, overline=overline)
        self.doc.newline()

    def _addressable_info(self, node: AddressableNode, level: int):
        self.doc.field(name="Absolute Address", value=hex(node.absolute_address))
        self.doc.field(name="Base Offset", value=hex(node.raw_address_offset))
        if node.is_array and node.array_dimensions is not None:
            size = node.size * reduce(mul, node.array_dimensions, 1)
            self.doc.field(name="Size", value=hex(size))
        else:
            self.doc.field(name="Size", value=hex(node.size))

        if node.is_array:
            self.doc.field(name="Array Dimensions", value=str(node.array_dimensions))
            self.doc.field(name="Array Stride", value=hex(node.array_stride))
            self.doc.field(name="Total Size", value=hex(node.total_size))

        desc = node.get_property("desc")
        if desc is not None:
            self.doc.field(name="Description", value=desc)

        self.doc.newline()


    def _convert_addrmap(self, node: AddressableNode, level: int):
        self._heading(level, node.inst_name)
        self._addressable_info(node, level)

        # Table of direct children
        headers = ["Offset", "Identifier", "Name"]
        table = []
        for child in node.children(unroll=False):
            name = child.get_html_name() or ""
            table.append([
                hex(child.raw_address_offset),
                child.inst_name,
                name,
            ])

        self.doc.table(headers, table)

        # Descend through child nodes
        for child in node.children(unroll=False):
            if isinstance(child, (AddrmapNode, RegfileNode)):
                self._convert_addrmap(child, level+1)
            elif isinstance(child, MemNode):
                self._convert_mem(child, level+1)
            elif isinstance(child, RegNode):
                self._convert_reg(child, level+1)

    def _convert_reg(self, node: AddressableNode, level: int):
        self._heading(level, node.inst_name)
        self._addressable_info(node, level)

        # Table of fields
        headers = ["Bits", "Identifier", "Access", "Reset", "Name"]
        table = []
        for field in node.fields():

            access = field.get_property("sw").name
            if field.get_property("onread") is not None:
                access += ", " + field.get_property("onread").name
            if field.get_property("onwrite") is not None:
                access += ", " + field.get_property("onwrite").name

            reset = field.get_property("reset", default="-")
            if isinstance(reset, int):
                reset = hex(reset)

            table.append([
                self._field_bits(field),
                field.inst_name,
                access,
                reset,
                field.get_property("name", default="-"),
            ])

        self.doc.table(headers, table)

        # Field descriptions
        for field in node.fields():
            desc = node.get_property("desc")
            if desc:
                self._heading(level+1, field.inst_name)
                self.doc.content(desc)
                self.doc.newline()


    def _field_bits(self, field: FieldNode):
        if field.msb == field.lsb:
            return str(field.lsb)
        else:
            return f"{field.msb}:{field.lsb}"


    def export(
        self,
        node: Union[AddrmapNode, RootNode],
        output_path: str,
    ):
        # Get the top node.
        top = node.top if isinstance(node, RootNode) else node

        # Ensure proper format of the output path and that the directory exists.
        if not output_path.endswith(".rst"):
            raise ValueError("The output file is not ReST file.")
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)

        ofh = open(output_path, "w+")
        self.doc = RstCloth(ofh)
        self._convert_addrmap(top, 1)
        ofh.close()




