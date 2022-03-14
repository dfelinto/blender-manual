
**************
Default Keymap
**************

While this isn't a comprehensive list,
this page shows common keys used in Blender's default keymap.

.. Even though this is not intended to be comprehensive,
   it could be expanded.


Global Keys
===========

.. list-table::
   :widths: 10 90

   * - :kbd:`Ctrl-O`
     - Open file.
   * - :kbd:`Ctrl-S`
     - Save file.
   * - :kbd:`Ctrl-N`
     - New file.
   * - :kbd:`Ctrl-Z`
     - Undo.
   * - :kbd:`Shift-Ctrl-Z`
     - Redo.
   * - :kbd:`Ctrl-Q`
     - Quit.
   * - :kbd:`F1`
     - Help *(context sensitive)*.
   * - :kbd:`F2`
     - Rename active item.
   * - :kbd:`F3`
     - Menu Search.
   * - :kbd:`F4`
     - File context menu.
   * - :kbd:`F5` - :kbd:`F8`
     - *Reserved for user actions.*
   * - :kbd:`F9`
     - Adjust last operation.
   * - :kbd:`F10`
     - *Reserved for user actions.*
   * - :kbd:`F11`
     - Show render window.
   * - :kbd:`F12`
     - Render the current frame.
   * - :kbd:`Q`
     - Quick access (favorites).
   * - :kbd:`Ctrl-Spacebar`
     - Toggle Maximize Area.
   * - :kbd:`Ctrl-Alt-Spacebar`
     - Toggle Fullscreen Area
   * - :kbd:`Ctrl-PageUp` / :kbd:`Ctrl-PageDown`
     - Next/previous Workspace.
   * - :kbd:`Spacebar`
     - User configurable.

       :Play: Toggle animation playback.
       :Tools: Tool switching with hotkeys (:kbd:`Shift-Spacebar` for play).
       :Search: Search for actions (:kbd:`Shift-Spacebar` for play).
   * - :kbd:`Shift-Ctrl-Spacebar`
     - Playback animation (reverse).


Common Editing Keys
===================

.. list-table::
   :widths: 10 90

   * - :kbd:`X`
     - Deletes the selected item, requires a confirmation dialog.
   * - :kbd:`Delete`
     - Deletes the selected item, does not require a confirmation dialog.


Common Editor Keys
==================

These keys are shared across editors such as the 3D Viewport, UV and Graph editor.

.. list-table::
   :widths: 10 90

   * - :kbd:`A`
     - Select all.
   * - :kbd:`Alt-A`
     - Select none.
   * - :kbd:`Ctrl-I`
     - Invert selection.
   * - :kbd:`H`
     - Hide selection.
   * - :kbd:`Alt-H`
     - Reveal hidden items.
   * - :kbd:`T`
     - Toggle Toolbar.
   * - :kbd:`N`
     - Toggle Sidebar.


3D Viewport Keys
================

.. list-table::
   :widths: 10 90

   * - :kbd:`Tab`
     - Edit-mode toggle.
   * - :kbd:`Ctrl-Tab`
     - Mode switching pie menu (toggles Pose Mode for armatures).
   * - :kbd:`1` - :kbd:`3`
     - Edit mesh vertex/edge/face toggle (:kbd:`Shift` extends, :kbd:`Ctrl` expands & contracts).
   * - :kbd:`AccentGrave`
     - 3D Viewport navigation pie menu.
   * - :kbd:`Ctrl-AccentGrave`
     - Toggle gizmos.
   * - :kbd:`Shift-AccentGrave`
     - Walk/Fly Navigation.


Platform Specific Keys
======================

macOS
-----

The :kbd:`Cmd` key can be used instead of :kbd:`Ctrl` on macOS
for all but a few exceptions which conflict with the operating system.

List of additional macOS specific keys:

.. list-table::
   :widths: 10 90

   * - :kbd:`Cmd-Comma`
     - Preferences.


.. _keymap-blender_default-prefs:

Keymap Preferences
==================

.. _keymap-blender_default-prefs-select_with:

Select with Mouse Button
   Controls which mouse button, either right or left, is used to select items in Blender.
   If *Left* is selected the :kbd:`RMB` will be a context sensitive menu,
   if *Right* is selected the :kbd:`LMB` will place the 3D Cursor.

