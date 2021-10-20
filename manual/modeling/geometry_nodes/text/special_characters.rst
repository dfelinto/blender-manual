.. index:: Geometry Nodes; Special Characters
.. _bpy.types.FunctionNodeInputSpecialCharacters:

***********************
Special Characters Node
***********************


.. figure:: /images/modeling_geometry-nodes_text_special-characters_node.png
   :align: center

   The Special Characters node.

The *Special Characters* node is used to output string characters that can't be typed directly with the keyboard.

.. tip::

   This node can be used to create a multiline string for
   the :doc:`String to Curves </modeling/geometry_nodes/text/string_to_curves>` node,
   when combined with the :doc:`Join Strings </modeling/geometry_nodes/text/join_strings>` node.


Inputs
======

This node has no inputs.


Properties
==========

This node has no properties.


Outputs
=======

Line Break
   A new line character (escape character ``\n``).

Tab
   A tab character used to add an indentation in the output.
