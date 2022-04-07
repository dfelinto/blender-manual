.. index:: Geometry Nodes; Switch
.. _bpy.types.GeometryNodeSwitch:

***********
Switch Node
***********

.. figure:: /images/node-types_GeometryNodeSwitch.webp
   :align: right
   :alt: Switch Node.

The *Switch* node outputs one of two inputs depending on a condition.
Only the input that is passed through the node is computed.


Inputs
======

Switch
   Determines which of the two inputs below will be passed through.

False
   Is passed through when the switch is set to false.

True
   Is passed through when the switch is set to true.


Properties
==========

Type
   Determines the type of the data that is handled by the node.


Outputs
=======

Output
   One of the two inputs without any modifications.
