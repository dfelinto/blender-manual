.. index:: Object Constraints; Action Constraint
.. _bpy.types.ActionConstraint:

*****************
Action Constraint
*****************

The *Action* constraint is powerful.
It allows you control
an :doc:`Action </editors/dope_sheet/action>` using the transformations of another object.

The underlying idea of the *Action* constraint is very similar to the one behind
the :doc:`Drivers </animation/drivers/index>`, except that the former uses a whole action
(i.e. multiple F-Curves of the same type), while the latter controls a single F-Curve of their "owner"...

Note that even if the constraint accepts the *Mesh* action type,
only the *Object*, *Pose* and *Constraint* types are really working,
as constraints can only affect objects' or bones' transform properties, and not meshes' shapes.
Also note that only the object transformation (location, rotation, scale) is affected by the action,
if the action contains keyframes for other properties they are ignored, as constraints do not influence those.

As an example, let us assume you have defined an *Object* action
(it can be assigned to any object, or even no object at all),
and have mapped it on your owner through an *Action* constraint,
so that moving the target in the (0.0 to 2.0)
range along its X axis maps the action content on the owner in the (0 to 100)
frame range. This will mean that when the target's *X* property is 0.0
the owner will be as if in frame 0 of the linked action;
with the target's *X* property at 1.0
the owner will be as if in frame 50 of the linked action, etc.


Options
=======

.. figure:: /images/animation_constraints_relationship_action_panel.png

   Action panel.

Target
   :ref:`ui-data-id` used to select the constraints target, and is not functional (red state) when it has none.
   See :ref:`common constraint properties <rigging-constraints-interface-common-target>` for more information.

Evaluation Time
   This property allows objects to be driven without a constraint target
   by interpolating between the *Action Start* and *End* frames.
   The relative position between the start and end frame can be controlled using the value slider.

   This is very helpful for more complex rigging and mechanical rigs, as it means the Action constraint
   can be controlled directly with a :doc:`Driver </animation/drivers/index>`
   or :ref:`Custom Property <files-data_blocks-custom-properties>`.

Mix
   Specifies how the keyframed transformation from the action is combined with the existing transformation.
   These modes are the same as in the :doc:`Copy Transforms </animation/constraints/transform/copy_transforms>`
   constraint.

   Before/After Original (Full)
      The keyframed transformation is added before/after the existing transformation, as if it was
      applied to an imaginary parent/child of the constraint owner. Scale is handled like in
      the most basic :ref:`Full Inherit Scale <bpy.types.EditBone.inherit_scale>` mode of bones,
      so combining non-uniform scale and rotation will create shear.

   Before/After Original (Aligned)
      The keyframed transformation is added before/after the existing transformation, as if it was
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

   .. warning::

      For technical reasons modes other than *After Original (Full)* and *After Original (Aligned)* may
      not work as expected for constraints on *objects* (not bones) without a parent.

Influence
   Controls the percentage of affect the constraint has on the object.
   See :ref:`common constraint properties <bpy.types.constraint.influence>` for more information.


Target
------

Channel
   This selector controls which transform property
   (location, rotation or scale along/around one of its axes) from the target to use as "action driver".

Target
   This constraint allows you to choose in which space to evaluate its target's transform properties.

Range Min, Max
   The lower and upper bounds of the driving transform property value.

   .. warning::

      Unfortunately, here again we find the constraint's limitations:

      - When using a rotation property as "driver",
        these values are "mapped back" to the (-180.0 to 180.0) range.
      - When using a scale property as "driver", these values are limited to null or positive values.


Action
------

Action
   Select the name of the action you want to use.

   .. warning::

      Even though it might not be in red state (UI refresh problems...),
      this constraint is obviously not functional when this field does not contain a valid action.

Object Action
   Bones **only**, when enabled,
   this option will make the constrained bone use the "object" part of the linked action,
   instead of the "same-named pose" part. This allows you to apply the action of an object to a bone.

Frame Start, End
   The starting and ending frames of the action to be mapped.

   .. note::

      - These values must be strictly positive.
      - By default, both values are set to 0, which disables the mapping
        (i.e. the owner just gets the properties defined at frame 0 of the linked action...).


.. (TODO rewrite) Notes section is a mess.

Notes
=====

- When the object or bone already has Action constraints, the next constraint using
  a newly keyframed action should be added before all others in order to get
  the same final combined transformation. This fact is not affected by the Mix mode.
- Unlike usual, you can have a *Start* value higher than the *End* one,
  or a *Min* one higher than a *Max* one: this will reverse the mapping of the action
  (i.e. it will be "played" reversed...), unless you have both sets reversed, obviously!
- When using a *Constraint* action, it is the constraint *channel's names*
  that are used to determine to which constraints of the owner apply the action.
  E.g. if you have a constraint channel named "trackto_empt1",
  its keyed *Influence* and/or *Head/Tail* values (the only ones you can key)
  will be mapped to the ones of the owner's constraint named "trackto_empt1".
- Similarly, when using a *Pose* action
  (which is obviously only meaningful and working when constraining a bone!),
  it is the bone's name that is used to determine which bone *channel's names* from the action to use
  (e.g. if the constrained bone is named "arm", it will use and only use the action's bone channel named "arm"...).
  Unfortunately, using a *Pose* action on a whole armature object
  (to affect all the keyed bones in the action at once) will not work...
- Actions can also be marked as :term:`Asset`, but with certain limitations.
  For more info, see :doc:`/animation/armatures/posing/editing/pose_library`.


Example
=======

.. peertube:: c138e7b5-34cb-49cb-af07-d5d5f27f1cfb
