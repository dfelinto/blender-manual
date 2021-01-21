.. _bpy.types.SoundSequence:

************
Sound Strips
************

As well as images and movies the VSE can also edit audio tracks.
You can add Waveform Audio format ``WAV``, ``mp3`` and other audio formats files from your drive,
or from sound encoded within a movie, and mix them using an F-curve as a volume control.

.. figure:: /images/video-editing_sequencer_strips_sound_editing.png

   Example of sound editing.


Working with Audio Tracks
=========================

A sound strip is just like any other strip in the VSE. You can select and move it,
adjust its starting offset using :kbd:`LMB` over the strip handles,
and :kbd:`K` cut it into pieces.
A useful example is cutting out the "um's" and dead voice time.

You can have as many sound strips as you wish and the result will be the mixing of all of them.
You can give each strip its own name and volume via the Sidebar region.

Overlapping strips are automatically mixed down during the rendering process.
For example, you can have the announcer on channel 5, background music on channel 6,
and Foley sound effects on channel 7.

.. seealso::

   In the :ref:`timeline-playback` menu of the Timeline you will find some options
   concerning audio playback behavior.


Animating Audio Track Properties
================================

To animate sound strips simply hit :kbd:`I` over any of its values.
Examples of animating an audio strip are to fade in/out background music or to adjust volume levels.
Layered/crossed sound strips are added together;
the lower channel does not override and cut out higher channels (unlike image and video strips).
This makes Blender an audio mixer.
By adding audio tracks and using the curves to adjust each tracks' sound level,
you have an automated dynamic multi-track audio mixer!

.. seealso::

   Sounds can be crossfaded by adding a :ref:`Sound Crossfade <bpy.ops.sequencer.crossfade_sounds>` effect.


Output
======

There are two ways to render out your audio.
You can either have it encoded with a video file or in its own audio file.
Read more on how to select a proper :ref:`audio format <render-output-video-encoding-audio>`
and how to start :doc:`rendering </render/output/index>`.


.. _bpy.ops.sequencer.sound_strip_add:

Add Sound Strip
===============

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Add --> Sound`

Relative Path
   Store the location of the image file relative to the blend-file.

Start Frame
   The :ref:`Start Frame <bpy.types.Sequence.frame_start>` to place the left handle of the strip.

Channel
   The :ref:`Channel <bpy.types.Sequence.channel>` to place the strip.

Replace Selection
   Replaces the currently selected strips with the new strip

Cache
   Cache the sound in memory, enables :ref:`Caching <bpy.types.Sound.use_memory_cache>` in the Source properties.

Mono
   Merge all the sound's channels into one channel,
   enables :ref:`Mono <bpy.types.Sound.use_mono>` in the Sound properties.
