.. index:: Geometry Nodes; Curl Hair Curves

****************
Curl Hair Curves
****************

Deforms existing hair curves into curls using guide curves.


Inputs
======

**Geometry**

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

Subdivision
   Subdivision level applied before deformation.

Curl Start
   Percentage along each curve to blend deformation from the root.

Radius
   Overall radius of the curls.

Factor Start
   Factor for the radius at the curl start.

Factor End
   Factor for the radius at the curl end.

Frequency
   Frequency factor of the curls.

Random Offset
   Amount of random offset per curve.

Seed
   Random Seed for the operation.


Properties
==========

This node has no properties.


Outputs
=======

**Geometry**
