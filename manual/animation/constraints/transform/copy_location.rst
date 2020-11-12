.. index:: Object Constraints; Copy Location Constraint
.. _bpy.types.CopyLocationConstraint:

************************
Copy Location Constraint
************************

The *Copy Location* constraint forces its owner to have the same location as its target.

.. important::

   Note that if you use such a constraint on a *connected* bone, it will have
   no effect, as it is the parent's tip which controls the position of your
   owner bone's root.


Options
=======

.. figure:: /images/animation_constraints_transform_copy-location_panel.png

   Copy Location panel.

Target
   :ref:`ui-data-id` used to select the constraints target, and is not functional (red state) when it has none.
   See :ref:`common constraint properties <rigging-constraints-interface-common-target>` for more information.

Axis
   These buttons control which axes are constrained.

Invert
   Invert their respective corresponding axis coordinates.

Offset
   When enabled, this control allows the owner to be moved (using its current transform properties),
   relative to its target's position.

Target/Owner
   Standard conversion between spaces.
   See :ref:`common constraint properties <rigging-constraints-interface-common-space>` for more information.

Influence
   Controls the percentage of affect the constraint has on the object.
   See :ref:`common constraint properties <bpy.types.constraint.influence>` for more information.


Examples
========

.. vimeo:: 170198049


Animation
---------

Let us animate the *Copy Location* constraint and its *Offset* button. For example,
you can make your owner (let us call it "moon") describe perfect circles centered on the (0.0, 0.0, 0.0)
point (using e.g. pydriven *LocX*/*LocY* animation curves, see :doc:`Drivers </animation/drivers/index>`),
and then make it copy the location of a target (call it "earth", for example) with the *Offset* button enabled.
Congratulation, you just modeled a satellite in a (simplified) orbit around its planet.
Just do the same thing with its planet around its star (which you might call "sun", what do you think?),
and why not, for the star around its galaxy.

Here is a small animation of a "solar" system created using (among a few others)
the technique described above:

.. vimeo:: 15187945

Note that, this "solar" system is not realistic at all
(the wrong scale, the "earth" is rotating in the wrong direction around the "sun", ...).

You can download
the `blend-file <https://wiki.blender.org/wiki/File:ManAnimationTechsUsingConstraintsExSolarSys.blend>`__
used to create this animation.

Furthermore you can also animate a few properties of each constraint using animation curves:
e.g. you can animate the *Influence* of a constraint.
It is used to first stick the camera to the "moon", then to the "earth",
and finally to nothing, using two *Copy Location* constraints with *Offset* set.
