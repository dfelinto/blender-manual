.. _editors-asset-browser:

*************
Asset Browser
*************

This section describes the *Asset Browser*. For general information on Blender's
asset library system, how to :ref:`create <asset-create>` and :ref:`edit <asset-edit>`
assets, and design choices, see :doc:`/files/asset_libraries/index`.

*The Asset Browser was introduced in Blender 3.0, and will be improved and
expanded over multiple subsequent releases.*

.. _assets-using:

Using Assets
=====================

As a general rule, **an asset can be used by dragging it from the Asset Browser
to the desired location**. Objects and Worlds can be dragged from the asset
browser into the scene, Materials can be dragged onto the object that should use
them. The use of pose assets is described in :ref:`pose-library-using`.

There are several things that can happen when an asset is used, depending on the
**Import Type** configuration of the asset browser:

Link
   *Same as File > Link...*

   The asset will be linked to the current blend file, and thus be read-only.
   Subsequent changes to the asset file will be reflected in all files that link
   it in.

Append
   *Same as File > Append...*

   All of the asset and all its dependencies will be appended to the current
   file. Dragging a material into the scene three times will result in three
   independent copies. Dragging an object into the scene three times will also
   result in three independent copies.

   "Dependencies" in this case means everything the asset refers to. For an
   object, this could be its mesh and materials, but also other objects used by
   modifiers, constraints, or drivers.

   Since the file now has its own copy of the asset, subsequent changes to the
   asset file will not be reflected in the file it's appended to.

Append (Reuse Data)
   *Specific to the asset browser.*

   The first time an asset is used, it will be appended, including its
   dependencies, just like described above. However, Blender will keep track of
   where it came from, and the next time the asset is used, as much data as
   possible will be reused. Dragging a material into the scene three times will
   only load it once, and just assign the same material three times. Dragging an
   object into the scene three times will create three copies of the object, but
   all copies will share their mesh data, materials, etc.

   Since the file now has its own copy of the asset, subsequent changes to the
   asset file will not be reflected in the file it's appended to.


Note that all regular Blender operations are available after the asset has been
added to the current file. For example, you could choose to link an Object to
the scene; this will also link its Mesh and its Materials. Subsequently you can
make the Object itself local (Object > Relations > Make Local... > Selected
Objects), while keeping the Mesh and Materials linked to the asset files. This
will result in a local, and thus editable, Object, and keep the Mesh and
Materials automatically up to date with any changes in the asset library.



Interface
=========

Main Region
-----------

The main region of the Asset Browser acts similar to the :doc:`/editors/file_browser` built into Blender.


Header Region
-------------

The Header Region is above the main region and can aid in navigating and adjust how items are displayed.


Source List Region
------------------

Todo Catalogs.


.. _bpy.types.AssetMetaData:

Asset Details Region
--------------------

Todo.

.. _bpy.types.AssetMetaData.author:

Author
   Name of the creator of the asset.


Preview
^^^^^^^

Todo.

Tags
^^^^

Todo.


Navigating
==========

See file browser...


Selecting
=========

See file browser...


Editing
=======

Todo explain items in the context menu.
