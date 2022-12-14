.. index:: Compositor Nodes; File Output
.. _bpy.types.CompositorNodeOutputFile:
.. _bpy.types.NodeOutputFileSlot:

****************
File Output Node
****************

.. figure:: /images/compositing_node-types_CompositorNodeOutputFile.webp
   :align: right
   :alt: File Output Node.

This node writes out an image, for each frame range specified,
to the filename entered, as part of a frameset sequence.

This node can be used as a way to automatically save the image after a render;
In addition, since this node can be hooked in anywhere in the node tree,
it can also save intermediate images automatically.


Inputs
======

Image
   The image(s) will be saved on rendering, writing to the current frame.
   An entire sequence of images will be saved, when an animation is rendered.

.. note::

   To support subsequent arrangement and layering of images, the node can supply a Z-depth map.
   However, please note that only the OpenEXR image formats save the Z information.


Properties
==========

Base Path
   Unlike the render output filepath, this node uses a base directory and an image name,
   by default the output path is composed of:
   ``{base path}/{file name}{frame number}.{extension}``.

   Besides being split into two settings, in all other respects,
   this setting is treated the same as the :ref:`render output path <bpy.types.RenderSettings.filepath>`.
File Format
   Label that shows the selected file format.

.. note::

   More options can be set in the Sidebar region.


Outputs
=======

This node has no output sockets.
