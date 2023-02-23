.. index:: Geometry Nodes; Interpolate Hair Curves

***********************
Interpolate Hair Curves
***********************

Interpolates existing guide curves on a surface mesh.


Inputs
======

**Guide Curves**

Surface Geometry
   Surface geometry for generation.

Surface Object
   Surface object for generation (Needs matching transforms).

Surface UV Map
   Surface UV map used for attachment.

Surface Rest Position
   Set the surface mesh into its rest position before attachment.

Follow Surface Normal
   Align the interpolated curves to the surface normal.

Part by Mesh Islands
   Use mesh islands of the surface geometry for parting.

Interpolation Guides
   Amount of guides to be used for interpolation per curve.

Distance to Guides
   Distance around each guide to spawn interpolated curves.

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

Guide Index
   Index of the main guide curve per curve.

Surface Normal
   Normal direction of the surface mesh at the attachment point.
