.. _bpy.ops.export:
.. _bpy.ops.import:

***************************
Importing & Exporting Files
***************************

.. reference::

   :Menu:      :menuselection:`Topbar --> File --> Import/Export`

Sometimes you may want to utilize files that either came from other 2D or 3D software,
or you may want to use the things you have made in Blender and edit them in other software.
Luckily, Blender offers a wide range of file formats (e.g. ABC, USD, OBJ, FBX, PLY, STL, etc.)
that can be used to import and export.

Popular formats are enabled by default, other formats are also supported and distributed with Blender,
these can be enabled in the Preferences through the use of :doc:`Add-ons </editors/preferences/addons>`.

.. toctree::
   :maxdepth: 1

   import_export/alembic.rst
   import_export/collada.rst
   import_export/usd.rst
   import_export/grease_pencil_svg.rst
   import_export/grease_pencil_pdf.rst

.. seealso::

   More information on the add-ons to import/export these file types
   can be found in the :ref:`add-ons section <addons-io>`.
