
Procedural Textures
===================


.. figure:: /images/25-Manual-Textures-Procedural-Menu.jpg
   :width: 240px
   :figwidth: 240px

   The Texture Type list in the Texture panel of the Texture Buttons. (Non procedural textures darkened out.)


Procedural textures are textures that are defined mathematically.
They are generally relatively simple to use, because they don't need to be mapped in a special
way - which doesn't mean that procedural textures can't become very complex.

These types of textures are 'real' 3D. By that we mean that they fit together perfectly at the
edges and continue to look like what they are meant to look like even when they are cut;
as if a block of wood had really been cut in two.
Procedural textures are not filtered or anti-aliased. This is hardly ever a problem:
the user can easily keep the specified frequencies within acceptable limits.

These are the available types:


- :doc:`Blend <textures/types/procedural/blend>`
- :doc:`Clouds <textures/types/procedural/clouds>`
- :doc:`Distorted Noise <textures/types/procedural/distorted_noise>`
- :doc:`Magic <textures/types/procedural/magic>`
- :doc:`Marble <textures/types/procedural/marble>`
- :doc:`Musgrave <textures/types/procedural/musgrave>`
- :doc:`Noise <textures/types/procedural/noise>`
- :doc:`Stucci <textures/types/procedural/stucci>`
- :doc:`Voronoi <textures/types/procedural/voronoi>`
- :doc:`Wood <textures/types/procedural/wood>`


Common options
--------------


Noise Basis
~~~~~~~~~~~


.. figure:: /images/Doc-26-Manual-Textures-Procedural-Noise-Basis.jpg
   :width: 300px
   :figwidth: 300px

   Noise Basis list


Each noise-based Blender texture (with the exception of Voronoi and simple noise) has a
:guilabel:`Noise Basis` setting that allows the user to select which algorithm is used to
generate the texture. This list includes the original Blender noise algorithm.
The :guilabel:`Noise Basis` settings makes the procedural textures extremely flexible
(especially :guilabel:`Musgrave`\ ).

The :guilabel:`Noise Basis` governs the structural appearance of the texture :


+-------------------------------------------------+-------------------------------------------+------------------------------------------------+
+.. figure:: /images/NoiseBasisBlenderOriginal.jpg|.. figure:: /images/NoiseBasisVoronoiF1.jpg|.. figure:: /images/NoiseBasisVoronoiF2-F1.jpg  +
+   :width: 160px                                 |   :width: 160px                           |   :width: 160px                                +
+   :figwidth: 160px                              |   :figwidth: 160px                        |   :figwidth: 160px                             +
+                                                 |                                           |                                                +
+   Blender Original                              |   Voronoi F1                              |   Voronoi F2-F1                                +
+-------------------------------------------------+-------------------------------------------+------------------------------------------------+
+.. figure:: /images/NoiseBasisOriginalPerlin.jpg |.. figure:: /images/NoiseBasisVoronoiF2.jpg|.. figure:: /images/NoiseBasisVoronoiCrackle.jpg+
+   :width: 160px                                 |   :width: 160px                           |   :width: 160px                                +
+   :figwidth: 160px                              |   :figwidth: 160px                        |   :figwidth: 160px                             +
+                                                 |                                           |                                                +
+   Original Perlin                               |   Voronoi F2                              |   Voronoi Crackle                              +
+-------------------------------------------------+-------------------------------------------+------------------------------------------------+
+.. figure:: /images/NoiseBasisImprovedPerlin.jpg |.. figure:: /images/NoiseBasisVoronoiF3.jpg|.. figure:: /images/NoiseBasisCellNoise.jpg     +
+   :width: 160px                                 |   :width: 160px                           |   :width: 160px                                +
+   :figwidth: 160px                              |   :figwidth: 160px                        |   :figwidth: 160px                             +
+                                                 |                                           |                                                +
+   Improved Perlin                               |   Voronoi F3                              |   Cell Noise                                   +
+-------------------------------------------------+-------------------------------------------+------------------------------------------------+
+.. figure:: /images/NoiseBasisVoronoiF4.jpg                                                                                                   +
+   :width: 160px                                                                                                                              +
+   :figwidth: 160px                                                                                                                           +
+                                                                                                                                              +
+   Voronoi F4                                                                                                                                 +
+-------------------------------------------------+-------------------------------------------+------------------------------------------------+

There are two more possible settings for :guilabel:`Noise Basis`\ ,
which are relatively similar to :guilabel:`Blender Original`\ :
Improved Perlin and Original Perlin


Nabla
~~~~~


Almost all procedural textures in Blender use derivatives for calculating normals for texture
mapping (with as exception :guilabel:`Blend` and :guilabel:`Magic`\ ).
This is important for Normal and Displacment Maps.
The strength of the effect is controlled with the :guilabel:`Nabla` Number Button.


Hints
-----


Use the size buttons in the :guilabel:`Mapping` panel to set the size that the procedural
textures are mapped to.

Procedural textures can either produce colored textures, intensity only textures,
textures with alpha values and normal textures.
If intensity only ones are used the result is a black and white texture,
which can be greatly enhanced by the use of ramps.
If on the other hand you use ramps and need an intensity value,
you have to switch on :guilabel:`No RGB` in the :guilabel:`Mapping` panel.


