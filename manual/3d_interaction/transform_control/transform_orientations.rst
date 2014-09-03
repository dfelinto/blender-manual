
..    TODO/Review: {{review|Need to change and explain the behavior of the transform orientation. It is toggled between the chosen orientation and the global orientation when transformations are made by shortcuts}} .


Transform Orientations
**********************

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object` and :guilabel:`Edit` modes
   | Hotkey:   :kbd:`alt-Space`


.. figure:: /images/Orientations-Menu-2.5+.jpg

   Transform orientations selection menu.


Orientations affect the behavior of Transformations: Location, Rotation, and Scale.
You will see an effect on the 3D Manipulator (the widget in the center of the selection),
as well as on transformation constraints (like :doc:`axis locking </3d_interaction/transform_control/axis_locking>`).
This means that, when you hit :kbd:`g-x`, it will constrain to the :guilabel:`global` x-axis,
but if you hit :kbd:`g-x-x` it will constrain to your :guilabel:`Transform Orientation` s x-axis.


.. figure:: /images/Alt+Space-Menu.jpg

   Alt+Space Menu.


The Orientations options can be set on the 3D View's header (or "footer",
since it is at the bottom of the view by default),
or with :kbd:`alt-Space` or through the :guilabel:`Orientation` menu in a 3D view header.


In addition to the four built-in options, you can define a
FIXME(TODO: Internal Link;
[[#Custom_Orientations|Custom Orientation]]
).


Our Demo Cube
=============

.. figure:: /images/Orientations-BasicSetup.jpg

   To demonstrate the various behaviors, we add some colors to the default cube, rotate it -15º along its local z- and x-axes, and we scale its "y" face down.


Please note two things:

- The "Mini-axis" in the lower-left corner, which represents the Global x/y/z orientation.
- The :doc:`"Object Manipulator" </3d_interaction/transform_control/manipulators>` widget emanating from the
  selection, which represents the current Transform Orientation.
  - If you click on one of the axes of the Manipulator with :kbd:`LMB`,
    it will allow you to constrain movement to only this direction. An example of a keyboard equivalent is :kbd:`g-z-z`.
  - If you :kbd:`Shift-LMB` click,
    it will lock the axis you clicked on and allow you to move in the plane of the two remaining axes.
    The keyboard analogue is :kbd:`g-Shift-Z-Shift-Z-`.


Orientations
============

.. figure:: /images/Manual-3D_interaction-Transform_Control-Transform_Orientations-01.Global.jpg

   Global.


Global
------

The manipulator matches the global axis.
When using the Global orientation, the orientation's x,y,z matches world's x,y,z axis.
When this mode is selected,
the local coordinates of the object are subjected to the Global coordinates.
This is good to place objects in the scene. To constrain an axis,
hit :kbd:`g` and the desired axis. To constrain to a local axis,
hit the desired axis two times. The difference between Global and Local, is more noticeable
when you have an object in which the origin is not located at the exact center of the object,
and doesn't match the Global coordinates.


.. figure:: /images/Manual-3D_interaction-Transform_Control-Transform_Orientations-02.Local.jpg

   Local.


Local
-----

The manipulator matches the object axis.
Notice that, here, the Manipulator is at a slight tilt
(it is most visible on the object's y-axis, the green arrow).
This is due to our 15º rotation of the object.
This demonstrates the difference between local coordinates and global coordinates.
If we had rotated the object 90º along its x-axis, we would see that the object's "Up" is the
world's "Forward" -- or the object's z-axis would now be the world's y-axis.
This orientation has an effect on many parts of the interface,
so it is important to understand the distinction.


.. figure:: /images/Manual-3D_interaction-Transform_Control-Transform_Orientations-03.Normal.jpg

   Normal.


Normal
------

The z-axis of the manipulator will match the normal vector of the selected object.
In Object Mode, this is equivalent to Local Orientation, but in Edit Mode,
it becomes more interesting.

As you see, the light blue lines indicate the faces' normals,
and the darker blue lines indicate the vertex normals (these were turned on in the
:kbd:`n` Properties Panel under :menuselection:`Mesh Display --> Normals --> Face` and
:guilabel:`Vertex`).
Selecting any given face will cause our Manipulator's z-axis to align with that normal.
The same goes for Vertex Select Mode.
Edge Select is different--A selected Edge has the z-axis aligned with it
(so you will have to look at the Manipulator widget to determine the direction of x and y).
If you select several elements, it will orient towards the average of those normals.

A great example of how this is useful is in Vertex Select Mode: Pick a vertex and then do
:kbd:`g-z-z` to tug it away from the mesh and shove it into the mesh.
To make this even more useful, select a nearby vertex and hit :kbd:`Shift-r` to repeat
the same movement---except along that second vertex's normal instead.


.. figure:: /images/Manual-3D_interaction-Transform_Control-Transform_Orientations-04.Gimbal.jpg

   Gimbal.


Gimbal
------

Gimbal's behavior highly depends on the :doc:`Rotation Mode </3d_interaction/transformations/basics/rotate>`
that you are in (accessible in the :kbd:`n` Properties Panel in the :guilabel:`3D View`,
in top section, :guilabel:`Transform`).

XYZ Euler
   the default rotation mode, the object Manipulator's z-axis will always point to the global z-axis,
   where the other two will remain perpendicular to each other.
   In the other :guilabel:`Euler` rotation modes,
   the last axis applied will be the one for which the Manipulator stays fixed.
   So, for :guilabel:`YZX Euler`, the x-axis of the Manipulator will be the same as the global x-axis.
Axis Angle
   The x, y, and z coordinates define a point relative to the object origin through which an imaginary "skewer" passes.
   The w value is the rotation of this skewer. Here, the Manipulator's z-axis stays aligned with this skewer.
Quaternion
   Though Quaternion rotation is very different from the Euler and Axis Angle rotation modes,
   the Manipulator behaves the same as in :guilabel:`Local` mode.


.. figure:: /images/Manual-3D_interaction-Transform_Control-Transform_Orientations-05.View.jpg

   View.


View
----

The manipulator will match the 3D view, Y → Up/Down, X → Left/Right,
Z → Towards/Away from you.

This way you can constrain movement to one View axis with :kbd:`g-x-x`.


..    Comment: <!--[[File:Manual-3D_interaction-Transform_Control-Transform_Orientations-06.Foozle.png|frame|right|Custom Orientations.]]
   Custom Orientations
   :(See below, [[#Custom_Orientations|Custom Orientations]]).--> .


Custom Orientations
===================

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object` and :guilabel:`Edit` modes
   | Hotkey:   :kbd:`Ctrl-Alt-Space`


