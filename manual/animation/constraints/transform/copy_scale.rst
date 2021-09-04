.. index:: Object Constraints; Copy Scale Constraint
.. _bpy.types.CopyScaleConstraint:

*********************
Copy Scale Constraint
*********************

The *Copy Scale* constraint forces its owner to have the same scale as its target.

.. note::

   Here we talk of *scale*, not of *size*! Indeed, you can have two objects,
   one much bigger than the other, and yet both of them have the same scale.
   This is also true with bones: in *Pose Mode*,
   they all have a unitary scale when they are in rest position,
   represented by their visible length.


Options
=======

.. figure:: /images/animation_constraints_transform_copy-scale_panel.png

   Copy Scale panel.

Target
   :ref:`ui-data-id` used to select the constraints target, and is not functional (red state) when it has none.
   See :ref:`common constraint properties <rigging-constraints-interface-common-target>` for more information.

Axis
   These buttons control which axes of the target scale are copied.

Power
   Allows raising the copied scale to the specified arbitrary power.

Make Uniform
   Instead of copying scale for individual axes, apply a uniform scaling factor
   to all axes of the owner that achieves the same overall change in volume.

Offset
   When enabled, the constraint combines the copied scale with the owner's scale,
   instead of overwriting it.

Additive
   Uses addition instead of multiplication in the implementation of the *Offset* option.

Target/Owner
   Standard conversion between spaces.
   See :ref:`common constraint properties <rigging-constraints-interface-common-space>` for more information.

Influence
   Controls the percentage of affect the constraint has on the object.
   See :ref:`common constraint properties <bpy.types.constraint.influence>` for more information.

.. note::

   Since scale is a multiplicative quantity, it should be combined using multiplication,
   and split into fractions or inverted via power. Thus the use of *Power* is
   more mathematically correct than *Influence*, which uses linear interpolation.
   The use of the *Additive* option is also not recommended.

.. tip::

   To copy scale from one axis of the target to all axes of the owner,
   disable other axes, enable *Make Uniform*, and set *Power* to 3.


Example
=======

.. peertube:: 2d3eab8a-cc80-4d90-a3f1-419e2aa063f3
