
***************
Arranging Nodes
***************

Snapping
========

.. _bpy.types.ToolSettings.use_snap_node:

The snapping options can be found on the rightmost side
of the node editor's header.

Snap
   Toggle snapping on or off.

Snap Node Element
   What to snap the selected nodes to:

   :Grid: Snap to the grid in the background.
   :Node X: Snap to the X coordinate of another node's vertical border.
   :Node Y: Snap to the Y coordinate of another node's horizontal border.
   :Node X/Y: Combination of the above.

Snap Target
   Which part of the selected nodes to snap:

   :Closest: Snap closest point onto target.
   :Center: Snap center of selected nodes onto target.
   :Median: Snap median of selected nodes onto target.
   :Active: Snap active node onto target.


.. _editors-nodes-usage-auto-offset:

Auto-Offset
===========

When you drop a node with at least one input and one output socket onto an existing connection between two nodes,
*Auto-offset* will, depending on the direction setting, automatically move the left or right node away to make room
for the new node.
*Auto-offset* is a feature that helps organizing node layouts interactively without interrupting the user workflow.

.. figure:: /images/interface_controls_nodes_arranging_auto-offset.png

Auto-offset is enabled by default, but it can be disabled from the editor's View menu.

You can toggle the offset direction while you are moving the node by pressing :kbd:`T`.

The offset margin can be changed using the *Auto-offset Margin*
setting in the Editing section of the Preferences.

.. seealso:: Example Video:

   `Auto-Offset. A workflow enhancement for Blender's node editors <https://vimeo.com/135125839>`__.
