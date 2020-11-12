.. index:: Object Constraints; Copy Rotation Constraint
.. _bpy.types.CopyRotationConstraint:

************************
Copy Rotation Constraint
************************

The *Copy Rotation* constraint forces its owner to match the rotation of its target.


Options
=======

.. figure:: /images/animation_constraints_transform_copy-rotation_panel.png

   Copy Rotation panel.

Target
   :ref:`ui-data-id` used to select the constraints target, and is not functional (red state) when it has none.
   See :ref:`common constraint properties <rigging-constraints-interface-common-target>` for more information.

Order
   Allows specifying which :term:`Euler` order to use during the copy operation.
   Defaults to the order of the owner.

Axis
   These buttons control which axes are constrained.

Invert
   Invert their respective corresponding axis coordinates.

Mix
   Specifies how the new rotation is combined with the existing rotation.

   Replace
      The new axis values replace existing values.
   Add
      The new axis values are added to the existing values.
   Before Original
      The new rotation is added before the existing rotation, as if it was applied to
      a parent of the constraint owner.
   After Original
      The new rotation is added after the existing rotation, as if it was applied to
      a child of the constraint owner.
   Offset (Legacy)
      This replicates the behavior of the original Offset checkbox. It was intended
      to be similar to the *Before Original* behavior, but does not work correctly
      with multiple axis rotations, and is thus deprecated.

Target/Owner
   Standard conversion between spaces.
   See :ref:`common constraint properties <rigging-constraints-interface-common-space>` for more information.

Influence
   Controls the percentage of affect the constraint has on the object.
   See :ref:`common constraint properties <bpy.types.constraint.influence>` for more information.


Example
=======

.. vimeo:: 171073854
