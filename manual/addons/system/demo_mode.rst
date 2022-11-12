
*********
Demo Mode
*********

Todo.


Activation
==========

- Open Blender and go to Preferences then the Add-ons tab.
- Click System then Demo Mode to enable the script.


Configuration
=============

This is done from :menuselection:`File --> Demo Mode (Setup)` in the File menu, from here you can select a directory
which is searched recursively for blend-files to loop over.

There are options as to what to do with each file at the moment the main options are to render or
play an animation with options as to how many cycles to play, time to wait after render is done.


Automatic Configuration
-----------------------

The *Auto* option selects between *Render* and *Play* option based on the window layout's use of image/node editors.
If you are happy to use these settings on all files, you can leave the *Run Immediately* option enabled and confirm.


Adjusting the Configuration
---------------------------

If you want to set options per file, you can disable *Run Immediately*,
during setup and select ``demo.py`` text data-block.
This file has one line per file and settings can be edited and saved with the blend-file.
When ``demo.py`` is present you only have to go to :menuselection:`File --> Demo Mode (Start)`.


Attributes
^^^^^^^^^^

These keyword arguments show up in generated ``demo.py``, e.g::

   dict(anim_cycles=2, anim_render=False, anim_screen_switch=0.0, anim_time_max=8.0, anim_time_min=4.0,
   display_render=4.0, file='foobar.blend', mode='AUTO'),

- ``anim_cycles`` -- Number of times to play the animation.
- ``anim_render`` -- Render entire animation (applies to ``mode='RENDER'`` only).
- ``anim_screen_switch`` -- Time between switching screens (in seconds) or 0 to disable.
- ``anim_time_max`` -- Maximum number of seconds to show the animation for
  (in case the end frame is very high for no reason).
- ``anim_time_min`` -- Minimum number of seconds to show the animation for (for small loops).
- ``display_render`` -- Time to display the rendered image before moving on (in seconds).
- ``file`` -- The filepath for the blend-file.
- ``mode`` -- ``AUTO`` / ``PLAY`` / ``RENDER`` -- what to do on load.


Portable Configuration
^^^^^^^^^^^^^^^^^^^^^^

Once you setup a ``demo.py`` you may want to move it to a different system.
In this case the paths might not match up, if so
update the ``search_path`` variable to point to the path on the new system.
You can also set the ``search_path`` to use the directory of the current blend-file::

   search_path = "//"


Usage
=====

Once the demo starts it will play, render and load different files in the same Blender instance.
Since its using a modal operator you can still use with Blender while the demo runs.

If you want to stop Demo Mode, you can press :kbd:`Esc` and continue using Blender.
To enable again there are three buttons at the right hand side of the file menu to navigate *Prev*/*Pause*/*Next*.


Limitations
===========

- One file can't play an animation then render, you need to copy the line in ``demo.py`` and
  set one mode to ``RENDER`` the other to ``PLAY``.


.. reference::

   :Category: System
   :Description: Demo Mode lets you select multiple blend-files and loop over them.
   :Location: :menuselection:`File --> Demo menu`
   :File: system_demo_mode folder
   :Author: Campbell Barton
   :License: GPL
   :Note: This add-on is bundled with Blender.
