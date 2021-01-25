.. _bpy.types.CompositorNodeGroup:
.. Editors Note: This page gets copied into:
   - :doc:`/editors/texture_node/types/groups`
   - :doc:`/render/shader_nodes/groups`
.. --- copy below this line ---

*****
Group
*****

:doc:`Group Nodes </interface/controls/nodes/groups.rst>` are a collection of nodes
that can be combined into a single node while selectively exposing inputs of the embedded nodes.
Group nodes can simplify a node tree by allowing instancing and hiding parts of the tree.


Make Group
==========

Creates a node group from the selected nodes, see :ref:`bpy.ops.node.group_make` for more information.


Ungroup
=======

Removes the selected nodes from a group, see :ref:`bpy.ops.node.group_ungroup` for more information.


Node Groups
===========

This section lists all the node groups either from the current blend-file or
:doc:`Linked or Appended </files/linked_libraries/link_append>` from another blend-file.
