
Procedural textures: Wood
*************************

.. figure:: /images/25-Manual-Textures-Procedural-Wood.jpg
   :width: 307px
   :figwidth: 307px

   Wood Texture Panels


Often used for
   Woods and ring-shaped patterns.
Result(s)
   Intensity only


Options
=======

Sin / Saw / Tri
   Shape of wave to produce bands
Bands / Rings / Band Noise / Ring Noise
   Set the bands to either straight or ring-shaped, with or without turbulence
Soft / Hard
   There are two methods available for the Noise function
Size
   Dimension of the Noise table
Turbulence
   Turbulence of the Band Noise and Ring Noise types


Technical Details
=================

Generation
   Bands are generated based on a sine formula. You can also add a degree of turbulence with the Noise formula.
Coordinates
   As the band is based on a sine formula, the texture repeats itself every pi units rather than every 1.0 units.  To correct this, scale the texture by a value of pi for the dimension you wish.

