
..    TODO/Review: {{review|text=Notes section is a mess.}} .


Action Constraint
=================

The :guilabel:`Action` constraint is powerful. It allows you control an :doc:`Action <animation/editors/dopesheet/action>` using the transformations of another object.

The underlying idea of the :guilabel:`Action` constraint is very similar to the one behind the :doc:`Drivers <animation/editors/graph/drivers>`\ , except that the former uses a whole action (i.e. a bunch a Fcurves of the same type), while the latter controls a single Fcurve of their "owner"…

Note that even if the constraint accepts the :guilabel:`Mesh` action type,
only the :guilabel:`Object`\ ,
:guilabel:`Pose` and :guilabel:`Constraint` types are really working,
as constraints can only affect objects' or bones' transform properties,
and not meshes' shapes… . Also note that only the object transformation (location, rotation,
scale) is affected by the action,
if the action contains keyframes for other properties they are ignored,
as constraints do not influence those.

As an example, let's assume you have defined an :guilabel:`Object` action
(it can be assigned to any object, or even no object at all),
and have mapped it on your owner through an :guilabel:`Action` constraint,
so that moving the target in the ``[0.0,
2.0]`` range along its X axis maps the action content on the owner in the ``[0,
100]`` frame range. This will mean that when the target's X property is **0.0**\ ,
the owner will be as if in frame **0** of the linked action;
with the target's X property at **1.0**\ ,
the owner will be as if in frame **50** of the linked action, etc.


Options
-------

.. figure:: /images/25-Manual-Constraints-Relationship-Action.jpg
   :width: 293px
   :figwidth: 293px

   Action panel


:guilabel:`Target`
   This constraint uses one target, and is not functional (red state) when it has none.

:guilabel:`Bone`\ :
   When target is an armature object, use this field to select the target bone.

:guilabel:`Transform Channel`
    This drop-down list controls which transform property (location, rotation or scale along/around one of its axes) from the target to use as "action driver".

:guilabel:`Target Space`
    This constraint allows you to choose in which space to evaluate its target's transform properties.

:guilabel:`To Action`
    Select the name of the action you want to use.

 .. warning::

   FIXME - warning body below

 Even though it might not be in red state (UI refresh problems…), this constraint is obviously not functional when this field does not contain a valid action.

:guilabel:`Object Action`
   **Bones only**\ , when enabled, this option will make the constrained bone use the "object" part of the linked action, instead of the "same-named pose" part. This allows you to apply the action of an object to a bone.

:guilabel:`Target Range` :guilabel:`Min`\ /\ :guilabel:`Max`
    The lower and upper bounds of the driving transform property value.
    By default, both values are set to **0.0**

 .. warning::

   FIXME - warning body below

 Unfortunately, here again we find the constraints limitations:

   - When using a rotation property as "driver", these values are "mapped back" to the ``[-180.0- , 180.0- [`` range.
   - When using a scale property as "driver", these values are limited to null or positive values.

:guilabel:`Action Range` :guilabel:`Start`\ /\ :guilabel:`End`
    The starting and ending frames of the action to be mapped.
    Note that:

   - These values must be strictly positive.
   - By default, both values are set to **0**\ , which disables the mapping (i.e. the owner just gets the properties defined at frame **0** of the linked action…).


Notes
-----

- When the linked action affects some location properties, the owner's existing location is added to the result of evaluating this constraint (exactly as when the :guilabel:`Offset` button of the :doc:`Copy Location constraint <constraints/transform/copy_location>` is enabled…).
- When the linked action affects some scale properties, the owner's existing scale is multiplied with the result of evaluating this constraint.
- When the linked action affects some rotation properties, the owner's existing rotation is overridden by the result of evaluating this constraint.
- Unlike usual, you can have a :guilabel:`Start` value higher than the :guilabel:`End` one, or a :guilabel:`Min` one higher than a :guilabel:`Max` one: this will reverse the mapping of the action (i.e. it will be "played" reversed…), unless you have both sets reversed, obviously!
- When using a :guilabel:`Constraint` action, it is the constraint *channel's names* that are used to determine to which constraints of the owner apply the action. E.g. if you have a constraint channel named "trackto_empt1", its keyed :guilabel:`Influence` and/or :guilabel:`Head/Tail` values (the only ones you can key) will be mapped to the ones of the owner's constraint named "trackto_empt1".
- Similarly, when using a :guilabel:`Pose` action (which is obviously only meaningful and working when constraining a bone!), it is the bone's name that is used to determine which bone *channel's names* from the action to use (e.g. if the constrained bone is named "arm", it will use and only use the action's bone channel named "arm"…). Unfortunately, using a :guilabel:`Pose` action on a whole armature object (to affect all the keyed bones in the action at once) won't work…
- Note also that you can use the :doc:`pose library feature <rigging/posing/pose_library>` to create/edit a :guilabel:`Pose` action datablock… just remember that in this situation, there's one pose per frame!


