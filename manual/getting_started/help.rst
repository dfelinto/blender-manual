
***********
Help System
***********

Blender has a range of built-in and web-based help options.


Tooltips
========

.. figure:: /images/getting-started_help_tooltip.png

   Tooltip of the Renderer selector in the Info Editor.

When hovering the mouse cursor over a button or setting, after a few instants a tooltip appears.


Elements
--------

The context-sensitive Tooltip might contain some of these elements:

Short Description
   Related details depending on the control.
Shortcut
   A keyboard or mouse shortcut associated to the tool.
Value
   The value of the property.
Library
   Source file of the active object. See also :doc:`/files/linked_libraries/index`.
Disabled (red)
   The reason why the value is not editable.
Python
   When :ref:`Python Tooltips <prefs-interface-tooltips-python>` are enabled,
   a Python expression is displayed for :ref:`scripting <scripting-index>` (usually an operator or property).


.. _help-manual-access:
.. _bpy.ops.wm.doc_view_manual_ui_context:

Context-Sensitive Manual Access
===============================

.. reference::

   :Mode:      All modes
   :Menu:      :menuselection:`Context menu --> Online Manual`
   :Shortcut:  :kbd:`F1`

You may want to access help for a tool or area from within Blender.

To do so; hover the cursor over the tool or button you need help with and
use the keyboard shortcut or context menu item to visit pages of this reference manual from within Blender.
This opens a web page relating to the button under the cursor, supporting both tool and value buttons.

.. note::

   We do not currently have 100% coverage.
   You may see an alert in the info header if a tool does not have a link to the manual.

   Other times, buttons may link to more general sections of the documentation.


.. _help-menu:

Help Menu
=========

Web Links
---------

The first options of this menu provide direct links to Blender-related websites.
The same links can also be found in the :ref:`splash`.

:doc:`Manual </index>`
   This is a link to the Official Blender Manual (which you are now reading).
`Tutorials <https://www.blender.org/support/tutorials>`__
   Multiple tutorials to help you learn to use Blender.
`Support <https://www.blender.org/support>`__
   Links to various sites, providing both community and professional support.

----

`User Communities <https://www.blender.org/community/>`__
   Lists of many different community sites and support venues.
`Developer Community <https://devtalk.blender.org>`__
   Blender's developer forum.

----

`Python API Reference <https://docs.blender.org/api/current/>`__
   Python application programming interface (API)

----

`Report a Bug <https://developer.blender.org/maniphest/task/edit/form/1/>`__
   The Blender Bug Tracker (registration needed).


.. _help-system-info:

Save System Info
----------------

This extracts system information which can be useful for including in bug reports,
inspecting the configuration, or diagnosing problems.

You will be prompted to save a text file called ``system-info.txt``.

It contains the following sections:

Blender
   This section shows you the Blender version, details about the build configuration,
   and the path in which Blender is running.
Python
   The version and path of your Python installation.
Directories
   Paths used for scripts, data files, presets and temporary files.

   Those directories are configured using the :doc:`Preferences </editors/preferences/file_paths>` Editor.
OpenGL
   Shows the OpenGL version, the name of the manufacturer,
   and the capabilities of your hardware and driver.
Enabled Add-Ons
   Lists add-ons currently in use.
