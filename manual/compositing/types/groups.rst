.. _bpy.types.CompositorNodeGroup:
.. Editors Note: This page gets copied into:
   - :doc:`/editors/texture_node/types/groups`
   - :doc:`/modeling/geometry_nodes/group`
   - :doc:`/render/shader_nodes/groups`
.. --- copy below this line ---

*****
Group
*****

:doc:`Group Nodes </interface/controls/nodes/groups>` are a collection of nodes
that can be combined into a single node while selectively exposing inputs of the embedded nodes.
Group nodes can simplify a node tree by allowing instancing and hiding parts of the tree.


Make Group
==========

Creates a node group from the selected nodes, see :ref:`bpy.ops.node.group_make` for more information.


Ungroup
=======

Removes the selected nodes from a group, see :ref:`bpy.ops.node.group_ungroup` for more information.


Group Input
===========

Adds a group input node, this serves as a convenient way to re-add the input node in case it is accidentally deleted.
Note, groups can only have one input/output, if more than one is added they are essentially duplicates of each other.


Group Output
============

Adds a group output node, this serves as a convenient way to re-add the output node in case it is accidentally deleted.
Note, groups can only have one input/output, if more than one is added they are essentially duplicates of each other.


Node Groups
===========

This section lists all the node groups either from the current blend-file or
:doc:`Linked or Appended </files/linked_libraries/link_append>` from another blend-file.
