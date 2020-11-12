
*********
Operators
*********

.. _bpy.ops.wm.operator_cheat_sheet:

Operator Cheat Sheet
====================

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Help --> Operator Cheat Sheet`
   :Context:   Enable :ref:`Developer Extras <prefs-interface-dev-extras>`

Creates a text file in the Text Editor that gives a list of all operators
and their default values in Python syntax, along with the generated docs.
This is a good way to get an overview of all Blender's operators.

.. seealso::

   `Blender's API documentation <https://docs.blender.org/api/current/>`__


System Operators
================

.. _bpy.ops.script.reload:

Reload Scripts
--------------

.. admonition:: Reference
   :class: refbox

   :Mode:      All Modes
   :Menu:      :menuselection:`Topbar --> Blender --> System --> Reload Scripts`
   :Hotkey:    :kbd:`Ctrl-Alt-T`

Reloads all scripts found in the scripts data folder;
any changes that have been made in the Text Editor will be lost!


.. _bpy.ops.wm.memory_statistics:

Memory Statistics
-----------------

.. admonition:: Reference
   :class: refbox

   :Mode:      ``--debug-memory``
   :Menu:      :menuselection:`Topbar --> Blender --> System --> Memory Statistics`

This operator which can be found by searching "Memory Statistics"
with the :doc:`Operator Search </interface/controls/templates/operator_search>`
will print useful information about memory objects, their size and user count.

.. important::

   To fully use this operator run Blender from the console with ``--debug-memory``.


.. _bpy.ops.wm.debug_menu:

Debug Menu
----------

.. admonition:: Reference
   :class: refbox

   :Mode:      All Modes
   :Menu:      :menuselection:`Topbar --> Blender --> System --> Debug Menu`
   :Hotkey:    :kbd:`Ctrl-Alt-D`

This operator brings up a menu to set Blender into a certain debug mode.

See the
`source code <https://developer.blender.org/diffusion/B/browse/master/source/blender/blenkernel/BKE_global.h>`__
for a description of what each value does.

.. tip::

   Developers can search the code for ``G.debug_value`` to find other possible uses for this operator.

.. note::

   Additional debug options are available by launching Blender in debug mode or setting ``bpy.app.debug = True``.


.. _bpy.ops.wm.redraw_timer:

Redraw Timer
------------

.. admonition:: Reference
   :class: refbox

   :Mode:      All Modes
   :Menu:      :menuselection:`Topbar --> Blender --> System --> Redraw Timer`
   :Hotkey:    :kbd:`Ctrl-Alt-T`

This operator brings up a menu with a list of tests
to benchmark UI render times along with undo/redo functions.


.. _bpy.ops.screen.spacedata_cleanup:

Clean-Up Space-Data
-------------------

.. admonition:: Reference
   :class: refbox

   :Mode:      All Modes
   :Menu:      :menuselection:`Topbar --> Blender --> System --> Clean-up Space-data`

Removes unused settings for invisible editors.
