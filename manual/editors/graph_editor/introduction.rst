
************
Introduction
************

The Graph Editor allows users to adjust animation curves over time for any animatable property.
:doc:`F-Curves </editors/graph_editor/fcurves/introduction>`.

.. figure:: /images/editors_graph-editor_introduction_example.png

   The Graph Editor.


Main Region
===========

The curve view allows you to view and edit F-curves.
An F-curve has several key parts:

Curve
   The curve defines the value (Y axis) of the property over time (X axis).

   See :doc:`F-Curves </editors/graph_editor/fcurves/index>`.
Keyframes
   Keyframes are user-defined values on certain frames and are represented
   by little black squares which become orange if selected.

   See :doc:`Keyframes </animation/keyframes/index>` for more information.
Handles
   Each keyframe has a handle that helps determine the values of the curve between keyframes.
   These handles are represented by extruding lines with circular ends
   and can be selected and modified to change the shape of the curve.

   See :ref:`F-Curve Handles <editors-graph-fcurves-settings-handles>` for more information.

.. figure:: /images/editors_graph-editor_introduction_f-curve-example.png

   A simple curve.

.. seealso::

   See :doc:`F-Curves </editors/graph_editor/fcurves/introduction>` for more info.


Navigation
----------

As with most editors, you can:

Pan
   Pan the view vertically (values) or horizontally (time) with click and drag :kbd:`MMB`.
Zoom
   Zoom in and out with the mouse wheel :kbd:`Wheel`.
Scale View
   Scale the view vertically or horizontally :kbd:`Ctrl-MMB`.

In addition, you can also use the scrollbars to pan and zoom the view.


.. _graph_editor-2d-cursor:
.. _bpy.types.SpaceGraphEditor.cursor:

Playhead & 2D Cursor
--------------------

.. figure:: /images/editors_graph-editor_introduction_2dcursor.png
   :align: right

   Graph Editor 2D Cursor.

The current frame is represented by a blue vertical line called the *Playhead*.

As in the :doc:`Timeline </editors/timeline>`,
you can change the current frame by :kbd:`LMB`-dragging in the scrubbing area at the top of the editor.

The blue horizontal line is called the *2D Cursor*.
This can be enabled or disabled via the *View Menu* or the *View Properties* panel.

These two lines can be used as a reference for moving and scaling keyframe handles.

.. seealso:: See Graph Editor's :ref:`graph_editor-view-properties`.


View Axes
---------

For *Actions* the X axis represents time,
the Y axis represents the value to set the property.

Depending on the selected curves, the values have different meaning:
for example rotation properties are shown in degrees.


Header
======

.. _graph-view-menu:

View Menu
---------

Realtime Updates
   When transforming keyframes, changes to the animation data are propagated to other views.
Show Cursor
   Toggles the visibility of the `Playhead & 2D Cursor`_.
Show Sliders
   A toggle option that shows the value sliders for the channels.
   See the Fig. :ref:`fig-dope-sheet-action`.
AutoMerge Keyframes
   Automatically merge nearby keyframes.

Show Markers
   Shows the markers region. When disabled, the `Markers Menu`_ is also hidden
   and markers operators are not available in this editor.

Use High Quality Display
   Display F-curves using :term:`Anti-Aliasing` and other effects (disable for a better performance).

.. _bpy.types.SpaceGraphEditor.show_extrapolation:

Show Extrapolation
   Toggles the visibility of the :ref:`extrapolated <editors-graph-fcurves-settings-extrapolation>`
   portion of curves.
Show Handles :kbd:`Ctrl-H`
   Toggles the display of a curve's handles in the curve view.
Only Selected Curve Keyframes
   Only shows the keyframes markers on the selected curves.
Only Selected Keyframes Handles
   Only shows the handles for the currently selected curves.
Frame All :kbd:`Home`
   Reset viewable area to show all keyframes.
Frame Selected :kbd:`NumpadPeriod`
   Reset viewable area to show selected keyframes.
Go to Current Frame :kbd:`Numpad0`
   Centers the area to the Playhead.

