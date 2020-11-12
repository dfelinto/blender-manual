
***
STL
***

.. admonition:: Reference
   :class: refbox

   :Category:  Import-Export
   :Menu:      :menuselection:`File --> Import/Export --> Stl (.stl)`

This format is useful if you intend to import/export the files for CAD software.
It is also commonly used for loading into 3D printing software.

.. warning::

   Currently the script does not handle importing or exporting of normals
   and does not handle endianness, there is nothing in the STL specification about it.


Properties
==========

Import
------

Transform
^^^^^^^^^

Scale
   TODO.
Scene Unit
   TODO.
Forward / Up Axis
   Since many applications use a different axis for pointing upwards, these are axis conversion for these settings,
   Forward and up axes -- By mapping these to different axes you can convert rotations
   between applications default up and forward axes.

   Blender uses Y forward, Z up (since the front view looks along the +Y direction).
   For example, it is common for applications to use Y as the up axis, in that case -Z forward, Y up is needed.


Geometry
^^^^^^^^

Facet Normals
   TODO.


Export
------

ASCII
   TODO.
Batch Mode
   TODO.


Include
^^^^^^^

Selection Only
   TODO.


Transform
^^^^^^^^^

Scale
   TODO.
Scene Unit
   TODO.
Forward / Up Axis
   Since many applications use a different axis for 'Up', these are axis conversion for these settings,
   Forward and Up axes -- By mapping these to different axes you can convert rotations
   between applications default up and forward axes.

   Blender uses Y Forward, Z Up (since the front view looks along the +Y direction).
   For example, it's common for applications to use Y as the up axis, in that case -Z Forward, Y Up is needed.


Geometry
^^^^^^^^

Apply Modifiers
   TODO.


Usage
=====

Use the operator to import ASCII or binary STL-files, you can select multiple files at once.
For exporting you can select multiple objects and they will be exported as a single STL-file.
You can select between ASCII/binary file format (binary is more compact).
You can also choose to enable or disable the modifiers during the export.