..    Comment: <!--[[File:Doc26-transformOrientationPanel.png|thumb|right|200px|Transform Orientation panel]]--> .


.. figure:: /images/Doc26-transformOrientationPanel-custom.jpg

   custom orientation


You can define custom transform orientations, using object or mesh elements. Custom transform
orientations defined from objects use the local orientation of the object whereas those
defined from selected mesh elements (vertices, edges, faces)
use the normal orientation of the selection.

The :guilabel:`Transform Orientations` panel, found in the "\ :kbd:`n` Properties Panel,
" can be used to manage transform orientations: selecting the active orientation,
adding and deleting custom orientations.


.. figure:: /images/Orientations-Custom-Name.jpg
   :width: 300px
   :figwidth: 300px

   Renaming a Custom Orientation


The default name for these orientations comes from whatever you have selected. If an edge,
it will be titled, "Edge," if an object, it will take that object's name, etc. The Toolshelf
(:kbd:`t` in the 3D View)
allows you to rename the custom orientation after you hit :kbd:`Ctrl-Alt-Space`.


.. figure:: /images/Orientations-Custom-Extrusion.jpg

   Figure 1.


The technique of creating custom orientations can become important in creating precise meshes.
In :guilabel:`Figure 1`, to achieve this effect:

- Select the object's sloping top edge
- Create a Custom Orientation with :kbd:`Ctrl-Alt-Space` and rename it "Top Edge".
- Select the objects's bottom, right edge.
- Extrude with :kbd:`e`.
- Cancel the extrusion's default movement by hitting :kbd:`RMB` or :kbd:`Escape`.
- Hit :kbd:`g` to reinitiate movement.
- Hit :kbd:`z-z` to constrain to the "Top Edge" orientation.

