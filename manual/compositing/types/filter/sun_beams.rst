.. index:: Compositor Nodes; Sun Beams
.. _bpy.types.CompositorNodeSunBeams:

**************
Sun Beams Node
**************

.. figure:: /images/compositing_node-types_CompositorNodeSunBeams.webp
   :align: right
   :alt: Sun Beams Node.

The Sun Beams node provides a computationally cheap way of
creating the name giving effect based on the image brightness alone.

Sun Beams is a 2D effect for simulating the effect of bright light getting scattered in a medium
`(Crepuscular Rays) <https://en.wikipedia.org/wiki/Crepuscular_rays>`__.
This phenomenon can be created by renderers, but full volumetric lighting is
a rather arduous approach and takes a long time to render.


Inputs
======

Image
   Standard color input.


Properties
==========

Source Width, Height
   Source point of the rays as a factor of the image dimensions.
Ray Length
   Length of the rays as a factor of the image size.


Outputs
=======

Image
   Standard color output.


Example
=======

Usually, the first step is to define the area from which rays are cast.
Any diffuse reflected light from surfaces is not going to contribute to such scattering in the real world,
so should be excluded from the input data.
Possible ways to achieve this are:

- Entirely separate image as a light source.
- Brightness/contrast tweaking to leave only the brightest areas.
- Muting shadow and midtone colors, which is a bit more flexible.
- Masking for ultimate control.

After generating the sun beams from such a light source image they can then be overlayed on the original image.
Usually, a simple "Add" Mix node is sufficient,
and physically correct because the scattered light adds to the final result.

.. figure:: /images/compositing_types_filter_sun-beams_example.jpg
   :width: 400px
