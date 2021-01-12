.. _splash-quick-start:

********
Defaults
********

When you start Blender for the first time, the interactive region of the :doc:`Splash Screen </interface/window_system/splash>`
is replaced with a couple of initial preferences to configure how you interact inside Blender.

.. note::

   These options can always be changed later in the :doc:`Preferences </editors/preferences/index>`.

Language
   The language used for translating the user interface.
   The list is broken up into categories determining how complete the translations are.
   More language preferences can be set in the :ref:`Translation Preferences <prefs-interface-translation>`.

Shortcuts
   Presets for the default :doc:`keymap </editors/preferences/keymap>` for Blender.
   Note that this manual assumes that you use the "Blender" keymap.

   Blender
      This is the default keymap.
      Read more about this keymap :doc:`here </interface/keymap/blender_default>`.
   Blender 2.7x
      This keymap is intended to match the last major series of Blender versions
      and is designed for people upgrading who do not want to learn the updated keymap.
   Industry Compatible
      This keymap is intended to match common creation software
      and is intended for people who use many different creation software.
      Read more about this keymap :doc:`here </interface/keymap/industry_compatible>`.

Select With
   Controls which mouse button, either right or left, is used to select items in Blender.
Spacebar
   Controls the action of :kbd:`Spacebar`.
   These and other shortcuts can be modified in the :doc:`keymap preferences </editors/preferences/keymap>`.

   Play
      Starts playing through the :doc:`Timeline </editors/timeline>`,
      this option is good for animation or video editing.
   Tools
      Opens the Toolbar underneath the cursor to quickly change the active tool.
      This option is good if doing a lot of modeling or rigging.
   Search
      Opens up the :doc:`Menu Search </interface/controls/templates/operator_search>`.
      This option is good for someone who is new to Blender and is unfamiliar with its menus and shortcuts.
Theme
   Choose between a light or dark theme for Blender.
   Themes can be customized more in the :doc:`Preferences </editors/preferences/themes>`.

Load Previous Version Settings
   Copies preferences and startup files from the previous version of Blender and then loads them.

   The settings need to be imported from previous versions because the configuration files of each Blender version
   are stored in separate folders. Refer to the :doc:`/advanced/blender_directory_layout` page
   for the location of these folders.

There are two areas where Blender's defaults are stored:

Preferences
   The :ref:`Preferences <prefs-menu>` file stores keymap, add-ons theme and other options.
Startup File
   The :ref:`Startup File <startup-file>` stores the scene, Workspaces and interface which is displayed at startup
   and when loading a new file (:menuselection:`File --> New`).


Saving Defaults
===============

The user preferences are automatically saved when changed.

Changing the default startup file can be done via
:menuselection:`File --> Defaults --> Save Startup File`
See :ref:`Startup File <startup-file>`.


Loading Factory Settings
========================

You can revert your own customizations to Blender's defaults:

Preferences
   The :ref:`Preferences <prefs-menu>` Load Factory Settings.
Startup File & Preferences
   :menuselection:`File --> Defaults --> Load Factory Settings`.

.. note::

   After loading the factory settings, the preferences won't be auto-saved.

   See :ref:`prefs-menu` for details.
