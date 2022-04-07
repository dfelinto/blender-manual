.. _bpy.types.CompositorNodeViewer:

***********
Viewer Node
***********

.. figure:: /images/compositing_node-types_CompositorNodeViewer.webp
   :align: right
   :alt: Viewer Node.

The *Viewer* node is a temporary, in-process viewer.
It can be plug in anywhere to inspect an image or value map in your node tree.

Select a view node with :kbd:`LMB` to switch between multiple viewer nodes.
It is possible to automatically plug any other node into a Viewer node
by pressing :kbd:`Shift-Ctrl-LMB` on it.


Inputs
======

See :doc:`Composite Node </compositing/types/output/composite>`.


Properties
==========

Tile Order
   The tile order can be defined for the backdrop image, using the *Tile order* field in the properties of
   the Viewer node (*Properties* panel in Sidebar region, with the Viewer node selected):

   Rule of thirds
      Calculates tiles around each of the nine zones defined by the *rule of thirds*.
   Bottom up
      Tiles are calculated from the bottom up.
   Random
      Calculates tiles in a non-specific order.
   Center
      Calculates the tiles around a specific center, defined by X and Y fields.

      X, Y


Outputs
=======

This node has no output sockets.

.. note::

   It is possible to add multiple Viewer nodes, though only the active one
   (last selected, indicated by a red header) will be shown on the backdrop or in the Image editor.


Using the Image Editor
======================

The Viewer node allows results to be displayed in the Image Editor.
The image is facilitated in the header by selecting *Viewer Node* in the linked *Image* data-block menu.
The Image Editor will display the image from the currently selected Viewer node.

To save the image being viewed,
use :menuselection:`Image --> Save As...`, :kbd:`Alt-S` to save the image to a file.

The Image Editor also has three additional options in its header to view Images with or
without Alpha, or to view the Alpha or Z itself.
Click and holding the mouse in the Image displayed allows you to sample the values.
