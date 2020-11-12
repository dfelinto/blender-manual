
****************
Opening & Saving
****************

Opening and saving blend-files is usually done using the :doc:`File Browser </editors/file_browser>`.

.. tip::

   Blend-files can also be opened by dragging and dropping blend-files into the Blender window.
   This method also allows to :doc:`link/append </files/linked_libraries/index>` the file.

.. note:: Unsaved Changes

   By default, when exiting Blender or loading a new blend-file, if you have unsaved changes,
   a pop-up will ask you to either confirm discarding those changes, or save them.

   This behavior can be disabled with the *Save Prompt* option in the :ref:`prefs-save-load` section
   of the *Preferences*.


.. _files-blend-open:

Opening Files
=============

.. figure:: /images/files_blend_open-save_file-browser-open.png

   The File Browser in open configuration.


Usage
-----

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`File --> Open...`
   :Hotkey:    :kbd:`Ctrl-O`

The upper text field displays the current directory path,
and the lower text field contains the selected filename.


Options
-------

.. _file-load-ui:

Load UI
   When enabled, the screen layout saved inside each blend-file is used,
   replacing the current layout and :doc:`Workspaces </interface/window_system/workspaces>`.
   Otherwise the file screen layout is ignored.

   .. tip::

      If you want to work on a blend-file using your own defaults, start a fresh Blender,
      open the File Browser and turn off the *Load UI* button, and open the desired file.

Trusted Source
   When enabled, Python scripts and drivers that may be included in the file will be run automatically.
   Enable this only if you created the file yourself,
   or you trust that the person who gave it to you did not include any malicious code with it.
   See :doc:`Python Security </advanced/scripting/security>` to configure default trust options.


.. _other-file-open-options:

Other File Open Options
-----------------------

From the *File* menu, you can also open files with the following tools:

Open Recent
   Lists recently used files. Click on one to load it in.
Recover Last Session
   This will load the ``quit.blend`` file Blender automatically saved just before exiting.
   This option enables you to recover your last work session if, for example, you closed Blender by accident.
Recover Auto Save
   This will allow you to open an automatically saved file to recover it.

.. seealso::

   :ref:`Auto Saves <troubleshooting-file-recovery>`


.. _files-blend-save:

Saving Files
============

.. figure:: /images/files_blend_open-save_file-browser-save.png

   The File Browser in save configuration.


Usage
-----

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`File --> Save`
   :Hotkey:    :kbd:`Ctrl-S`

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`File --> Save As...`
   :Hotkey:    :kbd:`Shift-Ctrl-S`

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`File --> Save Copy...`

There are a number of slightly different methods you can use to save your blend-file to your drive:

Save :kbd:`Ctrl-S`
   Save current blend-file over itself (if it was not saved yet, this will automatically switch to *Save As...*).
Save As... :kbd:`Shift-Ctrl-S`
   Choose a file path to save the blend-file to.
Save Copy
   Choose a file path to save the blend-file to, but return to editing the original file upon completion.
   This can be used to save backups of the current working state without modifying the original file.

.. warning::

   If a file with the same given name already exists,
   the text field will turn red as a warning that the file will be overwritten.

.. tip::

   Use the *plus* or *minus* buttons to the right of the file name,
   or :kbd:`NumpadPlus`, :kbd:`NumpadMinus` to increase/decrease a number at the end of the file name
   (e.g. changing ``file_01.blend`` to ``file_02.blend``).


Options
-------

.. _files-blend-compress:

Compress File
   When enabled, the saved file will be smaller, but take longer to save and load.

   .. note::

      While compression is useful for distributing files online
      and saving drive space for large projects it has drawbacks too.

      This option may slow down Blender when you quit,
      or under normal operation when Blender is saving your backup files.

   .. seealso::

      Linked Libraries :ref:`files-linked_libraries-known_limitations-compression`.

Remap Relative
   This option remaps :ref:`files-blend-relative_paths`
   (such as linked libraries and images) when saving a file in a new location.
Save Copy
   This option saves a copy of the actual working state but does not make the saved file active.

.. seealso::

   :ref:`Auto Save <troubleshooting-file-recovery>`


.. _files-blend-relative_paths:

Relative Paths
==============

Many blend-files reference external images or other linked blend-files.
A path tells Blender where to look for these files.
If the external files are moved, the blend-file that references them will not look right.

When you specify one of these external files, the default option is to make the path relative.
Blender stores a partial path evaluated relative to the directory location of the referencing blend-file.
This choice helps when you need to reorganize folders or move your files.

With a relative path, you can move the blend-file to a new location provided
the externally linked files are moved along with it.
For example, you could send someone a folder that contains a blend-file
and a subfolder of external images that it references.

When relative paths are supported, the File Browser provides a *Relative Path* checkbox,
when entering the path into a text field, use a double slash prefix (``//``) to make it so.

Relative paths are the default but this can be changed
in the :doc:`File </editors/preferences/file_paths>` tab of the *Preferences*.

.. note::

   You cannot use relative paths into a new *untitled* blend-file.
   Save it before linking to external files.

.. hint::

   If it is necessary to relocate a blend-file relative to its linked resources,
   use Blender's File :ref:`Save As... <files-blend-save>`
   function which has an option to *Remap Relative* file links.
