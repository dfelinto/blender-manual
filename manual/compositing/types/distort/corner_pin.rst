
***************
Corner Pin Node
***************

.. figure:: /images/compositing_node-types_CompositorNodeCornerPin.png
   :align: right

   Corner Pin Node.

The Corner Pin node uses explicit corner values for a plane warp transformation.
It works like the Plane Track Deform node,
but without using "plane track" data from the Movie Clip Editor.


Inputs
======

Image
   Standard image input.
Corners
   Four vector inputs to define the plane warping. (Z component of vector inputs is ignored.)


Properties
==========

This node has no properties.


Outputs
=======

Image
   Standard image output. (The image after distorting.)
Plane
   A black-and-white alpha mask of the plane.


Example
=======

.. figure:: /images/compositing_types_distort_corner-pin_example.png

   An example of the Corner Pin node.

.. figure:: /images/compositing_types_distort_corner-pin_example-result.jpg

   An example of the distorted image.

In the example above, the image of the bird is distorted by the vectors specified by the Corner Pin node.
