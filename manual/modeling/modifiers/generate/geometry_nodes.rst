.. index:: Modeling Modifiers; Geometry Nodes Modifier
.. _bpy.types.NodesModifier:

***********************
Geometry Nodes Modifier
***********************

The *Geometry Nodes* modifier creates a modifier with a node group which defines its functionality.

.. figure:: /images/modeling_modifiers_generate_geometry-nodes_panel.png

   A new Geometry Nodes modifier with a new node group.


Options
=======

Node Group
   A :doc:`Node Group </interface/controls/nodes/groups>` with the geometry input and output.
   Those are respectively what is received and passed to the previous and next modifier in the stack.
   See :doc:`Nodes </modeling/geometry_nodes/index>` for all available nodes.
Inputs
   A list of the node group's inputs which can have unique values even
   if the group is shared among multiple modifiers.
