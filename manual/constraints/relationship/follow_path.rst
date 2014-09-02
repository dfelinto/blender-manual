
..    TODO/Review: {{review|im=examples}} .

Follow Path Constraint
**********************

The :guilabel:`Follow Path` constraint places its owner onto a *curve* target object,
and makes it move along this curve (or path).
It can also affect its owner's rotation to follow the curve's bends,
when the :guilabel:`Follow Curve` option is enabled.

The owner is always evaluated in the global (world) space:

- Its location (as shown in the :guilabel:`Transform Properties` panel, :kbd:`N`) is used as an offset from its normal position on the path. E.g. if you have an owner with the ``(1.0, 1.0, 0.0)`` location, it will be one BU away from its normal position on the curve, along the X and Y axis. Hence, if you want your owner *on* its target path, clear its location (:kbd:`alt-G`)!
- This location offset is also proportionally affected by the *scale of the target curve*. Taking the same ``(1.0, 1.0, 0.0)`` offset as above, if the curve has a scale of ``(2.0, 1.0, 1.0)``, the owner will be offset *two* BU along the X axis (and one along the Y one)...
- When the :guilabel:`Curve Follow` option is enabled, its rotation is also offset to the one given by the curve (i.e. if you want the Y axis of your object to be aligned with the curve's direction, it must be in rest, non-constrained state, aligned with the global Y axis). Here again, clearing your owner's rotation (:kbd:`alt-R`) might be useful...

The movement of the owner along the target curve/path may be controlled in two different ways:

- The most simple is to define the number of frames of the movement,
  in the Path Animation panel of the Object Data context,
  via the numeric field Frames, and its start frame via the constraint's Offset option
  (by default, start frame: 1 [= offset of 0)], duration: 100).
- The second way, much more precise and powerful, is to define a :guilabel:`Evaluation Time` interpolation curve for the :guilabel:`Target` path (in the :guilabel:`Graph Editor`.  See the :doc:`animation chapter </animation>` to learn more about Fcurves.
- If you don't want your owner to move along the path, you can give to the target curve a flat :guilabel:`Speed` FCurve (its value will control the position of the owner along the path).

:guilabel:`Follow Path` is another constraint that works well with the :doc:`Locked Track one </constraints/tracking/locked_track>`. One example is a flying camera on a path. To control the camera's roll angle, you can use a :guilabel:`Locked Track` and a target object to specify the up direction, as the camera flies along the path.


.. note:: :guilabel:`Follow Path` and :guilabel:`Clamp To`

   Do not confuse these two constraints. Both of them constraint the location of their owner along a curve,
   but :guilabel:`Follow Path` is an "animation-only" constraint,
   inasmuch that the position of the owner along the curve is determined by the time (i.e. current frame),
   whereas the :doc:`Clamp To </constraints/tracking/clamp_to>` :guilabel:`constraint` determines the position of its
   owner along the curve using one of its location properties' values.



.. note::

   Note that you also need to keyframe Evaluation Time for the Path. Select the path, go to the path properties,
   set the overall frame to the first frame of the path (e.g. frame 1),
   set the value of Evaluation time to the first frame of the path (e.g. 1), right click on Evaluation time,
   select create keyframe, set the overall frame to the last frame of the path (e.g. frame 100),
   set the value of Evaluation time to the last frame of the path (e.g. 100), right click on Evaluation time,
   select create keyframe. ..    Comment: <!-- from http://overshoot.tv/node/1123 paragraph needs cleanup but this
   definitely needs to be in the documentation --> .



Options
=======

.. figure:: /images/25-Manual-Constraints-Relationship-FollowPath.jpg
   :width: 305px
   :figwidth: 305px

   Follow Path panel


:guilabel:`Target`
   This constraint uses one target, which *must be a curve object*,
   and is not functional (red state) when it has none.

:guilabel:`Curve Radius`
   Objects scale by the curve radius. See :doc:`Curve Editing </modeling/curves/editing/advanced>`
:guilabel:`Fixed Position`
   Object will stay locked to a single point somewhere along the length of the curve regardless of time
:guilabel:`Offset`
   The number of frames to offset from the "animation" defined by the path (by default, from frame **1**).
:guilabel:`Follow Curve`
   If this option is not activated, the owner's rotation isn't modified by the curve; otherwise,
   it's affected depending on the following options:

   :guilabel:`Forward`
      The axis of the object that has to be aligned with the forward direction of the path
      (i.e. tangent to the curve at the owner's position).
   :guilabel:`Up`
      The axis of the object that has to be aligned (as much as possible) with the world Z axis.
      In fact, with this option activated, the behavior of the owner shares some properties with
      the one caused by a :doc:`Locked Track constraint </constraints/tracking/locked_track>`,
      with the path as "axle", and the world Z axis as "magnet".


