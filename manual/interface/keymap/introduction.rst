
****************
Common Shortcuts
****************

Conventions
===========

.. Note that these conventions are for people reading the manual.
   we have more detailed list of conventions for authors under the writing style section.


Keyboards
---------

Hotkey letters are shown in this manual like they appear on a keyboard; for example:

:kbd:`G`
   refers to the lowercase ``g``.
:kbd:`Shift`, :kbd:`Ctrl`, :kbd:`Alt`
   are specified as modifier keys.
:kbd:`Ctrl-W`, :kbd:`Shift-Alt-A`, ...
   indicates that these keys should be pressed simultaneously.
:kbd:`Numpad0` to :kbd:`Numpad9`, :kbd:`NumpadPlus`
   refer to the keys on the separate numeric keypad.

Other keys are referred to by their names,
such as :kbd:`Esc`, :kbd:`Tab`, :kbd:`F1` to :kbd:`F12`.
Of special note are the arrow keys, :kbd:`Left`, :kbd:`Right` and so on.


Mice
----

This manual refers to mouse buttons as:

:kbd:`LMB`
   Left Mouse Button
:kbd:`RMB`
   Right Mouse Button
:kbd:`MMB`
   Middle Mouse Button
:kbd:`Wheel`
   Scrolling the wheel.


Mouse
=====

Blender's default keymap has two main interaction modes: Right- and left-click-select.

In the past, Blender has used right-click-select to have a more clear
distinction between selection and action.
In this mode, the :kbd:`RMB` (Right Mouse Button) is generally used for
selection and the :kbd:`LMB` (Left Mouse Button) initiates or confirms actions.

Today, Blender users can choose between the older right-click-select method
and left-click-select, which makes Blender feel more like other software.

Video: `Learn the benefits of right-click-select <https://vimeo.com/76335056>`__.


Hovering
========

While hovering (when the cursor is held over a button).


Properties
----------

- :kbd:`Ctrl-C` -- Copy the (single) value of the button.
- :kbd:`Ctrl-V` -- Paste the (single) value of the button.
- :kbd:`Ctrl-Alt-C` -- Copy the entire vector or color of the field.
- :kbd:`Ctrl-Alt-V` -- Paste the entire vector or color of the field.
- :kbd:`RMB` -- Open the context menu.
- :kbd:`Backspace` -- Clear the value (sets to zero or clears a text field).
- :kbd:`Minus` -- Negate number values (multiply by -1.0).
- :kbd:`Ctrl-Wheel` -- Change the value incremental steps.

  For pop-up option menus buttons, this cycles the value.
- :kbd:`Return` -- Activates menus or toggles the value.

- :kbd:`Alt` -- Hold while editing values to apply the change to all selected items
  (objects, bones, sequence-strips).

  This can be used for number fields and toggles.


Animation
---------

- :kbd:`I` -- Insert a keyframe.
- :kbd:`Alt-I` -- Clear the keyframe.
- :kbd:`Shift-Alt-I` -- Clear all keyframes (removing all F-curves).
- :kbd:`Ctrl-D` -- Assign a driver.
- :kbd:`Ctrl-Alt-D` -- Clear the driver.
- :kbd:`K` -- Add a Keying Set.
- :kbd:`Alt-K` -- Clear the Keying Set.


Python Scripting
----------------

- :kbd:`Ctrl-C` -- Over any :ref:`ui-operator-buttons` copies their Python command into the clipboard.

  This can be used in the Python Console or in the Text editor when writing scripts.
- :kbd:`Shift-Ctrl-C` -- Over property buttons copies their data path for this property
  (also available from the context menu).

  Useful when writing drivers or scripts.
- :kbd:`Shift-Ctrl-Alt-C` -- Over property buttons copies their *full* data path for the data-block and property.

  Note that in most cases it is best to access values based on the context, instead of by name.


Dragging
========

- :kbd:`Ctrl` -- While dragging, snap to discrete steps.
- :kbd:`Shift` -- Gives precision control over the value.
- :kbd:`Shift-Ctrl` -- Precise snap will move the object with high precision
  along with the snapping constraint.


.. _ui-text-editing:

Text Editing
============

- :kbd:`Home` -- Go to the start of the line.
- :kbd:`End` -- Go to the end of the line.
- :kbd:`Left`, :kbd:`Right` -- Move the cursor a single character.
- :kbd:`Ctrl-Left`, :kbd:`Ctrl-Right` -- Move the cursor an entire word.
- :kbd:`Backspace`, :kbd:`Delete` -- Delete characters.
- :kbd:`Ctrl-Backspace`, :kbd:`Ctrl-Delete` -- Delete words.
- :kbd:`Shift` -- Select while holding the key and moving the cursor.
- :kbd:`Ctrl-A` -- Select all text.
- :kbd:`Ctrl-C` -- Copy the selected text.
- :kbd:`Ctrl-X` -- Cut the selected text.
- :kbd:`Ctrl-V` -- Paste text at the cursor position.


Confirm & Cancel
================

- :kbd:`Esc`, :kbd:`RMB` -- Cancel.
- :kbd:`Return`, :kbd:`LMB` -- Confirm.

.. (todo?) deactivation: Some controls can be disabled, in Blender deactivated controls are still editable.
   That can be due to the current state or context. In that case, they appear in a lighter color.
