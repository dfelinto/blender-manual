.. index:: Object Constraints; Limit Distance Constraint
.. _bpy.types.LimitDistanceConstraint:

*************************
Limit Distance Constraint
*************************

The *Limit Distance* constraint forces its owner to stay either further from,
nearer to, or exactly at a given distance from its target. In other words,
the owner's location is constrained either outside, inside,
or at the surface of a sphere centered on its target.

When you specify a (new) target, the *Distance* value is automatically set to
correspond to the distance between the owner and this target.

.. important::

   Note that if you use such a constraint on a *connected* bone, it will have
   no effect, as it is the parent's tip which controls the position of your
   owner bone's root.


Options
=======

.. figure:: /images/animation_constraints_transform_limit-distance_panel.png

   Limit Distance panel.

Target
   :ref:`ui-data-id` used to select the constraint's target, and is not functional (red state) when it has none.
   See :ref:`common constraint properties <rigging-constraints-interface-common-target>` for more information.

Distance
   This number field sets the limit distance, i.e. the radius of the constraining sphere.

   Reset Distance ``X``
      When clicked, this small button will reset the *Distance* value,
      so that it corresponds to the actual distance between the owner and its target
      (i.e. the distance before this constraint is applied).

Clamp Region
   The *Limit Mode* select menu allows you to choose how to use the sphere
   defined by the *Distance* setting and target's origin:

   Inside
      The owner is constrained *inside* the sphere.
   Outside
      The owner is constrained *outside* the sphere.
   Surface
      The owner is constrained *on the surface* of the sphere.

Affect Transform
   Transform operators will take the constraint into account to immediately restrict
   the resulting transform property values.

Target/Owner
   Standard conversion between spaces.
   See :ref:`common constraint properties <rigging-constraints-interface-common-space>` for more information.

Influence
   Controls the percentage of affect the constraint has on the object.
   See :ref:`common constraint properties <bpy.types.constraint.influence>` for more information.

.. tip::

   Evaluating both owner and target in a :ref:`Custom Space <rigging-constraints-interface-common-space-types>`
   using the root bone or any other suitable parent bone will automatically scale the effective distance with
   the relevant part of the rig.


Example
=======

.. peertube:: 9e842440-3133-4550-be4f-8fe73d7dfee0
