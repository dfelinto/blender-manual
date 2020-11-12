
**************
Brush Settings
**************

.. figure:: /images/sculpt-paint_vertex-paint_tool-settings_brush-settings_tab.png
   :align: right

   Vertex Painting options.

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


Color Picker
============

The color of the brush. See :ref:`ui-color-picker`.

Press :kbd:`S` on any part of the image to sample that color and set it as the brush color.
Hold :kbd:`Ctrl` while painting to temporally paint with the secondary color.

Flip (cycle icon) :kbd:`X`
   Swaps the primary and secondary colors.

.. note::

   Note that Vertex Paint works in sRGB :term:`space <Color Space>`, and
   the RGB representation of the same colors will be different between the paint
   tools and the materials that are in linear space.


Advanced
========

Affect Alpha
   When this is disabled, it locks (prevents changes) the alpha channel while painting.
Accumulate
   This will allow a stroke to accumulate on itself, just like an airbrush would do.
Front Faces Only
   Only paint on the front side of faces.

.. toctree::
   :hidden:

   Texture </sculpt_paint/brush/texture.rst>
   Stroke </sculpt_paint/brush/stroke.rst>
   Falloff </sculpt_paint/brush/falloff.rst>
   Cursor </sculpt_paint/brush/cursor.rst>


Texture
=======

See the global brush settings for :doc:`Texture </sculpt_paint/brush/texture>` settings.


Stroke
======

See the global brush settings for :doc:`Stroke </sculpt_paint/brush/stroke>` settings.


Falloff
=======

See the global brush settings for :doc:`Falloff </sculpt_paint/brush/falloff>` settings.


Cursor
======

See the global brush settings for :doc:`Cursor </sculpt_paint/brush/cursor>` settings.
