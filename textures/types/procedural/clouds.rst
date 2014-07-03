


Procedural textures: Clouds
===========================


.. figure:: /images/25-Manual-Textures-Procedural-Clouds.jpg
   :width: 307px
   :figwidth: 307px

   Clouds Texture Panels


Clouds represent Perlin noise. In addition, each noise-based Blender texture
(with the exception of Voronoi and simple noise) has a "Noise Basis" setting that allows the
user to select which algorithm is used to generate the texture.

**Often used for**
   Clouds, Fire, Smoke. Well-suited to be used as a Bump map, giving an overall irregularity to the material.
**Result(s)**
   :guilabel:`Greyscale` (default) or RGB :guilabel:`Color`


Options
-------


:guilabel:`Greyscale`
   The standard noise, gives an intensity
:guilabel:`Color`
   The noise gives an RGB value
:guilabel:`Noise`
   :guilabel:`Soft` or :guilabel:`Hard`\ , changes contrast and sharpness
:guilabel:`Size`
   The dimension of the Noise table
:guilabel:`Depth`
   The depth of the :guilabel:`Clouds` calculation. A higher number results in a long calculation time, but also in finer details.


Technical Details
-----------------

A three-dimensional table with pseudo-random values is used,
from which a fluent interpolation value can be calculated with each 3D coordinate
(thanks to Ken Perlin for his masterful article "An Image Synthesizer",
from the SIGGRAPH proceedings 1985). This calculation method is also called Perlin Noise.


