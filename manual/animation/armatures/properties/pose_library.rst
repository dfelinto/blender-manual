
************
Pose Library
************

.. admonition:: Reference
   :class: refbox

   :Mode:      All Modes
   :Panel:     :menuselection:`Properties --> Object Properties --> Pose Library`

.. figure:: /images/animation_armatures_properties_pose-library_panel.png
   :align: right

   The Pose Library panel.

The pose library is a way to store pose positions so the same position
can be used again later in the animation or to store different rest poses.
Pose libraries are saved to :doc:`Actions </animation/actions>`.
They are not generally used as actions, but can be converted to and from.
The *Pose Library* panel is used to save, apply, and manage armature poses.

.. seealso::

   :doc:`Pose Library Editing </animation/armatures/posing/editing/pose_library>`.


Action
   A :ref:`ui-data-block` for Actions or pose libraries.

.. _bpy.types.ActionPoseMarkers.active_index:

Pose Libraries
   A :ref:`List view <ui-list-view>` of poses for the active pose library.

   Add ``+``
      If a pose is added, a :ref:`pose marker <marker-pose-add>` is created.
      The :ref:`Whole Character keying set <whole-character-keying-set>` is used to
      determine which bones to key. If any bones are selected, only keyframes for
      those bones are added, otherwise all bones in the keying set are keyed.
      Bones that are ignored by the *Whole Character* keying set are always ignored,
      regardless of their selection state.

      Add New
         Adds a new pose to the active pose library with the current pose of the armature.
      Add New (Current Frame).
         Will add a pose to the pose library based on the current frame selected in the Timeline.
         In contrast to *Add New* and *Replace Existing* which automatically allocate a pose to an action frame.
      Replace Existing
         Replace an existing pose in the active pose library with the current pose of the armature.

   .. _bpy.ops.poselib.apply_pose:

   Apply Pose (magnifying glass icon)
      Applies the active pose to the selected pose bones.

   .. _bpy.ops.poselib.action_sanitize:

   Sanitize Action (book icon)
      Makes an action suitable for use as a pose library.
      This is used to convert an Action to a pose library.
      A pose is added to the pose library for each frame with keyframes.

   .. _bpy.ops.poselib.pose_move:

   Move (up/down arrow icon)
      Moves the pose up/down in the list.
