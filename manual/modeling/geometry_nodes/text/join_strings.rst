.. index:: Geometry Nodes; Join Strings
.. _bpy.types.GeometryNodeJoinStrings:

*****************
Join Strings Node
*****************

.. figure:: /images/modeling_geometry-nodes_text_join-strings_node.png
   :align: center

   The Join Strings Node.

The *Join Strings* node combines any number of input strings into the output string.
The order of the result depends on the vertical ordering of the inputs in the multi-input socket.

Optionally, the *delimiter* input is placed in between each of the input strings.

.. tip::

   This node can be used to create a multi-line string for the 
   :doc:`String to Curves </modeling/geometry_nodes/text/string_to_curves>` node, when combined with
   the line break output from the :doc:`Special Characters </modeling/geometry_nodes/text/special_characters>` node.


Inputs
======

Delimiter
   String value to place between each concatenated string.

Strings
   Mutliple String values to be combined in connection order.


Properties
==========

This node has no properties.


Outputs
=======

String
   String result of the concatenation.
