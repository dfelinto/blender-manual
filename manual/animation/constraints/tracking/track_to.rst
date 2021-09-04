.. index:: Object Constraints; Track To Constraint
.. _bpy.types.TrackToConstraint:

*******************
Track To Constraint
*******************

The *Track To* constraint applies rotations to its owner,
so that it always points a given "To" axis towards its target,
with another "Up" axis permanently maintained as much aligned with the global Z axis
(by default) as possible. This tracking is similar to the "billboard tracking" in 3D
(see note below).

This is the preferred tracking constraint,
as it has a more easily controlled constraining mechanism.

This constraint shares a close relationship to
the :doc:`Inverse Kinematics constraint </animation/constraints/tracking/ik_solver>` in some ways.

.. tip:: Billboard Tracking

   The term "billboard" has a specific meaning in real-time CG programming (i.e. video games!),
   where it is used for plane objects always facing the camera
   (they are indeed "trackers", the camera being their "target").
   Their main usage is as support for tree or mist textures:
   if they were not permanently facing the camera, you would often see your trees squeezing to nothing,
   or your mist turning into a mille-feuille paste, which would be funny but not so credible.


Options
=======

.. figure:: /images/animation_constraints_tracking_track-to_panel.png

   Track To panel.

Target
   :ref:`ui-data-id` used to select the constraints target, and is not functional (red state) when it has none.
   See :ref:`common constraint properties <rigging-constraints-interface-common-target>` for more information.

Track Axis
   The tracking local axis, i.e. the owner's axis to point at the target.
   The negative options force the relevant axis to point away from the target.

Up
   The "upward-most" local axis, i.e. the owner's axis to be aligned (as much as possible)
   with the global Z axis (or target Z axis, when the *Target* button is enabled).

Target Z
   By default, the owner's *Up* axis is (as much as possible) aligned with the global Z axis,
   during the tracking rotations. When this button is enabled, the *Up* axis will be (as much as possible)
   aligned with the target's local Z axis?

Target/Owner
   Standard conversion between spaces.
   See :ref:`common constraint properties <rigging-constraints-interface-common-space>` for more information.

Influence
   Controls the percentage of affect the constraint has on the object.
   See :ref:`common constraint properties <bpy.types.constraint.influence>` for more information.

.. warning::

   If you choose the same axis for *Tracking Axis* and *Up*,
   the constraint will not be functional anymore (red state).


Example
=======

.. peertube:: 891bf27f-f782-4908-bfa0-f99e5dc46107
