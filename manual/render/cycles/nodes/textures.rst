.. _textures:

Texture Nodes
*************

Image Texture
=============

.. figure:: /images/Manual_cycles_nodes_tex_image.jpg
   :width: 200px
   :figwidth: 200px

   Image texture from `GoodTextures.com <http://www.goodtextures.com/>`__


Use an image file as a texture.

Image Datablock
   Image datablock used as the image source. Currently not all images supported by Blender can be used by Cycles.
   In particular, generated, packed images or animations are not supported currently.
Projection
   Projection to use for mapping the textures. :guilabel:`Flat` will use the XY coordinates for mapping.
   Box will map the image to the 6 sides of a virtual box, based on the normal, using XY,
   YZ and XYZ coordinates depending on the side.
Projection Blend
   For Box mapping, the amount to blend between sides of the box,
   to get rid of sharp transitions between the different sides.
   Blending is useful to map a procedural-like image texture pattern seamlessly on a model. 0.0 gives no blending;
   higher values give a smoother transition.
Color Space
   Type of data that the image contains, either Color or Non-Color Data.
   For most color textures the default of Color should be used, but in case of e.g. a bump or alpha map,
   the pixel values should be interpreted as Non-Color Data, to avoid doing any unwanted color space conversions.
Vector input
   Texture coordinate for texture lookup. If this socket is left unconnected,
   UV coordinates from the active UV render layer are used.
Color output
   RGB color from image. If the image has alpha, the color is premultiplied with alpha if the Alpha output is used,
   and unpremultiplied or straight if the Alpha output is not used.
Alpha output
   Alpha channel from image.


Environment Texture
===================

.. figure:: /images/Manual_cycles_nodes_tex_environment.jpg
   :width: 200px
   :figwidth: 200px

   HDR image from `OpenFootage.net <http://www.openfootage.net/?p=986>`__


Use an environment map image file as a texture.
The environment map is expected to be in Latitude/Longitude or 'latlong' format.

Image Datablock
   Image datablock used as the image source. Currently not all images supported by Blender can be used by Cycles.
   In particular, generated, packed images or animations are not supported currently.
Color Space
   Type of data that the image contains, either Color or Non-Color Data.
   For most color textures the default of Color should be used, but in case of e.g. a bump or alpha map,
   the pixel values should be interpreted as Non-Color Data, to avoid doing any unwanted color space conversions.
Vector input
   Texture coordinate for texture lookup. If this socket is left unconnected,
   the image is mapped as environment with the Z axis as up.
Color output
   RGB color from the image. If the image has alpha,
   the color is premultiplied with alpha if the Alpha output is used,
   and unpremultiplied if the Alpha output is not used.
Alpha output
   Alpha channel from image.


Sky Texture
===========

.. figure:: /images/Manual_cycles_nodes_tex_sky.jpg
   :width: 200px
   :figwidth: 200px

   Sky Texture


Procedural Sky texture.

Sky Type
   Sky model to use (Preetham or Hosek / Wilkie).
Sun Direction
   Sun direction vector.
Turbidity
   Atmospheric turbidity. (2: Arctic like, 3: clear sky, 6: warm/moist day, 10: hazy day)
Ground Albedo
   Amount of light reflected from the planet surface back into the atmosphere. (RGB 0,0,0 is black, 1,1,1 is white).
Vector
   Texture coordinate to sample texture at;
   defaults to Generated texture coordinates if the socket is left unconnected.
Color output
   Texture color output.


Noise Texture
=============

.. figure:: /images/Manual_cycles_nodes_tex_noise.jpg
   :width: 200px
   :figwidth: 200px

   Noise Texture with high detail


Procedural Perlin noise texture, similar to the Clouds texture in Blender Internal.

Vector input
   Texture coordinate to sample texture at;
   defaults to Generated texture coordinates if the socket is left unconnected.
Scale input
   Overall texture scale.
Detail input
   Amount of noise detail.
Distortion input
   Amount of distortion.
Color output
   Texture color output.
Fac output
   Texture intensity output.


Wave Texture
============

.. figure:: /images/Manual_cycles_nodes_tex_wave.jpg
   :width: 200px
   :figwidth: 200px

   Default wave texture


Procedural bands or rings texture with noise distortion.

Type
   :guilabel:`Bands` or :guilabel:`Rings` shaped waves.
Vector input
   Texture coordinate to sample texture at;
   defaults to Generated texture coordinates if the socket is left unconnected.
Scale input
   Overall texture scale.
Distortion input
   Amount of distortion of the wave (similar to the Marble texture in Blender Internal).
Detail input
   Amount of distortion noise detail.
Detail Scale input
   Scale of distortion noise.
Color output
   Texture color output.
Fac output
   Texture intensity output.


Voronoi Texture
===============

