.. _bpy.types.Speaker:
.. _bpy.ops.object.speaker:

*******
Speaker
*******

.. figure:: /images/render_output_audio_speaker_objects.png

   Speaker objects.

The speaker object is used to give sound in the 3D Viewport.
After adding the object, the various settings can be changed in the Properties.


Options
=======

Sound
-----

Open
   The :doc:`/interface/controls/templates/data_block` for loading audio files.
   There are two properties you can check when loading a sound:

   Cache
      This means the whole sound will be decoded and the raw audio data will be buffered in memory,
      which results in faster playback, but uses quite a lot of memory. So this should be used
      for short sound effects that get played more often, but not for longer audio files such as music.
   Mono
      For any 3D audio or panning effects the sound source has to be single channel,
      otherwise it's assumed that the 3D audio and panning information is already present in the multichannel file.
      Enable this if you want to use those effects for a file with multiple channels.
Mute
   Toggles whether or not the sound can be heard.
Volume
   Adjust the loudness of the sound.
Pitch
   Can be used to bend the pitch of the sound to be either deeper or higher.
   This basically changes the playback speed of the sound which also results in a pitch change.


Playback Time
^^^^^^^^^^^^^

There is no setting to choose the start time when the speaker should start playing,
because you might want a single speaker to play multiple times.
Therefore you have to open the *NLA Editor* where you can add sound strips
that define when the sound should start (nothing else,
so any other properties of the strips, like length don't matter).
When you add a speaker object such a strip will be added at the current frame.


Distance
--------

.. figure:: /images/render_output_audio_speaker_properties.png
   :align: right

   Speaker properties.

Distance attenuation relevant settings.

Volume
   Minimum/Maximum
      No matter how far away/close the object is, the distance-based volume won't be lower/higher than this value.
   Attenuation
      How strong the distance affects the volume.
      This factor sets the strength of the distance-based volume change,
      depending on the chosen distance model (see :ref:`scene settings <data-scenes-audio>`).

Distance
   Maximum
      If the object is farther away than this distance, this distance is used to calculate the distance-based volume.
      Influence of this value also depends on the distance model.
   Reference
      The distance at which the volume is 100% (1.0). Set this value to the distance used for recording the sound.
      Usually sound effects recordings should be made exactly 1 m away from sound to get an accurate volume.


Cone
----

Directionality relevant settings.

Imagine a cone with the top at the original of the speaker object
and the main axis of it facing in the same direction as the speaker.
There are two cones an inner and an outer cone. The angles represent their opening angles,
so 360° mean the cone is fully open and there's no directionality anymore.
Inside the inner cone the volume is 100% (1.0),
outside the outer cone the volume is, whatever one sets for the outer cone volume
and the volume between those two cones, linearly interpolated between this two volumes.

Angle
   Outer
      Angle of the outer cone in degrees. Outside this cone, the volume is equal to the *Outer* volume.
   Inner
      Angle of the inner cone in degrees. Inside the cone, the volume is 100%.
Volume
   Outer
      Volume outside the outer cone.
