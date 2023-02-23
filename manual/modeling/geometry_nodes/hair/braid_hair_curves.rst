.. index:: Geometry Nodes; Braid Hair Curves

*****************
Braid Hair Curves
*****************

Deforms existing hair curves into braids using guide curves.


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

Braid Start
   Percentage along each curve to blend deformation from the root.

Radius
   Overall radius of the braids.

Shape
   Shape of the braid radius along each curve.

Factor Min
   Factor of the minimum radius of the braids.

Factor Max
   Factor of the maximum radius of the braids.

Frequency
   Frequency factor of the braids.

Thickness
   Thickness of each strand of hair.

Thickness Shape
   Shape adjustment of the strand thickness for the braids.

Shape Asymmetry
   Asymmetry of the shape adjustment of the strand thickness.

Flare Length
   Length of the flare at the end of the braid.

Flare Opening
   Opening radius of the flare at the tip of the braid.

Hair Tie
   Object used for the hair tie instance.

Hair Tie
   Geometry used for the hair tie instance (priority).

Hair Tie Scale
   Scale of the hair tie instance.


Properties
==========

This node has no properties.


Outputs
=======

**Geometry**

Guide Index
   Guide index map that was used for the operation.

Flare Parameter
   Parameter from 0 to 1 along the flare.

Strand Index
   Index of the strand within a braid that each curve belongs to.
