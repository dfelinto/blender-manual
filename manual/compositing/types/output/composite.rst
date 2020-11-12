.. _bpy.types.CompositorNodeComposite:

**************
Composite Node
**************

.. figure:: /images/compositing_node-types_CompositorNodeComposite.png
   :align: right

   Composite Node.

The Composite node is where the actual output from the Compositor
is connected to the renderer.
This node is updated after each render, but also reflects changes in the node tree
(provided at least one finished input node is connected).


Inputs
======

Connecting a node to the Composite node will output the result of the prior
tree of that node to the Compositor.

Image
   RGB image. The default is black, so leaving this node unconnected will result in a black image.
Alpha
   Alpha channel.
Z
   Z depth.


Properties
==========

Use Alpha
   Used alpha channel, colors are treated alpha *premultiplied*.
   If disabled, alpha channel gets set to 1,
   and colors are treated as alpha *straight*, i.e. color channels does not change.


Outputs
=======

This node has no output sockets.

.. note::

   If multiple Composite nodes are added, only the active one
   (last selected, indicated by a red header) will be used.
