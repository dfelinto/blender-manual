.. index:: Geometry Nodes; Clump Hair Curves

*****************
Clump Hair Curves
*****************

Clumps together existing hair curves using guide curves.


Inputs
======

Geometry
   Input Geometry (May include other than curves).

Guide Index
   Guide index map to be used. This input has priority.

Guide Distance
   Minimum distance between two guides for new guide map.

Guide Mask
   Mask for which curve are eligible to be selected as guides.

Existing Guide Map
   Use the existing guide map attribute if available.

Factor
   Factor to blend overall effect.

Shape
   Shape of the influence along curves (0=constant, 0.5=linear).

Tip Spread
   Distance of random spread at the curve tips.

Clump Offset
   Offset of each clump in a random direction.

Distance Falloff
   Falloff distance for the clumping effect (0 means no falloff).

Distance Threshold
   Distance threshold for the falloff around the guide.

Seed
   Random seed for the operation.

Preserve Length
   Preserve each curve's length during deformation.


Properties
==========

This node has no properties.


Outputs
=======

**Geometry**

Guide Index
   Guide index map that was used for the operation.
