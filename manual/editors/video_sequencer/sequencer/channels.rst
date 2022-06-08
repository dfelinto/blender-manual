
********
Channels
********

Channels are horizontal tracks of along the timeline that contain content called Strips.
A strip can be an image, animation, or any number of effects.
Each channel is numbered consecutively on the Y axis,
starting from 1 and allows up to 128 total channels.
The X axis of each channel represents time. Each channel can contain as many strips
as it needs along the time axis as long as they do not overlap. If a strip needs to overlap another,
it needs to be placed on a channel above or below the other strip.


.. _bpy.types.SequenceTimelineChannel:

Channel Region
==============

The Channel region can be found on the left side of the timeline.
It is used to organize channels and control channels as a whole.
The visibility of this region can be toggled with :menuselection:`View --> Channels`

.. _bpy.types.SequenceTimelineChannel.name:

Name
   The name of the channel,
   this can be changed to help with project organization by double clicking on the name.

.. _bpy.types.SequenceTimelineChannel.mute:

Mute Channel
   Disable all the strips in the channel from having an affect on the render.
   Note that individual strips can also be muted which is different than muting the whole channel.

.. _bpy.types.SequenceTimelineChannel.lock:

Lock Channel
   Prevent any modifications the strips in the channel.
   Note that individual strips can also be locked which is different than locking the whole channel.
