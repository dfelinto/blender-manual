.. _bpy.types.CompositorNodeConvertColorSpace:

****************
Color Space Node
****************

.. figure:: /images/compositing_node-CompositorNodeConvertColorSpace.png
   :align: right

   Color Space Node.

The *Color Space Node* converts images from one :term:`color spaces <Color Space>`.

.. note::

    Images are automatically converted into linear color space unless specified in the image's
    :ref:`Colorspace <bpy.types.ColorManagedInputColorspaceSettings.name>` option.


Inputs
======

Image
   Standard color input.


Properties
==========

From, To
   The color space of the input image and the color space to convert the image to.

   The list of color spaces depends on the active :ref:`OCIO config <ocio-config>`.
   Using the default config will list the following options:

   :sRGB: Standard RGB display space.
   :Linear: Linear 709 (full range). Blender native linear space.
   :Linear ACES: ACES linear space.
   :XYZ: Standard linear XYZ space.
   :Non-Color: Color space used for images which contains non-color data (e.g. normal maps).
   :Raw: Does not automatically convert to linear; same as Non-Color.
   :Filmic Log: Intermediate log color space of Filmic view transform.


Outputs
=======

Image
   Standard color output.
