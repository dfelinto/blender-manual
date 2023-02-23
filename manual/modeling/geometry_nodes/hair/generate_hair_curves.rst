.. index:: Geometry Nodes; Generate Hair Curves

********************
Generate Hair Curves
********************

Generates new hair curves on a surface mesh.


Inputs
======

Surface
   Surface geometry for generation.

Surface
   Surface object for generation (Needs matching transforms).

Surface UV Map
   Surface UV map used for attachment.

Surface Rest Position
   Set the surface mesh into its rest position before attachment.

Hair Length
   Length of the generated hair curves.

Hair Material
   Material of the generated hair curves.

Control Points
   Amount of control points of the generated hair curves.

Poisson Disk Distribution
   Use poisson disk distribution method to keep a minimum distance.

Density
   Surface density of generated hair curves.

Density Mask
   Factor applied on the density for curve distribution.

Mask Texture
   Discard points based on an mask texture after distribution.

Viewport Amount
   Factor applied on the density for the viewport.

Seed
   Random seed for the operation.


Properties
==========

This node has no properties.


Outputs
=======

**Geometry**

**Curves**

Surface Normal
   Normal direction of the surface mesh at the attachment point.
