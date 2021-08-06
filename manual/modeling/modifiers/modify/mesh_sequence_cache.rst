.. index:: Modeling Modifiers; Mesh Sequence Cache Modifier

****************************
Mesh Sequence Cache Modifier
****************************

The Mesh Sequence Cache modifier loads data from :doc:`Alembic </files/import_export/alembic>`
and :doc:`USD </files/import_export/usd>` files.
It supports static meshes, but is mostly used to load animated meshes.
Despite its name, this modifier also supports curves. It also handles file sequences,
as well as meshes and curves with varying topology (like the result of fluid simulations).

When importing an :doc:`Alembic </files/import_export/alembic>` or
:doc:`USD </files/import_export/usd>` file,
Mesh Sequence Cache modifiers are automatically added to time-varying meshes.
For time-varying object transforms (so animation of rotation, location, or scale),
the :ref:`Transform Cache Constraint <bpy.types.TransformCacheConstraint>` is used.
Files other than Alembic or USD, like MDD and PC2 files, can be loaded using
the :doc:`Mesh Cache modifier </modeling/modifiers/modify/mesh_cache>`.


Options
=======

.. figure:: /images/modeling_modifiers_modify_mesh-sequence-cache_panel.png
   :align: right
   :width: 300px

Cache File
   Data-block menu to select the Alembic or USD file.

File Path
   Path to Alembic or USD file.

Sequence
   Whether or not the cache is separated in a series of files.

Override Frame
   Whether to use a custom frame for looking up data in the cache file,
   instead of using the current scene frame.

   The *Frame* value is the time to use for looking up the data in the cache file,
   or to determine which to use in a file sequence.

Frame Offset
   Subtracted from the current frame to use for looking up the data in the cache file,
   or to determine which file to use in a file sequence.

Velocity Attribute
   The name of the Alembic attribute used for generating motion blur data;
   by default, this is ``.velocities`` which is standard for most Alembic files.

   .. note:: The *Velocity Attribute* option is currently for Alembic files only.


Velocity Unit
   Defines how the velocity vectors are interpreted with regard to time.

   Frame
      The velocity unit was encoded in frames and does not need to be scale by scene FPS.
   Second
      The velocity unit was encoded in seconds and needs to be scaled by the scene FPS (1 / FPS).

   .. note:: The *Velocity Unit* option is currently for Alembic files only.

Object Path
   The path to the Alembic or USD object inside the archive or stage.

Read Data
   Type of data to read for a mesh object, respectively: vertices,
   polygons, UV maps and Vertex Color layers.

   Vertices, Faces, UV, Color

Velocity Scale
   Multiplier used to control the magnitude of the velocity vector for time effects such as motion blur.

   .. note:: The *Velocity Scale* option is currently for Alembic files only.
