
FIXME(Template Unsupported: Doc:2.5/Manual/Interface/Configuration/index;
{{Doc:2.5/Manual/Interface/Configuration/index}}
)

In the Input preferences, you can customize how Blender reacts to the mouse and keyboard as
well as define your own keymap.


.. figure:: /images/Manual-Interface-Configuration-Input-UserPreferencesInput.jpg
   :width: 650px
   :figwidth: 650px


Managing presets
****************

Blender lets you define multiple :guilabel:`Preset` input configurations.
Instead of deleting the default keymap to create yours,
you can just add new :guilabel:`Presets` for both the mouse and keyboard. Mouse options can be
found on the left hand side of the window and keyboard options to the right in the above
picture.


Adding and deleting presets
===========================

.. figure:: /images/Manual-Interface-Configuration-Input-AddDeletePreset.jpg

Before changing anything in the default configuration,
click on the "plus" symbol shown in the picture to add a new :guilabel:`Preset`. Blender will
ask you to name your new preset after which you can select the :guilabel:`Preset` from the
list to edit it. If you want to delete your :guilabel:`Preset`,
select it from the list and then click the "minus" symbol.


Selecting presets
=================

You can change the preset you are using by doing one of the following:


- Selecting the configuration from the :guilabel:`Interaction` menu of the splash screen at startup or by selecting :menuselection:`Help --> Splash Screen`.
- Selecting the configuration from the :guilabel:`User Preferences Input` window.


.. note::

   Note that either of the above options will only change the preset for the current file. If you select :menuselection:`File --> New` or :menuselection:`File --> Open`, the default preset will be re-loaded.


Setting presets to default
==========================

.. figure:: /images/Manual-Interface-Configuration-Input-SplashScreenInteraction.jpg
   :width: 307px
   :figwidth: 307px


Once you've configured your mouse and keyboard :guilabel:`Presets`,
you can make this the default configuration by:


- Opening the :guilabel:`User Preferences Input` editor and select your presets from the preset list or,
- Selecting your preset configuration from the splash screen.
- Saving your configuration using the :guilabel:`Save As Default` option from a :guilabel:`User Preferences` window or by pressing :kbd:`ctrl-u`.


Export/Import key configuration
===============================

In some cases, you may need to save your configuration in an external file (e.g.
if you need to install a new system or share your keymap configuration with the community).
Simply :kbd:`lmb` :guilabel:`Export Key Configuration` on the :guilabel:`Input` tab
header and a file browser will open so that you can choose where to store the configuration.
The :guilabel:`Import Key Configuration` button installs a keymap configuration that is on
your computer but not in Blender.


Mouse
*****

:guilabel:`Emulate 3 Button Mouse`
   It is possible to use Blender without a 3 button mouse (such as a two-button mouse,
   Apple single-button Mouse, or laptop).
   This functionality can be emulated with key/mousebutton combos.
   This option is only available if :guilabel:`Select With` is set to :guilabel:`Right`.
   :doc:`Read more about emulating a 3 button mouse » </interface/keyboard_and_mouse#mouse_button_emulation>`
:guilabel:`Continuous Grab`
   Allows moving the mouse outside of the view (for translation, rotation, scale for example).
:guilabel:`Drag Threshold`
   The number of pixels that a User Interface element has to be moved before it is recognized by Blender.
:guilabel:`Select with`
   You can choose which button is used for selection (the other one is used to place the 3D cursor).
:guilabel:`Double Click`
   The time for a double click (in ms).


.. note::

   If you're using a graphic tablet instead of mouse, and pressure doesn't work properly, try to place the mouse pointer to Blender window and then unplug/replug your graphic tablet. This might help.


Numpad emulation
****************

The Numpad keys are used quite often in Blender and are not the same keys as the regular
number keys. If you have a keyboard without a Numpad (e.g. on a laptop),
you can tell Blender to treat the standard number keys as Numpad keys.
Just check :guilabel:`Emulate Numpad`.


View manipulation
*****************

:guilabel:`Orbit Style`
   Select how Blender works when you rotate the 3D view (by default :kbd:`MMB`). Two styles are available. If you come from Maya or Cinema 4D, you will prefer :guilabel:`Turntable`.
:guilabel:`Zoom Style`
   Choose your preferred style of zooming in and out with :kbd:`Ctrl-MMB`
      :guilabel:`Scale`
         :guilabel:`Scale` zooming depends on where you first click in the view. To zoom out, hold :kbd:`ctrl-MMB` while dragging from the edge of the screen towards the center. To zoom in, hold :kbd:`ctrl-MMB` while dragging from the center of the screen towards the edge.
      :guilabel:`Continue`
         The :guilabel:`Continue` zooming option allows you to control the speed (and not the value) of zooming by moving away from the initial click-point with :kbd:`Ctrl-MMB`. Moving up from the initial click-point or to the right will zoom out, moving down or to the left will zoom in. The further away you move, the faster the zoom movement will be. The directions can be altered by the :guilabel:`Vertical` and :guilabel:`Horizontal` radio buttons and the :guilabel:`Invert Zoom Direction` option.
      :guilabel:`Dolly`
         :guilabel:`Dolly` zooming works similarly to :guilabel:`Continue` zooming except that zoom speed is constant.
      :guilabel:`Vertical`
         Moving up zooms out and moving down zooms in.
      :guilabel:`Horizontal`
         Moving left zooms in and moving right zooms out.
:guilabel:`Invert Zoom Direction`
   Inverts the Zoom direction for :guilabel:`Dolly` and :guilabel:`Continue` zooming.
:guilabel:`Invert Wheel Zoom Direction`
   Inverts the direction of the mouse wheel zoom.
:guilabel:`NDOF device`
   Set the sensitivity of a 3D mouse.


Keymap editor
*************

.. figure:: /images/Manual-Interface-Configuration-Input-KeymapEditor.jpg
   :width: 320px
   :figwidth: 320px


The Keymap editor lets you change the default Hotkeys. You can change keymaps for each window.


- Select the keymap you want to change and click on the white arrows to open up the keymap tree.
- Select which Input will control the function
  - Keyboard: Only hotkey or combo hotkey (:kbd:`E` or :kbd:`Shift-E`).
  - Mouse: Left/middle/right click. Can be combined with :kbd:`Alt`, :kbd:`Shift`, :kbd:`Ctrl`, :kbd:`Cmd`.
  - Tweak: Click and drag. Can also be combined with the 4 previous keys.
  - Text input: Use this function by entering a text
  - Timer: Used to control actions based on a time period. e.g. By default, Animation Step uses Timer 0, Smooth view uses Timer 1.
- Change hotkeys as you want. Just click on the shortcut input and enter the new shortcut.

If you want to restore the default settings for a keymap,
just click on the :guilabel:`Restore` button at the top right of this keymap.

