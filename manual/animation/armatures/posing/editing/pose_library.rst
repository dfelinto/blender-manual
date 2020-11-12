.. _bpy.ops.poselib:

************
Pose Library
************

.. admonition:: Reference
   :class: refbox

   :Mode:      Pose Mode
   :Menu:      :menuselection:`Pose --> Pose Library`

The pose library is a way to store pose positions so the same position
can be used again later in the animation or to store different rest poses.
*Pose libraries* are saved to :doc:`Actions </animation/actions>`.
They are not generally used as actions, but can be converted to and from.

.. seealso::

   :doc:`Pose Library Properties </animation/armatures/properties/pose_library>`.


.. _bpy.ops.poselib.browse_interactive:

Browse Poses
============

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Pose --> Pose Library --> Browse Poses`
   :Hotkey:    :kbd:`Alt-L`

Interactively browse poses in the 3D Viewport.
After running the operator, cycle through poses using the :kbd:`Left` and :kbd:`Right` arrow keys.
The name of the pose being previewed is displayed in the header region.
After the desired pose is selected using :kbd:`Return` or :kbd:`LMB` to make it the active pose;
to cancel browsing, use :kbd:`Esc` or :kbd:`RMB`.

Pose
   Index of the pose to apply (-2 for no change, -1 to use the active pose).


.. _bpy.ops.poselib.pose_add:

Add Pose
========

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Pose --> Pose Library --> Add Pose`
   :Hotkey:    :kbd:`Shift-L`

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


.. _bpy.ops.poselib.pose_rename:

Rename Pose
===========

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Pose --> Pose Library --> Rename Pose`
   :Hotkey:    :kbd:`Shift-Ctrl-L`

Changes the name of the specified pose from the active pose library.

New Pose Name
   The new name for the pose.
Pose
   The pose action to rename.


.. _bpy.ops.poselib.pose_remove:

Remove Pose
===========

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Pose --> Pose Library --> Remove Pose`
   :Hotkey:    :kbd:`Shift-Alt-L`

Deletes the specified pose from the active pose library.
