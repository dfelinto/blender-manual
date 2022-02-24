
*************
Wavefront OBJ
*************

.. reference::

   :Menu:      :menuselection:`File --> Import/Export --> Wavefront (.obj)`

OBJ is a widely used de facto standard in the 3D industry.
The OBJ format is a popular plain text format, however, it has only basic geometry and material support.

.. note::

   There is no support for armatures, lights, cameras, empty objects, parenting, or transformations.
   See `Compatibility`_ for more information.


Usage
=====

Export geometry and curves to the OBJ format.


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
   The first and last frame to export, used to determine the range of exported frames.


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
   For properties that have different settings for the viewport/final render pick which is used for output.
   One example where this is important is the :doc:`/modeling/modifiers/generate/subdivision_surface`.

   :Viewport (Default): Use viewport properties.
   :Render: Use final render properties.


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
   Export the name of the vertex group of a face.
   It is approximated by choosing the vertex group with the most members among the vertices of a face.
Smooth Groups
   Write Blender's sharp edges as smooth groups.
Bitflag Groups
   Generate Bitflags for smooth Groups.


Importing
=========

Importing OBJ-files is currently handled by a python importer which is included as an addon.
It's documentation can be found here: `OBJ Importer </addons/import_export/scene_obj>`.


Compatibility
=============

NURBS surfaces, text3D and metaballs are converted to meshes at export time.