.. _keymap-blender_default-spacebar_action:

Spacebar Action
   Controls the action of :kbd:`Spacebar`.
   These and other shortcuts can be modified in the :doc:`keymap preferences </editors/preferences/keymap>`.

   :Play:
      Starts playing through the :doc:`Timeline </editors/timeline>`,
      this option is good for animation or video editing work.
   :Tools:
      Opens the Toolbar underneath the cursor to quickly change the active tool.
      This option is good if you are doing a lot of modeling or rigging work.
   :Search:
      Opens up the :doc:`Menu Search </interface/controls/templates/operator_search>`.
      This option is good for someone who is new to Blender and is unfamiliar with the menus and shortcuts.

Activate Gizmo Event
   The activation event for gizmos that support drag motion.
   This option is only available when Left click *Select with Mouse Button* is chosen.

   :Press:
      Allows immediate activation, preventing click events being passed to the tool.
   :Drag:
      Allows click events to pass through to the tool, adding a small delay.

Right Mouse Select Action
   The default action for the right mouse button.
   This option is only available when Right click *Select with Mouse Button* is chosen.

   :Select & Tweak: Right mouse always tweaks the selected item.
   :Selection Tool: Right mouse uses the selection tool.

Tool Keys
   The method of keys to activate tools such as move, rotate, and scale.

   :Immediate: Activate actions immediately.
   :Active Tool: Activate the tool for editors that support tools.

Alt Click Tool Prompt
   Tapping :kbd:`Alt` shows a prompt in the status bar prompting a second keystroke to activate the tool.
   Note this option is not available when using :ref:`Emulate 3 Button Mouse <preferences-input-emulate-mouse>`.

Alt Tool Access
   Hold :kbd:`Alt` to use the :doc:`Active Tool </interface/tool_system>` when the gizmo would normally be required.
   This option is only available when Left click *Select with Mouse Button* is chosen.
   Note this option is not available when using :ref:`Emulate 3 Button Mouse <preferences-input-emulate-mouse>`.

Alt Cursor Access
   Hold :kbd:`Alt-LMB` to place the Cursor (instead of :kbd:`LMB`), allows tools to activate on press
   instead of drag. This option is only available when Right click *Select with Mouse Button* is chosen.
   Note this option is not available when using :ref:`Emulate 3 Button Mouse <preferences-input-emulate-mouse>`.

Select All Toggles
   Causes selection shortcut :kbd:`A` to deselect all when any selection exists.


3D Viewport
-----------

Grave Accent / Tilde Action
   :Navigate:
      Navigation pie menu, useful on systems without a numeric keypad.
   :Gizmos:
      Transform gizmos pie menu, useful for quickly switching between transform gizmos.

Middle Mouse Action
   The action when :kbd:`MMB` dragging in the viewport, this also applies to trackpads.

   :Orbit:
      Rotates the view around a pivot point, :kbd:`Shift-MMB` is used for panning the view.
   :Pan:
      Shifts the view towards the mouse, :kbd:`Shift-MMB` is used for orbiting the view.

Alt Middle Mouse Drag Action
   :Relative:
      Set the view axis where each mouse direction maps to an axis relative to the current orientation.
   :Absolute:
      Set the view axis where each mouse direction always maps to the same axis.

.. _keymap-pref-py_menu_on_drag:

Tab for Pie Menu
   Causes :kbd:`Tab` to open a pie menu (swaps :kbd:`Tab` and :kbd:`Ctrl-Tab`).

Pie Menu on Drag
   This allows keys to have a secondary drag action.

   :kbd:`Tab`
      :tap: Toggles Edit Mode.
      :drag: Object Mode pie menu.
   :kbd:`Z`
      :tap: Toggles wireframe view.
      :drag: Display mode pie menu.
   :kbd:`AccentGrave`
      :tap: First person :ref:`Fly/walk Navigation <3dview-fly-walk>`.
      :drag: View axis pie menu.

Extra Shading Pie Menu Items
   Show additional items in the shading menu (:kbd:`Z` key).


File Browser
------------

Open Folders on Single Click
   Navigate into folders by clicking on them once instead of twice.
