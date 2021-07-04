
******
Common
******

.. _rigging-constraints-interface-common-target:

Target
======

The Target :ref:`ui-data-id` field lets you link the constraint to a Target object of your choosing.
This link provides data to the constraint so that it can begin to function.
For example, the Copy Location Constraint needs location data to function.
Fill in the Target field, and the Copy Location constraint will begin to use location data from the Target object.

.. figure:: /images/animation_constraints_interface_common_target.png

   The Target field must be filled in for the constraint to function.

By default, the Target will use the :term:`Object Origin` as the target point.

If the Target field links to a :term:`Mesh` or :term:`Lattice` object, a :term:`Vertex Group` field will appear.
Enter the name of a vertex group and the constraint will target the median point
of this vertex group instead of the object's origin.

.. figure:: /images/animation_constraints_interface_common_target-vertex-group.png

If the Target field links to an :term:`Armature`, a :term:`Bone` field will appear
along with a *Head/Tail* slider.
Enter the name of a bone and the constraint will target the bone instead of the entire armature object origin.

.. figure:: /images/animation_constraints_interface_common_target-bone.png

The slider moves the precise position of the target between the :term:`Head` and :term:`Tail` of the bone.
Some constraints have a button next to the slider
that enables using the curved shape of :ref:`Bendy Bones <bendy-bones>`.


.. _rigging-constraints-interface-common-space:
.. _bpy.types.constraint.owner_space:
.. _bpy.types.constraint.target_space:

Space
=====

Constraints need a frame of reference in order to function.
This frame of reference is called the "space" of the constraint.
Choosing one space vs. another will change this frame of reference
and substantially alter the behavior of a constraint.

To understand how changing the space will change the behavior of the constraint,
consider experimenting with two empties.
Make sure they display as arrows so that you can see the local axes for each empty.
Make sure to size one empty a little larger than the other so that they are both always visible
even if directly on top of each other.
Then add a constraint to one empty that targets the other and experiment thoroughly by
moving, rotating and scaling the target in many different ways.

.. figure:: /images/animation_constraints_interface_common_space.png

   This constraint is set to use World Space as the frame of reference for both
   its *Target* space and its *Owner* space.


Target Space & Owner Space
--------------------------

The space used to evaluate the target of the constraint is called the *Target* space.
The space used to evaluate the constrained object (the object that owns the constraint) is called the *Owner* space.
Hover over the space select menu(s) to learn whether it affects the space of the target
or the space of the owner.

When the constraints use a *Target* and/or/nor an *Owner* space there will be no, one or two selector(s).
The Copy Location constraint in example use both Target **and** *Owner* space.

When a constraint uses both *Target* and *Owner* space,
the Target and Owner can be any combination of space types.


.. _rigging-constraints-interface-common-space-types:

Space Types
-----------

World Space
   In this space type the world is the frame of reference for the object (or bone).
   Location is relative to the world origin.
   Rotation and Scale are oriented to the world axes.
   Transformations to the object, the object's parent and any other constraints
   higher up in the constraint stack are all taken into account.

Local Space
   This space excludes all effects of the parent objects or bones, as well as the rest position
   and orientation of the bone itself. Only transformations applied to the object or bone itself
   are taken into account.

Local with Parent :guilabel:`Bones Only`
   The bone position and orientation is evaluated relative to its rest pose location and orientation,
   thus including both its own transformations and those caused by a possible parent relationship
   (i.e. the chain's transformations above the bone).

Pose Space :guilabel:`Bones Only`
   The bone position and orientation is evaluated in the armature object local space
   (i.e. independently from the armature transformations in *Object Mode*).
   Hence, if the armature object has null transformations,
   *Pose Space* will have the same effect as *World Space*.

Custom Space
   The position and orientation is evaluated relative to the current position and orientation of
   an arbitrary object or bone that is specified via additional input fields that appear when this option is selected.
   This can be used to evaluate the constraint using an arbitrary coordinate system.

Local Space (Owner Orientation) :guilabel:`Bone Targets Only`
   This space works like *Local Space*, with an additional coordinate space transformation
   that compensates for the difference in the rest pose orientations of the owner and target
   bones. If applied as the *Local Space* of the owner, this will produce the same global
   space movement as the target, provided parents are still at rest pose.

   This option replaces the following setup with two additional bones:

   1. An extra `child` bone of the `target`, rotated the same as `owner` in rest pose.
   2. An extra `sibling` bone of the `target`, positioned same as `child` in rest pose and using
      :doc:`Copy Transforms </animation/constraints/transform/copy_transforms>` in *World Space* from `child`.
   3. The constraint uses *Local Space* of `sibling`.

   This video demonstrates the difference from ordinary *Local Space*:

   .. youtube:: UtqZXs7u2Zw

.. _bpy.types.constraint.influence:

Influence
=========

The influence slider determines how much the constraint will affect the constrained object (target).

.. figure:: /images/animation_constraints_interface_common_influence.png

An influence of 0.0 will have no effect.
An influence of 1.0 will have the full effect.

Values between (0.0 and 1.0) will have a partial effect, but be careful.
These partial effects can be difficult to control,
especially as the :doc:`constraint stack </animation/constraints/interface/stack>` grows in complexity.

The influence value is animatable, allowing constraints to be turned off, or partially on as needed.

.. _bpy.ops.constraint.disable_keep_transform:

The ``X`` button after the influence slider can be used to disable the constraint while trying to
preserve the current object position. This may not work perfectly if other constraints remain active.
