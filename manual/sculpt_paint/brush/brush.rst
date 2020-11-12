.. _bpy.types.Brush:
.. _bpy.ops.brush:
.. _bpy.types.Brush.use_custom_icon:
.. _bpy.types.Brush.icon_filepath:
.. _bpy.types.UnifiedPaintSettings:

*******
Brushes
*******

.. admonition:: Reference
   :class: refbox

   :Mode:      Sculpt Mode
   :Panel:     :menuselection:`Sidebar --> Tools --> Brushes`

For painting/sculpting modes each brush type is exposed as a tool,
the brush can be changed from the tool setting.

.. figure:: /images/sculpt-paint_brush_brush_data-block-menu.png
   :align: right

   Brush data-block menu.

Brushes
   The :ref:`ui-data-block` to select a preset brush type or a custom brush.
   They are a combination of a "tool", along with stroke, texture, and options.

   Add Brush
      When you add a brush, the new brush is a clone of the current one.

   Brush Specials
      Enabled Modes
         Todo.
      Tool Selection
         Todo.
      Reset Brush
         Todo.

      Custom Icon
         Allows definition of a custom brush icon.

   .. note::

      In order to save a custom brush in a blend-user, enable Fake User.
