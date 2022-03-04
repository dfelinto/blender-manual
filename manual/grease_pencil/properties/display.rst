
****************
Viewport Display
****************

.. figure:: /images/grease-pencil_properties_display_panel.png
   :align: right

   Viewport Display panel.

Display settings for Edit Lines in *Edit Mode* and *Sculpt Mode*.

.. _bpy.types.GreasePencil.edit_line_color:

Edit Line Color
   Sets the color of the Edit Lines.


.. _bpy.types.GreasePencilGrid:

Canvas
======

In 3D space sometimes is difficult to assess on which plane are you drawing.
The Canvas is a display overlay helper that shows a grid at the current *Drawing Plane*.
You can enable the Canvas visualization in the :ref:`Viewport Overlays <3dview-overlay-grease-pencil>`.

See :doc:`Drawing Plane </grease_pencil/modes/draw/drawing_planes>` for more information.

.. _bpy.types.GreasePencilGrid.color:

Color
   Color of the Canvas grid lines.

.. _bpy.types.GreasePencilGrid.scale:

Scale X/Y
   Defines the X and Y scale of the Canvas.

.. _bpy.types.GreasePencilGrid.offset:

Offset X/Y
   Sets the Canvas position offset from the object's origin.

.. _bpy.types.GreasePencilGrid.lines:

Subdivisions
   Specifies the number of subdivisions to use for the grid.

.. figure:: /images/grease-pencil_properties_display_canvas.png
   :align: right

   Canvas example on the XZ drawing plane using a green color grid.
