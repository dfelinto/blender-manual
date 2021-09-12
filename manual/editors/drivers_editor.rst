
**************
Drivers Editor
**************

The Drivers Editor allows users to drive one property with another.
See :doc:`Drivers </animation/drivers/index>` and :doc:`F-Curves </editors/graph_editor/fcurves/introduction>`.

.. figure:: /images/editors_graph-editor_introduction_example.png

   The Drivers Editor.


Main Region
===========

The main view allows you to view and edit Driver F-curves.
An F-curve has several key parts:

Axes
   The curve defines the relationship between two properties:
   The current (driven) property (Y axis) and the driver (X axis).

   See :doc:`F-Curves </editors/graph_editor/fcurves/index>`.

Handles
   Each point on the driver curve has a handle that helps determine the relationship between the two values.
   They can be selected and modified to change the shape of the curve.

   See :ref:`F-Curve Handles <editors-graph-fcurves-settings-handles>` for more information.

.. figure:: /images/editors_graph-editor_introduction_f-curve-example.png

   A simple driver.

.. seealso::

   See :doc:`F-Curves </editors/graph_editor/fcurves/introduction>` for more info.


Navigation
----------

As with most editors, you can:

Pan :kbd:`MMB`
   Pan the view vertically (values) or horizontally (time) with click and drag :kbd:`MMB`.
Zoom :kbd:`Wheel`
   Zoom in and out with the mouse wheel.
Scale View :kbd:`Ctrl-MMB`
   Scale the view vertically or horizontally.
Frame All :kbd:`Home`
   Fit the curve in the available space.

In addition, you can also use the scrollbars to pan and zoom the view.


Header
======

View Controls
-------------

.. figure:: /images/editors_graph-editor_introduction_header-view.png
   :width: 350px

   View controls.

Normalize
   Normalize curves so the maximum and minimum points equal 1.0 and -1.0 respectively.

   Auto
      Automatically recalculate curve normalization on every curve edit.
      Disabling this setting may be useful to prevent curves from jumping after tweaking.

Show Only Selected (mouse cursor icon)
   Only include curves related to the selected objects and data.
Show Hidden (dashed object icon)
   Include curves from objects/bones that are not visible.
Show Only Errors (warning triangle icon)
   Only include curves and drivers that are disabled or have errors.
   Useful for debugging.

Create Ghost Curves (square with curve icon)
   Makes a visual indication in the background of the editor
   with a snapshot of the current state of the selected curves.
   This is useful to have a base for comparison on top of which to make edits.

Filter (funnel icon)
   Type Filter
      Filter curves by property type.

   Sort Data-Blocks (az icon)
      Object data-blocks appear in alphabetical order, so that it is easier to find where they occur
      (as well as helping to keep the animation of related objects together).

      This option may affect the playback speed for heavy scenes.


Curve Controls
--------------

.. figure:: /images/editors_graph-editor_introduction_header-edit.png
   :width: 250px

   Curve controls.

Pivot Point
   Pivot point for rotation.

   Bounding Box Center
      Center of the selected curve handles.
   2D Cursor
      Center of the *2D Cursor*. *Playhead* + *Cursor*.
   Individual Centers
      Rotate the selected curve handles.

Auto Snap
   Auto snap the curve handles when editing.

   - No Auto-Snap
   - Frame Step
   - Second Step
   - Nearest Frame
   - Nearest Second
   - Nearest Marker

Proportional Editing :kbd:`O`
   See :doc:`Proportional Editing </editors/3dview/controls/proportional_editing>`.


Sidebar Region
==============

Drivers Tab
-----------

See :doc:`/animation/drivers/drivers_panel`.


Modifiers Tab
-------------

See :doc:`F-Curve Modifiers </editors/graph_editor/fcurves/modifiers>`.


.. (Todo) duplicated here: \editors\graph_editor\fcurves\properties.rst

View Properties Panel
---------------------

.. figure:: /images/editors_graph-editor_introduction_view-panel.png

   View Properties panel.

Show Cursor
   Show the vertical *Cursor*.
Cursor from Selection
   Set the *2D cursor* to the center of the selected curve handles.
Cursor X
   *Time Cursor* X position.
Cursor Y
   Vertical *Cursor* Y position.
