
..    TODO/Review: {{review|partial=X|text=missing example}} .


Stars
=====

Description
-----------

Stars are randomly placed halo-like objects which appear in the background.
Not for use with Cycles renderer.


Options
-------

.. figure:: /images/25-Manual-World-StarPanel.jpg
   :width: 298px
   :figwidth: 298px

   Star panel


Size
   The actual size of the star halo. It is better to keep it much smaller than the proposed default,
   to keep the material smaller than pixel-size and have pin-point stars. This is much more realistic.
Colors
   Adds a random hue to the otherwise plain white stars.
Min. Dist
   The *minimum* distance from the camera at which stars are placed.
   This should be greater than the distance from the camera to the *furthest* object in your scene,
   unless you want to risk having stars *in front* of your objects.
Separation
   The *average* distance between stars. Stars are intrinsically a 3D feature, they are placed in space,
   not on the image.
