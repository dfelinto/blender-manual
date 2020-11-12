.. _bpy.types.ConsoleLine:
.. _bpy.types.SpaceConsole:
.. _bpy.ops.console:

**************
Python Console
**************

The Python Console is a quick way to execute commands,
with access to the entire Python API, command history and auto-complete.
The command prompt is typical for Python 3.x,
the interpreter is loaded and is ready to accept commands at the prompt ``>>>``.

The Python Console is a good way to explore the possibilities of Blender built-in Python.
The Python Console can be used to test small bits of Python code which can then be pasted into larger scripts.

.. figure:: /images/editors_python-console_default.png

   Python Console.


Interface
=========

Header Menus
------------

View Menu
^^^^^^^^^

Zoom In / Zoom Out
   Increases/Decreases the font size of the console text.
Move to Previous Word :kbd:`Ctrl-Left`
   Moves the cursor to the beginning of the previous word.
   If the cursor is in the middle of a word, the cursor is moved to the beginning of the current word.
Move to Next Word :kbd:`Ctrl-Right`
   Moves the cursor to the end of the next word.
   If the cursor is in the middle of a word, the cursor is moved to the end of the current word.
Move to Line Begin :kbd:`Home`
   Moves the cursor to the start of the current line.
Move to Line End :kbd:`End`
   Moves the cursor to the end of the current line.


Console Menu
^^^^^^^^^^^^

Clear All
   Refreshes the console giving the view a fresh start.
   Note that command history is not cleared.
Clear Line :kbd:`Shift-Return`.
   Removes everything from the prompt line.
Delete Previous Word :kbd:`Ctrl-Backspace`
   Deletes everything between the cursor and the beginning of the previous word (separated by periods).
   If the cursor is in the middle of a word, deletes everything to the beginning of the current word.
Delete Next Word :kbd:`Ctrl-Delete`
   Deletes everything between the cursor and the end of the next word.
   If the cursor is in the middle of a word, deletes everything to the end of the current word.
Copy as Script :kbd:`Shift-Ctrl-C`
   Copies the full history buffer to the clipboard,
   this can be pasted into a text file to be used as a Python script.
Copy :kbd:`Ctrl-C`
   Copy the selection.
Paste :kbd:`Ctrl-V`
   Paste into the command line.
Indent :kbd:`Tab`
   Inserts a tab character at the cursor.
Unindent :kbd:`Shift-Tab`
   Unindents the selection.
Backward in History :kbd:`Up`
   Changes the current command to previous command as they appear in the command history.
Forward in History :kbd:`Down`
   Changes the current command to next command as they appear in the command history.
Autocomplete :kbd:`Tab`
   See `Auto Completion`_ for more information.


Main View
---------

.. rubric:: Key Bindings

- :kbd:`Left` / :kbd:`Right` -- Cursor motion.
- :kbd:`Ctrl-Left` / :kbd:`Ctrl-Right` -- Cursor motion, by word.
- :kbd:`Backspace` / :kbd:`Delete` -- Erase characters.
- :kbd:`Ctrl-Backspace` / :kbd:`Ctrl-Delete` -- Erase words.
- :kbd:`Return` -- Execute command.
- :kbd:`Shift-Return` -- Add to command history without executing.


Usage
=====

Aliases
-------

Some variables and modules are available for convenience:

- ``C``: Quick access to ``bpy.context``.
- ``D``: Quick access to ``bpy.data``.
- ``bpy``: Top level Blender Python API module.


First Look at the Console Environment
-------------------------------------

To check what is loaded into the interpreter environment, type ``dir()``
at the prompt and execute it.

.. figure:: /images/editors_python-console_dir.png


.. _bpy.ops.console.autocomplete:

Auto Completion
---------------

Now, type ``bpy.`` and then press :kbd:`Tab` and you will see the Console
auto-complete feature in action.

.. figure:: /images/editors_python-console_completion.png

You will notice that a list of submodules inside of ``bpy`` appear. These modules encapsulate all
that we can do with Blender Python API and are very powerful tools.

Lets list all the contents of ``bpy.app`` module.

Notice the green output above the prompt where you enabled auto-completion.
What you see is the result of auto completion listing.
In the above listing all are module attributed names,
but if you see any name end with ``(``, then that is a function.

We will make use of this a lot to help our learning the API faster.
Now that you got a hang of this, lets proceed to investigate some of modules in ``bpy``.


Before Tinkering with the Modules
---------------------------------

If you look at the 3D Viewport in the default Blender scene,
you will notice three objects: Cube, Light and Camera.

- All objects exist in a context and there can be various modes under which they are operated upon.
- At any instance, only one object is active and there can be more than one selected object.
- All objects are data in the blend-file.
- There are operators/functions that create and modify these objects.

For all the scenarios listed above (not all were listed, mind you...)
the ``bpy`` module provides functionality to access and modify data.


Examples
========

bpy.context
-----------

.. note::

   For the commands below to show the proper output, make sure you have selected object(s) in the 3D Viewport.

.. figure:: /images/editors_python-console_bpy-context.png

``bpy.context.mode``
   Will print the current 3D Viewport mode (Object, Edit, Sculpt, etc.).

``bpy.context.object`` or ``bpy.context.active_object``
   Will give you access to the active object in the 3D Viewport.

Change the X location to a value of 1::

   bpy.context.object.location.x = 1

Move the object from previous X location by 0.5 unit::

   bpy.context.object.location.x += 0.5

Change the X, Y, Z location::

   bpy.context.object.location = (1, 2, 3)

Change only the X, Y components::

   bpy.context.object.location.xy = (1, 2)

The data type of object's location::

   type(bpy.context.object.location)

Now that is a lot of data that you have access to::

   dir(bpy.context.object.location)

``bpy.context.selected_objects``
   Will give access to a list of all selected objects.

Type this and then press :kbd:`Tab`::

   bpy.context.selected_objects

To print out the name of first object in the list::

   bpy.context.selected_objects[0]

The complex one... But this prints a list of objects not including the active object::

   [obj for obj in bpy.context.selected_objects if obj != bpy.context.object]


bpy.data
--------

``bpy.data`` has functions and attributes that give you access to all the data in the blend-file.

You can access following data in the current blend-file:
objects, meshes, materials, textures, scenes, screens, sounds, scripts, etc.

That is a lot of data.

.. figure:: /images/editors_python-console_bpy-data.png


bpy.ops
-------

The tool system is built around the concept of operators.
Operators are typically executed from buttons or menus but can be called directly from Python too.

See the `bpy.ops <https://docs.blender.org/api/current/bpy.ops.html>`__
API documentation for a list of all operators.
