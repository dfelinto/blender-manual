
**********
Fill Brush
**********

Fill brushes are the special type of brushes that uses Grease Pencil for the *Fill* tools.
The brush can be changed in the Tool Settings.

The different fill brushes are settings variations of the same *Fill Brush*.
You can create many brushes, each with unique settings to get different result when filling areas.


Tool Settings
=============

Brushes
-------

.. figure:: /images/grease-pencil_modes_draw_tool-settings_brushes_fill-brush_data-block.png
   :align: right

   Brush data-block panel.

Brush
   The :ref:`ui-data-block` to select a preset brush type or a custom brush.

   Add Brush
      When you add a brush, the new brush is a clone of the current one.

   Brush Specials
      Reset Brush
         Reset the current brush to its default settings.

      Reset All Brushes
         Reset all brushes to their default settings.

      Custom Icon
         Allows definition of a custom brush icon.

         Image Path
            Defines the path to the image to use as custom icon.

.. note::

   In order to save a custom brush in a blend-user, enable *Fake User*.


Brush Settings
--------------

.. _bpy.types.BrushGpencilSettings.fill_direction:

Direction :kbd:`Ctrl`
   The portion of area to fill.

   Normal
      Fills the area inside the shape under the cursor.
   Inverted
      Fills the area outside the shape under the cursor.

.. _bpy.types.BrushGpencilSettings.fill_leak:

Leak Size
   Size in pixel to consider the leak as closed.

Thickness
   The thickness radius of the boundary stroke in pixels.

.. _bpy.types.BrushGpencilSettings.fill_simplify_level:

Simplify
   Number of simplify steps to apply to the boundary line.
   Higher values reduce the accuracy of the final filled area.


Advanced
^^^^^^^^

.. _bpy.types.BrushGpencilSettings.fill_draw_mode:

Boundary
   Sets the type of fill boundary limits calculation to perform.

   All
      Use the thickness of the strokes and the editing lines together.
   Stroke
      Use only the thickness of the strokes (ignore edit lines).
   Line
      Use only the edit lines (ignore strokes).
   Show Lines (grid icon)
      Toggle show help lines to see the fill boundary.

.. _bpy.types.BrushGpencilSettings.fill_factor:

Resolution
   Multiplier for fill resolution.
   Higher values gives better fill boundary accuracy but slower time for calculations.

.. _bpy.types.BrushGpencilSettings.show_fill:
.. _bpy.types.BrushGpencilSettings.fill_threshold:

Ignore Transparent
   When enabled, strokes with transparency does not take into account on fill boundary calculations.

   The value slider controls the threshold to consider a material transparent.


Cursor
------

The cursor can be disabled by toggling the checkbox in the *Cursor* header.

Cursor Color
   Set the color of the brush ring.
