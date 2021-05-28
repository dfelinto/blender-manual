.. index:: Object Constraints; Limit Scale Constraint
.. _bpy.types.LimitScaleConstraint:

**********************
Limit Scale Constraint
**********************

An object or bone can be scaled along the X, Y and Z axes.
This constraint restricts the amount of allowed scaling along each axis,
through lower and upper bounds.

.. important::

   This constraint does not tolerate negative scale values
   (those you might use to mirror an object...): when you add it to an object or bone,
   even if no axis limit is enabled, nor the *Affect Transform* option,
   as soon as you scale your object,
   all negative scale values are instantaneously inverted to positive ones...
   And the boundary settings can only take strictly positive values.

It is interesting to note that even though the constraint limits the visual and rendered scale
of its owner, its owner's data-block still allows (by default)
the object or bone to have scale values outside the minimum and maximum ranges
(as long as they remain positive!).
This can be seen in its *Transform* panel.
When an owner is scaled and attempted to be moved outside the limit boundaries,
it will be constrained to those boundaries visually and when rendered, but internally,
its coordinates will still be changed beyond the limits. If the constraint is removed,
its ex-owner will seem to jump to its internally-specified scale.

Similarly, if its owner has an internal scale that is beyond the limits, scaling it back into
the limit area will appear to do nothing until the internal scale values are back
within the limit threshold (unless you enabled the *Affect Transform* option,
see below, or your owner has some negative scale values).

Setting equal the min and max values of an axis locks the owner's scaling along that axis.
Although this is possible,
using the *Transformation Properties* axis locking feature is probably easier.


Options
=======

.. figure:: /images/animation_constraints_transform_limit-scale_panel.png

   Limit Scale panel.

Minimum/Maximum X, Y, Z
   These buttons enable the lower boundary for the scale of the owner along respectively the X,
   Y and Z axes of the chosen *Space*.
   The *Min* and *Max* number fields to their right control the value of
   their lower and upper boundaries, respectively.

   .. note::

      If a min value is higher than its corresponding max value,
      the constraint behaves as if it had the same value as the max one.

Affect Transform
   As pointed out before by default, even though visually constrained, and except for the negative values,
   the owner can still have scales out of bounds (as shown by the *Transform* panel).
   When you enable this checkbox, this is no longer possible,
   the owner transform properties are also limited by the constraint.
   However, note that, the constraint does not directly modify the scale values:
   you have to scale its owner one way or another for this to take effect.

Owner
   This constraint allows you to choose in which space to evaluate its owner's transform properties.
   See :ref:`common constraint properties <rigging-constraints-interface-common-space>` for more information.

Influence
   Controls the percentage of affect the constraint has on the object.
   See :ref:`common constraint properties <bpy.types.constraint.influence>` for more information.


Example
=======

.. vimeo:: 171275278
