.. _bpy.types.PreferencesFilePaths:
.. _prefs-file-paths:

**********
File Paths
**********

The *File* section in *Preferences* allows you to configure auto-save preferences
and set default file paths for blend-files, rendered images, and more.

Locations for various external files can be set for the following options:

.. figure:: /images/editors_preferences_section_file-paths.png

   Preferences File Paths section.

.. hint::

   The default path ``//`` refers to the folder of the currently open blend-file
   (see :ref:`files-blend-relative_paths` for details).


Data
====

Fonts
   Default location to browse for :doc:`text object </modeling/texts/index>` font files.
Textures
   Default location to browse for image textures.
Scripts
   An additional location to search for Python scripts.

   By default Blender looks in several directories (platform dependent) for scripts.
   By setting a user script path in the preferences an additional directory is used.
   This can be used to store your own scripts and add-ons independently of the current Blender version.

   You will need to create specific subfolders in this path which match the structure of the ``scripts``
   folder found in Blender's installation directory.

   The following subdirectories will be used when present:

   ``startup/``
      Modules in this folder will be imported on startup.
   ``addons/``
      Add-ons located here will be listed in the add-ons preferences.
   ``modules/``
      Modules in this folder can be imported by other scripts.
   ``presets/``
      Presets in this folder will be added to existing presets.

   .. note::

      You have to restart Blender for all changes to the users scripts to take effect.

Sounds
   Default location to browse for sound files.
Temporary Files
   The location where temporary files are stored,
   leave blank to use the systems temporary directory
   (see :ref:`temp-dir` for details).


Render
======

Render Output
   Where rendered images/videos are saved.
Render Cache
   The location where cached render images are stored.


Applications
============

Image Editor
   The path to an external program to use for image editing.

.. _prefs-file_paths-animation_player:

Animation Player
   The program used for playing back rendered animations via
   :ref:`View Animation <topbar-render-view_animation>`.

   By default this is set to *Internal* which uses Blender's built-in
   :ref:`animation player <render-output-animation_player>`.

   This has the advantage that all image formats supported by Blender can be played back
   and no 3rd party application needs to be installed.


Development
===========

Only visible when :ref:`Developer Extras <prefs-interface-dev-extras>` are enabled.

I18n Branches
   The path to the ``/branches`` directory of your local svn-translation copy, to allow translating from the UI.


Known Limitations
=================

Permissions on Windows
----------------------

Be sure that you have the right privileges for running the executable accessing the path defined.
On Windows for instance, if the option *"Run this program as an administrator"* is enabled for the executable,
it will lead to a failure to open the editor due to a limitation within the OS User Account Control.
Running a program with elevated privileges is potentially dangerous!
