
*****
Strip
*****

Header
======

Type
   Strip type represented by an icon.

.. _bpy.types.Sequence.name:

Name
   You can name or rename your strips here.
Mute
   If checked the strip will not produce any output.


Compositing
===========

.. reference::

   :Panel:     :menuselection:`Sidebar --> Strip --> Compositing`

Blend
   Mode of blending strip with lower channels.
Opacity
   Set the opacity (alpha) of the strip.
   This value, when animated and with the :menuselection:`View --> Show F-Curves` option turned on,
   is drawn on the strip as a dark section that follows the animation curve.


.. _bpy.types.SequenceTransform:

Transform
=========

.. reference::

   :Panel:     :menuselection:`Sidebar --> Strip --> Transform`

.. _bpy.types.SequenceTransform.offset:

Position X, Y
   Used to move the frames along the X and Y axis.

.. _bpy.types.SequenceTransform.scale:

Scale X, Y
   Scale the image on the X and Y axis.

.. _bpy.types.SequenceTransform.rotation:

Rotation
   Rotates the input two-dimensionally along the Z axis.

.. _bpy.types.ImageSequence.use_flip:

Mirror
   Mirrors the image along the X axis (left to right) or the Y axis (top to bottom).


.. _bpy.types.SequenceCrop:

Crop
====

.. reference::

   :Panel:     :menuselection:`Sidebar --> Strip --> Crop`

Used to crop the source image. Use *Top*, *Left*,
*Bottom*, and *Right* to control the number of pixels that are cropped.


Video
=====

.. reference::

   :Panel:     :menuselection:`Sidebar --> Strip --> Video`

Strobe
   To only display each nth frame. For example, if you set this to 10,
   the strip will only display frames 1, 11, 21, 31, 41... of the source.
   *Strobe* is a float value -- this way you can get a strobe effect synced exactly to a beat,
   for example, by using non-integer values.
Reverse Frames
   Strip is played backwards starting from the last frame in the sequence.


Color
=====

.. reference::

   :Panel:     :menuselection:`Sidebar --> Strip --> Color`

Saturation
   Increase or decrease the saturation of an image.
Multiply
   Multiplies the colors by this value. This will increases the brightness.
Convert to Float
   Converts input to float data.


Sound
=====

.. reference::

   :Panel:     :menuselection:`Sidebar --> Strip --> Sound`

Volume
   The volume of the sound.
   This value, when animated and with the :menuselection:`View --> Show F-Curves` option activated,
   is drawn on the strip as a dark section that follows the animation curve.
   The value is also reflected in the waveform.
Pitch
   Coefficient of playback speed.
   This value will affect length of the strip, that will not be represented in the timeline.
Pan
   Used to pan the audio from left and right channels. Only works for mono sources.
   Values can be between -2 and 2, where 0 means front/center, -1 means to the left and 1 to the right.
   In case of multichannel audio (rear speakers) you can pan to those with the higher values: -2, 2 is back.
   So this value basically represents the angle at which it's played.

.. _bpy.types.SoundSequence.show_waveform:

Display Waveform
   Display an approximate waveform of the sound file inside of the sound strip.
   The waveform reflects strip volume and its animation using :doc:`keyframes </animation/keyframes/introduction>`.

.. _bpy.types.Sound.use_mono:

Mono
   Mixdown all audio channels into a single one.


Time
====

.. reference::

   :Panel:     :menuselection:`Sidebar --> Strip --> Time`

The Time panel is used to control source and timeline position of the strip.

Lock (padlock icon)
   Prevents the strip from being moved (found in the panel header).

.. _bpy.types.Sequence.channel:

Channel
   Changes the channel number, or row, of the strip.

.. _bpy.types.Sequence.frame_start:

Start
   Changes the starting frame number of the strip, which is the same as selecting and moving the strip.
Duration
   Changes the length, in frames of the strip. This works by changing the end frame,
   which is the same as selecting and moving the strip's right handle.
End
   Specifies the ending time and ending frame number for the strip.
Strip Offset Start/End
   Can be used to either extend the strip beyond the end frame by repeating the last frame.
   Or it can be used to shorten the strip, as if you were cropping the end frame.
   This is the same as adjusting the strip handles.

.. _sequencer-duration-hard:

Hold Offset Start/End
   Offset of the uncut strip content.
Current Frame
   The frame number relative to the start of the active strip.


Source
======

.. reference::

   :Panel:     :menuselection:`Sidebar --> Strip --> Source`

The Source panel is used to control sources of the strip
such as filename and file path and various methods of interpreting these files.

Path
   The directory that contains the source file.
   When the file is moved this can be updated instead of re-create the strip.
File
   The file name of the source file.
   For image strips showing an image sequence, this will be different for each frame.
Change Data/Files
   Same as the *Path* and *File* fields, but this time combined to open the File Browser in order to
   find the file(s) you search. Same as :menuselection:`Strip --> Inputs --> Change Paths/Files`.

MPEG Preseek
   Movie strip only -- Use Preseek field to tell Blender to look backward and compose an image
   based on the specified amount of previous frames (e.g. 15 for MPEG-2 DVD).
Color Space
   To specify the color space of the source file.
Alpha Mode
   If the source file has an Alpha (transparency) channel, you can choose:

   :term:`Straight Alpha` or :term:`Premultiplied Alpha`
Stream Index
   Movie strip only -- For files with several movie streams, use the stream with the given index.
Deinterlace
   Removes fields in a video file. For example,
   if it is an analog video and it has even or odd interlacing fields.

Source Information
   Displays information about the strip's media.

   Resolution
      Resolution of the active strip image output.
   FPS
      Movie strip only -- The frame rate encoded into the video file.
      If this value does not match the scene :ref:`Frame Rate <bpy.types.RenderSettings.fps>`
      the percieved speed of the media will be wrong unless the speed is
      :ref:`changed <video_editing-change_fps>` to account for the difference in frame rate.


Options for Sound Strips
------------------------

Sound
   :ref:`Data-block menu <ui-data-block>` to select a sound.
Path
   Path to the sound file used by this :ref:`data-block <ui-data-block>` menu.
Pack
   Pack sound into the blend-file.

.. _bpy.types.Sound.use_memory_cache:

Caching
   Sound file is decoded and loaded into the RAM.
