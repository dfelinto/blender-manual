
..    TODO/Review: {{review
   |im=examples
   }} .


Locked Track Constraint
***********************

The :guilabel:`Locked Track` constraint is a bit tricky to explain, both graphically and textually. Basically, it is a :doc:`Track To constraint </constraints/tracking/track_to>`, but with a locked axis, i.e. an axis that cannot rotate (change its orientation). Hence, the owner can only track its target by rotating around this axis, and unless the target is in the plane perpendicular to the locked axis, and crossing the owner, this owner cannot really point at its target.

Let's take the best real world equivalent: a compass.
It can rotate to point in the general direction of its target (the magnetic North,
or a neighbor magnet), but it can't point *directly at it*,
because it spins like a wheel on an axle.
If a compass is sitting on a table and there is a magnet directly above it,
the compass can't point to it. If we move the magnet more to one side of the compass,
it still can't point *at* the target,
but it can point in the general direction of the target,
and still obey its restrictions of the axle.

When using a :guilabel:`Locked Track` constraint, you can think of the target as a magnet,
and the owner as a compass.
The :guilabel:`Lock` axis will function as the axle around which the owner spins,
and the :guilabel:`To` axis will function as the compass' needle.
Which axis does what is up to you!

If you have trouble understanding the buttons of this constraint, read the tool-tips,
they are pretty good. If you don't know where your object's axes are,
turn on the :guilabel:`Axis` button in the :guilabel:`Object` menu's :guilabel:`Draw` panel.
Or, if you're working with bones, turn on the :guilabel:`Axes` button in the
:guilabel:`Armature` menu's :guilabel:`Display` panel.

This constraint was designed to work cooperatively with the :guilabel:`Track To` constraint.
If you set the axes buttons right for these two constraints,
:guilabel:`Track To` can be used to point the axle at a primary target,
and :guilabel:`Locked Track` can spin the owner around that axle to a secondary target.

This constraints also works very well for 2D billboarding.

This is all related to the topic discussed at length in the :doc:`2.49 BSoD tracking tutorial </ls/animation/armatures/bsod/tracking>`.


Options
=======

.. figure:: /images/25-Manual-Constraints-Tracking-LockedTrack.jpg
   :width: 304px
   :figwidth: 304px

   Locked track panel


:guilabel:`Target`
   This constraint uses one target, and is not functional (red state) when it has none.

:guilabel:`To`
   The tracking local axis (:guilabel:`Y` by default), i.e. the owner's axis to point at the target. The negative options force the relevant axis to point away from the target.

:guilabel:`Lock`
   The locked local axis (:guilabel:`Z` by default), i.e. the owner's axis which cannot be re-oriented to track the target.


 .. warning::

   FIXME - warning body below

 If you choose the same axis for *To* and *Lock*, the constraint will no longer be functional (red state).


