.. _tool-grease-pencil-draw-fill:

*********
Fill Tool
*********

.. reference::

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

.. _bpy.types.BrushGpencilSettings.fill_factor:

Precision
   Multiplier for fill boundary accuracy.
   Higher values are more accurate but slower.

.. _bpy.types.BrushGpencilSettings.fill_leak:

Leak Size
   Size in pixel to consider the leak as closed.

Thickness
   The thickness radius of the boundary stroke in pixels.


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
      Toggle show auxiliary lines to see the fill boundary.

.. _bpy.types.BrushGpencilSettings.fill_layer_mode:

Layers
   Determines which :doc:`Layers </grease_pencil/properties/layers>` are used for boundary strokes.

   :Visible: Calculates boundaries based on all visible layers.
   :Active:  Calculates boundaries based on the active later.
   :Layer Above: Calculates boundaries based on the layer above the active layer.
   :Layer Below: Calculates boundaries based on the layer below the active layer.
   :All Above: Calculates boundaries based on all layers above the active layer.
   :All Below: Calculates boundaries based on all layers below the active layer.

Stroke Extension
   Extends the actual stroke to close gaps in the fill area.
   The extended strokes are temporarily and will be not be rendered.
   The value control the extension length to use. Zero value means disabled.

   Show Extend Lines (grid icon)
      Toggle show extended lines helper.

.. _bpy.types.BrushGpencilSettings.fill_simplify_level:

Simplify
   Number of simplify steps to apply to the boundary line.
   Higher values reduce the accuracy of the final filled area.

.. _bpy.types.BrushGpencilSettings.show_fill:
.. _bpy.types.BrushGpencilSettings.fill_threshold:

Ignore Transparent
   When enabled, strokes with transparency does not take into account on fill boundary calculations.

   The value slider controls the threshold to consider a material transparent.

Limit to Viewport
   When enabled, fill only visible areas in the viewport.


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

   * - .. figure:: /images/grease-pencil_modes_draw_tools_fill_example-01.png
          :width: 200px

          Original Drawing.

     - .. figure:: /images/grease-pencil_modes_draw_tools_fill_example-02.png
          :width: 200px

          Use the fill tool to leak materials on closed areas.

     - .. figure:: /images/grease-pencil_modes_draw_tools_fill_example-03.png
          :width: 200px

          Final filled drawing.


Boundary Strokes
----------------

If you have a large gap in an area that you want fill,
you can use boundary strokes, a temporary auxiliary lines for closing open shapes.
To create a boundary stroke use :kbd:`Alt-LMB` and draw a line to close the desired area.

.. list-table::

   * - .. figure:: /images/grease-pencil_modes_draw_tools_fill_boundary-strokes-01.png
          :width: 200px

          Original drawing.

     - .. figure:: /images/grease-pencil_modes_draw_tools_fill_boundary-strokes-02.png
          :width: 200px

          Add boundary strokes to close open areas (red lines).

     - .. figure:: /images/grease-pencil_modes_draw_tools_fill_boundary-strokes-03.png
          :width: 200px

          Use the Fill tool to leak material on the new closed area.

When you are satisfied with the fill result you can delete the boundary strokes using
the *Clean Up* tool in the :doc:`Grease Pencil Menu </grease_pencil/modes/edit/grease_pencil_menu>` in Edit Mode.


Stroke Extension
----------------

A more automatic way to close gaps in an area that you want fill is using temporarily extended lines.
*Stroke Extension* are temporary extended auxiliary lines for closing open shapes.
Set a value more than zero to use the extended lines, click over the area you want to be filled
and change the length of the strokes using :kbd:`PageUp` :kbd:`PageDown` or :kbd:`Wheel`.
When you are satisfied with the length and you are sure the temporarily strokes cross each other,
click again to fill the area.

.. list-table::

   * - .. figure:: /images/grease-pencil_modes_draw_tools_fill_extended-strokes-01.png
          :width: 200px

          Original Drawing.

     - .. figure:: /images/grease-pencil_modes_draw_tools_fill_extended-strokes-02.png
          :width: 200px

          Use Strokes extension to close open areas (cyan lines).

     - .. figure:: /images/grease-pencil_modes_draw_tools_fill_extended-strokes-03.png
          :width: 200px

          Use Fill Tool to leak material on the new closed area.


Switch to Draw Tool
-------------------

Use :kbd:`Ctrl-LMB` to change temporary to the active draw tool.
For example to manually cover small areas difficult to reach for the Fill tool.
See :doc:`Draw Tool </grease_pencil/modes/draw/tools/draw>` for more information.
