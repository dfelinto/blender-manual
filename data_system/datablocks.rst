
..    TODO/Review: {{review|partial=X|text = elaborate, rna}} .


Datablocks
==========

The base unit for any blender project is the datablock. Examples of datablocks include:
meshes, objects, materials and textures. Be it a simple sphere floating over a plane,
or a full featured film, a project is defined by the datablocks it contains,
the properties set for those datablocks, and the way the datablocks link to each other.
Datablocks can reside within as many .blend files as needed for good project organization.


.. figure:: /images/Doc26-datablocks.jpg
   :width: 400px
   :figwidth: 400px

   Datablocks view


Types of Datablocks:

- RNA
- Filename
- File Has Unsaved Changes
- File is Saved
- Cameras
- Scenes
- Objects
- Materials
- Node Groups
- Meshes
- Lamps
- Libraries
- Screens
- Window Managers
- Images
- Lattices
- Curves
- Metaballs
- Vector Fonts
- Textures
- Brushes
- Worlds
- Groups
- Shape Keys
- Scripts
- Texts
- Speakers
- Sounds
- Armatures
- Actions
- Particles
- Grease Pencil
- Movie Clips
- Masks


Copying and Linking Datablocks
------------------------------

It is possible to copy or link any type of datablock.


To copy a :guilabel:`Scene` datablock,
use :guilabel:`Scene` list found in the header of :guilabel:`User Preferences` window.
The list is to the right of the menus and window workspace list.
Select :guilabel:`ADD NEW` to make a copy of the current scene.
Select :guilabel:`Full Copy` from the list that opened to make a copy.
The current scene will be **fully** copied to the new scene.

Instead of copying **everything**,
you can link datablocks by selecting :guilabel:`Link Objects`,
to use the same :guilabel:`Object` datablocks linked into the two scenes,
or :guilabel:`Link ObData`,
to create separated objects sharing the same :guilabel:`ObData` datablocks (meshes, curves,
materials, etc.). Note that if you select :guilabel:`Link Objects`,
in fact you copy nearly nothing,
as :guilabel:`Object` datablocks are parent of all :guilabel:`ObData` datablocks:
nearly all modifications (object location, mesh geometry, …)
in a scene will be reflected in the other ones linked this way as well.
As for :guilabel:`Link ObData`, it creates a "real" copy of the objects,
but not of their child datalocks: the locations,
scales and rotations of the objects will be specific to a scene,
but neither their forms nor their materials, textures, …, will be
(as defined by :guilabel:`ObData` datablocks).


Copying and Linking Object Datablocks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Full copy
   :kbd:`shift-D` is used to make normal copy of the selected objects.
   The object and some of it's child datablocks will really be duplicated, the other children are just linked; you can define the attributes to be duplicated in :guilabel:`User Preferences` → :guilabel:`Edit Methods`, button group :guilabel:`Duplicate with object:`.

Linked copy
   :kbd:`alt-D` makes a linked copy.
   All datablocks but the object one are linked.


Copying and Linking other Datablocks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When an :guilabel:`ObData` datablock is used (linked) by more than one object,
a small button with its number of linked objects (users) shows up next to its name,
in its settings window (:guilabel:`Editing` context for meshes, curves, cameras, …,
:guilabel:`Shading` context, :guilabel:`Material` sub-context for materials, etc.).
If you click on it, you create a copy of this datablock for the current object.


Unlinked Datablocks
-------------------

A datablock can become unlinked.
For example a material datablock will be unlinked if the object it was linked to is deleted.
If a datablock is unlinked, by default it will be deleted from the .
blend file when Blender is closed. To keep an unlinked datablock in a .blend file,
click the "F" button to the right of the object's name in the Objects and Links panel.


