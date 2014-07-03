
The Text Editor
===============

Blender has a :guilabel:`Text Editor` among its windows types, accessible via the :guilabel:`Text Editor` button (

.. figure:: /images/Manual-Part-XV-textButton.jpg


) of the :guilabel:`Window type` menu, or via :kbd:`shift-f11`\ .

The newly opened Text window is grey and empty, with a very simple toolbar (\ *Text Toolbar*\ ).


.. figure:: /images/Manual-Part-XX-Manual-Extensions-Python-Text-editor-Default-Toolbar.jpg

   Text Toolbar.


From left to right there are the standard :guilabel:`Window type` selection button and the
window menus. Then there is the Text ID Block browse button followed by the New button for
creating new Text files. Once you click it, you will find that the Toolbar has changed..
for good!


.. figure:: /images/Manual-Part-XX-Manual-Extensions-Python-Text-editor-Toolbar-with-file-open.jpg
   :width: 600px
   :figwidth: 600px

   Text Toolbar with a file open


Now you find a textbox to change name of your text file,
followed by **+** button to create new files. To remove the text block,
click the **X** button.

The following three buttons toggle display of line numbers,
word-wrap text and syntax  highlighting respectively.

Typing on the keyboard produces text in the text buffer. As usual,
pressing dragging and releasing :kbd:`Lmb` selects text.

The following keyboard commands apply:

- :kbd:`ctrl-C` - Copies the marked text into the text clipboard.
- :kbd:`ctrl-X` - Cuts out the marked text into the text clipboard.
- :kbd:`ctrl-V` - Pastes the text from the clipboard at the cursor location in the Text window.
- :kbd:`shift-ctrl-alt-S` - Saves unsaved text as a text file, a :guilabel:`File Browser` window appears.
- :kbd:`alt-S` - Saves an already open file.
- :kbd:`alt-O` - Loads a text, a :guilabel:`File Browser` window appears.
- :kbd:`alt-P` - Executes the text as a Python script.
- :kbd:`ctrl-Z` - Undo.
- :kbd:`ctrl-shift-Z` - Redo.
- :kbd:`alt-R` - Reopen (reloads) the current buffer (all non-saved modifications are lost).
- :kbd:`alt-M` - Converts the content of the text window into 3D text (max 100 chars).

To delete a text buffer just press the :guilabel:`X` button next to the buffer's name,
just as you do for materials, etc.

The most notable keystroke is :kbd:`alt-P` which makes the content of the buffer being parsed by the internal Python interpreter built into Blender. The next page will present an example of Python scripting. Before going on it is worth noticing that Blender comes with a fully functional Python interpreter built in, and with a lots of Blender-specific modules, as described in the :doc:`API references <extensions/python/references>`\ .

The :guilabel:`Text Editor` has now also some dedicated Python scripts,
which add some useful writing tools, like a class/function/variable browser, completion… You
can access them through the :guilabel:`Text` → :guilabel:`Text Plugins` menu entry.


Other usages for the Text window
--------------------------------

The text window is handy also when you want to share your .
blend files with the community or with your friends. A Text window can be used to write in a
README text explaining the contents of your blender file.
Much more handy than having it on a separate application. Be sure to keep it visible when
saving! If you are sharing the file with the community and you want to share it under some
license you can write the license in a text window.


Demonstration
=============


FIXME(Tag Unsupported:youtube;
<youtube>OzGZ_ssrmsQ</youtube>
)


Exercise
========


Copy the text below in the Text Editor.

::


   import bpy
   from math import radians, cos, sin

   # An object can exist in 20 layers,
   # so the following code determines on which layers you want it to be

   # Get the cursor's location
   cursor = bpy.context.scene.cursor_location

   # Radius of the circle
   radius = 5

   # Space the cubes around the circle. Default is 36 degrees apart
   # Get a list of angles converted to radians

   anglesInRadians = [radians(degree) for degree in range(0, 360, 36)]

   # Loop through the angles, determine x,y using polar coordinates
   # and create object
   for theta in anglesInRadians:
   x = cursor.x + radius * cos(theta)
   y = cursor.y + radius * sin(theta)
   z = cursor.z
   bpy.ops.mesh.primitive_cube_add(location=(x, y, z))


Execute the script with :kbd:`ALT-P`\ .

You can see the result of running the above script in this video.


FIXME(Tag Unsupported:youtube;
<youtube>pPR9Eog0S3E</youtube>
)

