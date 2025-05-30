.. _regmap__FOOBAR:

#################
AddressMap FOOBAR
#################

:Absolute Address: 0x000
:Base Offset: 0x000
:Size: 0x2C0


+----------+-----------------------------------+----------------------+
| Offset   | Identifier                        | Name                 |
+==========+===================================+======================+
| 0x000    | :ref:`R1<regmap__FOOBAR__R1>`     | First regmap         |
+----------+-----------------------------------+----------------------+
| 0x100    | :ref:`R2<regmap__FOOBAR__R2>`     | Another register map |
+----------+-----------------------------------+----------------------+
| 0x200    | :ref:`MEM<regmap__FOOBAR__MEM>`   | Memory               |
+----------+-----------------------------------+----------------------+
| 0x280    | :ref:`MEM2<regmap__FOOBAR__MEM2>` | Memory with stuff    |
+----------+-----------------------------------+----------------------+

.. _regmap__FOOBAR__R1:

**********
Regfile R1
**********

:Absolute Address: 0x000
:Base Offset: 0x000
:Size: 0x00C
:Description: Just a collection of registers


+----------+---------------------------------------------------------+-------------+
| Offset   | Identifier                                              | Name        |
+==========+=========================================================+=============+
| 0x000    | :ref:`PLL_EN<regmap__FOOBAR__R1__PLL_EN>`               |             |
+----------+---------------------------------------------------------+-------------+
| 0x002    | :ref:`PLACEHOLDER<regmap__FOOBAR__R1__PLACEHOLDER>`     | Placeholder |
+----------+---------------------------------------------------------+-------------+
| 0x004    | :ref:`PLACEHOLDERS[]<regmap__FOOBAR__R1__PLACEHOLDERS>` | Placeholder |
+----------+---------------------------------------------------------+-------------+

.. _regmap__FOOBAR__R1__PLL_EN:

Register PLL_EN
===============

:Absolute Address: 0x000
:Base Offset: 0x000
:Size: 0x002

.. bitfield::
   :bits: 16
   :lanes: 1
   :fontsize: 12
   :caption: PLL_EN

   [{"name": "EN", "bits": 1, "type": 4}, {"name": "E_NUM", "bits": 2,
   "type": 4}, {"name": "E_NUFF", "bits": 2, "type": 4}, {"name":
   "F_RDL_DESC", "bits": 3, "type": 4}, {"name": "unused0", "bits": 8,
   "type": 1}]

.. _regmap__FOOBAR__R1__PLL_EN__unused0:

+--------+-----------------------------------------------------------+-------------+-------------+-------------+--------+
| Bits   | Identifier                                                | SW Access   | HW Access   | Reset       | Name   |
+========+===========================================================+=============+=============+=============+========+
| 0      | :ref:`EN<regmap__FOOBAR__R1__PLL_EN__EN>`                 | rw          | r           | 0x0         |        |
+--------+-----------------------------------------------------------+-------------+-------------+-------------+--------+
| 2:1    | :ref:`E_NUM<regmap__FOOBAR__R1__PLL_EN__E_NUM>`           | rw          | r           | 0x0 (e_foo) |        |
+--------+-----------------------------------------------------------+-------------+-------------+-------------+--------+
| 4:3    | :ref:`E_NUFF<regmap__FOOBAR__R1__PLL_EN__E_NUFF>`         | rw          | r           | 0x1 (e_bar) |        |
+--------+-----------------------------------------------------------+-------------+-------------+-------------+--------+
| 7:5    | :ref:`F_RDL_DESC<regmap__FOOBAR__R1__PLL_EN__F_RDL_DESC>` | rw          | r           | 0x0         |        |
+--------+-----------------------------------------------------------+-------------+-------------+-------------+--------+
| 15:8   | unused0                                                   | r           | r           | 0x0         |        |
+--------+-----------------------------------------------------------+-------------+-------------+-------------+--------+

.. _regmap__FOOBAR__R1__PLL_EN__EN:

Field EN
--------

PLL enable

.. _regmap__FOOBAR__R1__PLL_EN__E_NUM:

Field E_NUM
-----------

Demonstrates RDL enum

my_enum_t:

  +------------+------------+-----------------+
  | Enumeral   | Encoding   |                 |
  +============+============+=================+
  | e_foo      | 0          | foo sticks      |
  +------------+------------+-----------------+
  | e_bar      | 1          | bar tab         |
  +------------+------------+-----------------+
  | e_baz      | 2          | baz woz ere     |
  +------------+------------+-----------------+
  | e_qux      | 3          | qux like a duck |
  +------------+------------+-----------------+

.. _regmap__FOOBAR__R1__PLL_EN__E_NUFF:

Field E_NUFF
------------

my_enum_t:

  +------------+------------+-----------------+
  | Enumeral   | Encoding   |                 |
  +============+============+=================+
  | e_foo      | 0          | foo sticks      |
  +------------+------------+-----------------+
  | e_bar      | 1          | bar tab         |
  +------------+------------+-----------------+
  | e_baz      | 2          | baz woz ere     |
  +------------+------------+-----------------+
  | e_qux      | 3          | qux like a duck |
  +------------+------------+-----------------+

