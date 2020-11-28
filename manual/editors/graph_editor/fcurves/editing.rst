
*******
Editing
*******

Transform
=========

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Key --> Transform`

An F-curve can be edited by transforming the locations of the keyframes.

Move, Rotate, Scale
   Like other elements in Blender, keyframes can be
   moved, rotated, or scaled as described in
   :doc:`Basic Transformations </scene_layout/object/editing/transform/introduction>`.
Extend
   Moves keyframes relative to the Playhead.
   If the mouse is to the left of the Playhead,
   this operator only affects the selected keyframes that are to the left of the Playhead.
   On the contrary, if the mouse is to the right of the Playhead,
   this operator only affects the selected keyframes that are to the right of the Playhead.

.. tip::

   For precise control of the keyframe position and value,
   you can set values in the *Active Keyframe* of the Sidebar region.


.. _bpy.ops.graph.snap:

Snap
====

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Key --> Snap`
   :Hotkey:    :kbd:`Shift-S`

Keyframes can be snapped to different properties by using the *Snap Keys* tool.

Selection to Current Frame
   Snap the selected keyframes to the *Playhead*.
Selection to Cursor Value
   Snap the selected keyframes to the *2D Cursor*.
Selection to Nearest Frame
   Snap the selected keyframes to their nearest frame individually.
Selection to Nearest Second
   Snap the selected keyframes to their nearest second individually, based on the *FPS* of the scene.
Selection to Nearest Marker
   Snap the selected keyframes to their nearest marker individually.
Flatten Handles
   Flatten the *Bézier* handles for the selected keyframes.

   .. list-table:: Flatten Handles snapping example.

      * - .. figure:: /images/editors_graph-editor_fcurves_editing_flatten-handles-1.png

             Before Flatten Handles.

        - .. figure:: /images/editors_graph-editor_fcurves_editing_flatten-handles-2.png

             After Flatten Handles.

Cursor to Selected :kbd:`Ctrl-G`
   Places the cursor at the midpoint between selected keyframes.

.. _bpy.ops.graph.snap_cursor_value:

Cursor Value to Selection
   Places the cursor value on the average value of selected keyframes.


.. _bpy.ops.graph.mirror:

Mirror
======

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Key --> Mirror`
   :Hotkey:    :kbd:`Ctrl-M`

Selected keyframes can be mirrored over different properties using the *Mirror Keys* tool.

By Times over Current Frame
   Mirror horizontally over the playhead.
By Values over Cursor Value
   Mirror vertically over the 2D cursor.
By Times over Time 0
   Mirror horizontally over frame 0.
By Values over Value 0
   Mirror vertically over value 0.
By Times over First Selected Marker
   Mirror horizontally over the first selected marker.


.. _bpy.ops.graph.keyframe_insert:

Insert Keyframes
================

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Key --> Insert Keyframes`
   :Hotkey:    :kbd:`Ctrl-RMB`, :kbd:`Shift-Ctrl-RMB`

Inserts a keyframe to the active F-curve at the mouse position.
The newly added keyframes will be selected, making it easier to quickly tweak the newly added keyframes.
All previously selected keyframes are kept selected by using :kbd:`Shift-Ctrl-RMB`.


Add F-Curve Modifier
====================

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Key --> Add F-Curve Modifier`
   :Hotkey:    :kbd:`Shift-Ctrl-M`

Opens a pop-up allowing you to add modifiers to the active F-curve.
Settings for the :doc:`modifier </editors/graph_editor/fcurves/sidebar/modifiers>` can be found in
the :menuselection:`Sidebar --> Modifiers` tab.


.. _bpy.ops.graph.sound_bake:

Bake Sound to F-Curves
======================

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Key --> Bake Sound to F-Curves`

The *Bake Sound to F-Curves* operator takes a sound file and uses its sound wave to create the animation data.

Lowest Frequency
   Cutoff frequency of a high-pass filter that is applied to the audio data.
Highest Frequency
   Cutoff frequency of a low-pass filter that is applied to the audio data.
Attack Time
   Value for the hull curve calculation that tells how fast the hull curve can rise.
   The lower the value the steeper it can rise.
Release Time
   Value for the hull curve calculation that tells how fast the hull curve can fall.
   The lower the value the steeper it can fall.
Threshold
   Minimum amplitude value needed to influence the hull curve.

Accumulate
   Only the positive differences of the hull curve amplitudes are summarized to produce the output.
Additive
   The amplitudes of the hull curve are summarized. If *Accumulate* is enabled,
   both positive and negative differences are accumulated.
Square
   Gives the output as a square curve.
   Negative values always result in -1, and positive ones in 1.

   Square Threshold
      All values lower than this threshold result in 0.


.. _bpy.ops.graph.frame_jump:

