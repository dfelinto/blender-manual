.. _tool-grease-pencil-draw-draw:

*********
Draw Tool
*********

.. reference::

   :Mode:      Draw Mode
   :Tool:      :menuselection:`Toolbar --> Draw`

The Draw tool allows you to draw free-hand strokes.


Brush Settings
==============

.. figure:: /images/grease-pencil_modes_draw_tools_draw_settings.png
   :width: 275px
   :align: right

Material
   Data-block selector for the :doc:`material </grease_pencil/materials/introduction>`.

Radius
   The radius of the brush in pixels.

   :kbd:`F` allows you to change the brush size interactively by dragging the pointer or
   by typing a number then confirm.

   Use Pressure (pressure sensitivity icon)
      Uses stylus pressure to control how strong the effect is.
      The gradient of the pressure can be customized using
      the :doc:`curve widget </interface/controls/templates/curve>`.

Strength
   Control the stroke transparency (alpha).
   From fully transparent (0.0) to fully opaque (1.0).

   You can change the brush strength interactively by pressing :kbd:`Shift-F`
   in the 3D Viewport and then moving the pointer and then :kbd:`LMB`.
   You can also enter the size numerically.

   Use Pressure (pressure sensitivity icon)
      Uses stylus pressure to control how strong the effect is.
      The gradient of the pressure can be customized using
      the :doc:`curve widget </interface/controls/templates/curve>`.


Advanced
--------

Input Samples
   Controls how often the input device is read to generate points on the stroke.
   Higher values give a higher precision (more points) but produce an irregular stroke,
   while lower values give a lower precision (fewer points) but produce a soften stroke.
   (0 disabled extra input device samples.)

   You have to set up this value according to your input device to obtain
   the right balance between accuracy and softness for your strokes.
   See :doc:`Input Device </getting_started/configuration/hardware>` for more information.

Active Smooth
   The number of smoothing iterations to apply to the stroke while drawing.

Angle
   Direction of the input device that gives the maximum thickness to the stroke (0° for horizontal).

   Factor
      Amount of thickness reduction when the stroke is perpendicular to the *Angle* value.

Hardness
   Amount of transparency (alpha) to apply from the border of the point to the center.
   Works only when the brush is using stroke materials of *Dot* or *Box* style.

   Aspect Ratio
      Controls the width and height of the alpha gradient.

      X, Y


Stroke
------

Post-Processing
^^^^^^^^^^^^^^^

Post-processing methods that are executed on the strokes
when you finished drawing, right after releasing the :kbd:`LMB` or :kbd:`Pen` tip.
You can toggle the use of post-processing using the checkbox in the section panel header.

Smooth
   Strength of smoothing process on the points location along the stroke.

   Iterations
      The number of smoothing iterations to apply to the stroke.

Subdivision Steps
   Number of subdivisions to apply to newly created strokes.

Simplify
   Reduces final points numbers in the stroke with an adaptive algorithm.

Trim Strokes End
   Automatically trim intersection strokes ends.


.. _bpy.types.BrushGpencilSettings.use_settings_random:
.. _bpy.types.BrushGpencilSettings.random:
.. _bpy.types.BrushGpencilSettings.uv_random:
.. _bpy.types.BrushGpencilSettings.pen_jitter:
.. _bpy.types.BrushGpencilSettings.use_jitter_pressure:

Randomize
^^^^^^^^^

Adds randomness to the position of the points along the stroke.
You can toggle the use of Randomize using the checkbox in the section panel header.

Radius
   The amount of randomness to apply using the pressure of the input device.

Strength
   The amount of randomness to apply to the stroke strength value (alpha).

UV
   The amount of randomness to apply to the UV rotation.

Hue, Saturation, Value
   Randomizes the hue, saturation, and value of the stroke's :ref:`Color <grease-pencil-draw-color>`.

Jitter
   The amount of jittering to add to the stroke.


.. rubric:: Common Options

Stroke Random (stroke icon)
   Use randomness only at stroke level.

Use Pressure (pressure sensitivity icon)
   Uses the stylus pressure to control how strong the effect is.
   The gradient of the pressure can be customized using
   the :doc:`curve widget </interface/controls/templates/curve>`.


.. _grease-pencil-draw-brushes-stabilizer:
.. _bpy.types.BrushGpencilSettings.use_settings_stabilizer:
.. _bpy.types.Brush.smooth_stroke:

Stabilize Stroke
^^^^^^^^^^^^^^^^

*Stabilize Stroke* helps to reduce jitter of the strokes while drawing by
delaying and correcting the location of points.
You can toggle the use of *Stabilize Stroke* using the checkbox in the section panel header.

Radius
   Minimum distance from the last point before the stroke continues.
Factor
   A smooth factor, where higher values result in smoother strokes but the drawing sensation
   feels like as if you were pulling the stroke.


Cursor
------

The cursor can be disabled by toggling the checkbox in the *Cursor* header.

Show Fill Color while Drawing
   Shows the brush linked material color in the viewport.


Usage
=====

Selecting a Brush and Material
------------------------------

In the Tool Settings select the brush, material and color type to use with the tool.
The Draw tool uses *Draw Brush* types.
See :ref:`grease-pencil-draw-common-options` for more information.


Free-hand Drawing
-----------------

Click and hold :kbd:`LMB` or use the pen tip to make free-hand drawing on the viewport.

.. list-table:: Drawing free-hand strokes.

   * - .. figure:: /images/grease-pencil_modes_draw_tools_draw_free-hand-01.png
          :width: 200px

     - .. figure:: /images/grease-pencil_modes_draw_tools_draw_free-hand-02.png
          :width: 200px

     - .. figure:: /images/grease-pencil_modes_draw_tools_draw_free-hand-03.png
          :width: 200px


Stabilize Stroke
----------------

:kbd:`Shift-LMB` toggle the use of :ref:`Stabilize Stroke <grease-pencil-draw-brushes-stabilizer>`
on the brush to have more control while drawing and get smoother lines.

.. list-table:: Drawing strokes using *Stabilize Stroke*.

   * - .. figure:: /images/grease-pencil_modes_draw_tools_draw_stabilizer-01.png

     - .. figure:: /images/grease-pencil_modes_draw_tools_draw_stabilizer-02.png

     - .. figure:: /images/grease-pencil_modes_draw_tools_draw_stabilizer-03.png


Straight Lines
--------------

:kbd:`Alt-LMB` Constrains the drawing of the strokes to horizontal or vertical straight lines.


Switching to the Erase Tool
---------------------------

:kbd:`Ctrl-LMB` changes temporally to the active Erase tool.
See :doc:`Erase Tool </grease_pencil/modes/draw/tools/erase>` for more information.

You can also use :kbd:`B` to delete all the points in the selected drawing area.
