
****************
Material Library
****************

Materials Library VX is a Blender add-on that will create a material library.
You can save, load and categorize materials that can be shared across all your projects.
This version uses a blend-file as database so all external render engines,
all node materials and textures are supported. It also makes use of Blender compression.

.. seealso::

   Please see `author's site <https://sites.google.com/site/aleonserra/home/scripts/matlib-vx-5-6>`__
   for the older original docs.


Activation
==========

- Open Blender and go to Preferences then the Add-ons tab.
- Click Material then Material Library VX to enable the script.

Add-ons Preferences
   Once the add-on is enabled you can open the preferences and
   choose to set a path to use your own materials in the library.


Interface
=========

Located in the :menuselection:`Properties --> Materials --> Material Library VX`.

.. figure:: /images/addons_materials_material-library_ui.jpg
   :align: right
   :width: 330px


Instructions
============

It's advisable to add a :term:`Fake User` to your materials and
to save your blend-file before use.

New Library ``+``
   Create a new Library and name it. The new library will have one material to start.

Add to Library ``+``
   Add your materials to the library.

Apply to Selected (material icon)
   Select a material in the list and apply it to the active object.

Reload Material (circular arrows icon)
   Restore the saved version of the material if you want to revert edits.

Preview Material (palette icon)
   Display the material in the materials *Preview* panel before adding it to the object.

Remove Preview (ghost icon)
   Restore the *Preview* panel.

Remove Material ``-``
   Delete the active material from the Matlib VX list and your library.

Settings (wrench icon)
   Extend the interface for some extra options.

Search
   Search the library for a material.

Category Tools:
   Here you can make sub categories.

   Filter (funnel icon)
      Apply the current filter.
   Set Type (up arrow icon)
      Apply the current selected category to the current material library.
   Add ``+``
      Add a new category.
   Remove ``-``
      Remove the current selected category from the list.


.. reference::

   :Category:  Material
   :Description: Materials Library VX system for library creation.
   :Location: :menuselection:`Properties --> Material`
   :File: materials_library_vx folder
   :Author: Mackraken
   :Maintainer: meta-androcto
   :License: GPL
   :Support Level: Community
   :Note: This add-on is bundled with Blender.
