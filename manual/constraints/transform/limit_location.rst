
Limit Location Constraint
*************************

Description
===========

An object or *unconnected* bone can be moved around the scene along the X, Y and Z axes.
This constraint restricts the amount of allowed translations along each axis,
through lower and upper bounds.

The limits for an object are calculated from its center, and the limits of a bone,
from its root.

It is interesting to note that even though the constraint limits the visual and rendered
location of its owner, its owner's data block still allows (by default)
the object or bone to have coordinates outside the minimum and maximum ranges.
This can be seen in its *Transform Properties* panel (:kbd:`N`).
When an owner is grabbed and attempted to be moved outside the limit boundaries,
it will be constrained to those boundaries visually and when rendered, but internally,
its coordinates will still be changed beyond the limits. If the constraint is removed,
its ex-owner will seem to jump to its internally specified location.

Similarly, if its owner has an internal location that is beyond the limits, dragging it back
into the limit area will appear to do nothing until the internal coordinates are back within
the limit threshold (unless you enabled the *For Transform* option, see below).

Setting equal the min and max values of an axis,
locks the owner's movement along that axis... Although this is possible,
using the *Transformation Properties* axis locking feature is probably easier!


Options
=======

.. figure:: /images/25-Manual-Constraints-Transform-LimitLoc.jpg
   :width: 302px
   :figwidth: 302px

   Limit Location panel


Minimum X, Minimum Y, Minimum Z
   These buttons enable the lower boundary for the location of the owner's center along, respectively, the X, Y and Z axes of the chosen :guilabel:`Space`.
   The numeric field below them controls the value of their limit.
   Note that if a min value is higher than its corresponding max value, the constraint behaves as if it had the same value as the max one.

Maximum X, Maximum Y, Maximum Z
   These buttons enable the upper boundary for the location of the owner's center along, respectively, the X, Y and Z axes of the chosen :guilabel:`Space`.
   Same options as above.

For Transform
   We saw that by default, even though visually constrained, the owner can still have coordinates out of bounds (as shown by the *Transform Properties* panel). Well, when you enable this button, this is no longer possible - the owner's transform properties are also limited by the constraint.
   Note however that the constraint does not directly modify the coordinates: you have to grab its owner one way or another for this to take effect...

Convert
   This constraint allows you to choose in which space to evaluate its owner's transform properties.


