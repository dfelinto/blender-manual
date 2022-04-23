
*************
Wavefront OBJ
*************

.. reference::

   :Category:  Import-Export
   :Menu:      :menuselection:`File --> Import --> Wavefront (.obj)`

OBJ is a widely used de facto standard in the 3D industry.
The OBJ format is a popular plain text format, however, it has only basic geometry and material support.

- Mesh: vertices, faces, edges, normals, UVs
- Separation by groups/objects
- Materials/textures
- NURBS curves and surfaces

.. note::

   There is no support for mesh Color Attributes, armatures, animation,
   lights, cameras, empty objects, parenting, or transformations.

.. note::

   Blender now only supports complex node-based shading. OBJ having a fixed pipeline-like support of materials,
   this add-on uses the :doc:`generic wrapper </addons/import_export/node_shaders_info>`
   featured by Blender to convert between both.

.. warning::

   Importing very large OBJ-files (over a few 100mb), can use a lot of RAM.


Usage
=====

Import geometry and curves to the OBJ format.

If there is a matching ``.MTL`` for the OBJ then its materials will be imported too.


Properties
==========

Import
------

Include
^^^^^^^

Image Search
   This enables a recursive file search if an image file can't be found.
Smooth Groups
   Surround OBJ smooth groups by sharp edges.
   Note that these will only be displayed when the Edge Split modifier is enabled.
Lines
   Import OBJ lines and two-sided faces as mesh edges.


Transform
^^^^^^^^^

Clamp Size
   OBJ-files often vary greatly in scale, this setting clamps the imported file to a fixed size.
Forward / Up
   Since many applications use a different axis for 'Up', these are axis conversion for these settings,
   Forward and Up axes -- By mapping these to different axes you can convert rotations
   between applications default up and forward axes.

   Blender uses Y Forward, Z Up (since the front view looks along the +Y direction).
   For example, it's common for applications to use Y as the up axis, in that case -Z Forward, Y Up is needed.


Geometry
^^^^^^^^

Split/Keep Vertex Order
   When importing an OBJ it's useful to split up the objects into Blender objects,
   named according to the OBJ-file. However, this splitting loses the vertex order
   which is needed when using OBJ-files as morph targets.It also loses any vertices
   that are not connected to a face or edge so this must be disabled if you want to
   keep the vertex order and loose vertices.
Split by Object & Split by Group
   When importing an OBJ it's useful to split up the objects into Blender objects,
   named according to the OBJ-file. However, this splitting loses the vertex order which
   is needed when using OBJ-files as morph targets. It also loses any vertices that
   are not connected to a face, so this must be disabled if you want to keep the vertex order.

   As far as Blender is concerned OBJ Objects and Groups are no difference,
   since they are just two levels of separation,
   the OBJ groups are not equivalent to Blender groups, so both can optionally be used for splitting.


OBJ Export
==========

Exporting OBJ-files is built into Blender without the need of an add-on.
It's documentation can be found here: `OBJ Exporter </files/import_export/obj>`.


Compatibility
=============

Missing
-------

Some of the following features are missing:

- Advanced Material Settings -- There are material options documented
  but very few files use them and there are few examples available.
- Normals -- Blender ignores normals from imported files, recalculating them based on the geometry.
