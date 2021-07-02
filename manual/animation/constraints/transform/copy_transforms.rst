.. index:: Object Constraints; Copy Transforms Constraint
.. _bpy.types.CopyTransformsConstraint:

**************************
Copy Transforms Constraint
**************************

The *Copy Transforms* constraint forces its owner to have the same transforms as its target.


Options
=======

.. figure:: /images/animation_constraints_transform_copy-transforms_panel.png

   Copy Transforms panel.

Target
   :ref:`ui-data-id` used to select the constraints target, and is not functional (red state) when it has none.
   See :ref:`common constraint properties <rigging-constraints-interface-common-target>` for more information.

Remove Target Shear
   Removes shearing from the target transformation after the target space conversion, ensuring it consists purely
   of translation, rotation and scale. Note that :doc:`Copy Rotation </animation/constraints/transform/copy_rotation>`
   always does this.

Mix
   Specifies how the copied transformation is combined with the existing transformation.

   Replace
      The new transformation replaces the existing transformation.

   Before/After Original (Full)
      The new transformation is added before/after the existing transformation, as if it was
      applied to an imaginary parent/child of the constraint owner. Scale is handled like in
      the most basic :ref:`Full Inherit Scale <bpy.types.EditBone.inherit_scale>` mode of bones,
      so combining non-uniform scale and rotation will create shear.

   Before/After Original (Aligned)
      The new transformation is added before/after the existing transformation, as if it was
      applied to an imaginary parent/child of the constraint owner. Scale is handled like in
      the :ref:`Aligned Inherit Scale <bpy.types.EditBone.inherit_scale>` mode of bones to
      avoid creating shear.

      This is equivalent to using the *Split Channels* option, but replacing the location component with
      the result of *Full*. If only uniform scale is used, the result is identical to *Full*.

   Before/After Original (Split Channels)
      Combines location, rotation and scale components of the transformation separately, similar
      to a sequence of three :doc:`Copy Location </animation/constraints/transform/copy_location>`,
      :doc:`Copy Rotation </animation/constraints/transform/copy_rotation>` and
      :doc:`Copy Scale </animation/constraints/transform/copy_scale>` (with Offset)
      constraints bundled together in one operation; the result may be slightly different
      in case of sheared inputs.

      Unlike *Aligned*, in this mode location channels are simply added together, so rotation
      and scale components of the input transformations cannot affect the resulting location.

   .. TODO: add video comparing mix modes

Target/Owner
   Standard conversion between spaces.
   See :ref:`common constraint properties <rigging-constraints-interface-common-space>` for more information.

Influence
   Controls the percentage of affect the constraint has on the object.
   See :ref:`common constraint properties <bpy.types.constraint.influence>` for more information.


Example
=======

.. vimeo:: 171108888
