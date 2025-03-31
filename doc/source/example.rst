*******
Example
*******

This page is hand-written, and contains examples of cross-referencing the regmap
proper, which is auto-generated.

.. note::
  All node names in the example RDL are IN CAPS. That's just a convention where
  I work, you're free to use mixed case.

Referencing
===========

The top level addrmap is named ``FOOBAR`` in the RDL, so we can do
:code:`:regmap:`FOOBAR\`` to refer to :regmap:`FOOBAR`.

.. code-block:: rst

  - It has sub addrmaps :regmap:`FOOBAR.R1` and :regmap:`FOOBAR.R2`.
  - R1 has a register :regmap:`FOOBAR.R1.PLL_EN`.
  - Referring to non-existent :regmap:`FOOBAD.R1` should generate a warning, and not give us a link.

Referring to everything hierarchically is getting annoying, so let's set the context:

.. code-block::

  .. regmap-context:: "FOOBAR.R1"

  - R1 has a register :regmap:`PLL_EN`, with field :regmap:`PLL_EN.EN` etc.
  - We can use the ``Text <Target>`` markup to change the text: :regmap:`PLL enable register <PLL_EN>`.

.. regmap-context:: FOOBAR.R1

- R1 has a register :regmap:`PLL_EN`, with field :regmap:`PLL_EN.EN` etc.
- We can use the ``Text <Target>`` markup to change the text: :regmap:`PLL enable register <PLL_EN>`.


Regmap
======

.. toctree::

  regmap



