.. _tool-grease-pencil-draw-erase:

**********
Erase Tool
**********

.. reference::

   :Mode:      Draw Mode
   :Tool:      :menuselection:`Toolbar --> Erase`

The Erase tool erase already drawn strokes.


Brush Settings
==============

Radius
   The radius of the brush in pixels.

   :kbd:`F` allows you to change the brush size interactively by dragging the pointer or
   by typing a number then confirm.

   Use Pressure (pressure sensitivity icon)
      Uses stylus pressure to control how strong the effect is.
   Occlude Eraser (overlapping squares icon)
      Erase only strokes visible and not occluded by geometry.

   .. _bpy.types.BrushGpencilSettings.use_default_eraser:

   Default Eraser
      Use this brush when enabling the eraser tool with the fast switch key (:kbd:`Ctrl`).


.. _bpy.types.BrushGpencilSettings.eraser_mode:

Mode
   Determines how the erase tool behaves.

   :Dissolve:
      To simulate a raster type eraser, this eraser type
      affects the strength and thickness of the strokes before actually delete a point.
   :Point:
      Delete one point at a time.
   :Stroke:
      Delete an entire stroke.

.. _bpy.types.BrushGpencilSettings.pen_strength:

Strength
   Control how much will affect the eraser has on the stroke transparency (alpha).

   You can change the brush strength interactively by pressing :kbd:`Shift-F`
   in the 3D Viewport and then moving the pointer and then :kbd:`LMB`.
   You can also enter the size numerically.

   .. _bpy.types.BrushGpencilSettings.use_strength_pressure:

   Use Pressure (pressure sensitivity icon)
      Uses stylus pressure to control how strong the effect is.

.. _bpy.types.BrushGpencilSettings.eraser_strength_factor:

Affect Stroke Strength
   The amount of deletion of the stroke strength (alpha) while erasing.

.. _bpy.types.BrushGpencilSettings.eraser_thickness_factor:

Affect Stroke Thickness
   The amount of deletion of the stroke thickness while erasing.

Display Cursor
   Shows the brush shape in the viewport.


Usage
=====

Selecting a Brush
-----------------

In the Tool Settings select the brush to use with the tool.
The Erase tool uses :ref:`Erase Brush <grease_pencil-draw-brushes-erase>` types (soft, point and stroke).


Dissolve Erasing
----------------

- Select an erase brush of type Soft/Hard.

- Adjust brush settings.

- Click and hold :kbd:`LMB` or use the :kbd:`Pen` tip to delete strokes on the viewport.

.. list-table::

   * - .. figure:: /images/grease-pencil_modes_draw_tools_erase_soft-01.png
          :width: 200px

          Original drawing.

     - .. figure:: /images/grease-pencil_modes_draw_tools_erase_soft-02.png
          :width: 200px

          The eraser affect the transparency of the strokes.

     - .. figure:: /images/grease-pencil_modes_draw_tools_erase_soft-03.png
          :width: 200px

          Final result.


Point Erasing
-------------

- Select an erase brush of type Point.

- Adjust brush settings.

- Click and hold :kbd:`LMB` or use the :kbd:`Pen` tip to delete strokes on the viewport.

.. list-table::

   * - .. figure:: /images/grease-pencil_modes_draw_tools_erase_point-01.png
          :width: 200px

          Original drawing.

     - .. figure:: /images/grease-pencil_modes_draw_tools_erase_point-02.png
          :width: 200px

          The eraser delete one point at a time.

     - .. figure:: /images/grease-pencil_modes_draw_tools_erase_point-03.png
          :width: 200px

          Final result.


Stroke Erasing
--------------

- Select an erase brush of type Stroke.

- Adjust brush settings.

- Click and hold :kbd:`LMB` or use the :kbd:`Pen` tip to delete strokes on the viewport.

.. list-table::

   * - .. figure:: /images/grease-pencil_modes_draw_tools_erase_stroke-01.png
          :width: 200px

          Original drawing.

     - .. figure:: /images/grease-pencil_modes_draw_tools_erase_stroke-02.png
          :width: 200px

          The eraser delete one stroke at a time.

     - .. figure:: /images/grease-pencil_modes_draw_tools_erase_stroke-03.png
          :width: 200px

          Final result.
