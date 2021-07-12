
******************
Material Utilities
******************

Materials Utilities/Specials is designed to help with batch materials tasks.
The add-on works in either Eevee or Cycles renderers.
Common tasks are available from the :kbd:`Shift-Q` pop-up menu and also the Materials Specials menu.


Activation
==========

- Open Blender and go to Preferences then the Add-ons tab.
- Click Material then Material Utilities to enable the script.

Add-ons Preferences
   Choose the default settings for the add-ons actions here.


Interface
=========

Located in the 3D Viewport :kbd:`Shift-Q` hotkey.

Located in the :menuselection:`Properties --> Materials --> Specials`.

.. figure:: /images/addons_materials_material-utils_example.jpg
   :align: right
   :width: 350px


Instructions
============

Assign Material ``+``
   Assign a material to the current selection. List of all materials and search for a material by name.

Select by Material (magnifying glass icon)
   In Edit or Object Mode you can select based on material.
   Faces with chosen material will become selected.
   All objects with a chosen material will be selected in Object Mode.

Copy Material to Selected (ID icon)
   Copy the material from the active object to selected objects.

Clean Slots (glossy sphere icon)
   Clean Material Slots ``X``
      For all selected objects, removes all empty and unused material slots (not assigned to any polygons).
      Due to Blender's current limitations, available only in Object Mode
      (the option will be grayed out in Edit Mode).
   Remove Active Material Slots ``-``
      Todo.
   Remove All Material Slots ``(X)``
      Removes All material slots of the active object.

Replace Material (overlay icon)
   Replace a material by name. Lets your replace one material by another.
   Optionally for all objects in the blend, otherwise for selected editable objects only.
   An additional option allows you to update object selection, to show which objects were affected and which not.

Set Fake User (shield icon)
   Lets you set all the materials to have a fake user. This is very useful when saving materials for use later.

Change Material Link (chain icon)
   Todo.
Specials (star icon)
   Merge Base Names
      Todo.
   Join by Material
      Todo.
   Set Auto Smooth
      Activate :ref:`Auto Smooth <auto-smooth>`.
   Slot to Top/Slot to Bottom
      Move the slot to top or bottom of the stack.

Further comprehensive documentation can be found in the co-author's
`Github repository <https://github.com/ChrisHinde/MaterialUtilities/blob/master/README.md>`__.


.. reference::

   :Category:  Material
   :Description: Menu of material tools (assign, select...) in the 3D Viewport.
   :Location: 3D Viewport :kbd:`Shift-Q`
   :File: materials_utils folder
   :Author: MichaleW, ChrisHinde
   :Maintainer: MichaleW, ChrisHinde
   :License: GPL 3+
   :Support Level: Community
   :Note: This add-on is bundled with Blender.
