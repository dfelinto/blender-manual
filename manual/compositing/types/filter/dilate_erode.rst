.. _bpy.types.CompositorNodeDilateErode:

*****************
Dilate/Erode Node
*****************

.. figure:: /images/compositing_node-types_CompositorNodeDilateErode.png
   :align: right

   Dilate/Erode Node.

The *Dilate/Erode node* provides a morphology (mathematical shape analysis) filter.


Inputs
======

Mask
   Single color channel (or a black-and-white image) input.


Properties
==========

Mode
   Step, Threshold, Distance, Feather
Distance
   The Distance is the filter radius.
   A *positive* value of Distance dilates (expands) the influence of a pixel on its surrounding pixels.
   A *negative* value erodes (shrinks) its influence.
Edge
   Edge to inset.
   .. TODO2.8 Explain.
Falloff
   Falloff type the feather.
   .. TODO2.8 Explain.


Outputs
=======

Mask
   The filtered mask output.


Example
=======

In this example, we wanted to take the rather boring array of ball bearings and
add some variation to it. So, we dilated the red and eroded the green, leaving the blue alone.
If we had dilated both red and green... (hint: red and green make yellow).
The amount of influence is increased by increasing the *Distance* values.
`Blend-file available here <https://wiki.blender.org/uploads/5/51/Derotest.blend>`__.

.. figure:: /images/compositing_types_filter_dilate-erode_example.png
