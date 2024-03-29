
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

   .. _bpy.ops.sequencer.strip_color_tag_set:

   Color Tag
      Besides the set of :ref:`Default Strip Colors <sequencer-strip-colors>`
      strips can also be given an alternative predefined color.
      This can be useful to help organize your sequence by for example,
      giving a special color to all graphic overlays and a different color for footage.

Mute
   If enabled the strip will not produce any output.


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

.. _bpy.types.SequenceTransform.filter:

Filter
   Interpolation Methods.

   :Nearest: No interpolation, uses nearest neighboring pixel.
   :Bilinear: Simple interpolation between adjacent pixels.

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

.. _bpy.types.SoundSequence.volume:

Volume
   The volume of the sound.
   This value, when animated and with the :menuselection:`View --> Show F-Curves` option activated,
   is drawn on the strip as a dark section that follows the animation curve.
   The value is also reflected in the waveform.

.. _bpy.types.SoundSequence.pan:

Pan
   Used to pan the audio between speakers in multichannel audio.
   Only works for mono sources. The number of audio channels can be configured in
   the :ref:`Audio Output <render-output-video-encoding-audio>` settings.
   For stereo output panning works from left (-1) to right (1). When
   the output uses more than two channels, values can be between -2 and 2,
   where 0 means front/center, -1 means to the left and 1 to the right.
   To address rear speakers, you can pan to those with the higher values:
   -2, 2 is back. This value basically represents the angle at
   which it's played if you multiply the value by 90 degrees.
   For smooth animation you can assign values outside the soft bounds,
   since the angle wraps around over multiple rotations.

.. _bpy.types.SoundSequence.show_waveform:

Display Waveform
   Display an approximate waveform of the sound file inside of the Sound strip.
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

Speed Factor
   Coefficient of playback speed.
   This value will affect length of the strip, that will not be represented in the timeline.

.. _bpy.types.Sequence.frame_start:

Start
   Changes the starting frame number of the strip, which is the same as selecting and moving the strip.

.. _bpy.types.Sequence.frame_final_duration:

Duration
   Changes the length, in frames of the strip. This works by changing the end frame,
   which is the same as selecting and moving the strip's right handle.
End
   Specifies the ending time and ending frame number for the strip.

.. _bpy.types.Sequence.frame_offset_start:
.. _bpy.types.Sequence.frame_offset_end:

Strip Offset Start/End
   Can be used to either extend the strip beyond the end frame by repeating the last frame.
   Or it can be used to shorten the strip, as if you were cropping the end frame.
   This is the same as adjusting the strip handles.

.. _bpy.types.MovieSequence.animation_offset_start:
.. _bpy.types.MovieSequence.animation_offset_end:
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

   The list of color spaces depends on the active :ref:`OCIO config <ocio-config>`.
   The default supported color spaces are described in detail here:
   :ref:`Default OpenColorIO Configuration <ocio-config-default-color-spaces>`
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
      the perceived speed of the media will be wrong unless the speed is
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

Source Information
   Displays information about the strip's media.

   Samplerate
      The number of samples per second the audio is encoded at.
   Channels
      The number of audio channels encoded into the audio stream.
