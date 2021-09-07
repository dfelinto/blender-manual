
***********
Frame Range
***********

.. figure:: /images/render_output_properties_frame_range_panel.png

   Frame Range panel.

This panel defines how long an animation will last in terms of frames.
Frames can be multiplied by the scene's :ref:`Frame Rate <bpy.types.RenderSettings.fps>`
to get the animation duration in terms of time.
For example, a 250 frame animation at a frame rate of 30 will last 125 seconds.

.. _bpy.types.Scene.frame_start:
.. _bpy.types.Scene.frame_end:

Frame Start, End
   Set the *Start* and *End* frames for :doc:`Rendering Animations </render/output/animation>`.

.. _bpy.types.Scene.frame_step:

Step
   Controls the number of frames to advance by for each frame in the timeline.


Time Remapping
==============

Use to remap the length of an animation.

.. _bpy.types.RenderSettings.frame_map_old:

Old
   The length in frames of the original animation.

.. _bpy.types.RenderSettings.frame_map_new:

New
   The length in frames the new animation will last.
