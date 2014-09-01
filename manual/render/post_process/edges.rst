
..    TODO/Review: {{review|copy=X}} .


Edge (Toon) Rendering
*********************

.. figure:: /images/Manual-Part-XI-Toon01.jpg
   :width: 240px
   :figwidth: 240px

   A scene with Toon materials.


Blender's toon shaders can give your rendering a comic-book-like or manga-like appearance,
affecting the shades of colors.
The effect is not perfect since real comics and manga also usually have china ink outlines.
Blender can add this feature as a post-processing operation.


Options
=======

.. figure:: /images/Manual-Part-XI-Render07.jpg

   Toon edge buttons (F10).


Edge
   This makes Blender search for edges in your rendering and add an 'outline' to them.


.. figure:: /images/Manual-Part-XI-Render08.jpg

   Toon edge settings (F10).


Before repeating the rendering it is necessary to set some parameters:

Threshold
   The threshold of the angle between faces for drawing edges,
   from 0 to 255. A value of 10 would just give outline of object against the background,
   whereas higher settings start to add outlines on surface edges, starting with sharper angles.
   At maximum intensity, Edge will even faintly display geometry subsurf edge lines in areas of imperfect smoothing.
Color / R/G/B
   The color of the rendered edges (black by default). Click on the swatch to see the color picker


Examples
========

.. figure:: /images/Manual-Part-XI-Toon02.jpg
   :width: 400px
   :figwidth: 400px

   Scene re-rendered with toon edge set.


.. figure:: /images/Manual-Renderlayer-Edge.jpg
   :width: 400px
   :figwidth: 400px

   Post-processing Edge and Renderlayers


It is possible to separate out the edge layer using a render layer dedicated to that purpose.
The alpha channel is 0 where there is no edge, and 1 where the edge is.
By separating out the edge layer, you can blur it, change its color, mask it, etc.
The image to the right shows how to do this.
I created an Edge render layer that only has the Sky and Edge layers
(I included sky so that we get the world color later on in the composite output).
The other render layer omits the Edge layer, so it returns just the normal image.
On the output panel I enabled Edge with a width of 10 in black.
I run that layer through a blur node. Using the Alphaover node,
I then composite the cube on top of the blurred edge.
The result gives a soft-shadow kind of effect.
Note that Premultiply is set because the Edge image already has an alpha of 1.0 set.


Dithering
*********

Dithering is a technique for blurring pixels to prevent banding that is seen in areas of
gradients, where stair-stepping appears between colors.
Banding artifacts are more noticeable when gradients are longer, or less steep.
Dithering was developed for graphics with low bit depths,
meaning they had a limited range of possible colors.

Dithering works by taking pixel values and comparing them with a threshold and neighboring
pixels then does calculations to generate the appropriate color. Dithering creates the
perceived effect of a larger color palette by creating a sort of visual color mixing.
For example, if you take a grid and distribute red and yellow pixels evenly across it,
the image would appear to be orange.

The :guilabel:`Dither` value ranges from 0 to 2.
