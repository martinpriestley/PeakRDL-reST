
.. |pkg| replace:: **PeakRDL-reST**

.. toctree::
   :hidden:
   :maxdepth: 3

   self
   example

************
PeakRDL-reST
************

Introduction
============

|pkg| is a reStructuredText documentation exporter for the `PeakRDL`_ toolchain.
In combination with `Sphinx`_ this can be used to generate register map
documentation in HTML, PDF and other formats.

Every node (addrmap, register, field) definition in the generated reST has a
`label
<https://www.sphinx-doc.org/en/master/usage/referencing.html#cross-referencing-arbitrary-locations>`_,
for easy cross-referencing from elsewhere in your documentation. To make this
even easier, |pkg| provides a sphinx extension to cross-reference nodes by
hierarchical name.

Motivation and Alternatives
---------------------------

|pkg| addresses two requirements not provided by other solutions:

  - Consistent HTML and PDF documentation
  - Easy cross-referencing from elsewhere in the documentation

It is possible to `PeakRDL-Markdown`_ with Sphinx to achieve consistent HTML and
PDF views, but there's no support for cross-referencing. At time of writing it's
also fairly feature-limited (e.g. no support for enums).

PeakRDL is bundled with an excellent `PeakRDL-HTML`_ exporter, which uses
sufficiently deterministic URLs that cross-referencing is possible\ [#fn-url]_.
If you're only looking for HTML docs this is probably the better approach. But
it's not practical for PDF output.

.. [#fn-url] I've used this approach in the past, with some custom Sphinx roles
  to reference nodes by name.

Installation
============

For now, install directly from github:

.. code-block::

  pip install git+ssh://git@github.com:RainUKLabs/PeakRDL-rest.git@main

or to bring in dependencies for rendering the bitfield :ref:`diagrams` in Sphinx:

.. code-block::

  pip install git+ssh://git@github.com:RainUKLabs/PeakRDL-rest.git[sphinxcontrib-bitfield]@main

.. todo::
  - Version tags
  - pypi releases

Usage
=====

Exporter
--------

To convert RDL to reST:

.. code-block::

  peakrdl rest [--diagrams] -o <outfile.rst> <infile(s).rdl>

and then include the reST in your document via a ``.. toctree::``.

.. note::
  You could use a ``.. include::`` directive, but then you'll have to match the
  heading styles used, and I'm not promising they won't change.

Sphinx Extension
----------------

To use the Sphinx extension, in your ``conf.py``:

.. code-block:: python

  extensions = [
      'peakrdl_rest',
      ...
  ]

And in your reST:

.. code-block:: rst

  Blah is controlled from :regmap:`MyAddrMap.MySubAddrMap.MyReg.MyField`.

  Its status can be read from :regmap:`the same register <MyAddrMap.MySubAddrMap.MyReg>`.

Or more conveniently when describing many things at the same hierarchy:

.. code-block:: rst

  .. regmap-context:: MyAddrMap.MySubAddrMap

  Blah is controlled from :regmap:`MyReg.MyField`.

The context persists until the next ``regmap-context`` directive, or the end of
the page.

Features
========

.. _diagrams:

Diagrams
--------

If the exporter is run with diagrams enabled, each register description is
preceded by a bitfield diagram generated using `sphinxcontrib-bitfield`_.

Unsupported Features
--------------------

There are likely many SystemRDL features that don't yet produce sensible output.
Some things I've not put any thought to are:

- The finer points of arrays
- Access modes beyond just read and write
- Counter and interrupt properties
- Signals
- User-defined properties

SystemRDL ``description`` and other text fields may contain text formatting
markup (defined in the `SystemRDL specification`_ Annex F). |pkg| does not
convert this to reST - the raw description is used.

Larger designs would benefit from being split across multiple pages. Perhaps
the pagination scheme of `PeakRDL-HTML`_ should be followed.

Credits
=======

Thanks to Alex Mykyta for the excellent `PeakRDL`_ / SystemRDL compiler projects.

Much inspiration was taken from Marek Pikuła's `PeakRDL-Markdown`_.



.. _SystemRDL specification: https://www.accellera.org/images/downloads/standards/systemrdl/SystemRDL_2.0_Jan2018.pdf
.. _PeakRDL: https://github.com/SystemRDL/PeakRDL-html
.. _PeakRDL-HTML: https://github.com/SystemRDL/PeakRDL-html
.. _PeakRDL-Markdown: https://github.com/SystemRDL/PeakRDL-Markdown
.. _sphinxcontrib-bitfield: https://github.com/Arth-ur/sphinxcontrib-bitfield
.. _Sphinx: https://www.sphinx-doc.org
