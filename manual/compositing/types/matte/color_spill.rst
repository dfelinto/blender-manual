.. _bpy.types.CompositorNodeColorSpill:

****************
Color Spill Node
****************

.. figure:: /images/compositing_node-types_CompositorNodeColorSpill.png
   :align: right

   Color Spill Node.

The *Color Spill* node reduces one of the RGB channels so that it is not greater
than any of the others.

This is common when compositing images that were shot in front of a green or blue screen.
In some cases, if the foreground object is reflective, it will show the green or blue color;
that color has "spilled" onto the foreground object. If there is light from the side or back,
and the foreground actor is wearing white, it is possible to get "spill" green (or blue)
light from the background onto the foreground objects,
coloring them with a tinge of green or blue. To remove the green (or blue) light,
you use this fancy node.


Inputs
======

Image
   Standard image input.
Factor
   Standard Factor.


Properties
==========

Despill Channel
   R, G, B
Algorithm
   Simple, Average
Limiting Channel
   R, G, B
Ratio
   Scale limit by value.
Unspill
   Allows you to reduce the selected channel's input to the image
   greater than the color spill algorithm normally allows.
   This is useful for exceptionally high amounts of the color spill.

   R, G, B


Outputs
=======

Image
   The image with the corrected channels.


Example
=======

Results with the nodes applied to an image from
the `Mango Open Movie <https://mango.blender.org/>`__.

.. list-table::

   * - .. figure:: /images/compositing_types_matte_color-spill_example-before.jpg

          Before: green border and green reflections.

     - .. figure:: /images/compositing_types_matte_color-spill_example-after.jpg

          After: no unwanted green.
