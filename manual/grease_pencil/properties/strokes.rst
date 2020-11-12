
*******
Strokes
*******

.. figure:: /images/grease-pencil_properties_strokes_panel.png
   :align: right

   Strokes panel.

General settings for Grease Pencil strokes.


Stroke Depth Order
==================

2D Layers
   The Strokes drawing order respect the order of the 2D layers list (top to bottom)
   and ignores the real position of the strokes in 3D space.
   See :doc:`2D Layers </grease_pencil/properties/layers>` for more information.

3D Location
   The strokes drawing order is based on the stroke location in 3D space.

.. list-table::

   * - .. figure:: /images/grease-pencil_properties_strokes_depth-order-2d.png
          :width: 320px

          Blue, Green and Red strokes in three different layers using 2D Layers depth order.

     - .. figure:: /images/grease-pencil_properties_strokes_depth-order-3d.png
          :width: 320px

          Blue, Green and Red strokes in three different layers using 3D Location depth order.


Stroke Thickness
================

World Space
   The thickness is relative to world space.
   Stroke thickness change with the screen zoom factor.

Screen Space
   The thickness is relative to screen space.
   Stroke thickness remains the same regardless of the screen zoom factor.

Thickness Scale
   Sets a thickness scale factor for all strokes.
