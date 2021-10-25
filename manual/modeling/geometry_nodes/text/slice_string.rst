.. index:: Geometry Nodes; Slice String
.. _bpy.types.GeometryNodeStringSubstring:

*****************
Slice String Node
*****************

.. figure:: /images/modeling_geometry-nodes_text_string-substring_node.png
   :align: center

   The Slice String node.

The *Slice String* node extracts a string segment from a larger string.


Inputs
======

String
   String value to be sliced.

Position
   Integer value used to determine the starting point of the new string within the input string.
   The first letter of the string is at index 0.

Length
   Integer value used to determine how many characters are extracted from the input string.


Properties
==========

This node has no properties.


Outputs
=======

String
   String value of the extracted substring.
