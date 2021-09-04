.. index:: Object Constraints; Spline IK Constraint
.. _bpy.types.SplineIKConstraint:

********************
Spline IK Constraint
********************

The *Spline IK* constraint aligns a chain of bones along a curve.
By leveraging the ease and flexibility of achieving aesthetically
pleasing shapes offered by curves and the predictability and well-integrated
control offered by bones, *Spline IK* is an invaluable tool in the riggers' toolbox.
It is particularly well suited for rigging flexible body parts such as tails, tentacles,
and spines, as well as inorganic items such as ropes.

To set up *Spline IK*, it is necessary to have a chain of
connected bones and a curve to constrain these bones to:

- With the last bone in the chain selected,
  add a *Spline IK* constraint from the *Bone Constraints* tab in the *Properties*.
- Set the 'Chain Length' setting to the number of bones in the chain
  (starting from and including the selected bone)
  that should be influenced by the curve.
- Finally, set *Target* to the curve that should control the curve.

.. note::

   The IK constraints are special in that they modify multiple bones.
   For this reason, they ignore their position in the stack and always run after
   all other constraints on the affected bones. To apply constraints after IK,
   it is necessary to first copy the final transformation to a new bone chain,
   e.g. using :doc:`Copy Transforms </animation/constraints/transform/copy_transforms>`.


Options
=======

.. figure:: /images/animation_constraints_tracking_spline-ik_panel.png

   Spline IK panel.

Target
   :ref:`ui-data-id` used to select the target curve.
   See :ref:`common constraint properties <rigging-constraints-interface-common-target>` for more information.

Influence
   Controls the percentage of affect the constraint has on the object.
   See :ref:`common constraint properties <bpy.types.constraint.influence>` for more information.


Fitting
-------

Chain Length
   How many bones are included in the chain.

Even Division
   Ignore the relative length of the bones when fitting to the curve.

Chain Offset
   Retain the offset of the root joint from the start point of the curve.


Chain Scaling
-------------

Use Curve Radius
   Average radius of the endpoints is used to tweak the X and Z scaling of
   the bones, on top of the X and Z scale mode.

Y Scale Mode
   Specifies how the length of a bone is scaled when it is fitted to the curve,
   in addition to the effects of target curve object scale and curvature.

   None
      The bone is reset to its rest pose length.
   Fit Curve
      The bones are stretched to cover the entire length of the curve.
   Bone Original
      The original Y axis scale of the bone is used.

XZ Scale Mode
   Scaling that a bone undergoes in the other two directions.

   None
      Do not scale the X and Z axes.
   Bone Original
      Use the original scaling of the bones.
   Inverse Scale
      Scale of the X and Z axes is the inverse of the Y scale.
   Volume Preservation
      Similar to the :ref:`Stretch To <constraints-stretch-to-volume-preservation>` constraint.

Use Original Scale
   Specifies that *Inverse Scale* or *Volume Preservation* should be applied on top of
   the original scaling of the bones, like in the Stretch To constraint.

.. seealso::

   This subject is seen in-depth in
   the :doc:`Armature Posing section </animation/armatures/posing/bone_constraints/inverse_kinematics/spline_ik>`.


Example
=======

.. peertube:: c17c1489-e4ae-440a-85e5-3ca5349d0cb9
