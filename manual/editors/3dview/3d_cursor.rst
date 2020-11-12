.. _bpy.types.View3DCursor:
.. _editors-3dview-3d_cursor:

*********
3D Cursor
*********

The 3D Cursor is a point in 3D space which can be used for a number of purposes.


Placement
=========

There are a few methods to position the 3D cursor.


Direct Placement with the Mouse
-------------------------------

.. figure:: /images/editors_3dview_3d-cursor_two-view-positioning.png
   :align: center

   Positioning the 3D cursor with two orthogonal views.

With the cursor tool enabled, using :kbd:`LMB` in the 3D Viewport will place the 3D cursor
directly under your mouse pointer.

The view space is used to control the rotation of the 3D Cursor.

For accuracy you should use two perpendicular orthogonal 3D Views,
i.e. any combination of top :kbd:`Numpad7`, front :kbd:`Numpad1` and side :kbd:`Numpad3`.
That way you can control the positioning along two axes in one view and
determine depth in the second view.

By default the depth of the geometry under the cursor is used,
this can be disabled using the *Cursor Surface Project* toggle
in the :doc:`Preferences </editors/preferences/editing>`.

.. seealso::

   The :doc:`Snap Menu </editors/3dview/controls/snapping>`
   which allows the cursor placement relative to scene objects.


3D Cursor Panel
---------------

.. admonition:: Reference
   :class: refbox

   :Mode:      All Modes
   :Panel:     :menuselection:`Sidebar region --> View --> 3D Cursor`

.. figure:: /images/editors_3dview_3d-cursor_panel.png

   The 3D Cursor panel of the Sidebar region.

The 3D cursor can also be positioned and oriented by editing these values:

Location
   The location of the 3D Cursor.

Rotation
   The rotation of the 3D Cursor.

Rotation Mode
   The Rotation mode of the 3D Cursor.


Usage
=====

The 3D Cursor is used as the origin for any added object, can be used and moved with
the :doc:`snap tool </editors/3dview/controls/snapping>`, and is an option for
the :doc:`pivot point </editors/3dview/controls/pivot_point/index>`.
