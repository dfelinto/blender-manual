.. _prefs-input-keymap-editor:

******
Keymap
******

The keymap editor lets you adjust your keymap via:

:Presets: Predefined keymaps which come with Blender and can be added to.
:Preferences: Keymaps may define their own preferences to change the functionality or add additional key bindings.
:Key Map Items: You may add/remove/edit individual keymap entries.

.. figure:: /images/editors_preferences_section_keymap.png

   Blender Preferences Keymap section.


.. _bpy.ops.preferences.keyconfig:

Preset Management
=================

Keymap Presets
   Select the keymap from a list of predefined keymaps.
Import
   Importing opens a File Browser to select a ``.py`` file to add to the list of keymap presets.
Export
   Saves the current keymap configuration as a preset others may use.

   All Keymaps
      When disabled, only the keymaps and categories that have been modified by the user will be exported.
      In addition, add-ons may register keymaps to their respective functions,
      however, these keymaps are not exported unless changed by the user.
      This exported file may be thought of as a *"keymap delta"* instead of a full keymap export.

      When enabled, the entire keymap is written.


Filtering
---------

.. _bpy.types.SpacePreferences.filter_type:

Filter Type
   Name
      Search the keymap item by the operator name it runs.
   Key Binding
      Search the keymap item by the key used to activate it.

      .. hint::

         You could for example search with ``Ctrl Shift C`` for keymap items that use all these keys.

.. _bpy.types.SpacePreferences.filter_text:

Search
   The text to search (leave blank to disable).


Preferences
===========

Keymaps may define their own preferences, these are predefined adjustments to the keymap you can make
without having to manually adjust individual keymap items which can cause problems with newer `Blender Versions`_.

See the :ref:`default keymap preferences <keymap-blender_default-prefs>`
for options available in the default keymap.


.. _bpy.ops.preferences.keyitem:
.. _bpy.types.KeyMapItem:

Editor
======

The Keymap editor lets you change the default hotkeys. You can change keymaps for each of Blender's editors.

.. figure:: /images/editors_preferences_keymap_keymap-editor.png

   Keymap editor.


.. rubric:: Usage

#. Select the keymap you want to change and click on the white arrows to open up the keymap tree.
#. Select which Input will control the function.
#. Change hotkeys as you want. Just click on the shortcut input and enter the new shortcut.

Active
   Uncheck to disable this keymap item.
Map Type
   Keyboard
      Single hotkey or key combination.
   Mouse
      Actions from mouse buttons, tablet or touchpad input.
   NDOF
      Movement from a 3D mouse (:term:`NDOF`) device.
   Tweak
      Mouse click and drag *(optionally map drag direction to different actions)*.
   Text Input
      Use this function by entering a text.
   Timer
      Used to control actions based on a time period.
      E.g. by default, *Animation Step* uses "Timer 0", *Smooth View* uses "Timer 1".
Operator ID Name
   The identifier for the operator to call.

   .. hint::

      See :mod:`blender_api:bpy.ops` for a list of operators (remove the ``bpy.`` prefix for the identifier).
Event
   Type
      The key or button that activates this keymap item (depending on the map type).
   Value
      The action (such as press, release, click, drag, etc.), (depending on the map type).
   Modifier
      Additional keys to hold (such as :kbd:`Ctrl`, :kbd:`Shift`, :kbd:`Alt`).
Operator Properties
   Changes to the defaults properties this operator is activated with

.. seealso::

   :ref:`keymap-customize` for more information on keymap editing.


Restoring
---------

If you want to restore the default settings for a keymap,
just click on the *Restore* button at the top right of this keymap.

.. tip::

   Instead of deleting the default keymap to create your custom one,
   you can just add a new *Preset* for both the mouse and keyboard.


Known Limitations
=================

Blender Versions
----------------

A problem with modifying your own keymap is newer Blender versions key change the way tools are accessed,
breaking your customized keymap.

While the keymap can be manually updated, the more customizations you make, the higher the chance of conflicts
in newer Blender versions is.
