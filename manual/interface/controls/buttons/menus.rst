.. _bpy.types.Menu:

*****
Menus
*****

Blender uses a variety of different menus for accessing options and :doc:`/interface/operators`.
Menus can be interacted with in the following ways:

Mouse selection
   :kbd:`LMB` on the desired item.
Numerical selection
   You can use the number keys or numpad to input an item in the list to select.
   For example, :kbd:`Numpad1` will select the first item and so on.

If a menu is too large to fit on the screen, a small
scrolling triangle appears on the top or bottom.
Scrolling is done by moving the mouse above or below this triangle.


.. rubric:: Shortcuts

- Use :kbd:`Wheel` while hovering with the mouse.
- Arrow keys can be used to navigate.
- Each menu item has an underlined character which can be pressed to activate it.
- Number keys or numpad can also be used to activate menu items.
  (:kbd:`1` for the first menu item, :kbd:`2` for the second etc.
  For larger menus, :kbd:`Alt-1` activates the 11th and so on, up to :kbd:`Alt-0` for the 20th.)
- Press :kbd:`Return` to activate the selected menu item.
- Press :kbd:`Esc` to close the menu without activating any menu item. This can also be
  done by moving the mouse cursor far away from the menu, or by :kbd:`LMB` clicking anywhere
  outside of it.


.. _bpy.types.UIPopupMenu:
.. _ui-header-menu:

Header Menus
============

.. figure:: /images/interface_controls_buttons_menus_menu-button.png
   :align: right

   Image menu in the Header of the Image editor.

Most :ref:`headers <ui-region-header>` exhibit a set of menus, located at the start of the header.
Header menus are used to configure the editor and access operators.
All menu entries show the relevant shortcut keys, if any.


Collapsing Menus
----------------

Sometimes it's helpful to gain some extra horizontal space in the header by collapsing menus.
This can be accessed from the header context menu:
click :kbd:`RMB` on the header and select *Collapse Menus*.

.. list-table::

   * - .. figure:: /images/interface_controls_buttons_menus_header-menu-expand.png

          Right-click on any of the header menus.

     - .. figure:: /images/interface_controls_buttons_menus_header-menu-collapsed.png

          Access the menu from the collapsed icon.


Select Menus
============

.. figure:: /images/interface_controls_buttons_menus_select-menu.png
   :align: right
   :figwidth: 150px

   The 3D Viewport Mode Select menu.

A Select menu (or "selector" for short) lets you choose between a set of options.
It appears as an icon and/or text with a down arrow on the right side.
To use it, click the button with :kbd:`LMB` to show the available options,
then click the desired option (once selected, it'll appear inside the button).
You can also use :kbd:`Ctrl-Wheel` to cycle through the options without opening the menu.

.. container:: lead

   .. clear


.. _bpy.types.UIPopover:

Popover Menus
=============

.. figure:: /images/interface_controls_buttons_menus_popup-menu.png
   :align: right

   The Transform Orientations popover menu.

Popover menus are similar to Select Menus, but can show more varied content
such as a title, buttons, sliders, etc.


Context Menu
============

Context menus are pop-ups that can be opened with :kbd:`RMB`.
In most editors, it's also possible to use the :kbd:`Menu` key.
The contents of the menu depend on the location of the mouse pointer.

When invoked in an editor, the menu contains a list of operators sensitive to the editor's mode.
When invoked over buttons and properties, common options include:

.. for the property associated with the control.

Single
   Apply the change to a single value of a set (e.g. only the X coordinate of an object's Location).
All
   Apply the change to all values in a set (e.g. all coordinates of an object's Location).

.. _bpy.ops.ui.reset_default_button:

Reset to Default Value(s) :kbd:`Backspace`
   Replaces the current value by the default.

Copy Data Path :kbd:`Shift-Ctrl-C`
   Copies the Python property data path, relative to the data-block.
   Useful for Python scripting.

Copy Full Data Path :kbd:`Shift-Ctrl-Alt-C`
   Copies the full Python property data path including any needed context information.

Copy As New Driver
   Creates a new driver using this property as input, and copies it to the clipboard.
   Use *Paste Driver* to add the driver to a different property, or *Paste Driver Variables*
   to extend an existing driver with a new input variable.

Copy To Selected
   Copies the property value to the selected object's corresponding property.
   A use case is if the Properties context is pinned.

Assign Shortcut
   Lets you define a keyboard or mouse shortcut for an operation.
   To define the shortcut you must first move the mouse cursor over the button that pops up.
   When "Press a key" appears you must press and/or click the desired shortcut.
   Press :kbd:`Esc` to cancel.

   .. seealso::

      :doc:`/interface/keymap/introduction`.

Change Shortcut
   Lets you redefine the shortcut.

Remove Shortcut
   Unlinks the existing shortcut.

Online Manual :kbd:`F1`
   Opens an online page of the Blender Manual in a web browser.

Online Python Reference
   Context-sensitive access to
   the `Python API Reference <https://docs.blender.org/api/current/>`__.

Edit Source
   For UI development -- Creates a text data-block with the source code associated with the control,
   in case the control is based on a Python script.
   In the Text Editor it points at the code line where the element is defined.

Edit Translation
   For UI development -- Points at the translation code line.


.. |specials-button| image:: /images/interface_controls_buttons_menus_specials.png
.. _ui-specials-menu:

Specials Menu
=============

The Specials pop-up menu is similar to a context menu, but is opened
using a button consisting of a down arrow on a dark background |specials-button|.


.. _bpy.types.UIPieMenu:

Pie Menus
=========

A pie menu is a menu whose items are spread radially around the mouse.

.. figure:: /images/interface_controls_buttons_menus_pie-menu.png
   :align: center

   The 3D Viewport Mode Pie menu.

.. tip::

   The fastest way to operate a Pie menu is to press down the key(s) that
   invoke the menu, move the mouse slightly towards a selection, and
   release the key(s) to activate the selection.

Releasing the key without moving the mouse will keep the menu open so you
can click the desired item.
If you do move the mouse before releasing, the item closest to the mouse
will be activated instantly.

An open disc widget at the center of the pie menu shows
the current direction of the pie menu. The selected item is also highlighted.
A pie menu will only have a valid direction for item selection
if the mouse is touching or extending beyond the disc widget at the center of the menu.

Pie menu items support key accelerators, which are the letters underlined on each menu item.
Number keys can also be used.

If there are sub-pies available, it is indicated by a plus icon.

.. seealso::

   :ref:`Pie menu settings <prefs-pie-menu>`.
