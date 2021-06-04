.. _bpy.types.PreferencesSystem:

******
System
******

The *System* section allows you to set graphics card options, memory limits & sound settings.

If your hardware does not support some of the options described on this page,
then they will either not show up or be corrected on startup.

.. figure:: /images/editors_preferences_section_system.png

   Preferences System section.


.. _editors_preferences_cycles:

Cycles Render Device
====================

Changes the computing device the :doc:`Cycles </render/cycles/index>` render engine uses to render images.
Cycles can use either the CPU or certain GPUs to render images,
for more information see the :doc:`GPU Rendering </render/cycles/gpu_rendering>` page.

None
   When set to *None* or when the only option is *None*:
   the CPU will be used as the computing device for Cycles.
CUDA
   If the system has a compatible Nvidia CUDA device, it will show up an option for rendering with Cycles.
OptiX
   If the system has a compatible Nvidia OptiX device, it will show up an option for rendering with Cycles.
OpenCL
   If the system has a compatible AMD OpenCL device, it will show up an option for rendering with Cycles.

.. _prefs-system-cycles-distributive-memory:

Distribute Memory Across Devices
   Allocates resources across multiple GPUs rather than duplicating data,
   effectively freeing up space for larger scenes. Note that in order for this option to be available,
   the GPUs must be connected together with a high bandwidth communication protocol.
   Currently only NVLink on Nvidia GPUs is supported.


Memory & Limits
===============

Undo Steps
   Number of Undo steps available.

Undo Memory Limit
   Maximum memory usage in Mb (0 is unlimited).

Global Undo
   This enables Blender to save actions done when you are **not** in *Edit Mode*.
   For example, duplicating objects, changing panel settings or switching between modes.

   .. warning::

      While disabling this option does save memory,
      it stops the :ref:`bpy.ops.screen.redo_last` panel from functioning,
      also preventing tool options from being changed in some cases.
      For typical usage, its best to keep this enabled.

.. seealso::

   :doc:`Read more about Undo and Redo options </interface/undo_redo>`.

Console Scroll-back Lines
   The number of lines, buffered in memory of the console window.
   Useful for debugging purposes and command-line rendering.

Texture Time Out
   Time since last access of a GL texture in seconds, after which it is freed.
   Set this to 0 to keep textures allocated.

   Garbage Collection Rate
      Number of seconds between each run of the GL texture garbage collector.

VBO Time Out
   Time since last access of a GL vertex buffer object (VBO) in seconds after which it is freed
   (set to 0 to keep VBO allocated).

   Garbage Collection Rate
      Number of seconds between each run of the GL vertex buffer object garbage collector.


.. _prefs-system-video-sequencer:

Video Sequencer
===============

.. _prefs-system-memory-cache-limit:

Memory Cache Limit
   Upper limit of the Video Sequencer and Movie Clip Editor memory cache (in megabytes).
   For an optimal Clip editor and Sequencer performance, high values are recommended.
Use Disk Cache
   Writes cached strips to disk which can store a lot more than RAM.
   To use the Disk Cache, this option must be enabled,
   the *Disk Cache Directory* and *Disk Cache Limit* set, then save or reopen the existing blend-file.
Directory
   The location on disk to store the cache.
Cache Limit
   Upper limit of the Video Sequencer's disk cache (in gigabytes), setting to zero disables disk cache.
Compression
   The level of compression to compress image in the disk cache.
   This has a trade off between saving disk space and requiring more processing.
   The more compression used requires faster disk write/read speeds and more CPU usage.

Proxy Setup
   When and how :doc:`Proxies </video_editing/sequencer/sidebar/proxy>` are created.

   :Automatic: Build proxies for added movie and image strips in each preview size.
   :Manual: Set up proxies manually.

.. seealso::

   :doc:`Sequencer Cache Properties </video_editing/sequencer/sidebar/cache>`


.. _prefs-system-sound:

Sound
=====

This panel contains the sound settings for live playback
within Blender and are only available with *SDL* or *OpenAL*.
To control these settings for exporting sound
see the :ref:`Encoding Panel <render-output-video-encoding-panel>`
and :ref:`Audio Panel <data-scenes-audio>`.

Audio Device
   Sets the audio engine to use to process and output audio.

   :None:
      No Audio support (audio strips can still be loaded normally).
   :SDL:
      Uses Simple Direct Media Layer API from `libsdl.org <https://www.libsdl.org>`__
      to render sounds directly to the sound device output. Very useful for Sequencer strips editing.
   :OpenAL:
      Provides buffered sound rendering with 3D/spatial support.
      Used for 3D source support by speaker objects.

Channels
   Sets the audio channel count.
Mixing Buffer
   Sets the number of samples used by the audio mixing buffer.
   Higher buffer sizes can cause latency issues,
   but if you hear clicks or other problems, try to increase the size.
Sample Rate
   Sets the audio `sampling rate <https://en.wikipedia.org/wiki/Sampling_(signal_processing)#Sampling_rate>`__.
Sample Format
   Sets the audio sample format.
