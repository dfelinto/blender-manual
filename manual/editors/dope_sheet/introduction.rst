
************
Introduction
************

.. figure:: /images/editors_dope-sheet_introduction_overview.png
   :width: 620px

   The Dope Sheet.

The Dope Sheet gives the animator a birds-eye-view of the keyframes inside the scene.

The Dope Sheet is inspired by classical hand-drawn animation process,
in which animators will make use of a chart, showing exactly when each drawing,
sound and camera move will occur, and for how long. This is called an exposure sheet or 'dope sheet'.
While CG foundations dramatically differ from classical hand-drawn animation,
Blender's *Dope Sheet* inherits a similar directive.


Dope Sheet Modes
================

.. figure:: /images/editors_dope-sheet_introduction_modes.png

   Dope Sheet modes.

While the Dope Sheet Mode allows you to edit multiple actions at once,
the other ones are dedicated to view and edit specific data-blocks used in different context of animation.

- Dope Sheet
- :doc:`Action Editor </editors/dope_sheet/action>`
- :ref:`Shape Key Editor <dope-sheet-shape-key>`
- :doc:`Grease Pencil </editors/dope_sheet/grease_pencil>`
- :ref:`Mask <dope-sheet-mask>`
- Cache File: Alembic Todo 2.78.


Main Region
===========

Navigation
----------

As with most editors, you can:

Pan
   Pan the view vertically (values) or horizontally (time) with click and drag (:kbd:`MMB`).
Zoom
   Zoom in and out with the mouse wheel (:kbd:`Wheel`).
Scale View
   Scale the view vertically or horizontally (:kbd:`Ctrl-MMB`).

In addition, you can also use the scrollbars to pan and zoom the view.


Keyframes
---------

.. figure:: /images/editors_dope-sheet_introduction_types.png

   The Dope Sheet Editor with object channels.

This area contains keyframes for all visible action channels.
As with the other time-based editors, the X axis represents time.
The Y axis represents a stack of action channels.

On these channels lay the keyframes, which can show different information:

.. list-table::
   :widths: 20 80

   * - Gray
     - Unselected
   * - Yellow
     - Selected
   * - Diamond
     - Free Keyframe Handle
   * - Round
     - Auto-Clamped Keyframe Handle
   * - Circle
     - Automatic Keyframe Handle
   * - Square
     - Vector Keyframe Handle
   * - Rhombus
     - Aligned Keyframe Handle
   * - Various colors
     - These represent custom keyframe tags set by the user (:menuselection:`Key --> Keyframe Type`)
   * - Gray bar between keys
     - Held key (the two keyframes are identical)
   * - Green line between keys
     - Fixed keyframe interpolation (set in :menuselection:`Key --> Interpolation Mode`)
   * - Upwards arrow
     - Maximum Extreme keyframe (visible if :menuselection:`View --> Show Curve Extremes` are enabled)
   * - Downwards arrow
     - Minimum Extreme keyframe (visible if :menuselection:`View --> Show Curve Extremes` are enabled)


Selecting Keyframes
-------------------

Selection tools are available in the Select menu in the header, and the main shortcuts are listed below:

Selecting
   Click on a key to select it. Hold :kbd:`Shift` to extend the current selection.
Box Selecting
   Click and drag to box select multiple keyframes at once.
   You can hold :kbd:`Shift` to extend or :kbd:`Ctrl` to subtract from the current selection.

Select/Deselect All
   - To select all keys, press :kbd:`A`.
   - To deselect all keys, press :kbd:`Alt-A`.
   - To inverse the selection, press :kbd:`Ctrl-I`.
Before/After Current Frame :kbd:`[`, :kbd:`]`
   Select all to the right or left.
   Or hold :kbd:`Shift-Ctrl` and click on either side of the Playhead.

See the Select menu for a full list of selection tools.


Manipulating Keyframes
----------------------

Keyframe tools are available in the Key menu in the header, and the main shortcuts listed below:

Moving Keyframes
   To move a single keyframe, click and drag on a key.
   To move multiple keyframes, make sure several keys are selected and press :kbd:`G`.
