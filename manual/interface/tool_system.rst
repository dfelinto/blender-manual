.. _ui-tool_system:
.. _bpy.ops.wm.tool:

***********
Tool System
***********

Tools are accessed from the :ref:`Toolbar <ui-region-toolbar>`.

This is a general introduction to tools, individual tools have their own documentation.

There can only be one active tool which is stored for each space & mode.

Tools may set their own keys which override other keys
although typically they use the :kbd:`LMB`, sometimes with modifier keys.
*Keymaps can be edited from the preferences.*

Some tools define gizmos (*Shear* and *Spin* for example) to help control the tool.


.. _ui-region-toolbar:

Toolbar
=======

.. admonition:: Reference
   :class: refbox

   :Hotkey:    :kbd:`T`

.. figure:: /images/interface_tool-system_buttons-popup.png
   :align: right

   Button with pop-up menu indicator.

The Toolbar shows buttons for each tool.
For tool buttons which have a small triangle in their bottom right corner, a pop-up menu will be revealed
when you :kbd:`LMB` drag so that you can select other tools of the same group.

Hovering your cursor over a tool for a short time will show its name,
while hovering longer will show the full tooltip.

Resizing the Toolbar horizontally will display the icons with two columns.
Expanding it further will display the icon and its text.


Pop-Up Toolbar
==============

.. admonition:: Reference
   :class: refbox

   :Hotkey:    :kbd:`Shift-Spacebar`

You can switch tools with a toolbar that will pop up at the location of your cursor
after pressing :kbd:`Shift-Spacebar`.
The shortcuts for selecting the tools are displayed on the right.

Alternatively, you can map this action to :kbd:`Spacebar` in the Preferences.
Then you'll be able use :kbd:`Spacebar`
like a modifier key (similar to pressing :kbd:`Ctrl` or :kbd:`Shift`).

:kbd:`Spacebar T` for Transform, :kbd:`Spacebar D` for Annotate,
:kbd:`Spacebar M` for measure, etc.
See :ref:`Spacebar Action <keymap-blender_default-spacebar_action>`.


Quick Favorites
===============

.. admonition:: Reference
   :class: refbox

   :Hotkey:    :kbd:`Q`

The Quick Favorites menu gather your favorite tools.
Any tool or menu can be added to this pop-up menu via the context menu of buttons and menus.


Changing Tools
==============

Pressing :kbd:`Alt` opens a tool prompt, shown in the :doc:`Status Bar </interface/window_system/status_bar>`,
for changing the active tool, pressing :kbd:`Alt` again closes the prompt.

Tools can be changed by pressing the appropriate icon or by pressing :kbd:`Alt`
then pressing the hotkey assigned to the desired tool.


Fallback Tool
-------------

The fallback tool is the default tool in the Toolbar as in the tool at the top of the list.
To switch to this tool use :kbd:`Alt-W` to open a pie menu to choose what the default drag action does.


Cycling Tools
-------------

If you bind a key to a tool which is part of a group, you can enable the *Cycle* option in the keymap editor.
Successive presses will cycle through the tools in that group.


Properties
==========

Tools can have their own settings, which are available from multiple places:

- The :menuselection:`Sidebar --> Tools --> Active Tool` panel.
- The *Active Tool* tab in the Properties.
- The *Tool Settings* region.
