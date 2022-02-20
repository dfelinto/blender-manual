
*************
Wavefront OBJ
*************

.. reference::

   :Category:  Import-Export
   :Menu:      :menuselection:`File --> Import/Export --> Wavefront (.obj)`

OBJ is a widely used de facto standard in the 3D industry.
The OBJ format is a popular plain text format, however, it has only basic geometry and material support.

- Mesh: vertices, faces, edges, normals, UVs
- Separation by groups/objects
- Materials/textures
- NURBS curves and surfaces

.. note::

   There is no support for mesh vertex colors, armatures, animation,
   lights, cameras, empty objects, parenting, or transformations.

.. note::

   Blender now only supports complex node-based shading. OBJ having a fixed pipeline-like support of materials,
   this add-on uses the :doc:`generic wrapper </addons/import_export/node_shaders_info>`
   featured by Blender to convert between both.


Usage
=====

Import/Export geometry and curves to the OBJ format.

If there is a matching ``.MTL`` for the OBJ then its materials will be imported too.


.. _bpy.ops.wm.obj_export:

Exporting
=========

Properties
----------

Animatioon
^^^^^^^^^^

Animation
   Exports a numbered OBJ for each frame from the start to the end frame.
   Please be aware that this can take quite a long time.
Frame Start, End
   Todo.


Object Properties
^^^^^^^^^^^^^^^^^

Axis Forward, Up
   Since many applications use a different axis for 'Up', there are axis conversion settings,
   Forward and Up axis -- By mapping these to different axis you can convert rotations
   between applications default up and forward axis.

   Blender uses Y Forward, Z Up (since the front view looks along the +Y direction).
   For example, its common for applications to use Y as the up axis, in that case -Z Forward, Y Up is needed.
Scale
   Global scale to use on export.
Selected Only
   Only export the selected objects. Otherwise export all objects in the scene.
Properties
   Todo.

   :Viewport (Default): todo.
   :Render: todo.


Geometry Export
^^^^^^^^^^^^^^^

UV Coordinates
   Write out the active UV layers coordinates from Blender.
Normals
   Write out Blender's face and vertex normals (depending on the faces smooth setting).

   Mostly this isn't needed since most applications will calculate their
   own normals but to match Blender's normal map textures you will need to write these too.
Materials
   Write out the MTL-file along with the OBJ. Most importers that support OBJ will also read the MTL-file.
Triangulated Mesh
   Write out quads as two triangles. Some programs only have very basic OBJ support and only support triangles.
Curves as NURBS
   Write out NURBS curves as OBJ NURBS rather than converting to geometry.


Grouping
^^^^^^^^

Object Groups
   Write out each Blender object as an OBJ object.

   .. note::

      Note that as far as Blender is concerned there is no difference between OBJ Groups and Objects,
      this option is only included for applications that treat them differently.
Material Groups
   Create OBJ groups per material.
Vertex Groups
   Todo.
Smooth Groups
   Write Blender's sharp edges as smooth groups.
Bitflag Groups
   Todo.


Importing
=========

Importing OBJ-files is currently handled by a python importer which is included as an addon.
It's documentation can be found here: `OBJ Importer </addons/import_export/scene_obj>`.


Compatibility
=============

NURBS surfaces, text3D and metaballs are converted to meshes at export time.

Some of the following features are missing:

- NURBS Surfaces -- this could be added but is not widely used.
- Advanced Material Settings -- There are material options documented
  but very few files use them and there are few examples available.
