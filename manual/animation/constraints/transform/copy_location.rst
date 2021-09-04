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

.. peertube:: 2f3dc43b-ef61-42ae-9d8e-7924a1758411


Animation
---------

Let us animate a solar system with the *Copy Location* constraint and its *Offset* option.
You can make the owner, called "moon", describe perfect circles centered on the world origin
(using e.g. *Location X/Y* sine and cosine F-curves, see :ref:`bpy.types.FModifierFunctionGenerator`).
Then copy the location of a target "earth" with the *Offset* checkbox enabled
to model a satellite in a (simplified) orbit around its planet.
Repeat these steps for more planets circling around its center star "sun".

Following video is a small animation of a solar system created using (among a few others)
the previously described technique:

.. peertube:: ff427260-9631-40d9-bd39-65f21f95e9ad

Note that, this 'solar' system is not realistic at all
(the wrong scale, the earth is rotating in the wrong direction around the sun, ...).

You can download
the `blend-file <https://wiki.blender.org/wiki/File:ManAnimationTechsUsingConstraintsExSolarSys.blend>`__
used to create this animation.

Furthermore you can also animate a few properties of each constraint using animation curves:
e.g. you can animate the *Influence* of a constraint.
It is used to first let the camera follow the moon, then the earth,
and finally using two *Copy Location* constraints with *Offset* set.
