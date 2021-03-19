.. _tool-grease-pencil-draw-circle:

***********
Circle Tool
***********

.. admonition:: Reference
   :class: refbox

   :Mode:      Draw Mode
   :Tool:      :menuselection:`Toolbar --> Circle`

The Circle tool create oval shapes.


Tool Settings
=============

You can configure the brush main settings exposed on the Tool Settings for convenience.
For the draw brushes configuration and settings see:
:doc:`Draw Brush </grease_pencil/modes/draw/tools/draw>`.

Subdivisions
   The number of stroke points between each stroke edge.

Thickness Profile
   Use a :doc:`curve widget </interface/controls/templates/curve>` to define the stroke thickness
   from the start (left) to end (right) of the stroke.

   Use Curve
      When enabled, the stroke use a curve profile to control the thickness along the line.


Usage
=====

Selecting a Brush and Material
------------------------------

In the Tool Settings select the brush, material and color type to use with the tool.
The Circle tool uses *Draw Brush* types.
See :ref:`grease-pencil-draw-common-options` for more information.


Creating Circles
----------------

#. Click (:kbd:`LMB` or the :kbd:`Pen` tip) and drag the start point.
#. Release on the desired end point.
#. After releasing you can move the start and end point by clicking and dragging on the yellow manipulators.
#. Then confirm (:kbd:`Return`/:kbd:`MMB`) or cancel (:kbd:`Esc`/:kbd:`RMB`).

While dragging you can use :kbd:`Shift` to make a perfect circle
or use :kbd:`Alt` to create the circle from a center point.

:kbd:`NumpadPlus` and :kbd:`NumpadMinus` or using the mouse :kbd:`Wheel`
will increase or decrease the amount of points in the final circle.

.. list-table::

   * - .. figure:: /images/grease-pencil_modes_draw_tools_circle_example-01.png
          :width: 200px

          Click and dragging the start point.

     - .. figure:: /images/grease-pencil_modes_draw_tools_circle_example-02.png
          :width: 200px

          Moving start and end points with manipulators.

     - .. figure:: /images/grease-pencil_modes_draw_tools_circle_example-03.png
          :width: 200px

          The circle after confirming.
