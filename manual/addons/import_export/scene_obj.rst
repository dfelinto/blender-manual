
*************
Wavefront OBJ
*************

.. admonition:: Reference
   :class: refbox

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

.. warning::

   - Importing very large OBJ-files (over a few 100mb), can use a lot of RAM.
   - OBJ's export using Unix line endings ``\n`` even on windows,
     if you open the files in a text editor it must recognize ``\n`` line endings.


Usage
=====

Import/Export geometry and curves to the OBJ format.

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
   named according to the OBJ-file. However, this splitting looses the vertex order which
   is needed when using OBJ-files as morph targets. It also looses any vertices that
   are not connected to a face so this must be disabled if you want to keep the vertex order.
Split by Object & Split by Group
   When importing an OBJ it's useful to split up the objects into Blender objects,
   named according to the OBJ-file. However, this splitting looses the vertex order which
   is needed when using OBJ-files as morph targets. It also looses any vertices that
   are not connected to a face, so this must be disabled if you want to keep the vertex order.

   As far as Blender is concerned OBJ Objects and Groups are no difference,
   since they are just two levels of separation,
   the OBJ groups are not equivalent to Blender groups, so both can optionally be used for splitting.


Export
------

Include
^^^^^^^

Selected Objects
   Only export the selected objects. Otherwise export all objects in the scene.
Objects as OBJ Objects / Groups
   Write out each Blender object as an OBJ object.

   .. note::

      Note that as far as Blender is concerned there is no difference between OBJ Groups and Objects,
      this option is only included for applications which treat them differently.

Material Groups
   Create OBJ groups per material.
Animation
   Exports a numbered OBJ for each frame from the start to the end frame.
   Please be aware that this can take quite a long time.


Transform
^^^^^^^^^

Scale
   Global scale to use on export.
Path Mode
   When referencing paths in exported files you may want some control as to the method used since absolute paths
   may only be correct on you're own system. Relative paths on the other hand are more portable
   but mean you have to keep your files grouped when moving about on your local file system.
   In some cases the path doesn't matter since the target application will search
   a set of predefined paths anyway so you have the option to strip the path too.

   :Auto: Uses relative paths for files which are in a subdirectory of the exported location,
          absolute for any directories outside that.
   :Absolute: Uses full paths.
   :Relative: Uses relative paths in every case (except when on a different drive on windows).
   :Match: Uses relative / absolute paths based on the paths used in Blender.
   :Strip Path: Only write the filename and omit the path component.
   :Copy: Copy the file on exporting and reference it with a relative path.

Forward / Up
   Since many applications use a different axis for 'Up', there are axis conversion there settings,
   Forward and Up axis -- By mapping these to different axis you can convert rotations
   between applications default up and forward axis.

   Blender uses Y Forward, Z Up (since the front view looks along the +Y direction).
   For example, its common for applications to use Y as the up axis, in that case -Z Forward, Y Up is needed.


Geometry
^^^^^^^^

Apply Modifiers
   Export mesh objects as seen in the 3D Viewport with all modifiers applied.
   Mostly you will want this unless you are exporting a subdivision surface cage.
Smooth Groups
   Write Blender's sharp edges as smooth groups.
Bitflag Groups
   Todo.
Write Normals
   Write out Blender's face and vertex normals (depending on the faces smooth setting).

   Mostly this isn't needed since most applications will calculate their
   own normals but to match Blender's normal map textures you will need to write these too.
Include UVs
   Write out the active UV layers coordinates from Blender.
Write Materials
   Write out the MTL-file along with the OBJ. Most importers that support OBJ will also read the MTL-file.
Triangulate Faces
   Write out quads as two triangles. Some programs only have very basic OBJ support and only support triangles.
Curves as NURBS
   Write out NURBS curves as OBJ NURBS rather than converting to geometry.
Polygroups
   Write faces into OBJ groups based on the meshes vertex group.
   Note that this does a best guess since a face's vertices can be in multiple vertex groups.
Keep Vertex Order
   Maintain vertex order on export. This is needed when OBJ is used for morph targets.


Compatibility
=============

NURBS surfaces, text3D and metaballs are converted to meshes at export time.


Missing
-------

Some of the following features are missing:

- NURBS Surfaces -- this could be added but is not widely used.
- Advanced Material Settings -- There are material options documented
  but very few files use them and there are few examples available.
- Normals -- Blender ignores normals from imported files, recalculating them based on the geometry.
