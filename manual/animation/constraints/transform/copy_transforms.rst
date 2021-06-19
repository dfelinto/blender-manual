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

Mix
   Specifies how the copied transformation is combined with the existing transformation.

   Replace
      The new transformation replaces the existing transformation.
   Before Original
      The new transformation is added before the existing transformation, as if it was
      applied to an imaginary parent of the constraint owner. Scale is handled like in
      the :ref:`Aligned Inherit Scale <bpy.types.EditBone.inherit_scale>` mode of bones
      to avoid creating shear.
   After Original
      The new transformation is added after the existing transformation, as if it was
      applied locally to an imaginary child of the constraint owner. Scale is handled like
      in the :ref:`Aligned Inherit Scale <bpy.types.EditBone.inherit_scale>` mode of bones
      to avoid creating shear.

Target/Owner
   Standard conversion between spaces.
   See :ref:`common constraint properties <rigging-constraints-interface-common-space>` for more information.

Influence
   Controls the percentage of affect the constraint has on the object.
   See :ref:`common constraint properties <bpy.types.constraint.influence>` for more information.


Example
=======

.. vimeo:: 171108888