Scaling Keyframes
   To scale (stretch) selected keys, press :kbd:`S`.
Extending Keyframes
   To extend the time between two keys, select all with :kbd:`A`,
   place the Playhead between two keyframes and press :kbd:`E`.

See the Key menu for a full list of selection tools.


Channels Region
---------------

.. _fig-dope-sheet-action:

.. figure:: /images/editors_dope-sheet_introduction_action-editor-sliders.png

   The Action editor's channels region.

See :doc:`/editors/graph_editor/channels`.


Header
------

Here you find the menus, a first group of controls related to the editor "mode",
a second one concerning the action data-blocks, and a few other tools
(like the copy/paste buttons, and snapping type).


.. _dope-sheet-view-menu:

View Menu
^^^^^^^^^

.. figure:: /images/animation_keyframes_introduction_interpolation.png
   :align: right

   Handle types.

Show Handles and Interpolation
   Instead of displaying all keyframes as diamonds, different icons are used to show the Bézier handle type.
   When curves use a different interpolation type, a line is shown between keys to highlight that.

   See :ref:`Handles & Interpolation Display <keyframe-handle-display>`.

.. figure:: /images/editors_dope-sheet_introduction_extremes.png
   :align: right

   Extreme markers.

Show Extremes
   Detect keys where the curve changes direction based on comparing with the adjacent key values,
   and display that by changing the keyframe icons to resemble an arrow.
   A muted version of the icon is used if the curve overshoots the extreme,
   or for groups with different results for contained curves.

See Graph editor's :ref:`graph-view-menu`.


Markers Menu
^^^^^^^^^^^^

:doc:`Markers </animation/markers>` are used to denote frames with key points or significant events
within an animation. Like with most animation editors, markers are shown at the bottom of the editor.

.. figure:: /images/editors_graph-editor_introduction_markers.png

   Markers in animation editor.

There are some options that are exclusive to the Dope Sheet editor:

Sync Markers
   Sync Markers with keyframe edits.
Show Pose Markers
   Available in :doc:`Action </editors/dope_sheet/action>` and :doc:`Shape Key </editors/dope_sheet/shape_key>` modes.
   Shows pose markers owned by the active action instead of the scene ones.
Make Markers Local
   Available in :doc:`Action </editors/dope_sheet/action>` and :doc:`Shape Key </editors/dope_sheet/shape_key>` modes.
   Converts selected scene markers in pose markers, assigning them to the active action.

For more information and the description of the other marker tools,
see :ref:`Editing Markers <animation-markers-editing>`.


Key Menu
^^^^^^^^

Keyframe Type :kbd:`R`
   Sets the :ref:`keyframe-type` of the selected keyframes.

See :doc:`F-Curve </editors/graph_editor/fcurves/index>`.


.. _bpy.types.DopeSheet.show_summary:

Filters
^^^^^^^

Only Show Selected
   Only include keyframes related to the selected objects and data.
Show Hidden
   Include keyframes from objects or bones that are not visible.
Only Show Errors
   Only include curves and drivers that are disabled or have errors.
   Useful for debugging.

F-Curve Name Filter
   Fuzzy/Multi-Word name filtering matches word snippets/partial words,
   instead of having to match everything. It breaks down the search text based on whitespace placement.
   e.g. "lo ro" will filter all location and rotation, while "lc rt" will *not* work.

Filter by Type
   Filter curves by property type.

Filtering Collection
   Select a collection to only show keyframes from objects contained in that collection.

Sort Data-Blocks
   Objects data-blocks appear in alphabetical order, so that it is easier to find where they occur
   (as well as helping to keep the animation of related objects together in the NLA editor for instance).

   If you find that your playback speed suffers from this being enabled
   (it should only really be an issue when working with lots of objects in the scene),
   you can turn this off.

Summary
   Toggles the "Dope Sheet Summary" channel at the top of the `Channels Region`_.
   This is used to give an overview of all the channels by combining all the actions into one channel.
