.. _tool-grease-pencil-draw-arc:

********
Arc Tool
********

.. admonition:: Reference
   :class: refbox

   :Mode:      Draw Mode
   :Tool:      :menuselection:`Toolbar --> Arc`

The Arc tool create simple arcs.


Usage
=====

Selecting a Brush and Material
------------------------------

In the Tool Settings select the brush, material and color type to use with the tool.
The Arc tool uses *Draw Brush* types.
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
      When enabled, the stroke use a curve profile to control the thickness along the arc.

.. list-table:: Different thickness profile samples.

   * - .. figure:: /images/grease-pencil_modes_draw_tool-settings_arc_thickness-profile-01.png
          :width: 200px

     - .. figure:: /images/grease-pencil_modes_draw_tool-settings_arc_thickness-profile-02.png
          :width: 200px

     - .. figure:: /images/grease-pencil_modes_draw_tool-settings_arc_thickness-profile-03.png
          :width: 200px


Creating Arcs
-------------

#. Click (:kbd:`LMB` or the :kbd:`Pen` tip) and drag the start point.
#. Release on the desired end point.
#. After releasing you can tweak the arc using a single cyan manipulator (hand icon).
#. Then confirm (:kbd:`Return`/:kbd:`MMB`) or cancel (:kbd:`Esc`/:kbd:`RMB`).

While dragging you can use :kbd:`Shift` to make a perfect arc,
use :kbd:`Alt` to create the arc from a center point or :kbd:`M` to flip.

:kbd:`NumpadPlus` and :kbd:`NumpadMinus` or using the mouse :kbd:`Wheel`
will increase or decrease the amount of points in the final arc.

.. list-table::

   * - .. figure:: /images/grease-pencil_modes_draw_tool-settings_arc_example-01.png
          :width: 200px

          click and dragging the start point.

     - .. figure:: /images/grease-pencil_modes_draw_tool-settings_arc_example-02.png
          :width: 200px

          Tweaking arc with the manipulator.

     - .. figure:: /images/grease-pencil_modes_draw_tool-settings_arc_example-03.png
          :width: 200px

          The arc after confirming.


Extruding
---------

Before confirming you can use :kbd:`E` to extrude the end point of the arc
to generate multiple connected arcs.

.. list-table::

   * - .. figure:: /images/grease-pencil_modes_draw_tool-settings_arc_extrude-01.png
          :width: 200px

          End point extruding.

     - .. figure:: /images/grease-pencil_modes_draw_tool-settings_arc_extrude-02.png
          :width: 200px

          Tweaking the last arc with the manipulator.

     - .. figure:: /images/grease-pencil_modes_draw_tool-settings_arc_extrude-03.png
          :width: 200px

          The connected arcs after confirming.
