.. _bpy.ops.sequencer.crossfade_sounds:

***************
Sound Crossfade
***************

The *Sound Crossfade* transition works by animating the *Volume*
of two overlapping sound strips to evenly fade between them.
Because this simply animates a value it does not create a strip like other effects or transitions.


.. _bpy.types.CrossSequence:

*****
Cross
*****

The *Cross* transition fades from one strip to another, also known as a crossfade.
Strips can be overlapping or have a gap between them,
however, when strips contain a gap the last and first frame of each strip
is extend which can cause a pause if any of the strips are a sequence.


Options
=======

Default Fade
   Automatically calculates a linear fade over the length of the strip.

   Effect Fader
      Allows you to manually :doc:`keyframe </animation/keyframes/index>` a custom fade.
      This can be used with different :ref:`easings <editors-graph-fcurves-settings-easing>`
      to fine-tune the fade in/out.


Example
=======

.. figure:: /images/video-editing_sequencer_strips_transitions_cross_example.png

   Cross Effect.


.. _bpy.types.GammaCrossSequence:

***********
Gamma Cross
***********

The *Gamma Cross* transition is similar to the `Cross`_ transition,
however, the *Gamma Cross* transition uses color correction while transitioning between the two strips,
resulting in a smoother transition that is easier on the eyes.


Options
=======

Default Fade
   Automatically calculates a linear fade over the length of the strip.

   Effect Fader
      Allows you to manually :doc:`keyframe </animation/keyframes/index>` a custom fade.
      This can be used with different :ref:`easings <editors-graph-fcurves-settings-easing>`
      to fine-tune the fade in/out.
