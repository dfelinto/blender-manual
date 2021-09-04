.. index:: Object Constraints; Locked Track Constraint
.. _bpy.types.LockedTrackConstraint:

***********************
Locked Track Constraint
***********************

The *Locked Track* constraint is a bit tricky to explain, both graphically and textual.
Basically, it is a :doc:`Track To constraint </animation/constraints/tracking/track_to>`,
but with a locked axis, i.e.
an axis that cannot rotate (change its orientation). Hence,
the owner can only track its target by rotating around this axis,
and unless the target is in the plane perpendicular to the locked axis, and crossing the owner,
this owner cannot really point at its target.

Let us take the best real-world equivalent: a compass.
It can rotate to point in the general direction of its target
(the magnetic North, or a neighbor magnet), but it cannot point *directly at it*,
because it spins like a wheel on an axle.
If a compass is sitting on a table and there is a magnet directly above it,
the compass cannot point to it. If we move the magnet more to one side of the compass,
it still cannot point *at* the target,
but it can point in the general direction of the target,
and still obey its restrictions of the axle.

When using a *Locked Track* constraint, you can think of the target as a magnet,
and the owner as a compass.
The *Lock* axis will function as the axle around which the owner spins,
and the *To* axis will function as the compass' needle.
Which axis does what is up to you!

If you have trouble understanding the buttons of this constraint, read the tooltips,
they are pretty good. If you do not know where your object's axes are,
enable *Axis* in :menuselection:`Properties --> Armature --> Viewport Display`.
Or, if you are working with bones, turn on the *Axes* in the armature's *Viewport Display* panel.

This constraint was designed to work cooperatively with the *Track To* constraint.
If you set the axes buttons right for these two constraints,
*Track To* can be used to point the axle at a primary target,
and *Locked Track* can spin the owner around that axle to a secondary target.

This constraint also works very well for 2D billboarding.


Options
=======

.. figure:: /images/animation_constraints_tracking_locked-track_panel.png

   Locked track panel.

Target
   :ref:`ui-data-id` used to select the constraints target, and is not functional (red state) when it has none.
   See :ref:`common constraint properties <rigging-constraints-interface-common-target>` for more information.

Track Axis
   The tracking local axis, i.e. the owner's axis to point at the target.
   The negative options force the relevant axis to point away from the target.

Locked Axis
   The locked local axis, i.e. the owner's axis which cannot be re-oriented to track the target.

.. important::

   If you choose the same axis for *Tracking Axis* and *Locked Axis*,
   the constraint will no longer be functional (red state).

Influence
   Controls the percentage of affect the constraint has on the object.
   See :ref:`common constraint properties <bpy.types.constraint.influence>` for more information.


Example
=======

.. peertube:: 5ce2dc9b-de49-4977-8e1f-9ddd5c2366d7
