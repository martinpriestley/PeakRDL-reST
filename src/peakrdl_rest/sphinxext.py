from docutils import nodes
from sphinx import addnodes
from sphinx.util import logging
from sphinx.util.docutils import SphinxDirective, ReferenceRole

log = logging.getLogger(__name__)

# Global variable to store the current regmap context
current_regmap_context = None

class RegmapRole(ReferenceRole):
    """
    Custom role for linking to register map definitions.
    """

    def run(self):
        # Infer the label from the target
        global current_regmap_context
        reftext = self.target
        if current_regmap_context:
            reftext = f"{current_regmap_context}.{self.target}"

        label = f"regmap__{reftext.replace('.', '__')}"
        label = label.lower() # All labels are forced to lowercase

        text = self.title if self.has_explicit_title else self.target
        innernode = nodes.inline('', text)

        # Create a pending_xref node
        refnode = addnodes.pending_xref(
            '',
            innernode,
            refdomain='std',
            reftype='ref',
            reftarget=label,
            refwarn=True,
            refexplicit=True,
        )

        return [refnode], []


class RegmapContextDirective(SphinxDirective):
    """
    A directive to set the context for the regmap role.
    """

    has_content = False
    required_arguments = 1

    def run(self):
        """
        Set the regmap context, so that subsequent :regmap: roles
        will use this context as a prefix.
        """
        global current_regmap_context

        # The argument is expected to be the context, e.g., FOO
        context = self.arguments[0]
        current_regmap_context = context

        return []


def clear_context(app, docname, source):
    """
    Clear the regmap context each time a new source is read. This means the
    regmap-context directive only has effect until the end of the page on which
    it's invoked.
    """
    global current_regmap_context
    current_regmap_context = None


def setup(app):
    """
    Set up the Sphinx extension, registering the `:regmap:` role and `regmap-context` directive.

    Args:
        app: The Sphinx application instance.
    """
    # Add the `regmap` role
    app.add_role('regmap', RegmapRole())

    # Add the `regmap-context` directive
    app.add_directive('regmap-context', RegmapContextDirective)

    app.connect('source-read', clear_context)

    # Optional: Log that the extension has been loaded
    log.info("Sphinx regmap extension with context loaded.")
