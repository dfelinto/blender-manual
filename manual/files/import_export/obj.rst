
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

Animation
^^^^^^^^^

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
Apply Modifiers
   Export objects using the evaluated mesh, meaning the resulting mesh after all
   :doc:`Modifiers </modeling/modifiers/index>` have been calculated.
Properties
   For properties that have different settings for the viewport/final render pick which is used for output.
   One example where this is important is the :doc:`/modeling/modifiers/generate/subdivision_surface`.

   :Viewport: Use viewport properties.
   :Render: Use final render properties.
Path Mode
   When referencing paths in exported files you may want some control as to the method used since absolute paths
   may only be correct on your own system. Relative paths, on the other hand, are more portable
   but mean that you have to keep your files grouped when moving about on your local file system.
   In some cases, the path doesn't matter since the target application will search
   a set of predefined paths anyway so you have the option to strip the path too.

   :Auto: Uses relative paths for files which are in a subdirectory of the exported location,
          absolute for any directories outside that.
   :Absolute: Uses full paths.
   :Relative: Uses relative paths in every case (except when on a different drive on Windows).
   :Match: Uses relative / absolute paths based on the paths used in Blender.
   :Strip Path: Only write the filename and omit the path component.
   :Copy: Copy the file on exporting and reference it with a relative path.


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
   Generate an OBJ group for each part of a geometry using a different material.
Vertex Groups
   Export the name of the vertex group of a face.
   It is approximated by choosing the vertex group with the most members among the vertices of a face.
Smooth Groups
   Write Blender's sharp edges as smooth groups.
Bitflag Groups
   Generate Bitflags for smooth Groups.


Compatibility
-------------

NURBS surfaces, text3D and metaballs are converted to meshes at export time.


.. _bpy.ops.wm.obj_import:

Importing
=========

Import geometry and curves to the OBJ format.

If there is a matching ``.MTL`` for the OBJ then its materials will be imported too.

.. note::

   Blender now only supports complex node-based shading. OBJ having a fixed pipeline-like support of materials,
   this add-on uses the :doc:`generic wrapper </addons/import_export/node_shaders_info>`
   featured by Blender to convert between both.


Properties
----------

Transform
^^^^^^^^^

Clamp Bounding Box
   OBJ-files often vary greatly in scale, this setting clamps the imported file to a fixed size.
Axis Forward, Up
   Since many applications use a different axis for 'Up', these are axis conversion for these settings,
   Forward and Up axes -- By mapping these to different axes you can convert rotations
   between applications default up and forward axes.

   Blender uses Y Forward, Z Up (since the front view looks along the +Y direction).
   For example, it's common for applications to use Y as the up axis, in that case -Z Forward, Y Up is needed.


Options
^^^^^^^

Vertex Groups
   Import OBJ groups as vertex groups.
Validate Meshes
   Checks the imported mesh data for errors and corrects them if needed.
   This slows down the importing process but can fix glitches in the imported mesh.
