
*******
Editing
*******

.. _editors-outliner-editing-context_menu:

Context Menu
============

Show the context menu for a data-block with :kbd:`RMB` on the icon or name.
Depending on the type of the preselected data-block(s), you will have all or part of the following options:

Copy/Paste
   Copy/pastes selected data-blocks.

.. _bpy.ops.outliner.delete:

Delete
   Deletes the selected data-block.

Select, Select Hierarchy, Deselect
   Add object to current selection without making it the active one.


.. _editors-outliner-editing-collections:

Collections
-----------

Collections are a way Blender uses to organize scenes.
Collections contain objects and everything else in a scene.
They can include collections themselves and are fully recursive.

.. seealso::

   Read more about :doc:`Collections </scene_layout/collections/index>`.

.. _bpy.ops.outliner.collection_new:

New
   Creates a new collection.

.. _bpy.ops.outliner.collection_duplicate:

Duplicate Collections
   Recursively duplicates the collection including all child collections, objects, and object data.

.. _bpy.ops.outliner.collection_duplicate_linked:

Duplicate Linked
   Duplicate entire hierarchy keeping content linked with original.

Delete Hierarchy
   Deletes the collection and removes all its child objects or collections.
   It is important to note that this only deletes the collection,
   if child objects are part of another collection they will stay in the scene collection
   and their data-blocks will not be deleted from the blend-file.

.. _bpy.ops.outliner.collection_instance:

Instance to Scene
   Creates a new :doc:`collection instance </scene_layout/object/properties/instancing/collection>`.

Visibility
   Controls the collection's visibility in the 3D Viewport and the final render.

   .. _bpy.ops.outliner.collection_isolate:

   Isolate
      Hides all collections except the selected collection and any parent collections (if any exist).

   .. _bpy.ops.outliner.collection_show:
   .. _bpy.ops.outliner.collection_hide:

   Show/Hide
      Shows/Hides the selected collection from the :doc:`View Layer </scene_layout/view_layers/index>`.

   .. _bpy.ops.outliner.collection_show_inside:
   .. _bpy.ops.outliner.collection_hide_inside:

   Show/Hide Inside
      Shows/Hides all items that are a member of the selected collection, include child collections,
      from the :doc:`View Layer </scene_layout/view_layers/index>`.

   .. _bpy.ops.outliner.collection_enable:
   .. _bpy.ops.outliner.collection_disable:

   Enable/Disable in Viewports
      Enables/disables drawing in the :doc:`View Layer </scene_layout/view_layers/index>`.

   .. _bpy.ops.outliner.collection_enable_render:
   .. _bpy.ops.outliner.collection_disable_render:

   Enable/Disable in Renders
      Enables/disables visibility of the collection in renders.

View Layer
   Controls the collection's interactions with the :doc:`View Layer </render/layers/layers>`.

   .. _bpy.ops.outliner.collection_exclude_clear:
   .. _bpy.ops.outliner.collection_exclude_set:

   Disable/Enable in View Layer
      Disables/Enables the collection from the view layer.

.. _bpy.ops.outliner.collection_color_tag_set:

Set Color Tag
   Assigns or clears a collection's :ref:`color tag <scene_layout-collections-color-tagging>`
   for the selected collection.

.. _bpy.ops.outliner.id_operation:

ID Data
-------

Unlink
   To unlink a data-block from its "owner" (e.g. a material from its mesh).
Make Local
   To create a "local" duplicate of this data-block.
Make Single User
   This feature is not yet implemented.
Delete
   Deletes the selected data-block.
Add Library Override
   Add a local :doc:`override </files/linked_libraries/library_overrides>` of this linked data-block.
Add Library Override Hierarchy
   Add a local :doc:`override </files/linked_libraries/library_overrides>` of this linked data-block,
   and its hierarchy of dependencies.
Convert Proxy to Override
   Converts the selected :doc:`Proxy </files/linked_libraries/library_proxies>`
   data-block to an :doc:`override </files/linked_libraries/library_overrides>`
   and its hierarchy of dependencies. See also, :ref:`bpy.ops.object.convert_proxy_to_override`.
Reset Library Override
   Reset this local :doc:`override </files/linked_libraries/library_overrides>` to its linked values.
Reset Library Override Hierarchy
   Reset this local :doc:`override </files/linked_libraries/library_overrides>` to its linked values,
   as well as its hierarchy of dependencies. This allows you to update local overrides
   when the relationship between data-blocks changed in the linked library data.
Resync Library Override Hierarchy
   Rebuilds the local :doc:`override </files/linked_libraries/library_overrides>`
   from its linked reference, as well as its hierarchy of dependencies.
Delete Library Override Hierarchy
   Deletes the local :doc:`override </files/linked_libraries/library_overrides>`
   (including its hierarchy of override dependencies) and relinks its users to the linked data-blocks.
Remap Users
   Remap Users of a data-block to another one (of same type of course).
   This means you can e.g. replace all usages of a material or texture by another one.
Copy/Paste
   Copy/pastes selected data-blocks.
Add Fake User, Clear Fake User
   Adds a "dummy" (fake) user so that the selected data-block always gets saved even if it has no users.
   The fake user can be removed with *Clear Fake User*.
Rename :kbd:`F2`
   Renames the selected data-block.
Select Linked
   Selects the linked data, see :ref:`bpy.ops.object.select_linked` for more information.


View
----

The view menu is part of the context menu and supported in all the Outliner elements.

Show Active :kbd:`Period`
   Centers the Tree View to selected object.
Show Hierarchy :kbd:`Home`
   To collapse all levels of the tree.
Show/Hide One Level :kbd:`NumpadPlus`/ :kbd:`NumpadMinus`
   Expand one level down in the tree or collapse one level using the keyboard shortcuts.
