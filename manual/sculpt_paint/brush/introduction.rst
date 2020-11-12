
************
Introduction
************

.. figure:: /images/sculpt-paint_brush_introduction_brush-circle.png
   :align: center

   Brush cursor.


Brush Control
=============

- Set brush size :kbd:`F`
- Set brush strength :kbd:`Shift-F`
- Rotate brush texture :kbd:`Ctrl-F`
- Invert stroke toggle :kbd:`Ctrl`

You can then either adjust the value interactively or by typing in numbers.
After pressing the hotkey move the mouse to increase/reduce the value
(additionally with precision and/or snapping activated).
Finally confirm (:kbd:`LMB`, :kbd:`Return`) or cancel (:kbd:`RMB`, :kbd:`Esc`).


Selection Masking
=================

If you have a complex mesh, it is sometimes not easy to paint on all vertices.
Suppose you only want to paint on a small area of the Mesh and keep the rest untouched.
This is where "selection masking" comes into play. When this mode is enabled,
a brush will only paint on the selected vertices or faces.
The option is available from the header of the 3D View
(see icons surrounded by the yellow frame):

.. figure:: /images/sculpt-paint_brush_introduction_select.png

   You can choose between *Face Selection masking* (left button)
   and *Vertex selection masking* (right button).

Selection masking has some advantages over the default paint mode:

- The original mesh edges are shown, even when modifiers are active.
- You can select faces to restrict painting to the vertices of the selected faces.


Details About Selecting
-----------------------

The following standard selection operations are supported:

- :kbd:`RMB` -- Single faces. Use :kbd:`Shift-RMB` to select multiple.
- :kbd:`A` -- All faces, also to deselect.
- :kbd:`B` -- Box selection.
- :kbd:`C` -- Circle select with brush.
- :kbd:`L` -- Pick linked (under the mouse cursor).
- :kbd:`Ctrl-L` -- Select linked.
- :kbd:`Ctrl-I` -- Invert selection *Inverse*.


Vertex Selection Masking
------------------------

.. admonition:: Reference
   :class: refbox

   :Mode:      Vertex and Weight Paint Modes
   :Header:    :menuselection:`Vertex Selection`
   :Hotkey:    :kbd:`V`

In this mode you can select one or more vertices and then paint only on the selection.
All unselected vertices are protected from unintentional changes.

.. figure:: /images/sculpt-paint_brush_introduction_vertex-select.png

   Vertex Selection masking.


.. _bpy.types.Mesh.use_paint_mask:

Face Selection Masking
----------------------

.. admonition:: Reference
   :class: refbox

   :Mode:      Texture, Vertex, and Weight Paint Modes
   :Header:    :menuselection:`Paint Mask`

The *Face Selection masking* allows you to select faces and limit the paint
tool to those faces, very similar to Vertex selection masking.

.. figure:: /images/sculpt-paint_brush_introduction_face-select.png

   Face Selection masking.


Hide/Unhide Faces
-----------------

.. figure:: /images/sculpt-paint_brush_introduction_face-select-hidden.png

   Hidden faces.

You also can hide selected faces as in Edit Mode with the keyboard Shortcut :kbd:`H`,
then paint on the remaining visible faces and finally unhide the hidden faces again by using
:kbd:`Alt-H`.


Hide/Unhide Vertices
--------------------

You cannot directly hide selected faces in vertex mask selection mode.
However, you can use a trick:

#. First go to Face selection mask mode.
#. Select the areas you want to hide and then hide the faces (as explained above).
#. Switch back to Vertex Selection mask mode.

Now the vertices belonging to the hidden Faces will remain hidden.


The Clipping Region
-------------------

To constrain the paint area further you can use the *Clipping Region*.
Press :kbd:`Alt-B` and :kbd:`LMB`-drag a rectangular area.
The selected area will be "cut out" as the area of interest.
The rest of the 3D Viewport gets hidden.

.. figure:: /images/sculpt-paint_brush_introduction_border-select.png

   The Clipping Region is used to select interesting parts for local painting.

You make the entire mesh visible again by pressing :kbd:`Alt-B` a second time.

All paint tools that use the view respect this clipping, including box select, and of course brush strokes.
