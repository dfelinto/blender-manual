
***************
Animation Tools
***************

.. _bpy.ops.gpencil.blank_frame_add:

Insert Blank Keyframe
=====================

.. reference::

   :Mode:      Draw Mode, Edit Mode, Sculpt Mode
   :Menu:      :menuselection:`Stroke --> Animation --> Insert Blank Keyframe (Active Layer)`
               :menuselection:`Stroke --> Animation --> Insert Blank Keyframe (All Layers)`
   :Shortcut:  :kbd:`Shift-I`

Active Layer
   Add a new blank keyframe to the active layer at the current frame.
   If there is already a keyframe at the current frame,
   a new blank keyframe will be added on the next frame.

All Layers
   When enabled, Blank keyframe will be created on all layers, not only the active one.


.. _bpy.ops.gpencil.frame_duplicate:

Duplicate Active Keyframe
=========================

.. reference::

   :Mode:      Draw Mode, Edit Mode, Sculpt Mode
   :Menu:      :menuselection:`Stroke --> Animation --> Duplicate Active Keyframe (Active Layer)`
               :menuselection:`Stroke --> Animation --> Duplicate Active Keyframe (All Layers)`

Duplicates the strokes on the last keyframe by copying them to the current frame.

Mode
   Active
      Duplicate only the active layer.

   All
      Duplicate all the layers.


.. _bpy.ops.gpencil.active_frames_delete_all:

Delete Active Keyframe
======================

.. reference::

   :Mode:      Draw Mode, Edit Mode, Sculpt Mode
   :Menu:      :menuselection:`Stroke --> Animation --> Delete Active Keyframe (Active Layer)`
               :menuselection:`Stroke --> Animation --> Delete Active Keyframes (All Layers)`
   :Shortcut:  :kbd:`Shift-X`

Deletes the last keyframe in the Dope Sheet or the current keyframe if you are on one.


.. _grease-pencil-animation-tools-interpolation:
.. _bpy.ops.gpencil.interpolate_sequence:

Interpolate Sequence
====================

.. reference::

   :Mode:      Draw Mode, Edit Mode
   :Menu:      :menuselection:`Grease Pencil --> Interpolate Sequence`
   :Shortcut:  :kbd:`Shift-Ctrl-E`

Interpolate strokes between the previous and next keyframe by adding *multiple* keyframes.
A breakdown keyframe will be added on every frame between the previous and next keyframe.


.. _bpy.ops.gpencil.mesh_bake:
.. _bpy.ops.gpencil.bake_mesh_animation:

Bake Mesh to Grease Pencil
==========================

.. reference::

   :Editor:    3D Viewport
   :Mode:      Object and Pose Modes
   :Menu:      :menuselection:`Object --> Animation --> Bake Mesh to Grease Pencil...`

Converts each frame of a mesh animation within a selected frame range to
a Grease Pencil object keyframed strokes. The *Bake Action* tool computes the final animation of
the selected objects with all those modifiers, drivers, and constraints applied, and keyframes the result.

Target Object
   Select the target Grease Pencil object for the baked animation or a new one if there is nothing yet.
Start Frame, End Frame
   Start/End frame for the baking process.
Step
   Frame steps for the baking process
Thickness
   Strokes thickness.
Threshold Angle
   Threshold value that determine the strokes end.
Stroke Offset
   Sets offset to separate strokes from filled strokes.
Only Seam Edges
   Convert only edges marked as seam.
Export Faces
   Convert faces as filled strokes.
Only Selected Keyframes
   Convert only the selected keyframes.
Target Frame
   Target destination frame for the baked animation.
Projection Type
   Sets the projection type to use for the converted strokes.


.. _bpy.ops.gpencil.bake_grease_pencil_animation:

Bake Object Transform to Grease Pencil
======================================

.. reference::

   :Editor:    3D Viewport
   :Mode:      Object and Pose Modes
   :Menu:      :menuselection:`Object --> Animation --> Bake Object Transform to Grease Pencil`

Applies all transform animation at Object level within a selected frame range to Grease Pencil object keyframes.

Start Frame, End Frame
   Start/End frame for the baking process.
Step
   Frame steps for the baking process.
Only Selected Keyframes
   Convert only the selected keyframes.
Target Frame
   Target destination frame for the baked animation.
Projection Type
   Sets the projection type to use for the converted strokes.