+-----------------------------------------------------------------+-------------------------------------------------------------+
+.. figure:: /images/Manual_cycles_nodes_tex_voronoi_intensity.jpg|.. figure:: /images/Manual_cycles_nodes_tex_voronoi_cells.jpg+
+   :width: 200px                                                 |   :width: 200px                                             +
+   :figwidth: 200px                                              |   :figwidth: 200px                                          +
+                                                                 |                                                             +
+   Voronoi texture, type: Intensity                              |   Voronoi texture, type: Cells                              +
+-----------------------------------------------------------------+-------------------------------------------------------------+


Procedural texture producing Voronoi cells.

Type
   :guilabel:`Intensity` or :guilabel:`Cells` output.
Vector input
   Texture coordinate to sample texture at;
   defaults to Generated texture coordinates if the socket is left unconnected.
Scale input
   Overall texture scale.
Color output
   Texture color output.
Fac output
   Texture intensity output.


Musgrave Texture
================

Advanced procedural noise texture. Note that it often needs some adjustments
(multiplication and addition) in order to see more detail.

+--------------------------------------------------------------+--------------------------------------------------------------+
+.. figure:: /images/Manual_cycles_nodes_tex_musgrave_nodes.jpg|.. figure:: /images/Manual_cycles_nodes_tex_musgrave.jpg      +
+   :width: 200px                                              |   :width: 200px                                              +
+   :figwidth: 200px                                           |   :figwidth: 200px                                           +
+                                                              |                                                              +
+   Nodes for the image to the right                           |   Remapped Musgrave texture such that most values are visible+
+--------------------------------------------------------------+--------------------------------------------------------------+


Type
   Multifractal, Ridged Multifractal, Hybrid Multifractal, fBM, Hetero Terrain.
Vector input
   Texture coordinate to sample texture at;
   defaults to Generated texture coordinates if the socket is left unconnected.
Scale input
   Overall texture scale.
Detail input
   Amount of noise detail.
Dimension input
   *TBD*
Lacunarity input
   *TBD*
Offset input
   *TBD*
Gain input
   *TBD*
Color output
   Texture color output.
Fac output
   Texture intensity output.


Gradient Texture
================

.. figure:: /images/Manual_cycles_nodes_tex_gradient.jpg
   :width: 200px
   :figwidth: 200px

   Gradient texture using object coordinates


A gradient texture.

Type
   The gradient can be :guilabel:`Linear`, :guilabel:`Quadratic`, :guilabel:`Easing`, :guilabel:`Diagonal`,
   :guilabel:`Spherical`, :guilabel:`Quadratic Sphere` or :guilabel:`Radial`.
Vector input
   Texture coordinate to sample texture at;
   defaults to Generated texture coordinates if the socket is left unconnected.
Color output
   Texture color output.
Fac output
   Texture intensity output.


Magic Texture
=============

.. figure:: /images/Manual_cycles_nodes_tex_magic.jpg
   :width: 200px
   :figwidth: 200px

   Magic texture: Depth 10, Distortion 2.0


Psychedelic color texture.

Depth
   Number of iterations.
Vector input
   Texture coordinate to sample texture at;
   defaults to Generated texture coordinates if the socket is left unconnected.
Distortion input
   Amount of distortion.
Color output
   Texture color output.
Fac output
   Texture intensity output.


Checker Texture
===============

.. figure:: /images/Manual_cycles_nodes_tex_checker.jpg
   :width: 200px
   :figwidth: 200px

   Default Checker texture


Checkerboard texture.

Vector input
   Texture coordinate to sample texture at;
   defaults to Generated texture coordinates if the socket is left unconnected.
Color1/2 input
   Color of the checkers.
Scale input
   Overall texture scale.
Color output
   Texture color output.
Fac output
   Checker 1 mask (1 = Checker 1).


Brick Texture
=============

.. figure:: /images/Manual_cycles_nodes_tex_brick.jpg
   :width: 200px
   :figwidth: 200px

   Brick texture: Colors changed, Squash 0.62, Squash Frequency 3.


Procedural texture producing Bricks.


Options
"""""""

Offset
   Determines the brick offset of the various rows.
Frequency
   Determines the offset frequency. A value of 2 gives a even/uneven pattern of rows.
Squash
   Amount of brick squashing.
Frequency
   Brick squashing frequency.


Sockets
"""""""

Color 1/2 and Mortar
   Color of the bricks and mortar.
Scale
   Overall texture scale.
Mortar Size
   The Mortar size; 0 means no Mortar.
Bias
   The color variation between Brick color 1 / 2.
   Values of -1 and 1 only use one of the two colors; values in between mix the colors.
Brick Width
   The width of the bricks.
Row Height
   The height of the brick rows.

Color output
   Texture color output.
Fac output
   Mortar mask (1 = mortar).
