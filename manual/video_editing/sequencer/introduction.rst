
************
Introduction
************

The Sequencer region is horizontally divided into channels,
each channel can contain what is called a strip.
A strip can be an image, animation, or any number of effects.
Each channel is numbered consecutively on the Y axis,
starting from zero and allows up to 32 total channels.
The X axis represents time. Each channel can contain as many strips
as it needs as long as they do not overlap. If a strip needs to overlap another,
it needs to be placed on a channel above or below the other strip.
When strips are stacked, they stack from bottom to top where the lowest channel
forms the background and the highest the foreground.

.. note::

   The first channel 0 is unusable as a place to put strips.
   This is because it is used by the :doc:`Sequencer Display </video_editing/preview/introduction>`
   to show a composite of all strips above channel 0.

This region is where strips can be :doc:`selected </video_editing/sequencer/selecting>`,
:doc:`modified </video_editing/sequencer/editing>` by moving, cutting, or extending strips.
There are also several built-in :doc:`effects </video_editing/sequencer/strips/effects/index>`
that can be combined with other strips to change their appearance.
