.. _bpy.types.CompositorNodeDespeckle:

**************
Despeckle Node
**************

.. figure:: /images/compositing_node-types_CompositorNodeDespeckle.png
   :align: right

   Despeckle Node.

The *Despeckle node* is used to smooth areas of an image in which noise is noticeable,
while leaving complex areas untouched.

This works by the standard deviation of each pixel and its neighbors is calculated to determine
if the area is one of high complexity or low complexity.
If the complexity is lower than the threshold then the area is smoothed using a simple mean filter.


Inputs
======

Factor
   Controls the amount the filter effects the image.
Image
   Standard color input.


Properties
==========

Threshold
   The threshold to control high/low complexity.
Neighbor
   The threshold to control the number of pixels that must match.


Outputs
=======

Image
   Standard color output.
