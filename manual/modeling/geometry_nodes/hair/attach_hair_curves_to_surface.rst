.. index:: Geometry Nodes; Attach Hair Curves to Surface

*****************************
Attach Hair Curves to Surface
*****************************

Attaches hair curves to a surface mesh.


Inputs
======

Geometry
   Input Geometry (may include other than curves).

Surface
   Surface Object to attach to (needs to have matching transforms).

Surface
   Surface Geometry to attach hair curves to.

Surface UV Map
   Surface UV map used for attachment.

Surface Rest Position
   Set the surface mesh into its rest position before attachment.

Sample Attachment UV
   Sample the surface UV map at the attachment point.

Snap to Surface
   Snap the root of each curve to the closest surface point.

Align to Surface Normal
   Align the curve to the surface normal (need guide as reference).

Blend along Curve
   Blend deformation along each curve from the root.


Properties
==========

This node has no properties.


Outputs
=======

**Geometry**

Surface UV Coordinate
   Surface UV coordinate at the attachment point.

Surface Normal
   Surface normal at the attachment point.

