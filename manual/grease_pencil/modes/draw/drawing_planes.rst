.. _bpy.types.GPencilSculptSettings.lock_axis:

**************
Drawing Planes
**************

.. admonition:: Reference
   :class: refbox

   :Mode:      Draw Mode and Sculpt Mode
   :Header:    :menuselection:`Drawing Planes`

The Drawing Planes selector helps to select
the plane in which the newly created strokes are drawn.

To see which plane you are using when drawing strokes,
you can enable *Canvas* in :ref:`Viewport Overlays <3dview-overlay-grease-pencil>`.
See :doc:`Viewport Display </interface/controls/templates/curve>` to know more about Canvas settings.

.. note::

   The Drawing Plane selected has effect only for new strokes and does not affect the existing ones.


Plane Options
=============

.. figure:: /images/grease-pencil_modes_draw_drawing-planes_selector.png
   :align: right

   Drawing Planes selector in the 3D Viewport header.

Front
   Strokes are drawn on the plane determined by the XZ axes (front view).

Side
   Strokes are drawn on the plane determined by the YZ axes (side view).

Top
   Strokes are drawn on the plane determined by the XY axes (top view).

View
   Strokes are drawn with the current 3D Viewport orientation.

Cursor
   Strokes are drawn with the current 3D cursor orientation.


Examples
========

.. list-table:: Stroke using different Drawing Planes with Canvas overlay activated.

   * - .. figure:: /images/grease-pencil_modes_draw_drawing-planes_front.png
          :width: 200px

          Front.

     - .. figure:: /images/grease-pencil_modes_draw_drawing-planes_side.png
          :width: 200px

          Side.

     - .. figure:: /images/grease-pencil_modes_draw_drawing-planes_top.png
          :width: 200px

          Top.

     - .. figure:: /images/grease-pencil_modes_draw_drawing-planes_view.png
          :width: 200px

          View.

     - .. figure:: /images/grease-pencil_modes_draw_drawing-planes_cursor.png
          :width: 200px

          Cursor.
