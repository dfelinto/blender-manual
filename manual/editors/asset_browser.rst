.. index:: Editors; Asset Browser

*************
Asset Browser
*************

This section describes the *Asset Browser*, which is the main interface for organizing and using assets.

The Asset Browser was introduced in Blender 3.0, and will be improved and
expanded over multiple upcoming releases.

.. seealso::

   :doc:`/files/asset_libraries/index`
      For general information on Blender's asset library system, including how to
      :ref:`create <asset-create>` and :ref:`edit <asset-edit>` assets, and design choices.

   :doc:`/files/asset_libraries/catalogs`
      For organizing assets.

   :doc:`/animation/armatures/posing/editing/pose_library`
      Build on top of the Asset Browser.


Interface
=========

.. figure:: /images/asset_browser-gold-material.png

   Asset Browser, showing materials in an asset library.


Main Region
-----------

The main region of the Asset Browser acts similar to the :doc:`/editors/file_browser` built into Blender.
It shows the assets contained in the selected catalog.

Click an asset to select and activate it. Box select by dragging :kbd:`LMB` or
extend the selection with :kbd:`Shift-LMB` to select multiple assets.
Every asset has a context menu.


Source List Region
------------------

The Source List region can be used for navigating and `Using Assets`_.

.. _bpy.types.FileAssetSelectParams.asset_library_ref:

Library
   Shows the active :doc:`asset library </files/asset_libraries/index>`,
   and allows switching between asset libraries.
   The library ":ref:`Current File <asset-library-current-file>`" is special,
   and will always show the assets from the current blend-file,
   regardless of whether it is part of an asset library or not.

.. _bpy.ops.asset.bundle_install:

Copy Asset Bundle to Library
   Shown when the Library selector is set to Current File,
   the current blend-file file is considered an :ref:`Asset Bundle <asset-bundles>`,
   and is not yet located inside any asset library.

   The Copy Asset Bundle operator makes it simple to copy the file into the asset library.
   The catalogs of the asset bundle will be merged into the asset library.

Catalog
   Tree view that shows the :doc:`catalogs </files/asset_libraries/catalogs>` of the active asset library.

   Catalogs can be renamed by double clicking on there name.
   Catalogs can also be nested inside others by dragging and dropping one catalog into another.

Add-ons and features like the :doc:`/animation/armatures/posing/editing/pose_library`
can show custom panels here.


.. _bpy.types.AssetMetaData:
.. _editing-asset-metadata:

Asset Details Region
--------------------

The Asset Details region on the right shows metadata of the active asset.
**Only metadata of assets contained in the current blend-file can be edited**.

Name
   The asset data-block name. This name is unique for the asset data type within
   the same blend-file.

.. _bpy.types.WindowManager.asset_path_dummy:

Source
   The full path of the blend-file that contains the asset.

   .. _bpy.ops.asset.open_containing_blend_file:

   Open Blend File
      This button will start a new Blender instance and open the blend-file that contains the asset.
      In the background Blender will keep monitoring that new Blender instance;
      when it is quit, the Asset Browser will be refreshed to show any updated assets.

.. _bpy.types.AssetMetaData.description:

Description
   Optional field for the asset description. Not used by Blender itself.

.. _bpy.types.AssetMetaData.author:

Author
   Optional field for the asset author. Not used by Blender itself.


Preview
^^^^^^^

Shows the preview image of the asset. See :ref:`asset-previews`.

.. _bpy.ops.ed.lib_id_load_custom_preview:

Load Custom Preview
   Opens a window with the File Browser to select an image for the asset preview.

.. _bpy.ops.ed.lib_id_generate_preview:

Generate Preview
   Generate/update a preview for the asset.

Preview
   Menu of additional preview operators.

   .. _bpy.ops.ed.lib_id_generate_preview_from_object:

   Render Active Object
      Generates a preview by based on the 3D Viewport's :term:`Active` object.
      This is useful for node groups, particularly for geometry nodes,
      which cannot automatically generate their own preview.


.. _bpy.ops.asset.tag_add:
.. _bpy.ops.asset.tag_remove:
.. _bpy.types.AssetMetaData.active_tag:

Tags
^^^^

Panel for viewing and editing asset tags.
These do not have any meaning to Blender, and can be chosen freely.
When using the search field to filter the assets, those assets whose tags (partially) match
the search term will also be shown.

.. note::

   Depending on the current mode of the object and the selected asset types, more panels may be shown.
   For example, see :doc:`/animation/armatures/posing/editing/pose_library`.


