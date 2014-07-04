
Graph Editor
============

The graph editor is the main animation editor.
It allows you to modify the animation for any properties using :doc:`F-Curves <animation/editors/graph/fcurves>`.

The graph editor has two modes, *F-Curve* for :doc:`Actions <animation/basics/actions>`,
and *Drivers* for :doc:`Drivers <animation/basics/drivers>`. Both are very similar in function.


.. figure:: /images/Doc_Graph_Editor.jpg
   :width: 600px
   :figwidth: 600px

   The Graph Editor.


Curve Editor Area
-----------------

Here you can see and edit the curves and keyframes.


.. figure:: /images/Doc_Graph_Curve.jpg

   A curve with different types of interpolation.


See :doc:`F-Curves <animation/editors/graph/fcurves>`
and :doc:`Editing <animation/editors/graph/editing>` for more info.


Navigation
__________

As with most windows, you can:

*Pan* :kbd:`mmb`
   Pan the view vertically (values) or horizontally (time) with click and drag.

*Zoom* :kbd:`wheel`
   Zoom in and out with the mouse wheel.

*Scale View* :kbd:`ctrl-mmb`
   Scale the view vertically or horizontally.

These are some other useful tools.

*View All* :kbd:`Home`
   Reset viewable area to show all keyframes.

*View Selected* :kbd:`Numpad-.`
   Reset viewable area to show selected keyframes.


2D Cursor
_________

.. figure:: /images/Doc_Graph_2DCursor.jpg

   Graph Editor 2D Cursor.


The current frame is represented by a green vertical line called the *Time Cursor*.

As in the :doc:`Timeline <animation/editors/timeline>`, you can change the current frame by pressing or holding :kbd:`lmb`.

The green horizontal line is called the *Cursor*.
This can be disabled via the *View Menu* or the *View Properties* panel.

The *Time Cursor* and the *Cursor* make the *2D Cursor*.
The *2D Cursor* mostly used for editing tools.


View Axes
_________

For *Actions* the X-axis represents time,
the Y-axis represents the value to set the property.

For *Drivers* the X-axis represents the *Driver Value*,
the Y-axis represents the value to set the property.

Depending on the selected curves, the values have different meaning:
For example rotation properties are shown in degrees,
location properties are shown in Blender Units.
Note that *Drivers* use radians for rotation properties.


Markers
_______

Like with most animation editors, markers are shown at the bottom of the editor.


.. figure:: /images/Doc_Graph_Markers.jpg

   Graph Editor Markers.


*Markers* can be modified in the *Graph Editor* though its usually best to use the *Timeline*.

See :doc:`Marker Menu <animation/editors/graph/editing#marker_menu>` or :doc:`Markers <animation/basics/markers>` for more info.


Header
------

Here you'll find.


- The menus.
- Graph Editor mode.
- View controls.
- Curve controls.


Menus
_____

See :doc:`Header Menus <animation/editors/graph/editing#header_menus>` for more info.


Header Controls
_______________

.. figure:: /images/Doc_Graph_Header_Mode.jpg

   Graph Mode.



*Mode*
   F-Curve for :doc:`Actions <animation/basics/actions>`, and Drivers for :doc:`Drivers <animation/basics/drivers>`.


.. figure:: /images/Doc_Graph_Header_View.jpg

   View Controls.



View controls
   *Show Only Selected*
      Only include curves related to the selected objects and data.

   *Show Hidden*
      Include curves from objects/bones that are not visible.

   *Show Only Errors*
      Only include curves that are disabled or have errors.

   *Search Filter*
      Only include curves with keywords contained in the search text.

   *Type Filter*
      Filter curves by property type.

   *Normalize*
      Normalize curves so the maximum or minimum point equals 1.0 or -1.0.

      *Auto*
          Automatically recalculate curve normalization on every curve edit.


.. figure:: /images/Doc_Graph_Header_Edit.jpg

   Curve Controls.



Curve controls
   *Auto Snap*
      Auto snap the keyframes for transformations.

      *No Auto-Snap*
      *Time Step*
      *Nearest Frame*
      *Nearest Marker*

   *Pivot Point*
      Pivot point for rotation.

      *Bounding Box Center*
          Center of the select keyframes.

      *2D Cursor*
          Center of the *2D Cursor*. *Time Cursor* + *Cursor*.

      *Individual Centers*
          Rotate the selected keyframe *Bezier* handles.

   *Copy Keyframes* :kbd:`Ctrl-C`
      Copy the selected keyframes to memory.

   *Paste Keyframes* :kbd:`Ctrl-V`
      Paste keyframes from memory to the current frame for selected curves.

   *Create Snapshot*
      Creates a picture with the current shape of the curves.


