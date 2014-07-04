
Graph Editor - Editing
======================

Tools and menus for the :doc:`F-Curves <animation/editors/graph/fcurves>` in the *Graph Editor*.

By default, when new channels are added, the *Graph Editor* sets them to *Edit Mode*.
Selected channels can be locked by pressing :kbd:`tab`.


Basic Tools
-----------

These are some basic tools to modify the curves and keyframes.


Transformations
_______________

.. figure:: /images/Doc_Graph_Active_Keyframe_Panel.jpg

   Active Keyframe Panel.


*Grab/Move* selected keyframes :kbd:`G`

*Rotate* selected keyframes :kbd:`R`

*Scale* selected keyframes :kbd:`S`

Additionally, for translation and scaling, you can lock the transformation along the X
(time frame) or Y (value),
as usual by pressing :kbd:`X` or :kbd:`Y` during transformation.

For precise control of the keyframe position and value,
you can set values in the *Active Keyframe* of the Properties Region.


Selection
_________

*Select Keyframe* :kbd:`RMB`

*Toggle Select* multiple keyframes :kbd:`Shift-RMB`

*Toggle Select All* :kbd:`A`

*Select Linked* :kbd:`L`

*Border Select* :kbd:`B` :kbd:`Drag-LMB`

*Border Deselect* :kbd:`B` :kbd:`Shift-Drag-LMB`


Editing
_______

*Duplicate selected keyframes* :kbd:`Shift-D`

*Add keyframe to active curve* :kbd:`Ctrl-LMB`

*Insert keyframes to the Time Cursor* :kbd:`I`

*Copy Keyframes* :kbd:`Ctrl-C`
   Copy the selected keyframes to memory.

*Paste Keyframes* :kbd:`Ctrl-V`
   Paste keyframes from memory to the current frame for selected curves.


Curves and Keyframes
____________________

*Set Keyframe Extrapolation* :kbd:`Shift-E`
   *Constant Extrapolation*
   *Linear Extrapolation*
   *Make Cyclic (F-Modifier)*
   *Clear Cyclic (F-Modifier)*

*Set Keyframe Interpolation* :kbd:`T`
   *Constant*
   *Linear*
   *Bezier*

*Set Keyframe Handle Type* :kbd:`V`
   *Free*
   *Vector*
   *Aligned*
   *Automatic*
   *Auto Clamped*

See :doc:`F-Curves <animation/editors/graph/fcurves>` for more info.


View Tools
__________

*View All* :kbd:`Home`

*View Selected* :kbd:`Numpad-.`

*Set Preview Range* :kbd:`Ctrl-P`

*Auto-Set Preview Range* :kbd:`Ctrl-Alt-P`

*Clear Preview Range* :kbd:`Alt-P`

*Toggle Show Handles* :kbd:`Ctrl-H`

*Toggle Show Seconds* :kbd:`Ctrl-T`


More Tools
----------

Some other tools used to modify the the curves and keyframes.


Transform Snapping
__________________

When transforming keyframes with :kbd:`G`, :kbd:`R`, :kbd:`S`,
the transformation can be snapped to increments.

Snap Transformation to 1.0 :kbd:`Ctrl`

Divide Transformation by 10.0 :kbd:`Shift`

Keyframes can be snapped to different properties by using the *Snap Keys* tool.

*Snap Keys* :kbd:`Shift-S`
   :guilabel:`Current Frame`
      Snap the selected keyframes to the *Time Cursor*.
   :guilabel:`Cursor Value`
      Snap the selected keyframes to the *Cursor*.
   :guilabel:`Nearest Frame`
      Snap the selected keyframes to their nearest frame individually.
   :guilabel:`Nearest Second`
      Snap the selected keyframes to their nearest second individually, based on the *FPS* of the scene.
   :guilabel:`Nearest Marker`
      Snap the selected keyframes to their nearest marker individually.
   :guilabel:`Flatten Handles`
      Flatten the *Bezier* handles for the selected keyframes.


+-----------------------------------+-------------------------------------------------------------------+-------------------------------------------------------------------+
+*Flatten Handles snapping example.*|.. figure:: /images/Manual-Animation-F-Curves-Flatten-Handles-1.jpg|.. figure:: /images/Manual-Animation-F-Curves-Flatten-Handles-2.jpg+
+                                   |   :width: 200px                                                   |   :width: 200px                                                   +
+                                   |   :figwidth: 200px                                                |   :figwidth: 200px                                                +
+                                   |                                                                   |                                                                   +
+                                   |   Before Flatten Handles.                                         |   After Flatten Handles.                                          +
+-----------------------------------+-------------------------------------------------------------------+-------------------------------------------------------------------+


Mirror
______

Selected keyframes can be mirrored over different properties using the the *Mirror Keys*
tool.

