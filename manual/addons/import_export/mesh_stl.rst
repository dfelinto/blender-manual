
***
STL
***

.. reference::

   :Category:  Import-Export
   :Menu:      :menuselection:`File --> Import/Export --> Stl (.stl)`

This format is useful if you intend to import/export the files for CAD software.
It is also commonly used for loading into 3D printing software.

.. warning::

   Currently the script does not handle importing or exporting of normals
   and does not handle endianness, there is nothing in the STL specification about it.


Importing
=========

.. note::

   The STL importer Add-on is deprecated and being replaced with the much faster
   :ref:`Integrated STL Importer <bpy.ops.wm.stl_import>`.


Properties
----------

Transform
^^^^^^^^^

Scale
   Value by which to scale the imported objects in relation to the world's origin.
Scene Unit
   Apply current scene's unit (as defined by unit scale) to imported data.
Forward / Up Axis
   Since many applications use a different axis for pointing upwards, these are axis conversion for these settings,
   Forward and up axes -- By mapping these to different axes you can convert rotations
   between applications default up and forward axes.

   Blender uses Y forward, Z up (since the front view looks along the +Y direction).
   For example, it is common for applications to use Y as the up axis, in that case -Z forward, Y up is needed.


Geometry
^^^^^^^^

Facet Normals
   Use (import) facet normals (note that this will still give flat shading).


Exporting
=========

Properties
----------

ASCII
   TODO.
Batch Mode
   TODO.


Include
^^^^^^^

Selection Only
   When checked, only selected objects are exported.
   Instanced objects, for example collections that are instanced in the scene,
   are considered 'selected' when their instancer is selected.


Transform
^^^^^^^^^

Scale
   Value by which to scale the exported objects in relation to the world's origin.
Scene Unit
   Apply current scene's unit (as defined by unit scale) to exported data.
Forward / Up Axis
   Since many applications use a different axis for 'Up', these are axis conversion for these settings,
   Forward and Up axes -- By mapping these to different axes you can convert rotations
   between applications default up and forward axes.

   Blender uses Y Forward, Z Up (since the front view looks along the +Y direction).
   For example, it's common for applications to use Y as the up axis, in that case -Z Forward, Y Up is needed.


Geometry
^^^^^^^^

Apply Modifiers
   Export objects using the evaluated mesh, meaning the resulting mesh after all
   :doc:`Modifiers </modeling/modifiers/index>` have been calculated.


Usage
=====

Use the operator to import ASCII or binary STL-files, you can select multiple files at once.
For exporting you can select multiple objects and they will be exported as a single STL-file.
You can select between ASCII/binary file format (binary is more compact).
You can also choose to enable or disable the modifiers during the export.
