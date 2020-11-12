
**************
Brush Settings
**************

.. figure:: /images/sculpt-paint_weight-paint_tool-settings_brush-settings_brush-panel.png
   :align: right
   :width: 200

   Brush panel.

Painting needs paint brushes and Blender provides a Brush Panel within the Toolbar
when it operates in *Weight Paint Mode*.

Weight :kbd:`W`
   The weight (color) to be used by the brush.
   However, the weight value is applied to the vertex group
   in different ways depending on the selected Brush Blending mode (see below).

   Use :kbd:`Ctrl-LMB` to sample the weight value of clicked vertex.
   :kbd:`Shift-LMB` lets you select the group from which to sample from.

Radius
   This option controls the radius of the brush, measured in pixels.
   :kbd:`F` allows you to change the brush size interactively by
   dragging the mouse and then :kbd:`LMB` (the texture of the brush should be visible inside the circle).
   Typing a number then enter while using :kbd:`F` allows you to enter the size numerically.

   Size Pressure
      Brush size can be affected by enabling the pressure sensitivity icon,
      if you are using a :ref:`Graphics Tablet <hardware-tablet>`.
   Use Unified Radius
      Use the same brush *Radius* across all brushes.

Strength
   How powerful the brush is when applied.

   Size Pressure
      Brush *Strength* can be affected by enabling the pressure sensitivity icon,
      if you are using a :ref:`Graphics Tablet <hardware-tablet>`.
   Use Unified Radius
      Use the same brush *Strength* across all brushes.


Advanced
========

Accumulate
   This will allow a stroke to accumulate on itself, just like an airbrush would do.
Front Faces Only
   Only paint on the front side of faces.

.. toctree::
   :hidden:

   Stroke </sculpt_paint/brush/stroke.rst>
   Falloff </sculpt_paint/brush/falloff.rst>
   Cursor </sculpt_paint/brush/cursor.rst>


Stroke
======

See the global brush settings for :doc:`Stroke </sculpt_paint/brush/stroke>` settings.


Falloff
=======

See the global brush settings for :doc:`Falloff </sculpt_paint/brush/falloff>` settings.


Cursor
======

See the global brush settings for :doc:`Cursor </sculpt_paint/brush/cursor>` settings.
