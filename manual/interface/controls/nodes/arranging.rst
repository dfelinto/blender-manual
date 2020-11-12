
***************
Arranging Nodes
***************

Snapping
========

Snap
   Toggle snapping mode for moving nodes around.
Snap Node Element Selector
   This selector provide the following node elements for snap:

   :Grid: Snap to grid background.
   :Node X: Snap to left/right node border.
   :Node Y: Snap to top/bottom node border.
   :Node X/Y: Snap to any node border.

Snap Target
   Which part to snap onto the target.

   :Closest: Snap closest point onto target.
   :Center: Snap center onto target.
   :Median: Snap median onto target.
   :Active: Snap active onto target.


.. _editors-nodes-usage-auto-offset:

Auto-Offset
===========

When you drop a node with at least one input and one output socket onto an existing connection between two nodes,
*Auto-offset* will, depending on the direction setting, automatically move the left or right node away to make room
for the new node.
*Auto-offset* is a feature that helps organizing node layouts interactively without interrupting the user workflow.

.. figure:: /images/interface_controls_nodes_arranging_auto-offset.png

Auto-offset is enabled by default, but it can be disabled from the editor's header.

You can toggle the offset direction while you are moving the node by pressing :kbd:`T`.

The offset margin can be changed using the *Auto-offset Margin*
setting in the editing section of the Preferences.

.. seealso:: Example Video:

   `Auto-Offset. A workflow enhancement for Blender's node editors <https://vimeo.com/135125839>`__.
