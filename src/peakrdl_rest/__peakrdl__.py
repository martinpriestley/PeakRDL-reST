"""PeakRDL ReStructuredText plug-in."""

__authors__ = [
    "Martin Priestley <martin@rainlabs.ai>",
]

from typing import TYPE_CHECKING

from peakrdl.plugins.exporter import ExporterSubcommandPlugin  # type: ignore

from .exporter import RestExporter

if TYPE_CHECKING:
    import argparse
    from typing import Union

    from systemrdl.node import AddrmapNode, RootNode  # type: ignore


class Exporter(ExporterSubcommandPlugin):
    """PeakRDL ReStructuredText exporter plug-in."""

    short_desc = "Generate ReStructuredText documentation"
    long_desc = "Export the register model to ReStructuredText"

    def add_exporter_arguments(self, arg_group: "argparse._ActionsContainer"):  # type: ignore
        """Add PeakRDL exporter arguments."""
        arg_group.add_argument(
            "-d",
            "--diagrams",
            default=False,
            action="store_true",
            help="Generate sphinxcontrib-bitfields diagram for each register",
        )

    def do_export(
        self, top_node: "Union[AddrmapNode, RootNode]", options: "argparse.Namespace"
    ):
        """Perform the export of SystemRDL node to ReStructuredText.

        Arguments:
            top_node -- top node to export.
            options -- argparse options from the `peakrdl` tool.
        """
        RestExporter().export(
            top_node,
            options.output,
            bitfield_diagrams = options.diagrams
        )
