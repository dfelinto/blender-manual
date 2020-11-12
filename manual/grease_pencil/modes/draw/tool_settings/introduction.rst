
************
Introduction
************

.. _grease-pencil-draw-common-options:

Common Options
==============

In the Tool Settings you can select the brush and material to use with the tool.

Brush
   The :ref:`ui-data-block` to select a preset brush type or a custom brush.
   See :ref:`Brush <grease-pencil-draw-brushes>` options.

Material
   Data-block selector for the :doc:`material </grease_pencil/materials/introduction>`.
   Except for the *Erase* tool of course.

   Pin Material (pin icon)
      Pin the material to the brush.

      The final appearance of the strokes is a combination of the brush and material used,
      binding the material to the brush gives more control and avoids a lack of coordination between the two.


.. _grease-pencil-draw-color:

Color
-----

Controls the source of the stroke color.
The mode can be pinned to the brush by enabling the Pin icon in the Tool Settings header.


Material
^^^^^^^^

Use the stroke/fill base color material.


Vertex Color
^^^^^^^^^^^^

Use Vertex color.

Color Picker
   The color of the brush. See :ref:`ui-color-picker`.

Color Palette
   Active Color Palette. See :ref:`ui-color-palette`.

Mode
   Stroke
      Only paint over strokes.

   Fill
      Only paint over fill areas.

   Stroke and Fill
      Paint over strokes and fill areas.

Mix Factor
   Mixing factor between the selected color and the base material color.
