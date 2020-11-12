.. (todo 2.78 add) images: https://code.blender.org/2016/05/
.. an-in-depth-look-at-how-b-bones-work-including-details-of-the-new-bendy-bones/

.. _bendy-bones:

***********
Bendy Bones
***********

.. admonition:: Reference
   :class: refbox

   :Mode:      All Modes
   :Panel:     :menuselection:`Bone --> Bendy Bones`

Bendy Bones (B-Bones) are an easy way to replace long chains of many small rigid bones.
A common use case for curved bones is to model spine columns or facial bones.


Technical Details
=================

Blender treats the bone as a section of a Bézier curve passing through the bones' joints.
Each of the *Segments* will bend and roll to follow this invisible curve
representing a tessellated point of the Bézier curve.
The control points at each end of the curve are the endpoints of the bone.
The shape of the B-Bones can be controlled using a series of properties or
indirectly through the neighboring bones (i.e. first child and parent).
The properties construct handles on either end of the bone to control the curvature.

.. move to constraint > common?

When using the B-bone as a constraint target :ref:`ui-data-id` offers an option to follow the curvature.

.. note::

   However, if the bone is used as a target rather than to deform geometry,
   only *Armature* and *Copy Transforms* constraints will use the full
   transformation including roll and scale.


Display
=======

You can see these segments only if bones are visualized as *B-bones*.

When not visualized as *B-Bone*\ s, bones are always shown as rigid sticks,
even though the bone segments are still present and effective.
This means that even in e.g. *Octahedron* visualization,
if some bones in a chain have several segments,
they will nonetheless smoothly deform their geometry.


Rest Pose
=========

The initial shape of a B-Bone can be defined in Edit Mode as a rest pose of that bone.
This is useful for curved facial features like curved eyebrows or mouths.

B-Bones have two sets of the Bendy Bone properties -- one for Edit Mode (i.e. the Rest Pose/Base Rig) and
another for Pose Mode -- adding together their values to get the final transforms.


Example
=======

.. list-table::

   * - .. _fig-rig-bone-intro-bbone:

       .. figure:: /images/animation_armatures_bones_properties_bendy-bones_b-bones-1.png

          Bones with just one segment in Edit Mode.

     - .. figure:: /images/animation_armatures_bones_properties_bendy-bones_b-bones-2.png

          The Bézier curve superposed to the chain, with its handles placed at bones' joints.

   * - .. _fig-rig-bone-intro-same:

       .. figure:: /images/animation_armatures_bones_properties_bendy-bones_b-bones-3.png

          The same armature in Object Mode.

     - ..

In Fig. :ref:`fig-rig-bone-intro-bbone` we connected three bones,
each one made of five segments.

Look at Fig. :ref:`fig-rig-bone-intro-same`,
we can see how the bones' segments smoothly "blend" into each other, even for roll.

.. figure:: /images/animation_armatures_bones_properties_bendy-bones_pose-mode.png

   An armature in Pose Mode, B-Bone visualization: Bone.003 has one segment,
   Bone.004 has four, and Bone.005 has sixteen.


Options
=======

Segments
--------

The *Segments* number field allows you to set the number of segments, which the given bone is subdivided into.
Segments are small, rigid linked child bones that interpolate between the root and the tip.
The higher this setting, the smoother "bends" the bone, but the heavier the pose calculations.


Curve XY Offsets
----------------

Applies offsets to the curve handle positions on the plane perpendicular to the bone's primary (Y) axis.
As a result, the handle moves per axis (XY) further from its original location, causing the curve to bend.


Roll
----

Roll In, Out
   The roll value (or twisting around the main Y axis of the bone) is interpolated per segment,
   between the start and end roll values.
   It is applied as a rotational offset on top of the previous rotation.
Inherit End Roll
   If enabled, the *Roll Out* value of the *Start Handle* bone (connected parent by default)
   will be implicitly added to the *Roll In* setting of the current bone.


Scale
-----

Scale In X/Y, Scale Out X/Y
   Scaling factor that adjusts the thickness of each segment for the X and Y axes only,
   i.e. length (Z axis) is not affected. Similar to *Roll* it is interpolated per segment.


Easing
------

Ease In, Out
   The *Ease In/Out* number fields, change the "length" of the :ref:`"auto" <curve-handle-type-auto>` Bézier handle
   to control the "root handle" and "tip handle" of the bone, respectively.

   These values are proportional to the default length,
   which of course automatically varies depending on bone length,
   angle with the reference handle, and so on.

.. list-table:: Ease In/Out settings example, with a materialized Bézier curve.

   * - .. figure:: /images/animation_armatures_bones_properties_bendy-bones_curve-in-out-1.png
          :width: 320px

          Bone.004 with default In and Out (1.0).

     - .. figure:: /images/animation_armatures_bones_properties_bendy-bones_curve-in-out-2.png
          :width: 320px

          Bone.004 with In at 2.0, and Out at 0.0.


Custom Handles
--------------

B-Bones can use custom bones as their reference bone handles, instead of only using the connected parent/child bones.

Start, End Handle Type
   Specifies the type of the handle from the following choices:

   Automatic
      The connected parent (or first connected child) of the bone is chosen as the handle.
      Calculations are done according to the *Absolute* handle type below.
   Absolute
      The Bézier handle is controlled by the **position** of the head (tail)
      of the handle bone relative to the head (tail) of the current bone.
      Note that for this to work, there must be a non-zero distance between these bones.
      If the handle is also a B-Bone, additional processing is applied to further
      smooth the transition, assuming that the bones in effect form a chain.
   Relative
      The Bézier handle is controlled by the **offset** of the head (tail) of the handle bone from its rest pose.
      The use of this type is not recommended due to numerical stability issues near zero offset.
   Tangent
      The Bézier handle is controlled by the **orientation** of the handle bone, independent of its location.

Custom Handle
   For types other than *Automatic*, a bone to use as handle has to be manually selected.
   Switching to a custom handle type without selecting a bone can be used to effectively disable the handle.

   It is valid for two bones to refer to each other as handles -- this correlation is applied
   in connected chains with *Automatic* handles.

.. tip:: Keying Set

   The "BBone Shape" Keying Set includes all Bendy Bones properties.


Example
-------

.. figure:: /images/animation_armatures_bones_properties_bendy-bones_settings-demo.png

   Visualization of the Bendy Bones properties.

   From Left: 1) Curve X/Y offsets, 2) Scale In/Out, 3) Roll In/Out
