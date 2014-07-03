
..    TODO/Review: {{review|}} .


Grab/Move
=========

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object` Mode, :guilabel:`Edit` Mode, and :guilabel:`Pose` Mode for the 3D View; :guilabel:`UV/Image Editor` Tools, :guilabel:`Sequence Editor`\ ,
   |           :guilabel:`Dopesheet`\ , and :guilabel:`Graph Editor` for other specific types of Grab/Move operations.
   | Menu:     Context Sensitive, Object Based → :guilabel:`Transform` → :guilabel:`Grab/Move`
   | Hotkey:   :kbd:`g` or combinations for specific Axis constraint


This option lets you translate your Objects when in Object Mode, or the elements that are used
in the Object construction in the 3D space of the active 3D Viewport.It offers similar
functionality in various other editor environments like Node editor, Graph editor, UV editor,
Sequencer etc.
Further details of the option will be discussed in the related sections in detail.


.. figure:: /images/Doc_Blender_26_3D_inter_translate_value_display.jpg

   Translation Display


While translating, the amount of change in the co-ordinates is displayed at the bottom left
corner of the 3D view window.


3D View
-------

There are **2** types of Grab/Move options in the :guilabel:`3D View`\ :

- Using shortcuts and combinations of shortcuts.
- Using the :guilabel:`Transform Widget` helper, when you choose the :guilabel:`Translation Widget` in the header of the 3DView.


Transform Widget
~~~~~~~~~~~~~~~~

.. figure:: /images/FAQ-Transform_widget-2.jpg

   Translation Widget


In the default installation of Blender,
this is the :guilabel:`Transform Widget` active by default. You can access this option by
click holding :kbd:`lmb` and dragging the 3D translatation widget in the 3D view itself.


Shortcuts in the 3D View
~~~~~~~~~~~~~~~~~~~~~~~~

One of the fastest ways to move things in 3D space is with :kbd:`g`\ .
Pressing this hotkey will enter the "grab/move" transformation mode,
where the selected object or data is moved freely, according to the mouse pointer's location.
Using combinations of this shortcut with specifc shortcuts to specify a chosen axis,
will give you full control over your transformation

:kbd:`lmb`
   Confirm the move, and leave the object or data at its current location on the screen.


.. figure:: /images/Doc_blender_26_3D_interaction_trans_basics_grab_mmb.jpg

   Axis-Constraint in action


:kbd:`mmb`
   Constrain the move to the X, Y or Z axis automatically, according to the position of the mouse pointer in the 3D View. After pressing the :kbd:`g` key, if the :kbd:`mmb` is pressed, a visual option to constrain the translation will be available, showing the three axis in the 3D View space. The axis of choice to confirm the operation, will depend on the axis about which the :kbd:`mmb` is released. At any point during th eoperation, the chosen axis can be changed by hitting :kbd:`X`\ , :kbd:`Y`\ , :kbd:`Z` on the keyboard.

:kbd:`rmb` or :kbd:`esc`
   Cancel the move, and return the object or data to its original location.

:kbd:`alt + G`
   Clears all the previously done transformation on the object.Works only in Object Mode.


.. figure:: /images/Doc_blender_26_manual_basic_trans_grab_shift_xyz.jpg

   Shift+X in action


:kbd:`shift` and :kbd:`X`\ :kbd:`Y`\ :kbd:`Z`
   Complementary axis transformation constraint. With this option, we can isolate the transformation to axis complementary to the choosen axis. When a specific axis is choosen, the translation will occur in all axes other than the chooosen one. This can be seen in the example image


Controling Grab/Move Precision
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In addition to the Axis constraint options listed above, Blender offer some options to limit
the amount of the transformation in small or predefined steps.

:kbd:`Shift`
   Slow transformation option. While still in the grab mode i.e.,after :kbd:`g` pressed, if the :kbd:`shift` key is pressed, the rate of transformation is reduced giving you precise translation.

:kbd:`Ctrl`
   :doc:`Snap <3d_interaction/transform_control/snap>` while grabbing the object based on the snapping constraint which has been already set. For this option you may not necessarily enable the snap option. It will work from the snap disabled mode itself.

:kbd:`Ctrl`\ :kbd:`+`\ :kbd:`Shift`
    Intuitively this is the combination of the :kbd:`Ctrl` and the :kbd:`Shift` operations individually. This option will move the object with high precission along with the snapping constraint.

:kbd:`X/Y/Z + <Decimal Number>`
   This option will limit the transformation to the specified axis and the decimal number specified will be the magnitude of the translation along that axis. This decimal number which is being entered will be displayed at the bottom left corner of the 3D view window. Hitting backspace during the number entry will remove the numerical specification option but the object will be in the same axis.The number can be retyped to specify the translation.At any point of time, axis can be changed by hitting x/y/z key. You can also use this to move to a specific location or increase distance for the object location.

Orientations
------------

There are 5 orientations for all tranformations.
[[File:Doc_blender_26_3d_interaction_grab_orientation.png|frame|right|Orientation choice menu]]

- Global(default)
- Local
- Normal
- Gimbal
- View

Read more about transform orientations [[Doc:2.6/Manual/3D_interaction/Transform_Control/Transform_Orientations|Here]]

Each mode is a co-ordinate system in which the transformations can be carried out. These
orientations can be chosen from the pop up menu just by the side of transformation manipulator
choice widget group.

   {{Shortcut|G}} key followed by {{Shortcut|xx}} or {{Shortcut|yy}} or {{Shortcut|zz}} will directly allow you to translate the objects in local axis. Of course this can also be followed by numerical specification of the displacement of entity.

   Similar to above operation, {{Shortcut|G}} key followed by {{Shortcut|Shift}} and {{Shortcut|xx}} or {{Shortcut|yy}} or {{Shortcut|zz}} will directly allow you to translate the objects in local axis complementary to the one specified.

{{clr}}

[[File:Doc_blender_26_manual_basic_trans_grab_xyz_number.png|frame|right|Numerical Entry Display]]
{{clr}}


Other Editor Windows
--------------------

For the other Editor Windows, like UV/Image Editor Tools, Sequence Editor, Dopesheet, and Graph Editor,
the Grab/Move Operations are used to move Objects or elements based in their context, but,
differently from the 3D View, you will see only two axis, **X** and **Y** normally,
and although we are explaining the Grab/Move in the **3D Interaction** section,
those Objects and elements are shown in a 3D Interface.
Blender will simply constrain the movement of a third possible axis.
Most of the shortcuts used in the 3D View,
are also used when interacting with those Editor Windows.
This is also true for all of the other transformations, like rotate and scale.


Python Scripting
----------------

You can also use Python Scripting in Blender to Grab/Move Objects or elements to a specific
location, either using the Python interactive console,
or running a Python script in the Text Editor Window.


Getting the location vector for current object ``bpy.context.scene.objects.active.location``
Returns you the location vector for the active object in the scene.One can assign a different
value to the location vector to change the position of the object.

Operator for translating active object and its syntax:

.. code-block:: python

   bpy.ops.transform.translate(value=(<DX>, <DY>, <DZ>), constraint_axis=(<bool>, <bool>,<bool>), constraint_orientation='<ORIENTATION NAME>', mirror=<bool>, proportional='<ENABLE?DISABLE>', proportional_edit_falloff='<FALLOFF TYPE>', proportional_size=<INT>, snap=<bool>, snap_target='<SNAP TARGET>', snap_point=<x,y,z>, snap_align=<bool>, snap_normal=<x,y,z>, texture_space=<bool>, release_confirm=<bool>)


Hints
-----

- Moving object in Object mode is clearly different from moving the object by selecting all its vertices/edges/faces in Edit mode. Doing this can lead to disturbed Center of Transformation for the given object.
- If G+x/y/z  is used in non global orientations, it won't confine the translation to x axis in that orientation but to the global X axis orientation only


{{Page/Footer|2.6x|Doc:2.6/Manual/3D interaction/Transformations/Basics/Grab Properties|Doc:2.6/Manual/3D interaction/Transformations/Basics/Grab}}