Channels Region
---------------

.. figure:: /images/Doc_Graph_Channels.jpg

   Channels Region.


The channels region is used to select and manage the curves for the graph editor.

*Hide curve*
   Represented by the eye icon.

*Deactive/Mute curve*
   Represented by the speaker icon.

*Lock curve from editing*
   Represented by the padlock icon.


Channel Editing
_______________

*Select channel* :kbd:`LMB`

*Multi Select/Deselect* :kbd:`Shift-LMB`

*Toggle Select All* :kbd:`A`

*Border Select* :kbd:`Drag-LMB` or :kbd:`B` :kbd:`Drag-LMB`

*Border Deselect* :kbd:`Shift-Drag-LMB` or :kbd:`B` :kbd:`Shift-Drag-LMB`

*Delete selected* :kbd:`X` or :kbd:`Delete`

*Lock selected* :kbd:`Tab`

*Make only selected visible* :kbd:`V`

*Enable Mute Lock selected*  :kbd:`Shift-Ctrl-W`

*Disable Mute Lock selected* :kbd:`Alt-W`

*Toggle Mute Lock selected* :kbd:`Shift-W`

See :doc:`Channel Menu <animation/editors/graph/editing#channel_menu>` for more info.


Properties Region
-----------------

The panels in the *Properties Region*.


View Properties Panel
_____________________

.. figure:: /images/Doc_Graph_View_Properties_Panel.jpg

   View Properties Panel.


*Show Cursor*
   Show the vertical *Cursor*.

*Cursor from Selection*
   Set the *2D cursor* to the center of the selected keyframes.

*Cursor X*
   *Time Cursor* X position.

   *To Keys*
      Snap selected keyframes to the *Time Cursor*.

*Cursor Y*
   Vertical *Cursor* Y position.

   *To Keys*
      Snap selected keyframes to the *Cursor*.


Active F-Curve Panel
____________________

.. figure:: /images/Doc_Graph_Active_Fcurve_Panel.jpg

   Active F-Curve Panel.


This panel displays properties for the active *F-Curve*.

*Channel Name* (X Location)
   *ID Type* + Channel name.

*RNA Path*
   *RNA Path* to property + Array index.

*Color Mode*
   *Color Mode* for the active *F-Curve*.

   *Auto Rainbow*
      Increment the *HUE* of the *F-Curve* color based on the channel index.

   *Auto XYZ to RGB*
      For property sets like location xyz, automatically set the set of colors to red, green, blue.

   *User Defined*
      Define a custom color for the active *F-Curve*.


Active Keyframe Panel
_____________________

.. figure:: /images/Doc_Graph_Active_Keyframe_Panel.jpg

   Active Keyframe Panel.


*Interpolation*
   Set the forward interpolation for the active keyframe.

   *Constant*
      Keep the same value till the next keyframe.

   *Linear*
      The difference between the next keyframe.

   *Bezier*
      Bezier interpolation to the next keyframe.

*Key*
   *Frame*
      Set the frame for the active keyframe.

   *Value*
      Set the value for the active keyframe.

*Left Handle*
   Set the position of the left interpolation handle for the active keyframe.

*Right Handle*
   Set the position of the right interpolation handle for the active keyframe.


Drivers Panel
_____________

.. figure:: /images/Doc_Graph_Drivers_Panel.jpg

   Drivers Panel.


See :doc:`Drivers Panel <animation/basics/drivers#drivers_panel>` for more info.


Modifiers Panel
_______________

.. figure:: /images/Doc_Graph_Modifiers_Panel.jpg

   Modifiers Panel.


See :doc:`F-Modifiers <animation/editors/graph/fmodifiers>` for more info.


See Also
--------

- :doc:`Graph Editor - F-Curves <animation/editors/graph/fcurves>`
- :doc:`Graph Editor - F-Modifiers <animation/editors/graph/fmodifiers>`
- :doc:`Graph Editor - Editing <animation/editors/graph/editing>`
- :doc:`Actions <animation/basics/actions>`
- :doc:`Drivers <animation/basics/drivers>`


