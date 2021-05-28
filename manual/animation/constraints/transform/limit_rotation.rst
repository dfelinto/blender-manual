.. index:: Object Constraints; Limit Rotation Constraint
.. _bpy.types.LimitRotationConstraint:

*************************
Limit Rotation Constraint
*************************

An object or bone can be rotated around the X, Y and Z axes.
This constraint restricts the amount of allowed rotations around each axis,
through lower and upper bounds.

It is interesting to note that even though the constraint limits the visual and
rendered rotations of its owner, its owner's data-block still allows (by default)
the object or bone to have rotation values outside the minimum and maximum ranges.
This can be seen in the *Transform* panel.
When an owner is rotated and attempted to be rotated outside the limit boundaries,
it will be constrained to those boundaries visually and when rendered, but internally,
its rotation values will still be changed beyond the limits. If the constraint is removed,
its ex-owner will seem to jump to its internally specified rotation.

Similarly, if its owner has an internal rotation that is beyond the limit, rotating it back
into the limit area will appear to do nothing until the internal rotation values are back
within the limit threshold (unless you enabled the *Affect Transform* option, see below).

Setting equal the min and max values of an axis,
locks the owner's rotation around that axis... Although this is possible,
using the *Transformation Properties* axis locking feature is probably easier.

This transform does not constrain the bone if it is manipulated by the IK solver.
For constraining the rotation of a bone for IK purposes,
see the "Inverse Kinematics" section of Bone properties.


Options
=======

.. figure:: /images/animation_constraints_transform_limit-rotation_panel.png

   Limit Rotation panel.

Limit X, Y, Z
   These buttons enable the rotation limit around respectively the X, Y and Z axes of the owner,
   in the chosen *Owner* space.
   The *Min* and *Max* number fields to their right control the value of
   their lower and upper boundaries, respectively.

   .. note::

      - If a min value is higher than its corresponding max value,
        the constraint behaves as if it had the same value as the max one.
      - Unlike the :doc:`Limit Location constraint </animation/constraints/transform/limit_location>`,
        you cannot enable separately lower or upper limits...

Affect Transform
   As pointed out before by default, even though visually constrained,
   the owner can still have rotations out of bounds (as shown by the *Transform* panel).
   When you enable this checkbox, this is no more possible --
   the owner transform properties are also limited by the constraint.
   However, note that, the constraint does not directly modify the rotation values:
   you have to rotate one way or the other its owner, for this to take effect...

Owner
   This constraint allows you to choose in which space evaluate its owner's transform properties.
   See :ref:`common constraint properties <rigging-constraints-interface-common-space>` for more information.

Influence
   Controls the percentage of affect the constraint has on the object.
   See :ref:`common constraint properties <bpy.types.constraint.influence>` for more information.


Example
=======

.. vimeo:: 171115852
