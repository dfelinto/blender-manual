
***********
Erase Brush
***********

Erase brushes are the special types of brushes that uses Grease Pencil for *Erase* tools.
The brush can be changed in the Tool Settings.

Soft and hard eraser brushes are settings variations of the same *Erase Brush*.
You can create many brushes, each with unique settings to get different effects while erasing.

The *Erase Brush* has also other two special eraser types: point and stroke.


Tool Settings
=============

Brushes
-------

.. figure:: /images/grease-pencil_modes_draw_tool-settings_brushes_erase-brush_data-block.png
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

   To save a custom brush in a blend-user, enable *Fake User*.


Brush Settings
--------------

Radius
   The radius of the brush in pixels.

   :kbd:`F` allows you to change the brush size interactively by dragging the mouse/pen or
   by typing a number then confirm.

   Use Pressure (pressure sensitivity icon)
      Uses stylus pressure to control how strong the effect is.
   Occlude Eraser (overlapping squares icon)
      Erase only strokes visible and not occluded by geometry.

Mode
   Determines how the erase tool behaves.

   Dissolve
      To simulate a raster type eraser, this eraser type
      affects the strength and thickness of the strokes before actually delete a point.

      Strength
         Control how much will affect the eraser has on the stroke transparency (alpha).

         You can change the brush strength interactively by pressing :kbd:`Shift-F`
         in the 3D Viewport and then moving the mouse/pen and then :kbd:`LMB`.
         You can also enter the size numerically.

         Use Pressure (pressure sensitivity icon)
            Uses stylus pressure to control how strong the effect is.

      Affect Stroke Strength
         The amount of deletion of the stroke strength (alpha) while erasing.
      Affect Stroke Thickness
         The amount of deletion of the stroke thickness while erasing.

   Point
      Delete one point at a time.
   Stroke
      Delete an entire stroke.

Display Cursor
   Shows the brush shape in the viewport.
