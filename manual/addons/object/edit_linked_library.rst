
*******************
Edit Linked Library
*******************

When working in larger projects that involve scenes with assets linked from a blend-file library,
it can get very time-consuming to save your current scene, track down the proper linked blend-file,
make your modifications, save, and return to your original scene file.
This add-on allows you to accomplish this process with only a pair of mouse clicks
(one to get to the linked library and one to resume work on your scene).


Activation
==========

- Open Blender and go to Preferences then the Add-ons tab.
- Click Object then Edit Linked Library to enable the script.


Usage
=====

Select an object that is been linked from a separate blend-file. In the 3D Viewport's Sidebar,
the Edit Linked Library panel will show a button labeled *Edit Linked Library*.
Click this button to open the blend-file that the active object is linked from.

Once you complete your work to the linked file, return to the Sidebar and
click the *Return to Original File* button. In addition,
the :kbd:`Shift-NumpadSlash` hotkey can be used to toggle between the linked file and
the original (the *Local View* functionality is maintained for non-linked objects).

By default, this add-on automatically saves your current file before opening the linked library or
returning to the original file. This can be disabled using the *Autosave* toggle
in the Edit Linked Library panel of the Sidebar.

.. vimeo:: 41440647


.. admonition:: Reference
   :class: refbox

   :Category:  Object
   :Description: Allows editing of objects linked from a blend-file library.
   :Location: :menuselection:`File --> External Data`, :menuselection:`3D Viewport --> Sidebar --> Item tab`
   :File: object_edit_linked.py
   :Author: Jason van Gumster (Fweeb), Bassam Kurdali, Pablo Vazquez, Rainer Trummer
   :License: GPL
   :Note: This add-on is bundled with Blender.
