
***
STL
***

.. reference::

   :Category:  Import-Export
   :Menu:      :menuselection:`File --> Import/Export --> Stl (.stl) (experimental)`

.. note::

   This is the experimental STL importer designed to replace the much slower
   :doc:`STL Importer Add-on </addons/import_export/mesh_stl>`

The STL-file format is useful if you intend to import/export the files for CAD software.
It is also commonly used for loading into 3D printing software.


.. _bpy.ops.wm.stl_import:

Importing
=========

Properties
----------

Scale
   Value by which to scale the imported objects in relation to the world's origin.

Scene Unit
   Apply current scene's unit (as defined by unit scale) to imported data.

Facet Normals
   Use (import) facet normals (note that this will still give flat shading).

Forward / Up Axis
   Since many applications use a different axis for pointing upwards, these are axis conversion for these settings,
   Forward and up axes -- By mapping these to different axes you can convert rotations
   between applications default up and forward axes.

   Blender uses Y forward, Z up (since the front view looks along the +Y direction).
   For example, it is common for applications to use Y as the up axis, in that case -Z forward, Y up is needed.

Validate Mesh
   Check the imported mesh for corrupt data and fix it if necessary.
   This option will make the importing slower but is often not necessary.


Exporting
=========

In order to export STL-files you must currently use the :doc:`STL Add-on </addons/import_export/mesh_stl>`.