.. _assets-using:

Using Assets
============

As a general rule, **an asset can be used by dragging it from the Asset Browser to the desired location**.
Objects and worlds can be dragged from the Asset Browser into the scene,
Materials can be dragged onto the object that should use them.
The use of pose assets is different, and is described in :doc:`/animation/armatures/posing/editing/pose_library`.

There are several things that can happen when an asset is used,
depending on the **Import Type** configuration of the Asset Browser:

Link
   *Same as* :menuselection:`File --> Link...`

   The asset will be linked to the current blend-file, and thus be read-only.
   Later changes to the asset file will be reflected in all files that link it in.

Append
   *Same as* :menuselection:`File --> Append...`

   All of the asset and all its dependencies will be appended to the current file.
   Dragging a material into the scene three times will result in three independent copies.
   Dragging an object into the scene three times will also result in three independent copies.

   "Dependencies" in this case means everything the asset refers to.
   For an object, this can be its mesh and materials, but also other objects
   used by modifiers, constraints, or drivers.

   Since the file now has its own copy of the asset, later changes to
   the asset file will not be reflected in the file it's appended to.

Append (Reuse Data)
   *Specific to the Asset Browser*.

   The first time an asset is used, it will be appended, including its dependencies,
   just like described previously. However, Blender will keep track of where it originated,
   and the next time the asset is used, as much data as possible will be reused.
   Dragging a material into the scene three times will only load it once,
   and just assign the same material three times.
   Dragging an object into the scene three times will create three copies of the object,
   but all copies will share their mesh data, materials, etc.

   Since the file now has its own copy of the asset, later changes to
   the asset file will not be reflected in the file it's appended to.

Instancing Collections
   *Mimics the Instance Collections option when* :ref:`appending from the file browser <bpy.ops.wm.append>`

   Some asset types such as collections can be created as an instanced collection.
   This is done by enabling the *Instance* option after dragging collection assets into the 3D Viewport.
   By enabling this option an empty object is added that uses an instance of the collection.
   If this option is disabled then the full collection hierarchy will be added to the scene.

   Collection Assets from the current file will always be instanced.


Note that all regular Blender operations are available after the asset has been added to the current file.
For example, you could choose to link an object to the scene; this will also link its mesh and its materials.
Then you can make the object itself local
(:menuselection:`Object --> Relations --> Make Local... --> Selected Objects`),
while keeping the mesh and materials linked to the asset files. This will result in a local,
and thus editable, object, and keep the mesh and materials automatically up to date with
any changes in the asset library.


.. _asset-previews:

Asset Previews
==============

.. figure:: /images/asset-browser-preview-panel.png
   :align: right

   Preview panel in the Asset Browser.

Preview images are typically automatically generated when you
:ref:`mark a data-block as asset <bpy.ops.asset.mark>`. The auto-generated
preview tries to capture the object from the front. However this only works if
the geometry is laid out so that it matches what Blender considers to be the
front. That is, the geometry that should be the front needs to point down the -Y
axis of the object. The rotation may have to be applied to get the expected
result. Collection assets use the global -Y  axis as the front (instead of the
local one, as collections themselves don't have a rotation).

It's also possible to load image files from drive, to replace the auto-generated previews.

For previews of pose assets, see :ref:`poselib-preview-images`.


.. _asset-bundles:

Asset Bundles
=============

*Asset bundles* are blend-files that do not reference any other file,
and whose name ends in ``_bundle.blend``. Any textures and other external
files need to be :doc:`packed </files/blend/packed_data>` into the current blend-file.

Asset bundles can be copied to an asset library via the :ref:`Asset Browser <bpy.ops.asset.bundle_install>`:

- Open the asset bundle blend-file.
- Switch its Asset Browser to *Current File* (if it's not set at that already).
- Click on *Copy Bundle to Asset Library*.
- Choose the asset library to copy it to.
- A File Browser will open, showing the files of the selected asset library.
  Choose the desired location of the blend-file, and click the *Copy to Asset Library* button.
- The blend-file will be saved at the chosen location, and any :doc:`catalogs </files/asset_libraries/catalogs>` of
  the asset bundle will be merged into the target asset library.

.. note::

   Both the word "asset" and the word "bundle" are commonly used,
   and not necessarily with the same meaning as described here.
   Not everything that's presented as an "asset bundle" will have
   the *Copy to Asset Library* functionality available; for that,
   the bundle file needs to adhere to the definition above.
