.. _bpy.types.GPencilSculptGuide:

******
Guides
******

.. admonition:: Reference
   :class: refbox

   :Mode:      Draw Mode
   :Header:    :menuselection:`Guides`

Guides are drawing aids that make it easier to create different types of strokes.
The Guides can be activated with the button next to the selector (grid icon).


.. _bpy.types.GPencilSculptGuide.type:

Guide Types
===========

.. figure:: /images/grease-pencil_modes_draw_guides_selector.png
   :align: right

   Guide selector activated in the 3D Viewport header.

Circular
   Constrains the drawing of new strokes to form rings from the selected reference point.

Radial
   Constrains the drawing of new strokes to form rays from the selected reference point.

Parallel
   Constrains the drawing of new strokes to form parallel lines.

   Angle
      Angle direction of the parallel lines.

Grid
   Constrains the drawing of new strokes to form parallel horizontal or vertical lines.

Isometric
   Constrains the drawing of new strokes to vertical or isometric lines.

   Angle
      Angle direction of the isometric lines.


.. _bpy.types.GPencilSculptGuide.use_snapping:
.. _bpy.types.GPencilSculptGuide.reference_point:

Common Options
--------------

Use Snapping
   When enabled, snap the drawn strokes to an angle or spacing.

   Spacing
      Guide spacing.

Reference Point
   Determines the origin point to use for the creation of the lines.
   Applies only for *Circular* and *Radial* guides.

   Cursor
      Use the cursor as a reference point.

   Custom
      Use a custom location as a reference point.

      Custom Location
         X, Y Z

   Object
      Use an object as a reference point.

      Object
         An :ref:`Data ID menu <ui-data-id>` to select the object (usually an empty),
         which location will be used as a reference point.


Examples
========

.. list-table:: Examples of strokes using different types of Guides.

   * - .. figure:: /images/grease-pencil_modes_draw_guides_circular.png
          :width: 200px

          Circular Guides.

     - .. figure:: /images/grease-pencil_modes_draw_guides_radial.png
          :width: 200px

          Radial Guides.

     - .. figure:: /images/grease-pencil_modes_draw_guides_parallel.png
          :width: 200px

          Parallel Guides (30° Angle).

     - .. figure:: /images/grease-pencil_modes_draw_guides_grid.png
          :width: 200px

          Grid Guides.
