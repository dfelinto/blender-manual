.. _bpy.types.MulticamSequence:

*****************
Multicam Selector
*****************

The Multicam Selector strip is used for multi-camera editing.
Multi-camera editing is when a scene is recorded using multiple cameras from different angles
and then edited together afterwards. This process can be rather easy in the :abbr:`VSE (Video Sequence Editor)`
if you properly setup every to improve your workflow.


Options
=======

Source Channel
   The channel which the Multicam Selector gets its input from.
Cut To
   Cuts the Multicam strip at the current frame and
   changes the *Source Channel* automatically to the selected channels.


Workflow
========

#. First you are going to want to add in each of your video strips.
#. Next, you will want to sync all your cameras by either using
   :doc:`Audio Waveforms </video_editing/sequencer/strips/sound>` or by the movement of objects.

   .. tip::

      To make syncing strips easier you can group cameras, their audio,
      and their effects together using :doc:`Meta Strips </video_editing/sequencer/meta>`.

#. Add a viewer region for every input channel and to improve the performance use proxies.
#. Add a Multicam Selector strip *above* all the channel tracks.

   After completing these steps you should get something similar to the image below:

   .. figure:: /images/video-editing_sequencer_strips_effects_multicam_example.png

      Multi-camera editing setup.

#. Now select the Multicam strip, if you take a look at the strip options (in the Sidebar),
   you will notice, that Multicam is a rather simple effect strip:
   It just takes a selected channel as its input. That is all.
   The magic comes with the convenient keyboard layout.
#. When you select the Multicam strip, the keys :kbd:`1` to :kbd:`9` are mapped to the cut buttons.
   So, select the Multicam strip and start playback and press the keys
   for the correct input while watching the individual cameras.
#. You will end up with a small Multicam Selector strip for every cut.

In reality, it boils down to: watch a few seconds to see, what is coming,
watch it again and do a rough cut using the number keys,
do some fine-tuning by selecting the outer handles of two neighboring Multicam for A/B rolling.
