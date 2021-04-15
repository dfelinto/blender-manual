
*****
Layer
*****

.. admonition:: Reference
   :class: refbox

   :Mode:      Sculpt Mode
   :Tool:      :menuselection:`Toolbar --> Layer`
   :Shortcut:  :kbd:`L`

This brush is similar to *Draw*, except that the height of the displacement layer is capped.
This creates the appearance of a solid layer being drawn.
This brush does not draw on top of itself; a brush stroke intersects itself.
Releasing the mouse button and starting a new stroke
will reset the depth and paint on top of the previous stroke.


Brush Settings
==============

.. _bpy.types.Brush.height:

Height
   The amount of displacement for each layer.

.. _bpy.types.Brush.use_persistent:

Persistent
   You can keep sculpting on the same layer between strokes when this is on.

.. _bpy.ops.sculpt.set_persistent_base:

Set Persistent Base
   This button resets the base so that you can add another layer.
