.. _tool-grease-pencil-draw-fill:

*********
Fill Tool
*********

.. admonition:: Reference
   :class: refbox

   :Mode:      Draw Mode
   :Tool:      :menuselection:`Toolbar --> Fill`

The Fill tool is used to automatically fill closed strokes areas.


Brush Settings
==============

You can also configure the brush main settings exposed on the Tool Settings for convenience.

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
--------

.. _bpy.types.BrushGpencilSettings.fill_draw_mode:

Boundary
   Sets the type of fill boundary limits calculation to perform.

   :All:    Use the thickness of the strokes and the editing lines together.
   :Stroke: Use only the thickness of the strokes (ignore edit lines).
   :Line:   Use only the edit lines (ignore strokes).

   .. _bpy.types.BrushGpencilSettings.show_fill_boundary:

   Show Lines (grid icon)
      Toggle show help lines to see the fill boundary.

.. _bpy.types.BrushGpencilSettings.fill_layer_mode:

Layers
   Determines which :doc:`Layers </grease_pencil/properties/layers>` are used for boundary strokes.

   :Visible: Calculates boundaries based on all visible layers.
   :Active:  Calculates boundaries based on the active later.
   :Layer Above: Calculates boundaries based on the layer above the active layer.
   :Layer Below: Calculates boundaries based on the layer below the active layer.
   :All Above: Calculates boundaries based on all layers above the active layer.
   :All Below: Calculates boundaries based on all layers below the active layer.

.. _bpy.types.BrushGpencilSettings.fill_factor:

Precision
   Multiplier for fill boundary accuracy.
   Higher values are more accurate but slower.

.. _bpy.types.BrushGpencilSettings.show_fill:
.. _bpy.types.BrushGpencilSettings.fill_threshold:

Ignore Transparent
   When enabled, strokes with transparency does not take into account on fill boundary calculations.

   The value slider controls the threshold to consider a material transparent.


Usage
=====

Selecting a Brush and Material
------------------------------

In the Tool Settings select the brush, material and color type to use with the tool.
The Fill tool uses *Fill Brush* types.
See :ref:`grease-pencil-draw-common-options` for more information.


Filling Areas
-------------

Click :kbd:`LMB` in a closed stroke area. The tool will automatically calculate
the boundary and create a new closed stroke filled with the material selected.

.. list-table::

   * - .. figure:: /images/grease-pencil_modes_draw_tool-settings_fill_example-01.png
          :width: 200px

          Original Drawing.

     - .. figure:: /images/grease-pencil_modes_draw_tool-settings_fill_example-02.png
          :width: 200px

          Use the fill tool to leak materials on closed areas.

     - .. figure:: /images/grease-pencil_modes_draw_tool-settings_fill_example-03.png
          :width: 200px

          Final filled drawing.


Boundary Strokes
----------------

If you have a large gap in an area that you want fill,
you can use *Boundary Strokes*, a temporary help lines for closing open shapes.
To create a Boundary Strokes use :kbd:`Alt-LMB` and draw a line to close the desired area.

.. list-table::

   * - .. figure:: /images/grease-pencil_modes_draw_tool-settings_fill_boundary-strokes-01.png
          :width: 200px

          Original Drawing.

     - .. figure:: /images/grease-pencil_modes_draw_tool-settings_fill_boundary-strokes-02.png
          :width: 200px

          Add Boundary Strokes to close open areas (red lines).

     - .. figure:: /images/grease-pencil_modes_draw_tool-settings_fill_boundary-strokes-03.png
          :width: 200px

          Use Fill Tool to leak material on the new closed area.

When you are satisfied with the fill result you can delete the Boundary strokes using
the *Clean Up* tool in the :doc:`Grease Pencil Menu </grease_pencil/modes/edit/grease_pencil_menu>` in Edit Mode.


Switch to Draw Tool
-------------------

Use :kbd:`Ctrl-LMB` to change temporary to the active draw tool.
For example to manually cover small areas difficult to reach for the Fill tool.
See :doc:`Draw Tool </grease_pencil/modes/draw/tools/draw>` for more information.
