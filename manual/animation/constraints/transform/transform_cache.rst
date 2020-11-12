.. index:: Object Constraints; Transform Cache Constraint
.. _bpy.types.TransformCacheConstraint:

**************************
Transform Cache Constraint
**************************

The *Transform Cache Constraint* is used to stream animations from
:doc:`Alembic </files/import_export/alembic>` made at the transformation matrix level
(for example rigid bodies, or camera movements).

When :doc:`importing an Alembic file </files/import_export/alembic>`,
Transform Cache constraints are automatically added to objects with animated transforms.
For time-varying meshes (so deforming animations),
the :doc:`Mesh Sequence Cache modifier </modeling/modifiers/modify/mesh_sequence_cache>` is used.


Options
=======

.. figure:: /images/animation_constraints_transform_transform-cache_panel.png

   Transform Cache Constraint.

Cache File
   Data-block menu to select the Alembic file.

File Path
   Path to Alembic file.

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

Manual Scale
   Value by which to enlarge or shrink the object with respect to the world's origin.

Velocity Attribute
   The name of the Alembic attribute used for generating motion blur data;
   by default, this is ``.velocities`` which is standard for most Alembic files.

Velocity Unit
   Defines how the velocity vectors are interpreted with regard to time.

   Frame
      The velocity unit was encoded in frames and does not need to be scaled by scene FPS.
   Second
      The velocity unit was encoded in seconds and needs to be scaled by the scene FPS (1 / FPS).

Object Path
   The path to the Alembic object inside the archive.

Influence
   Controls the percentage of affect the constraint has on the object.
   See :ref:`common constraint properties <bpy.types.constraint.influence>` for more information.
