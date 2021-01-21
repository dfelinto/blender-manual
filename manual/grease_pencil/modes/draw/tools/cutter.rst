.. _tool-grease-pencil-draw-cutter:

***********
Cutter Tool
***********

.. admonition:: Reference
   :class: refbox

   :Mode:      Draw Mode
   :Tool:      :menuselection:`Toolbar --> Cutter`

The Cutter tool delete points in between intersecting strokes.


Tool Settings
=============

Flat Caps
   Mark newly created :ref:`End Caps <bpy.ops.gpencil.stroke_caps_set>` as *Flat*.


Usage
=====

Draw a dotted line around the strokes you want to be cut.
After releasing the mouse button all the points on the selected strokes
will be deleted until another intersecting stroke is found.

.. list-table::

   * - .. figure:: /images/grease-pencil_modes_draw_tool-settings_cutter_example-01.png
          :width: 200px

          Original drawing.

     - .. figure:: /images/grease-pencil_modes_draw_tool-settings_cutter_example-02.png
          :width: 200px

          Lasso Selecting the strokes to be cut.

     - .. figure:: /images/grease-pencil_modes_draw_tool-settings_cutter_example-03.png
          :width: 200px

          Final result.
