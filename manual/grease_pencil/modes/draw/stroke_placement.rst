.. _bpy.types.ToolSettings.gpencil_stroke_placement:

****************
Stroke Placement
****************

.. admonition:: Reference
   :class: refbox

   :Mode:      Draw Mode
   :Header:    :menuselection:`Stroke Placement`

The Stroke Placement selector helps to select the location
in which the newly created strokes are drawn.

.. note::

   The Stroke Placement selected has effect only for new strokes and does not affect the existing ones.


Placement Options
=================

.. figure:: /images/grease-pencil_modes_draw_stroke-placement_selector.png
   :align: right

   Stroke Placement selector on 3D Viewport header.

Origin
   Strokes are placed at Grease Pencil object origin.

3D Cursor
   Strokes are placed at 3D cursor.

Surface
   Strokes will stick on mesh surfaces.

   Offset
      Distance from the mesh surface to place the new strokes.

Stroke
   Strokes will stick on other strokes.

   Target
      All Points
         All the points of the new stroke sticks to other strokes.

      End Points
         Only the start and end points of the new stroke sticks to other strokes.

      First Point
         Only the start point of the new stroke sticks to other strokes.


Examples
========

.. list-table:: Stroke using different Stroke Placements.

   * - .. figure:: /images/grease-pencil_modes_draw_stroke-placement_origin.png
          :width: 200px

          Origin.

     - .. figure:: /images/grease-pencil_modes_draw_stroke-placement_3D-cursor.png
          :width: 200px

          3D Cursor.

     - .. figure:: /images/grease-pencil_modes_draw_stroke-placement_surface.png
          :width: 200px

          Surface.

     - .. figure:: /images/grease-pencil_modes_draw_stroke-placement_stroke.png
          :width: 200px

          Stroke.
