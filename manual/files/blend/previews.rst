
********************
Blend-Files Previews
********************

A blend-file can store previews, both for itself, and for some of its :doc:`data-blocks </files/data_blocks>`.
You can disable writing any previews when saving a blend-file using the *Save Preview Images* setting
from the :ref:`prefs-save-load` section of the Preferences.


Blend-File Preview
==================

Blender saves by default a small preview of current scene in the blend-file.
This will show in the *Thumbnail* view of the :doc:`File Browser </editors/file_browser>`.

During its installation, Blender also adds a small tool to your OS,
that will allow your system file browser to show those previews as file thumbnails as well.


Data-Blocks Previews
====================

Blender will automatically generate previews for some type of data, mainly the ones related to shading
(like images, textures, materials, lights and world shaders).

It can also store previews for scenes, collections and objects, but those need to be generated manually.

These previews can then be used by the *Thumbnail* view of the File Browser, when linking or appending data-blocks.


.. _bpy.ops.wm.previews_ensure:

Refresh Data-Block Previews
---------------------------

.. reference::

   :Menu:      :menuselection:`File --> Data Previews --> Refresh Data-blocks Previews`

Refresh all data-block previews that can be automatically generated by Blender (shading-related ones),
in the current blend-file. You still need to save the file if you want to write them to the drive.


.. _bpy.ops.wm.previews_batch_generate:

Batch Generate Previews
-----------------------

.. reference::

   :Menu:      :menuselection:`File --> Data Previews --> Batch Generate Previews`

Generate some data-block types' previews (you can choose which in its options),
in one or more blend-files on your drive. You should not use this operator on the file currently opened in Blender.

This is currently the only way to generate and store in blend-files previews for scenes, collections and objects.
Note that since this involves a lot of rendering, even of small sizes, the process may take some time to complete.

Scenes
   Generate previews of scenes and their collections.
Collections
   Generate previews of collections of objects.
Objects
   Generate previews of objects.
Materials & Textures
   Generates previews for materials, textures, images, and other internal data.
Trusted Blend Files
   When enabled, Python scripts and drivers that may be included in the file will be run automatically.
   Enable this only if you created the file yourself,
   or you trust that the person who gave it to you did not include any malicious code with it.
   See :doc:`Python Security </advanced/scripting/security>` to configure default trust options.
Save Backups
   Keep a :ref:`backup version <prefs-save_load-backups>` (``blend1-file``)
   of the files when saving with generated previews.


.. _bpy.ops.wm.previews_clear:

Clear Data-Block Previews
-------------------------

.. reference::

   :Menu:      :menuselection:`File --> Data Previews --> Clear Data-blocks Previews`

Clear all, a generic type of, or a specific data-block type of previews in the current blend-file.
You still need to save the file if you want to clear them from the drive.


.. _bpy.ops.wm.previews_batch_clear:

Batch Clear Previews
--------------------

.. reference::

   :Menu:      :menuselection:`File --> Data Previews --> Batch Clear Previews`

Clear some data-block types' previews (you can choose which in its options),
in one or more blend-files on your drive. You should not use this operator on the file currently opened in Blender.

Scenes
   Generate previews of scenes and their collections.
Collections
   Generate previews of collections of objects.
Objects
   Generate previews of objects.
Materials & Textures
   Generates previews for materials, textures, images, and other internal data.
Trusted Blend Files
   When enabled, Python scripts and drivers that may be included in the file will be run automatically.
   Enable this only if you created the file yourself,
   or you trust that the person who gave it to you did not include any malicious code with it.
   See :doc:`Python Security </advanced/scripting/security>` to configure default trust options.
Save Backups
   Keep a :ref:`backup version <prefs-save_load-backups>` (``blend1-file``)
   of the files when saving with generated previews.
