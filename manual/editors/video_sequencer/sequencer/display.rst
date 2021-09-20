
*******
Display
*******

.. _bpy.types.SpaceSequenceEditor.show_strip_overlay:
.. _bpy.types.SequencerTimelineOverlay:

Sequencer Overlays
==================

Overlays are information that is displayed on top of the strip region.
There is a toggle to display or hide all overlays for the strip region.

.. _bpy.types.SequencerTimelineOverlay.show_strip_name:

Name
   Shows the :ref:`Name <bpy.types.Sequence.name>` on the strip.

.. _bpy.types.SequencerTimelineOverlay.show_strip_source:

Source
   Shows the path to the strip file on the strip.

.. _bpy.types.SequencerTimelineOverlay.show_strip_duration:

Duration
   Shows the length of the strip in frames on the strip.

.. _bpy.types.SpaceSequeSequencerTimelineOverlaynceEditor.show_strip_offset:

Offsets
   Shows overflow bars of "extra" content from either cutting or sliding strips.

.. _bpy.types.SequencerTimelineOverlay.show_fcurves:

F-Curves
   Show animation curves for opacity and volume values as darkened sections of the strip.

.. _bpy.types.SequencerTimelineOverlay.waveform_display_type:

Waveform Display
   Global options for waveform display on sound strips.

   :Waveform Off: Disable waveforms for all strips.
   :Waveform On: Enable waveforms for all strips.
   :Use Strip Option:
      Set waveform per strip configured with
      :ref:`Display Waveform <bpy.types.SoundSequence.show_waveform>`.