*Mirror Keys* :kbd:`Shift-M`
   :guilabel:`By Times Over Current Frame`
      Mirror horizontally over the *Time Cursor*.
   :guilabel:`By Values over Cursor Value`
      Mirror vertically over the *Cursor*.
   :guilabel:`By Times over Time 0`
      Mirror horizontally over frame 0.
   :guilabel:`By Values over Value 0`
      Mirror vertically over value 0.
   :guilabel:`By Times over First Selected Marker`
      Mirror horizontally the over the first selected *Marker*.


Clean Keyframes
_______________

*Clean Keyframes* resets the keyframe tangents to their auto-clamped shape, if they have been modified.

*Clean Keyframes* :kbd:`O`


+-------------------------------------------+-------------------------------------------+
+.. figure:: /images/Doc26-fcurve-clean1.jpg|.. figure:: /images/Doc26-fcurve-clean2.jpg+
+   :width: 300px                           |   :width: 300px                           +
+   :figwidth: 300px                        |   :figwidth: 300px                        +
+                                           |                                           +
+   Fcurve before cleaning                  |   Fcurve after cleaning                   +
+-------------------------------------------+-------------------------------------------+


Smoothing
_________

(:kbd:`Alt-O` or :menuselection:`Key --> Smooth Keys`)
There is also an option to smooth the selected curves , but beware: its algorithm seems to be
to divide by two the distance between each keyframe and the average linear value of the curve,
without any setting, which gives quite a strong smoothing! Note that the first and last keys
seem to be never modified by this tool.


+-------------------------------------------+-------------------------------------------+
+.. figure:: /images/Doc26-fcurve-clean1.jpg|.. figure:: /images/Doc26-fcurve-smooth.jpg+
+   :width: 300px                           |   :width: 300px                           +
+   :figwidth: 300px                        |   :figwidth: 300px                        +
+                                           |                                           +
+   Fcurve before smoothing                 |   Fcurve after smoothing                  +
+-------------------------------------------+-------------------------------------------+


Sampling and Baking Keyframes
_____________________________

:guilabel:`Sample Keyframes` :kbd:`Shift-O`
   Sampling a set a keyframes replaces interpolated values with a new keyframe for each frame.


+-------------------------------------------+--------------------------------------------+
+.. figure:: /images/Doc26-fcurve-sample.jpg|.. figure:: /images/Doc26-fcurve-sample2.jpg+
+   :width: 300px                           |   :width: 300px                            +
+   :figwidth: 300px                        |   :figwidth: 300px                         +
+                                           |                                            +
+   Fcurve before sampling                  |   Fcurve after sampling                    +
+-------------------------------------------+--------------------------------------------+


:guilabel:`Bake Curves`  :kbd:`Alt-C`
   Baking a curve replaces it with a set of sampled points, and removes the ability to edit the curve.


Header Menus
------------

*Graph Editor* header menus.


View Menu
_________

Apart from the standard options like zoom-in/out, maximize window, center view on cursor,
etc., this menu gathers various other options.

:guilabel:`Properties` :kbd:`N`
   Opens the properties panel on the right side of the graph editor.

:guilabel:`Realtime Updates`
   When transforming keyframes, changes to the animation data are flushed to other views.

:guilabel:`Show Frame Number Indicator`
   Show frame number beside the current frame indicator line.

:guilabel:`Show Cursor`
   Shows the 2d cursor.

:guilabel:`Show Sliders`
   Show sliders beside F-Curve channels.

:guilabel:`Show Group Colors`
   Draw groups and channels with colors matching their corresponding groups.

:guilabel:`AutoMerge Keyframes`
   Automatically merge nearby keyframes.

:guilabel:`Use High Quality Drawing`
   Draw F-Curves using Anti-Aliasing and other fancy effects (disable for better performance).

:guilabel:`Show Handles`
   Show handles of Bezier control points.

:guilabel:`Only Selected Curve Keyframes`
   Only keyframes of selected F-Curves are visible and editable.

:guilabel:`Only Selected Keyframe handles`
   Only show and edit handles of selected keyframes.

:guilabel:`Show Seconds`
   Show timing in seconds not frames.

:guilabel:`Set Preview Range`, :guilabel:`Clear Preview Range` (:kbd:`ctrl-P`, :kbd:`alt-P`)
   These entries allow you to define/clear a temporary preview range to use for the :kbd:`alt-A` realtime playback (this is the same thing as the :guilabel:`Pr` option of the :doc:`Timeline window header <animation/timeline#header_controls>`).

:guilabel:`Auto-Set Preview Range` :kbd:`Ctrl-alt-P`
   Automatically set Preview Range based on range of keyframes.

:guilabel:`View All` :kbd:`Home`
   Reset viewable area to show full keyframe range.

:guilabel:`View Selected` :kbd:`pad-.`
   Reset viewable area to show selected keyframe range.


