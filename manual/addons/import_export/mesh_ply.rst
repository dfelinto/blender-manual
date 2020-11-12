
************
Stanford PLY
************

.. admonition:: Reference
   :class: refbox

   :Category:  Import-Export
   :Menu:      :menuselection:`File --> Import/Export --> Stanford (.ply)`

.. warning::

   Only one mesh can be exported at a time.


Properties
==========

Import
------

The import does not have any properties.


Export
------

Include
^^^^^^^

Selection Only
   Todo.


Transform
^^^^^^^^^

Forward / Up
   Since many applications use a different axis for 'Up', these are axis conversion for these settings,
   Forward and Up axes -- By mapping these to different axes you can convert rotations
   between applications default up and forward axes.

   Blender uses Y Forward, Z Up (since the front view looks along the +Y direction).
   For example, its common for applications to use Y as the up axis, in that case -Z Forward, Y Up is needed.

Scale
   TODO.


Geometry
^^^^^^^^

Apply Modifiers
   Todo.
Normals
   Todo.
UVs
   Todo.
Vertex Colors
   Todo.


Usage
=====

Use the operator to import ASCII or binary PLY-files, you can select multiple files at once.
For exporting, you can choose to enable or disable the modifiers during the export
and you can choose which data you want to export (UV textures, vertex colors, ...).