.. _regmap__FOOBAR__R1__PLL_EN__F_RDL_DESC:

Field F_RDL_DESC
----------------

This description uses some [b]SystemRDL[/b] [i]text formatting[/i] to
format the text, for things like:  [list]   [*] Bold   [*] Italic   [*]
Lists [/list]

.. _regmap__FOOBAR__R1__PLACEHOLDER:

Register PLACEHOLDER
====================

:Absolute Address: 0x002
:Base Offset: 0x002
:Size: 0x002
:Description: Placeholder register

.. bitfield::
   :bits: 16
   :lanes: 1
   :fontsize: 12
   :caption: PLACEHOLDER

   [{"name": "unused0", "bits": 16, "type": 1}]

.. _regmap__FOOBAR__R1__PLACEHOLDER__unused0:

+--------+--------------+-------------+-------------+---------+--------+
| Bits   | Identifier   | SW Access   | HW Access   | Reset   | Name   |
+========+==============+=============+=============+=========+========+
| 15:0   | unused0      | r           | r           | 0x0     |        |
+--------+--------------+-------------+-------------+---------+--------+

.. _regmap__FOOBAR__R1__PLACEHOLDERS:

Register PLACEHOLDERS[]
=======================

:Absolute Address: 0x004
:Base Offset: 0x004
:Size: 0x008
:Array Dimensions: [4]
:Array Stride: 0x002
:Total Size: 0x008
:Description: Placeholder register

.. bitfield::
   :bits: 16
   :lanes: 1
   :fontsize: 12
   :caption: PLACEHOLDERS

   [{"name": "unused0", "bits": 16, "type": 1}]

.. _regmap__FOOBAR__R1__PLACEHOLDERS__unused0:

+--------+--------------+-------------+-------------+---------+--------+
| Bits   | Identifier   | SW Access   | HW Access   | Reset   | Name   |
+========+==============+=============+=============+=========+========+
| 15:0   | unused0      | r           | r           | 0x0     |        |
+--------+--------------+-------------+-------------+---------+--------+

.. _regmap__FOOBAR__R2:

**********
Regfile R2
**********

:Absolute Address: 0x100
:Base Offset: 0x100
:Size: 0x002
:Description: Nothing to see here


+----------+-----------------------------------------------------+-------------+
| Offset   | Identifier                                          | Name        |
+==========+=====================================================+=============+
| 0x000    | :ref:`PLACEHOLDER<regmap__FOOBAR__R2__PLACEHOLDER>` | Placeholder |
+----------+-----------------------------------------------------+-------------+

.. _regmap__FOOBAR__R2__PLACEHOLDER:

Register PLACEHOLDER
====================

:Absolute Address: 0x100
:Base Offset: 0x000
:Size: 0x002
:Description: Placeholder register

.. bitfield::
   :bits: 16
   :lanes: 1
   :fontsize: 12
   :caption: PLACEHOLDER

   [{"name": "unused0", "bits": 16, "type": 1}]

.. _regmap__FOOBAR__R2__PLACEHOLDER__unused0:

+--------+--------------+-------------+-------------+---------+--------+
| Bits   | Identifier   | SW Access   | HW Access   | Reset   | Name   |
+========+==============+=============+=============+=========+========+
| 15:0   | unused0      | r           | r           | 0x0     |        |
+--------+--------------+-------------+-------------+---------+--------+

.. _regmap__FOOBAR__MEM:

**********
Memory MEM
**********

:Absolute Address: 0x200
:Base Offset: 0x200
:Size: 0x040
:Description: An example memory

.. _regmap__FOOBAR__MEM2:

***********
Memory MEM2
***********

:Absolute Address: 0x280
:Base Offset: 0x280
:Size: 0x040
:Description: An example memory containing registers


+----------+-----------------------------------------------------------------+-------------+
| Offset   | Identifier                                                      | Name        |
+==========+=================================================================+=============+
| 0x000    | :ref:`PLACEHOLDER_REG[]<regmap__FOOBAR__MEM2__PLACEHOLDER_REG>` | Placeholder |
+----------+-----------------------------------------------------------------+-------------+

.. _regmap__FOOBAR__MEM2__PLACEHOLDER_REG:

Register PLACEHOLDER_REG[]
==========================

:Absolute Address: 0x280
:Base Offset: 0x000
:Size: 0x008
:Array Dimensions: [4]
:Array Stride: 0x002
:Total Size: 0x008
:Description: Placeholder register

.. bitfield::
   :bits: 16
   :lanes: 1
   :fontsize: 12
   :caption: PLACEHOLDER_REG

   [{"name": "unused0", "bits": 16, "type": 1}]

.. _regmap__FOOBAR__MEM2__PLACEHOLDER_REG__unused0:

+--------+--------------+-------------+-------------+---------+--------+
| Bits   | Identifier   | SW Access   | HW Access   | Reset   | Name   |
+========+==============+=============+=============+=========+========+
| 15:0   | unused0      | r           | r           | 0x0     |        |
+--------+--------------+-------------+-------------+---------+--------+

