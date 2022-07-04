.. _bpy.types.NodeGroup:

***********
Node Groups
***********

.. figure:: /images/interface_controls_nodes_groups_example.png
   :align: right

   Example of a node group.

Grouping nodes can simplify a node tree by hiding away complexity and reusing repetitive parts.

Conceptually, node groups allow you to treat a *set* of nodes as though it were just one node.
They're similar to functions in programming:
they can be reused (even in different node trees) and can be customized by changing their "parameters."

As an example, say you created a "Wood" material that you would like to have in different colors.
One way of doing this would be to duplicate the entire material for every color, but if you did that,
you'd have to go over all those copies again if you later wanted to change the density of the grain lines.
Instead, it would be better to move the nodes that define the wood look into a node group.
Each material can then reuse this node group and just supply it with a color.
If you then later want to change the grain line density, you only have to do it once inside the node group,
rather than for every material.

Node groups can be nested (that is, node groups can contain other node groups).

.. note::

   Recursive node groups are prohibited for all the current node systems to prevent infinite recursion.
   A node group can never contain itself (or another group that contains it).


Interface
=========

When a node group is created, new *Group Input* and *Group Output* nodes are generated
to represent the data flow into and out of the group. Furthermore connections to input sockets coming
from unselected nodes will become attached to new sockets on the *Group Input* node.
Similarly, outgoing connections to input sockets of unselected nodes will become attached to
the new *Group Output* node.

If you want to pass an additional parameter into the group,
a socket must be added to the *Group Input* node.
To do this, drag a connection from the hollow socket on the right side of the *Group Input* node
to the desired input socket on the node requiring an input.
The process is similar for the *Group Output* regarding data
you want to be made available outside the group.


.. _bpy.ops.node.tree_socket_add:
.. _bpy.ops.node.tree_socket_remove:
.. _bpy.ops.node.tree_socket_move:

Sidebar
-------

.. reference::

   :Panel:     :menuselection:`Sidebar --> Group --> Inputs`, :menuselection:`Sidebar --> Group --> Outputs`

.. figure:: /images/interface_controls_nodes_groups_interface-panel.png
   :align: right

   The interface panel for editing groups.

The Sidebar lets you add, remove, reorder, and edit the sockets of the group's input and output nodes.

.. _bpy.types.NodeSocketInterface.name:

Name
   The name of the socket to display in the node's interface.

.. _bpy.types.NodeSocketInterface.description:

Tooltip
   The message displayed when hovering over socket properties.
   Currently only supported for :doc:`Geometry Node Editor </editors/geometry_node>`.

.. _bpy.types.NodeSocketInterface*.default_value:

Default
   The value to use when nothing is connected to the socket.

.. _bpy.types.NodeSocketInterface*.min_value:
.. _bpy.types.NodeSocketInterface*.max_value:

Min, Max
   The minimum and maximum value for the UI button shown in the node interface.
   Note, this is not a minimum or maximum for the data that can pass through the node.
   If a socket passes a higher value than the maximum, it will still pass into the node unchanged.

.. _bpy.types.NodeSocketInterface.hide_value:

Hide Value
   Hide the socket value even when the socket is not connected.


.. _bpy.ops.node.tree_path_parent:

Edit Group
==========

.. reference::

   :Menu:      :menuselection:`Node --> Edit Group`
   :Header:    :menuselection:`Go to Parent Node Tree`
   :Shortcut:  :kbd:`Tab`, :kbd:`Ctrl-Tab`

With a node group selected, press :kbd:`Tab` to move into it and see its content.
Press :kbd:`Tab` again (or :kbd:`Ctrl-Tab`) to leave the group and go back to
its parent, which could be the top-level node tree or another node group.
You can refer to the breadcrumbs in the top left corner of the node editor
to see where you are in the hierarchy.

.. figure:: /images/render_cycles_optimizations_reducing-noise_glass-group.png
   :width: 620px

   Example of an expanded node group.


.. _bpy.ops.node.group_make:

Make Group
==========

.. reference::

   :Menu:      :menuselection:`Node --> Make Group`
   :Shortcut:  :kbd:`Ctrl-G`

To create a node group, select the nodes you want to include, then
press :kbd:`Ctrl-G` or click :menuselection:`Group --> Make Group`.
A node group will have a green title bar. All selected nodes will now be contained within the node group.
Default naming for the node group is "NodeGroup", "NodeGroup.001" etc.
There is a name field in the node group you can click into to change the name of the group.
Change the name of the node group to something meaningful.

When appending node groups from one blend-file to another,
Blender does not make a distinction between material node groups or composite node groups.
So it is recommended to use some naming convention that will allow you to distinguish between the two types.

.. tip::

   The "Add" menu of each node editor contains an "Output" category with node types such as "Material Output."
   These node types should not be confused with the "Group Output" node found in node groups,
   and should not be used in node groups either (only in the top-level node tree).


.. _bpy.ops.node.group_ungroup:

Ungroup
=======

.. reference::

   :Menu:      :menuselection:`Node --> Ungroup`
   :Shortcut:  :kbd:`Ctrl-Alt-G`

Removes the group and places the individual nodes into your editor workspace.
No internal connections are lost, and now you can link internal nodes to other nodes in your workspace.

Separate :kbd:`P`
   Separate selected nodes from the node group.

   Copy
      Copy to parent node tree, keep group intact.
   Move
      Move to parent node tree, remove from group.


.. _bpy.ops.node.group_insert:

Group Insert
============

.. reference::

   :Menu:      :menuselection:`Node --> Group Insert`

.. move node into selected group

Selecting a set of nodes, ending with the destination group node,
and pressing :menuselection:`Node --> Group Insert` will move those nodes into that group.
The moved nodes are collected into a group of their own to preserve their connection context,
having their own group input and output nodes.
The group's existing input and output nodes are updated with new sockets, if any, from the new nodes.
The node group must be edited to contain a single *Group Input* and a single *Group Output* node.


Reusing Node Groups
===================

.. reference::

   :Menu:      :menuselection:`Add --> Group`
   :Shortcut:  :kbd:`Shift-A`

Existing node groups can be placed again after they're initially defined, be it in the same
node tree or a different one. It's also possible to import node groups from a different blend-file
using :menuselection:`File --> Link/Append`.
