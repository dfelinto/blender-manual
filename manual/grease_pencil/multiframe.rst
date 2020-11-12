.. _bpy.types.GreasePencil.use_multiedit:
.. _bpy.types.GPencilSculptSettings.use_multiframe_falloff:

**********
Multiframe
**********

Multiframe allows you to edit, sculpt, or weight painting on several frames at the same time.
Extremely useful to avoid repeating a task one frame at a time when animating.

.. figure:: /images/grease-pencil_multiframe_panel.png

   Multiframe panel.


Usage
=====

#. Select the desired keyframes to edit or sculpt at the same time.
#. Activate the Multiframe tool in the 3D Viewport's header with the toggle button (faded lines icon).
#. Once activated you can:

   - Select the points in all the selected keyframes and make your editions.
   - Start sculpting. The sculpt brushes will affects all the strokes in the selected keyframes.
   - Start weight painting. The weight paint brush will affect all the strokes in the selected keyframes.

Use Falloff
   When enabled, the effects on the strokes start to falloff from the current frame
   as defined by a :doc:`curve widget </interface/controls/templates/curve>`.
