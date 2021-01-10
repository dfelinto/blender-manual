.. _bpy.types.CompositorNodeBrightContrast:
.. Editors Note: This page gets copied into:
.. - :doc:`</render/shader_nodes/color/bright_contrast>`

.. --- copy below this line ---

********************
Bright/Contrast Node
********************

.. figure:: /images/compositing_node-types_CompositorNodeBrightContrast.png
   :align: right

   Brightness/Contrast Node.


Inputs
======

Image
   Standard image input.
Brightness
   An additive-type factor by which to increase the overall brightness
   of the image. Use a negative number to darken an image.
Contrast
   A scaling type factor by which to make brighter pixels brighter, but keeping the darker pixels dark.
   Higher values make details stand out. Use a negative number to decrease the overall contrast in the image.


Properties
==========

Convert Premultiplied
   By default, it is supposed to work in *premultiplied* alpha.
   If the *Convert Premul* checkbox is not enabled, it is supposed to work in *straight* alpha.

   See :term:`Alpha Channel`.


Outputs
=======

Image
   Standard image output.


Notes
=====

It is possible that this node will put out a value set that has values beyond the normal range,
i.e. values greater than one and less than zero.
If you will be using the output to mix with other images in the normal range,
you should clamp the values using the Map Value node (with the Min and Max enabled),
or put through a Color Ramp node (with all normal defaults).

.. figure:: /images/compositing_types_color_bright-contrast_clamp-values.png
   :width: 600px

   Clamp the values to normal range.

Either of these nodes will scale the values back to normal range.
In the example image, we want to amp up the specular pass.
The bottom thread shows what happens if we do not clamp the values;
the specular pass has valued much less than one in the dark areas;
when added to the medium gray, it makes black. Passing the brightened image through either
the Map Value or the Color Ramp node produces the desired effect.


Example
=======

.. figure:: /images/compositing_types_color_bright-contrast_basic-example.png
   :width: 600px

   A basic example.
