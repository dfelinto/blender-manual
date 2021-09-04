.. index:: Object Constraints; Pivot Constraint
.. _bpy.types.PivotConstraint:

****************
Pivot Constraint
****************

The *Pivot* constraint allows the owner to rotate around a target object.
It was originally intended for pivot joints found in humans
e.g. fingers, feet, elbows, etc.


Options
=======

.. figure:: /images/animation_constraints_relationship_pivot_panel.png

   Pivot panel.

Target
   :ref:`ui-data-id` for the selection of the object to be used as a pivot point.
   See :ref:`common constraint properties <rigging-constraints-interface-common-target>` for more information.

Use Relative Offset
   Offset will be an absolute point in space instead of relative to the target.

Pivot Point X, Y, Z
   Offset of pivot from target.

Rotation Range
   Rotation range on which pivoting should occur.

   Always
      Use the pivot point in every rotation.
   -X/-Y/-Z/X/Y/Z Rotation
      Use the pivot point in the corresponding direction around the corresponding axis.

Influence
   Controls the percentage of affect the constraint has on the object.
   See :ref:`common constraint properties <bpy.types.constraint.influence>` for more information.


Example
=======

.. peertube:: 1505f963-e5b7-4c31-96e8-d33ff09db532
