.. index:: Geometry Nodes; Boolean Math
.. _bpy.types.FunctionNodeBooleanMath:

*****************
Boolean Math Node
*****************

.. figure:: /images/modeling_geometry-nodes_utilities_boolean-math_node.png
   :align: right
   :alt: Boolean Math Node.

The *Boolean Math* node performs a basic logical operation on its inputs.


Inputs
======

Boolean
   Two standard Boolean inputs.


Properties
==========

Mode
   :AND:
      True when both inputs are true.
      (`AND <https://en.wikipedia.org/wiki/AND_gate>`__)
   :OR:
      True when at least one input is true.
      (`OR <https://en.wikipedia.org/wiki/OR_gate>`__)
   :NOT:
      Opposite of the input.
      (`NOT <https://en.wikipedia.org/wiki/NOT_gate>`__)
   :NAND:
      (True when at least one input is false.
      `NAND <https://en.wikipedia.org/wiki/NAND_gate>`__)
   :NOR:
      True when both inputs are false.
      (`NOR <https://en.wikipedia.org/wiki/NOR_gate>`__)
   :EQV:
      True when both inputs are equal. Also known as "exclusive nor".
      (`XNOR <https://en.wikipedia.org/wiki/XNOR_gate>`__)
   :NEQV:
      (`XOR <https://en.wikipedia.org/wiki/XOR_gate>`__)
      True when both inputs are different. Also known as "exclusive or".
   :IMPLY:
      True unless the first input is true and the second is false.
      (`IMPLY <https://en.wikipedia.org/wiki/IMPLY_gate>`__)
   :NIMPLY:
      True when the first input is true and the second is false. Also known as ""not imply".
      (`NIMPLY <https://en.wikipedia.org/wiki/NIMPLY_gate>`__)



Output
======

Boolean
   Standard Boolean output.
