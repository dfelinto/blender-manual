
******
Topbar
******

Menus
=====

.. figure:: /images/interface_window-system_topbar_menus.png


.. _topbar-blender_menu:

Blender Menu
------------

Splash Screen
   Open the :ref:`splash`.

.. _bpy.ops.wm.splash_about:

About Blender
   Opens a menu displaying the following information about Blender:

   - **Version**: The Blender version.
   - **Date**: Date when Blender was compiled.
   - **Hash**: The Git Hash of the build.
     This can be useful to give to support personnel when diagnosing a problem.
   - **Branch**: Optional branch name.
   - **Windowing Environment**: On Linux, this will show either Wayland or X11 depending
     on the windowing environment that Blender is running on.

   - **Release Notes**: Open the latest release notes.
   - **Credits**: Open credits website.
   - **License**: Open License website.
   - **Blender Website**: Open main Blender website.
   - **Blender Store**: Open the Blender store.
   - **Development Fund**: Open the developer fund website.

Install Application Template
   Install a new :ref:`application template <app_templates>`.


File Menu
---------

The options to manage files are:

New :kbd:`Ctrl-N`
   Clears the current scene and loads the selected application template.
Open :kbd:`Ctrl-O`
   :ref:`Open <bpy.ops.wm.open_mainfile>` a blend-file.
Open Recent :kbd:`Shift-Ctrl-O`
   Displays a list of the most :ref:`recently opened <other-file-open-options>` blend-files.
   Select any of the file names in the list to open that blend-file.
Revert
   Reopens the current file to its last saved version.
Recover
   Recover Last Session
      This will load a blend-file that Blender automatically saves just before exiting.
      So this option enables you to :doc:`recover </troubleshooting/recover>`
      your last work :term:`session`, e.g. if you closed Blender by accident.
   Recover Auto Save
      This will open an automatically saved file
      to :doc:`recover </troubleshooting/recover>` it.
Save :kbd:`Ctrl-S`
   :ref:`Save <bpy.ops.wm.save_mainfile>` the current blend-file.
Save As... :kbd:`Shift-Ctrl-S`
   Opens the File Browser to specify file name and location of :ref:`save <bpy.ops.wm.save_mainfile>`.
Save Copy...
   :ref:`Saves <bpy.ops.wm.save_mainfile>` a copy of the current file.
Link...
   Links data from an external blend-file (library) to the current one.
   The editing of that data is only possible in the external library.
   *Link* and *Append* are used to load in only selected parts from another file.
   See :doc:`Linked Libraries </files/linked_libraries/index>`.
Append...
   Appends data from an external blend-file to the current one.
   The new data is copied from the external file, and completely unlinked from it.
Data Previews
   Tools for managing :doc:`data-block previews </files/blend/previews>`.
Import
   Blender can use information stored in a variety of other format files which are created by
   other graphics programs. See :doc:`Import/Export </files/import_export>`.
Export
   Normally you save your work in a blend-file,
   but you can export some or all of your work to a format that can be processed by other graphics programs.
   See :doc:`Import/Export </files/import_export>`.
