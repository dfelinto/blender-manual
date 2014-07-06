
Post Install Configuration
**************************

Blender will normally run fine without _any_ configuration but there are some changes you may
want to make depending on your hardware.

This section **only** covers system specific user preferences.


.. admonition:: Info
   :class: nicetip

   The key combination :kbd:`ctrl-U` saves all the settings of the currently open Blender file into the default Blender file. The settings in the default Blender file are read when Blender is first started or when :kbd:`ctrl-N` is pressed to start a new file. If you accidentally change the settings in your default Blender file (i.e. you save your work in progress as the default) you can restore factory settings from the file menu  press :kbd:`ctrl-U` to save the newly loaded factory settings.


The following section titles match the user preference categories.


Input
=====

- If you don't have a numpad you may want to enable 'Emulate Numpad'
- If you don't have a middle mouse button you can enable 'Emulate 3 Button Mouse'


File Paths
==========

This isn't essential but you may want to set the paths for more useful default locations.


- Temp Directory: You may want to change this if you have a faster disk for temp file storage.
- Image Editor: Useful so you can edit images externally (from the image space), The path to the gimp for example can be set here.


.. admonition:: Info
   :class: nicetip

   "//" at the start of a path in blender signifies the directory of the currently opened blend file, used to reference relative-paths.


System
======

While there are many settings here you may want to set in special-cases,
this document focuses on common features.


- VBOs (Vertex Buffer Objects), can give a good speed boost to the viewport performance, keep this enabled unless it gives problems (some older hardware does not support VBOs)

Sequencer / Clip Editor:

- Memory Cache Limit: If you use the sequencer of movie clips you may want to increase the cache limit since this will make scrubbing a lot faster - but take care the limit stays well under your total system memory.


