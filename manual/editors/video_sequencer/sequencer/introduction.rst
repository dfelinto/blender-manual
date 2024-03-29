
************
Introduction
************

This Sequencer view is where strips can be :doc:`selected </video_editing/edit/montage/selecting>`,
:doc:`modified </video_editing/edit/montage/editing>` by moving, cutting, or extending strips.
There are also several built-in :doc:`effects </video_editing/edit/montage/strips/effects/index>`
that can be combined with other strips to change their appearance.

The Sequencer view is horizontally divided into :doc:`Channels </editors/video_sequencer/sequencer/channels>`
each channel can contain what is called a strip.
A strip can be an image, animation, or any number of effects.
Each channel is numbered consecutively on the Y axis,
starting from zero and allows up to 128 total channels.
The X axis represents time. Each channel can contain as many strips
as it needs as long as they do not overlap. If a strip needs to overlap another,
it needs to be placed on a channel above or below the other strip.
When strips are stacked, they stack from bottom to top where the lowest channel
forms the background and the highest the foreground.

.. note::

   The first channel 0 is unusable as a place to put strips.
   This is because it is used by the :doc:`Sequencer Display </editors/video_sequencer/preview/introduction>`
   to show a composite of all strips above channel 0.