External Data
   External data, like texture images and other resources,
   can be stored inside the blend-file (packed) or as separate files (unpacked).
   Blender keeps track of all unpacked resources via a relative or absolute path.
   See :ref:`pack or unpack external data <pack-unpack-data>`.

   Automatically Pack Into .blend
      This option activates the file packing.
      If enabled, every time the blend-file is saved, all external files will be saved (packed) in it.
   Pack All Into .blend
      Pack all used external files into the blend-file.
   Unpack Into Files
      Unpack all files packed into this blend-file to external ones.
   Make All Paths Relative
      Make all paths to external files :ref:`files-blend-relative_paths` to current blend-file.
   Make All Paths Absolute
      Make all paths to external files absolute (= full path from the system's root).
   Report Missing Files
      This option is useful to check if there are links to unpacked files that no longer exist.
      After selecting this option, a warning message will appear in the Info editor's header.
      If no warning is shown, there are no missing external files.
   Find Missing Files
      In case you have broken links in a blend-file, this can help you to fix the problem.
      A File Browser will show up. Select the desired directory (or a file within that directory),
      and a search will be performed in it, recursively in all contained directories.
      Every missing file found in the search will be recovered.
      Those recoveries will be done as absolute paths,
      so if you want to have relative paths you will need to select *Make All Paths Relative*.

      .. note::

         Recovered files might need to be reloaded. You can do that one by one, or
         you can save the blend-file and reload it again, so that all external files are reloaded at once.

Clean Up
   Unused Data-Blocks
      Remove unused data-blocks from both the current blend-file and any
      :doc:`Linked Data </files/linked_libraries/link_append>` (cannot be undone).
      See the :ref:`Outliner <bpy.ops.outliner.orphans_purge>` for more information.
   Recursive Unused Data-Blocks
      Remove all unused data-blocks from both the current blend-file and any
      :doc:`Linked Data </files/linked_libraries/link_append>`
      including any indirectly used data-blocks i.e. those only used by unused data-blocks.
   Unused Linked Data-Blocks
      Remove unused data-blocks from only :doc:`Linked Data </files/linked_libraries/link_append>`.
   Recursive Unused Linked Data-Blocks
      Remove all unused data-blocks from only :doc:`Linked Data </files/linked_libraries/link_append>`
      including any indirectly used data-blocks i.e. those only used by unused data-blocks.
   Unused Local Data-Blocks
      Remove all unused data-blocks from only the current blend-file.
   Recursive Unused Local Data-Blocks
      Remove all unused data-blocks from only the current blend-file
      including any indirectly used data-blocks i.e. those only used by unused data-blocks.


.. _startup-file:

Defaults
   This menu manages the startup file which is used to store the default scene,
   workspace, and interface displayed when creating a new file.

   Initially this contains the :doc:`startup scene </editors/3dview/startup_scene>` included with Blender.
   This can be replaced by your own customized setup.

   .. _bpy.ops.wm.save_homefile:

   Save Startup File
      Saves the current blend-file as the startup file.
   
   .. _bpy.ops.wm.read_factory_settings:

   Load Factory Settings
      Restores the default startup file and preferences.

   When an :doc:`/advanced/app_templates` is in use the following operators are shown:

   Load Factory Blender Settings
      Loads the default settings to the original Blender settings without
      the changes made from the current application template.
   Load Factory (Application Template Name) Settings
      Loads the default settings to the original application template.

   .. seealso:: :ref:`prefs-menu`.

Quit :kbd:`Ctrl-Q`
   Closes Blender. The current scene is saved to a file called "quit.blend" in Blender's temporary directory
   (which can be found on the "File Paths" tab of the :doc:`Preferences </editors/preferences/file_paths>`).


Edit Menu
---------

Undo/Redo/History
   See :doc:`/interface/undo_redo`.
Menu Search
   Find a menu based on its name.
Operator Search
   Execute an operator based on its name (:ref:`Developer Extras <prefs-interface-dev-extras>` only).
Rename Active Item
   Rename the active object or node;
   see :ref:`Rename tool <tools_rename-active>` for more information.
Batch Rename
   Renames multiple data types at once;
   see :ref:`Batch Rename tool <bpy.ops.wm.batch_rename>` for more information.

.. _bpy.types.ToolSettings.lock_object_mode:

Lock Object Modes
   Prevents selecting objects that are in a different mode than the current one.

   .. note::

      This option can prevent accidental mode changes, such as when you're
      trying to select a bone in Pose Mode to animate it, but instead
      click a piece of background scenery (which would normally select that
      piece and switch to Object Mode).

      You may want to disable *Lock Object Modes* for example when weighting rigged objects
      or sculpting/painting where you intentionally want to switch between objects in different modes.

Preferences
   Open the Preferences window.


.. _topbar-render:

Render Menu
-----------

Render Image :kbd:`F12`
   Render the active scene at the current frame.
Render Animation :kbd:`Ctrl-F12`
   Render the animation of the active scene.

   .. seealso::

      - :doc:`Rendering Animations </render/output/animation>` for details.
Render Audio
   Mix the scene's audio to a sound file.

   .. seealso::

      - :doc:`Rendering audio </render/output/audio/introduction>` for details.
View Render :kbd:`F11`
   Show the Render window. (Press again to switch back to the main Blender window.)

.. _topbar-render-view_animation:

View Animation :kbd:`Ctrl-F11`
   Playback rendered animation in a separate player.

   .. seealso::

      - :ref:`Animation player <bpy.ops.render.play_rendered_anim>` for details.
      - :ref:`Preferences <prefs-file_paths-animation_player>` for selecting a
        different animation player than the default one.
Lock Interface
   Lock interface during rendering in favor of giving more memory to the renderer.


.. _topbar-window:

Window Menu
-----------

New Window
   Create a new window by copying the current window.
New Main Window
   Create a new window with its own workspace and scene selection.
Toggle Window Fullscreen
   Toggle the current window fullscreen.
Next Workspace
   Switch to the next workspace.
Previous Workspace
   Switch to the previous workspace.

.. _bpy.types.Screen.show_statusbar:

Show Status Bar
   Choose whether the :doc:`Status Bar </interface/window_system/status_bar>`
   at the bottom of the window should be displayed.

.. _bpy.ops.screen.screenshot:

Save Screenshot
   Capture a picture of the current Blender window.
   A File Browser will open to choose where the screenshot is saved.

.. _bpy.ops.screen.screenshot_area:

Save Screenshot (Editor)
   Capture a picture of the selected Editor.
   Select the Editor by clicking :kbd:`LMB` within its area after running the operator.
   A File Browser will open to choose where the screenshot is saved.


Help Menu
---------

See :doc:`/getting_started/help`.


Workspaces
==========

.. figure:: /images/interface_window-system_topbar_workspaces.png
   :align: center

This set of tabs is used to switch between :doc:`Workspaces </interface/window_system/workspaces>`,
which are essentially predefined window layouts.


Scenes & Layers
===============

.. figure:: /images/interface_window-system_topbar_scenes-layers.png
   :align: center

These :ref:`data-block menus <ui-data-block>` are used to select
the current :doc:`Scene </scene_layout/scene/index>` and :doc:`View Layer </scene_layout/view_layers/index>`.
