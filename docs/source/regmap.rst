.. _regmap__FOOBAR:

######
FOOBAR
######

:Absolute Address: 0x000
:Base Offset: 0x000
:Size: 0x102


+----------+-------------------------------+----------------------+
| Offset   | Identifier                    | Name                 |
+==========+===============================+======================+
| 0x000    | :ref:`R1<regmap__FOOBAR__R1>` | First regmap         |
+----------+-------------------------------+----------------------+
| 0x100    | :ref:`R2<regmap__FOOBAR__R2>` | Another register map |
+----------+-------------------------------+----------------------+

.. _regmap__FOOBAR__R1:

**
R1
**

:Absolute Address: 0x000
:Base Offset: 0x000
:Size: 0x00C
:Description: Just a collection of registers


+----------+-------------------------------------------------------+-------------+
| Offset   | Identifier                                            | Name        |
+==========+=======================================================+=============+
| 0x000    | :ref:`PLL_EN<regmap__FOOBAR__R1__PLL_EN>`             |             |
+----------+-------------------------------------------------------+-------------+
| 0x002    | :ref:`PLACEHOLDER<regmap__FOOBAR__R1__PLACEHOLDER>`   | Placeholder |
+----------+-------------------------------------------------------+-------------+
| 0x004    | :ref:`PLACEHOLDERS<regmap__FOOBAR__R1__PLACEHOLDERS>` | Placeholder |
+----------+-------------------------------------------------------+-------------+

.. _regmap__FOOBAR__R1__PLL_EN:

PLL_EN
======

:Absolute Address: 0x000
:Base Offset: 0x000
:Size: 0x002

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

EN
--

PLL enable

.. _regmap__FOOBAR__R1__PLL_EN__E_NUM:

E_NUM
-----

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

E_NUFF
------

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

F_RDL_DESC
----------

This description uses some [b]SystemRDL[/b] [i]text formatting[/i] to
format the text, for things like:  [list]   [*] Bold   [*] Italic   [*]
Lists [/list]

.. _regmap__FOOBAR__R1__PLACEHOLDER:

PLACEHOLDER
===========

:Absolute Address: 0x002
:Base Offset: 0x002
:Size: 0x002
:Description: Placeholder register

.. _regmap__FOOBAR__R1__PLACEHOLDER__unused0:

+--------+--------------+-------------+-------------+---------+--------+
| Bits   | Identifier   | SW Access   | HW Access   | Reset   | Name   |
+========+==============+=============+=============+=========+========+
| 15:0   | unused0      | r           | r           | 0x0     |        |
+--------+--------------+-------------+-------------+---------+--------+

.. _regmap__FOOBAR__R1__PLACEHOLDERS:

PLACEHOLDERS
============

:Absolute Address: 0x004
:Base Offset: 0x004
:Size: 0x008
:Array Dimensions: [4]
:Array Stride: 0x002
:Total Size: 0x008
:Description: Placeholder register

.. _regmap__FOOBAR__R1__PLACEHOLDERS__unused0:

+--------+--------------+-------------+-------------+---------+--------+
| Bits   | Identifier   | SW Access   | HW Access   | Reset   | Name   |
+========+==============+=============+=============+=========+========+
| 15:0   | unused0      | r           | r           | 0x0     |        |
+--------+--------------+-------------+-------------+---------+--------+

.. _regmap__FOOBAR__R2:

**
R2
**

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

PLACEHOLDER
===========

:Absolute Address: 0x100
:Base Offset: 0x000
:Size: 0x002
:Description: Placeholder register

.. _regmap__FOOBAR__R2__PLACEHOLDER__unused0:

+--------+--------------+-------------+-------------+---------+--------+
| Bits   | Identifier   | SW Access   | HW Access   | Reset   | Name   |
+========+==============+=============+=============+=========+========+
| 15:0   | unused0      | r           | r           | 0x0     |        |
+--------+--------------+-------------+-------------+---------+--------+