.. seealso::

   - See Graph Editor's :ref:`graph_editor-view-properties`.
   - See Timeline's :ref:`timeline-view-menu`.


.. _graph-preview-range:

Preview Range
^^^^^^^^^^^^^

Set Preview Range :kbd:`P`
   Interactively define frame range used for playback.
   Allows you to define a temporary preview range to use for animation playback
   (this is the same thing as the *Playback Range* option of
   the :ref:`Timeline editor header <animation-editors-timeline-headercontrols>`).
Clear Preview Range :kbd:`Alt-P`
   Clears the preview range.
Set Preview Range to Selected :kbd:`Ctrl-Alt-P`
   Sets the preview range to playback the selected NLA strips.


Markers Menu
------------

:doc:`Markers </animation/markers>` are used to denote frames with key points or significant events
within an animation. Like with most animation editors, markers are shown at the bottom of the editor.

.. figure:: /images/editors_graph-editor_introduction_markers.png

   Markers in animation editor.

For descriptions of the different marker tools see :ref:`Editing Markers <animation-markers-editing>`.


View Controls
-------------

.. figure:: /images/editors_graph-editor_introduction_header-view.png

   View controls.

Show Only Selected
   Only include curves related to the selected objects and data.
Show Hidden
   Include curves from objects/bones that are not visible.
Show Only Errors
   Only include curves and drivers that are disabled or have errors.
   Useful for debugging.

Filter (funnel icon)
   Only include curves with keywords contained in the search field.

   Multi-Word
      Fuzzy/Multi-Word name filtering matches word snippets/partial words,
      instead of having to match everything. It breaks down the search text based on whitespace placement.
      e.g. "lo ro" will filter all location and rotation, while "lc rt" will *not* work.

   Type Filter
      Filter curves by property type.

   Filtering Collection
      Select a collection to only show keyframes from objects contained in that collection.

   Sort Data-Blocks
      Objects data-blocks appear in alphabetical order, so that it is easier to find where they occur
      (as well as helping to keep the animation of related objects together in the NLA for instance).

      If you find that your playback speed suffers from this being enabled
      (it should only really be an issue when working with lots of objects in the scene),
      you can turn this off.

Normalize
   Normalize curves so the maximum or minimum point equals 1.0 or -1.0.

   Auto
      Automatically recalculate curve normalization on every curve edit.
      This is useful to prevent curves from jumping after tweaking it.


F-Curve Controls
----------------

.. figure:: /images/editors_graph-editor_introduction_header-edit.png

   F-Curve controls.

Proportional Editing :kbd:`O`
   See :doc:`Proportional Editing </editors/3dview/controls/proportional_editing>`.
Auto Snap
   Auto snap the keyframes for transformations.

   - No Auto-Snap
   - Frame Step
   - Second Step
   - Nearest Frame
   - Nearest Second
   - Nearest Marker

Pivot Point
   Pivot point for rotation.

   Bounding Box Center
      Center of the selected keyframes.
   2D Cursor
      Center of the *2D Cursor*. *Playhead* + *Cursor*.
   Individual Centers
      Rotate the selected keyframe *Bézier* handles.

Create Ghost Curves (framed F-curve icon)
   Creates a picture with the current shape of the curves.


Sidebar Region
==============

The panels in the *Sidebar region*.


.. _bpy.types.SpaceGraphEditor.show_cursor:
.. _graph_editor-view-properties:

View Tab
--------

.. figure:: /images/editors_graph-editor_introduction_view-panel.png
   :align: right

   View Tab.

Show Cursor
   Toggles the visibility of the :ref:`2D Cursor <graph_editor-2d-cursor>`.
Cursor X, Y
   Moves the cursor to the specified frame (X value) and value (Y value).
Cursor to Selection
   Places the *2D Cursor* at the midpoint of the selected keyframes.

.. seealso::

   Graph Editor's :ref:`graph-view-menu`.


Further Tabs
------------

F-Curve Tab
   See :doc:`F-Curve </editors/graph_editor/fcurves/properties>`.
Modifiers Tab
   See :doc:`F-Curve Modifiers </editors/graph_editor/fcurves/modifiers>`.
