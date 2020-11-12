.. _tool-grease-pencil-draw-polyline:

*************
Polyline Tool
*************

.. admonition:: Reference
   :class: refbox

   :Mode:      Draw Mode
   :Tool:      :menuselection:`Toolbar --> Polyline`

The Polyline tool create multiple straight lines.


Usage
=====

Selecting a Brush and Material
------------------------------

In the Tool Settings select the brush, material and color type to use with the tool.
The Line tool uses *Draw Brush* types.
See :ref:`grease-pencil-draw-common-options` for more information.


Common Brush Options
--------------------

You can configure the brush main settings exposed on the Tool Settings for convenience.
For the draw brushes configuration and settings see:
:doc:`Draw Brush </grease_pencil/modes/draw/tool_settings/brushes/draw_brush>`.

Thickness Profile
   Use a :doc:`curve widget </interface/controls/templates/curve>` to define the stroke thickness
   from the start (left) to end (right) of the stroke.

   Use Curve
      When enabled, the stroke use a curve profile to control the thickness along the line.

.. list-table:: Different thickness profile samples.

   * - .. figure:: /images/grease-pencil_modes_draw_tool-settings_polyline_thickness-profile-01.png
          :width: 200px

     - .. figure:: /images/grease-pencil_modes_draw_tool-settings_polyline_thickness-profile-02.png
          :width: 200px

     - .. figure:: /images/grease-pencil_modes_draw_tool-settings_polyline_thickness-profile-03.png
          :width: 200px


Creating Polylines
------------------

#. Click (:kbd:`LMB` or the :kbd:`Pen` tip) and drag the start point.
#. Release on the desired end point.
#. Click multiple times on different locations to create multiple connected lines.
#. Then confirm (:kbd:`Return`/:kbd:`MMB`) or cancel (:kbd:`Esc`/:kbd:`RMB`).

While dragging you can use :kbd:`Shift` to snapping the line to horizontal, vertical or 45° angle.

:kbd:`NumpadPlus` and :kbd:`NumpadMinus` or using the mouse :kbd:`Wheel`
will increase or decrease the amount of points in the final line.

.. list-table::

   * - .. figure:: /images/grease-pencil_modes_draw_tool-settings_polyline_example-01.png
          :width: 200px

          click and dragging the start point.

     - .. figure:: /images/grease-pencil_modes_draw_tool-settings_polyline_example-02.png
          :width: 200px

          Click multiple times to create multiple connected lines.

     - .. figure:: /images/grease-pencil_modes_draw_tool-settings_polyline_example-03.png
          :width: 200px

          The polyline after confirming.
