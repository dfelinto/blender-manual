.. _bpy.types.Collection:
.. _bpy.ops.collection:

***********
Collections
***********

There can be many objects in a scene: A typical stage scene consists of furniture, props,
lights, and backdrops.
Blender helps you keep everything organized by allowing you to group like objects together.
Objects can be grouped together without any kind of transformation relationship (unlike parenting).
Collections are used to just logically organize your scene,
or to facilitate one-step appending or linking between files or across scenes.


Collections Menu
================

.. admonition:: Reference
   :class: refbox

   :Mode:      Object Mode
   :Menu:      :menuselection:`Object --> Collection`
   :Hotkey:    :kbd:`M`, :kbd:`Shift-M`, :kbd:`Ctrl-G`, etc.

Move to Collection :kbd:`M`
   Move selected objects to an existing or new collection.
Link to Collection :kbd:`Shift-M`
   Link selected objects to a collection.
   A new collection can be created in the pop-up.
Create New Collection :kbd:`Ctrl-G`
   Creates a new collection and adds the selected object(s) to it.
   The name of the new collection can be specified in
   the *Create New Collection* :ref:`ui-undo-redo-adjust-last-operation` panel.
   This collection is not linked to the active scene.
Remove from Collection :kbd:`Ctrl-Alt-G`
   Remove the selected objects from a collection. If the object belongs to more than one collection,
   a pop-up lets you select the collection and an option to remove it from all collections.
Remove from All Collections :kbd:`Shift-Ctrl-Alt-G`
   Remove the selected objects from all collections.
Add Selected to Active Collection :kbd:`Shift-Ctrl-G`
   Adds the selected objects to the collections to which the active object belongs.
Remove Selected from Active Collection :kbd:`Shift-Alt-G`
   Causes the selected objects to be removed from the collections to which the active object belongs.


.. _scene-layout_collections_collections_panel:

Collections Panel
=================

.. admonition:: Reference
   :class: refbox

   :Mode:      Object Mode
   :Panel:     :menuselection:`Object tab --> Collections`

.. figure:: /images/scene-layout_collections_collections_panel.png

   Collections panel.

All collections that an object has been assigned to are listed in the Properties
:menuselection:`Object tab --> Collections panel`.

Add to Collection
   Adds the selected object to a collection.
   A pop-up lets you specify the collection to add to.
New ``+``
   Creates a new collection and adds the selected object to it.
Name
   To rename a collection, simply click in the collections name field.
Remove ``X``
   To remove an object from a collection,
   find the name of the collection from which you wish to remove the object,
   and click the ``X`` button to the right of the collection name.
Specials
   Unlink Collection, Select Collection, Set Offset from Cursor
Offset
   Applies a spatial offset of the instanced collections from the original object's origin.

.. seealso:: Appending or Linking Collections

   To append a collection from another blend-file,
   consult :doc:`this page </files/linked_libraries/index>`.
   In summary, :menuselection:`File --> Link/Append Link` Select a blend-file and then the collection.

.. tip:: Selecting Collections

   Collections can be selected, see :ref:`Select Grouped <bpy.ops.object.select_grouped>` for more information.
