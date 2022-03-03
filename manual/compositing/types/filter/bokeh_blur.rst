.. _bpy.types.CompositorNodeBokehBlur:

***************
Bokeh Blur Node
***************

.. figure:: /images/compositing_node-types_CompositorNodeBokehBlur.png
   :align: right
   :alt: Bokeh Blur Node.

The Bokeh Blur node generates a bokeh type blur similar to Defocus.
Unlike defocus an in-focus region is defined in the Compositor.
There is also more flexibility in the type of blur applied through
the :doc:`Bokeh Image </compositing/types/input/bokeh_image>` node.

Several performance optimizations are also available such as OpenCL support,
calculation area restriction and masking.


Inputs
======

Image
   Standard color input.
Bokeh
   This is an input for the :doc:`Bokeh Image </compositing/types/input/bokeh_image>` node.
Size
   Size controls the amount of blur. Size can either be a single value across the entire image or a variable value
   controlled by an input image. In order to use the latter, the Variable Size option must be selected.
   See the examples section below for more on how to use this.
Bounding Box
   This can be used with a :doc:`Box Mask </compositing/types/matte/box_mask>`
   matte node or with a :doc:`Mask </compositing/types/input/mask>`
   input node to restrict the area of the image the blur is applied to. This could be helpful, for example,
   when developing a node system by allowing only a small area of the image to be filtered
   thus saving composite time each time adjustments are made.


Properties
==========

Variable Size
   Allows a variable blur radius, if the Size input is an image.
Max Blur
   Max Blur is intended to act as an optimization tool by
   limiting the number of pixels across which the blur is calculated.


Outputs
=======

Image
   Standard color output.


Examples
========

Three examples of how the size input may be used follow.

An :doc:`ID masked </compositing/types/converter/id_mask>`
alpha image can be used so that a background is blurred while foreground objects remain in focus.
To prevent strange edges the :doc:`Dilate Node </compositing/types/filter/dilate_erode>` should be used.

The Z pass can be visualized using a :doc:`Map Value </compositing/types/vector/map_value>` node
and a :doc:`Color Ramp </compositing/types/converter/color_ramp>` node
as described in :doc:`Render Layers </compositing/types/input/render_layers>`.
A *multiply* :doc:`Math </compositing/types/converter/math>` node can be used following the color ramp
so that a blur value greater than one is used for objects outside the focal range.

.. figure:: /images/compositing_types_filter_bokeh-blur_example-1.png
   :width: 640px

   Z pass used.

A manually created grayscale image can be used to define the sharp and blurry areas of a pre-existing image.
Again, a Multiply Node can be used so that a blur value greater than one is used.

.. figure:: /images/compositing_types_filter_bokeh-blur_example-2.png
   :width: 640px

   Image used.

.. list-table::

   * - .. figure:: /images/compositing_types_filter_bokeh-blur_example-1-render.jpg

          Z pass used.

     - .. figure:: /images/compositing_types_filter_bokeh-blur_example-2-render.jpg

          Image used.
