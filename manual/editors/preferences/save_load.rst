.. _prefs-save-load:

***********
Save & Load
***********

.. figure:: /images/editors_preferences_section_save-load.png

   Preferences Save/Load section.


Blend Files
===========

Save
   Save Prompt
      Asks for confirmation before closing or opening a new blend-file
      if the current file has unsaved changes.

File Preview Types
   Select how blend-file preview are generated.
   These previews are used both in the :doc:`File Browser </editors/file_browser>`
   and for previews shown in the operating system's file browser.

   :None: Do not generate any blend-file previews.
   :Auto:
      If there is no camera in the 3D Viewport a preview using a screenshot of the active Workspace is generated.
      If a camera is in the scene, a preview of the viewport from the camera view is used.
   :Screenshot: Generate a preview by taking a screenshot of the active Workspace.
   :Camera View: Generate a preview of a Workbench render from the camera's point of view.

Default To
   Relative Paths
      Default value for :ref:`Relative Paths <files-blend-relative_paths>` when loading external files
      such as images, sounds, and linked libraries. It will be ignored if a path is already set.
   Compress File
      Default value for :ref:`Compress file <files-blend-compress>` when saving blend-files.
   Load UI
      Default value for :ref:`Load UI <file-load-ui>` when loading blend-files.

Text Files
   Tabs as Spaces
      Entering :kbd:`Tab` in the Text Editor adds the appropriate number of spaces
      instead of using characters.

.. _prefs-save_load-backups:

Save Versions
   Number of versions created (for backup) when saving newer versions of a file.

   This option keeps saved versions of your file in the same directory,
   using extensions: ``.blend1``, ``.blend2``, etc.,
   with the number increasing to the number of versions you specify.

   Older files will be named with a higher number.
   E.g. with the default setting of 2, you will have three versions of your file:

   :``*.blend``: last saved.
   :``*.blend1``: second last saved.
   :``*.blend2``: third last saved.

Recent Files
   Number of files displayed in :menuselection:`File --> Open Recent`.


.. _prefs-auto-save:

Auto Save
---------

Enables :doc:`Auto Save </troubleshooting/recover>`.
Tells Blender to *automatically* save a backup copy of your work-in-progress files to the :ref:`temp-dir`.

Timer
   This specifies the number of minutes to wait between each :doc:`Auto Save </troubleshooting/recover>`.
   The default value of the Blender installation is 2 minutes.
   The minimum is 1, and the Maximum is 60 (save every hour).


.. _bpy.ops.preferences.autoexec:
.. _prefs-auto-execution:

Auto Run Python Scripts
-----------------------

Python scripts (including driver expressions) are not executed by default for security reasons.
You may be working on projects where you only load files from trusted sources,
making it more convenient to allow scripts to be executed automatically.

Excluded Paths
   Blend-files in these folders will *not* automatically run Python scripts.
   This can be used to define where blend-files from untrusted sources are kept.

.. seealso::

   :doc:`Python Security </advanced/scripting/security>`.


File Browser
============

Show Locations
   Recent
      Hide the *Recent* panel of the :doc:`File Browser </editors/file_browser>`
      which displays recently accessed folders.
   System
      Hide System Bookmarks in the *File Browser*.

Defaults
   Filter Files
      By activating this, the file region in the File Browser will only show appropriate files
      (i.e. blend-files when loading a complete Blender setting).
      The selection of file types may be changed in the file region.

   Show Hidden Files/Data-Blocks
      Hide files which start with ``.`` in File Browsers and data IDs.

      .. hint::

         Data-blocks beginning with a ``.`` can be selected by typing in the ``.`` characters.
         When explicitly written, the setting to hide these data-blocks is ignored.