Jump to Keyframes
=================

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Key --> Jump to keyframes`
   :Hotkey:    :kbd:`Ctrl-G`

Places the 2D cursor at the center of the selected keyframes.


.. _bpy.ops.graph.copy:
.. _bpy.ops.graph.paste:

Copy/Paste
==========

.. admonition:: Reference

   :Menu:      :menuselection:`Key --> Copy Keyframes`, :menuselection:`Key --> Paste Keyframes`
   :Hotkey:    :kbd:`Ctrl-C`, :kbd:`Ctrl-V`

Use :kbd:`Ctrl-C` to copy selected keyframes and :kbd:`Ctrl-V` to paste the previously copied keyframes.
During the paste action, the :ref:`ui-undo-redo-adjust-last-operation` panel provides some options in
how the paste is applied.

Offset
   No Offset
      Pastes the keyframes in the location they were copied from.
   Frame Relative
      Pastes the keyframe relative to the Playhead position based on the locations of
      the keyframes relative to the Playhead when they were copied.
   Frame Start
      Pastes the keyframes with the first keyframe of the copied set placed at the Playhead.
   Frame End
      Pastes the keyframes with the last keyframe of the copied set placed at the Playhead.
Type
   Mix
      Integrates the pasted keyframes in with existing keyframes only overwriting keyframes that share a frame.
   Overwrite All
      Removes all previous keyframes and replaces them with the pasted keyframes.
   Overwrite Range
      TODO
   Overwrite Entire Range
      TODO
Flipped
   TODO


.. _bpy.ops.graph.duplicate_move:

Duplicate
=========

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Key --> Duplicate`
   :Hotkey:    :kbd:`Shift-D`

Duplicates the selected keyframes. You can reposition them by moving the mouse.


.. _bpy.ops.graph.delete:

Delete Keyframes
================

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Key --> Delete Keyframes`
   :Hotkey:    :kbd:`X`, :kbd:`Delete`

Pressing :kbd:`X` or :kbd:`Delete` opens a pop-up menu from where you can delete the selected keyframes.


.. _bpy.ops.graph.handle_type:

Handle Type
===========

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Key --> Handle Type`
   :Hotkey:    :kbd:`V`

Sets the :ref:`handle type <editors-graph-fcurves-settings-handles>` of the selected keyframes.


.. _bpy.ops.graph.interpolation_type:

Interpolation Mode
==================

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Key --> Interpolation Mode`
   :Hotkey:    :kbd:`T`

Sets the :ref:`interpolation mode <editors-graph-fcurves-settings-interpolation>` between the selected keyframes.


.. _bpy.ops.graph.easing_type:

Easing Mode
===========

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Key --> Easing Mode`
   :Hotkey:    :kbd:`Ctrl-E`

Sets the :ref:`easing mode <editors-graph-fcurves-settings-easing>` of the selected keyframes.


.. _bpy.ops.graph.decimate:

Decimate
========

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Key --> Decimate (Ratio)`
   :Menu:      :menuselection:`Key --> Decimate (Allowed Change)`

The *Decimate* tool simplifies an F-curve by removing
keyframes that influence the curve shape the least.

Mode
   Controls which method is used pick the number of keyframes to use.

   Ratio
      Deletes a defined percentage of keyframes,
      the amount of keyframes to delete is define by the *Remove* property.
   Error Margin
      Deletes keyframes which only allowing the F-curve to change by a defined amount.
      The amount of change is controlled by the *Max Error Margin*
      which controls how much the new decimated curve is allowed to deviate from the original.


.. _bpy.ops.graph.clean:

Clean Keyframes
===============

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Key --> Clean Keyframes`
   :Hotkey:    :kbd:`X`

*Clean Keyframes* resets the keyframe tangents on selected keyframes
to their auto-clamped shape, if they have been modified.

.. list-table::

   * - .. figure:: /images/editors_graph-editor_fcurves_editing_clean1.png

          F-Curve before cleaning.

     - .. figure:: /images/editors_graph-editor_fcurves_editing_clean2.png

          F-Curve after cleaning.


Clean Channels
==============

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Key --> Clean Channels`
   :Hotkey:    :kbd:`X`

Acts like the *Clean Keyframes* tool but will also delete the channel itself if it is only left with
a single keyframe containing the default property value and
it's not being used by any generative F-curve modifiers or drivers.

.. note::

   The modified curve left after the *Clean* tool is run is not the same as the original,
   so this tool is better used before doing custom editing of F-curves and after initial keyframe insertion,
   to get rid of any unwanted keyframes inserted while doing mass keyframe insertion
   (by selecting all bones and pressing :kbd:`I` for instance).


.. _bpy.ops.graph.smooth:

Smooth Keys
===========

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Key --> Smooth Keys`
   :Hotkey:    :kbd:`Alt-O`

There is also an option to smooth the selected curves, but beware: its algorithm seems to be
to divide by two the distance between each keyframe and the average linear value of the curve,
without any setting, which gives quite a strong smoothing! Note that the first and last keys
seem to be never modified by this tool.

.. list-table::

   * - .. figure:: /images/editors_graph-editor_fcurves_editing_clean1.png

          F-Curve before smoothing.

     - .. figure:: /images/editors_graph-editor_fcurves_editing_smooth.png

          F-Curve after smoothing.


.. _bpy.ops.graph.sample:

Sample Keyframes
================

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Key --> Sample Keyframes`
   :Hotkey:    :kbd:`Shift-Alt-O`

Sampling a set of keyframes replaces interpolated values with a new keyframe for each frame.

.. list-table::

   * - .. figure:: /images/editors_graph-editor_fcurves_editing_sample.png

          F-Curve before sampling.

     - .. figure:: /images/editors_graph-editor_fcurves_editing_sample2.png

          F-Curve after sampling.


.. _bpy.ops.graph.bake:

Bake Curve
==========

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Key --> Bake Curve`
   :Hotkey:    :kbd:`Alt-C`

Baking a curve replaces it with a set of sampled points, and removes the ability to edit the curve.


.. _bpy.ops.graph.euler_filter:

Discontinuity (Euler) Filter
============================

Todo.