Select Menu
___________

:guilabel:`Select All` :kbd:`A`
   In edit mode, select/deselect all keyframes.
   In locked mode, select/deselect all visible channels.

:guilabel:`Invert Selection` :kbd:`Ctrl-I`
   Inverts selected keys.

:guilabel:`Border Select` :kbd:`B`
   Allows selection of keyframes within a region.

:guilabel:`Border Axis Range` :kbd:`Alt-B`
   Axis Range...
:guilabel:`Border (include Handles` :kbd:`Ctrl-B`
   Include Handles, handles tested individually against the selection criteria.

:guilabel:`Columns on Selected Keys` :kbd:`K`
   Select all keys on same frame as selected one(s).

:guilabel:`Column on current Frame` :kbd:`Ctrl-K`
   Select all keyframes on the current frame.

:guilabel:`Columns on selected Markers` :kbd:`Shift-K`
   Select all keyframes on the frame of selected marker(s).

:guilabel:`Between Selected Markers` :kbd:`Alt-K`
   Select all keyframes between selected markers.

:guilabel:`Before Current Frame` :kbd:`[`
   Select all keys before the current frame.

:guilabel:`After Current Frame` :kbd:`]`
   Select all keys after the current frame.

:guilabel:`Select More` :kbd:`ctrl-pad+`
   Grow keyframe selection along Fcurve.

:guilabel:`Select Less` :kbd:`ctrl-pad-`
   Shrink keyframe selection along Fcurve.

:guilabel:`Select Linked` :kbd:`L`
   Selects all keyframes on Fcurve of selected keyframe.


Marker Menu
___________

*Add Marker* :kbd:`M`

*Duplicate Marker* :kbd:`Shift-D`

*Duplicate Marker to Scene*

*Delete Marker* :kbd:`X` or :kbd:`Delete`
   Note, make sure no channels are selected.

*Rename Marker* :kbd:`Ctrl-M`

*Grab/Move Marker* :kbd:`Tweak Select`

*Jump to Next Marker*

*Jump to Previous Marker*


Channel Menu
____________

*Delete Channels* :kbd:`X` or :kbd:`Delete`

*Group Channels* :kbd:`Ctrl-G`

*Ungroup Channels* :kbd:`Alt-G`

*Toggle Channel Settings* :kbd:`Shift-W`
   *Protect*
   *Mute*

*Enable Channel Settings* :kbd:`Shift-Ctrl-W`
   *Protect*
   *Mute*

*Disable Channel Settings* :kbd:`Alt-W`
   *Protect*
   *Mute*

*Toggle Channel Editability* :kbd:`Tab`

*Set Visibilty* :kbd:`V`

*Extrapolation Mode* :kbd:`Shift-E`
   *Constant Extrapolation*
   *Linear Extrapolation*
   *Make Cyclic (F-Modifiers)*
   *Clear Cyclic (F-Modifiers)*

*Expand Channels* :kbd:`Numpad-+`

*Collapse Channels* :kbd:`Numpad--`

*Move...*
   *To Top* :kbd:`Shift-PageUp`
   *Up* :kbd:`PageUp`
   *Down* :kbd:`PageDown`
   *To Bottom* :kbd:`Shift-PageDown`

*Revive Disabled F-Curves*


Key Menu
________

*Transform*
   *Grab/Move* :kbd:`G`
   *Extend* :kbd:`E`
   *Rotate* :kbd:`R`
   *Scale* :kbd:`S`

*Snap* :kbd:`Shift-S`
   *Current Frame*
   *Cursor Value*
   *Nearest Frame*
   *Nearest Second*
   *Nearest Marker*
   *Flatten Handles*

*Mirror* :kbd:`Shift-M`
   *By Times over Current Frame*
   *By Values over Current Value*
   *By Times over Time=0*
   *By Values over Value=0*
   *By Times over First Selected Marker*

*Insert Keyframes* :kbd:`I`

*Add F-Curve Modifier*

*Bake Sound to F-Curves*

*Jump to Keyframes* :kbd:`Ctrl-G`

*Duplicate* :kbd:`Shift-D`

*Delete Keyframes* :kbd:`X` or :kbd:`Delete`

*Handle Type* :kbd:`V`
   *Free*
   *Vector*
   *Aligned*
   *Automatic*
   *Auto Clamped*

*Interpolation Mode* :kbd:`T`
   *Constant*
   *Linear*
   *Bezier*

*Clean Keyframes* :kbd:`O`

*Smooth Keyframes* :kbd:`Alt-O`

*Sample Keyframes* :kbd:`Shift-O`

*Bake Curve* :kbd:`Alt-C`

*Copy Keyframes* :kbd:`Ctrl-C`

*Paste Keyframes* :kbd:`Ctrl-V`

*Discontinuity (Euler) Filter*


