
***************************
Universal Scene Description
***************************

Universal Scene Description (USD) files can contain complex layering, overriding,
and references to other files. Blender's USD Exporter takes a much simpler approach.
When exporting, all visible, supported objects in the scene are exported, optionally limited by their selection state.
Blender does not (yet) support exporting invisible objects, USD layers, variants, skeletal animation, etc.

The following objects can be exported to USD:

- Meshes (of different kinds, see below).
- Cameras (perspective cameras only at the moment, not orthogonal ones).
- Light (all types except area lights).
- Hair (exported as curves, and limited to parent strands).

When exporting an animation, the final, evaluated mesh is written to USD.
This means that the following meshes can be exported:

- Static meshes.
- Deforming meshes; here the topology of the mesh does not change,
  but the locations of the vertices change over time. Examples are animated characters or
  bouncing (but not cracking) objects.
- Arbitrarily animated meshes; here the topology does change.
  An example is the result of a fluid simulation, where splashes of fluid can break off the main body.
- Metaballs are exported as animated meshes.

.. figure:: /images/files_import-export_usd_example.png

   Shot from `Spring <https://cloud.blender.org/p/spring/>`__ exported to USD and opened in USDView.


.. _bpy.ops.wm.usd_export:

Export Options
==============

The following options are available when exporting to USD:

Selection Only
   When checked, only selected objects are exported.
   Instanced objects, for example collections that are instanced in the scene,
   are considered 'selected' when their instancer is selected.

Visible Only
   Only exports objects that are not :doc:`hidden </scene_layout/object/editing/show_hide>`.
   Invisible parents of exported objects are exported as empty transforms.

Animation
   When checked, the entire scene frame range is exported.
   When unchecked, only the current scene frame is exported.

Hair
   When checked, parent hair strands are exported as a curve system.
   Hair strand colors are not exported.

UV Maps
   When checked, includes UV coordinates for exported meshes.
   The name of the UV map in USD is the same as the name in Blender.
   In USD the default name is ``st`` whereas in Blender the default name is ``UVMap``.
   To export to the standard UV map name ``st``, rename the UV map in Blender to ``st``.

Normals
   When checked, includes normals for exported meshes. This includes custom loop normals.

Materials
   When checked, exports the viewport materials of meshes.
   When a mesh has multiple materials assigned, a geometry subset is created for each material.

   The first material (if any) is always applied to the mesh itself as well
   (regardless of the existence of geometry subsets),
   because the Hydra viewport does not support materials on subsets.
   See `USD issue #542 <https://github.com/PixarAnimationStudios/USD/issues/542>`__
   for more information.

Use Settings for
   Determines the whether to use *Viewport* or *Render* visibility of collection, modifiers,
   or any other property that can be set for both the *Viewport* and *Render*.


Experimental
------------

Instancing
   As this is an experimental option. When unchecked,
   duplicated objects are exported as real objects, so a particle system with
   100 particles that is displayed with 100 meshes will have 100 individual meshes
   in the exported file. When checked, duplicated objects are exported as
   a reference to the original object. If the original object is not part of the export,
   the first duplicate is exported as real object and used as reference.


Limitations
===========

Single-sided and Double-sided Meshes
   USD seems to support neither per-material nor per-face-group double-sidedness,
   so Blender uses the flag from the first material to mark the entire mesh as single/double-sided.
   If there is no material it defaults to double-sided.

Mesh Normals
   The mesh subdivision scheme in USD is 'Catmull-Clark' by default,
   but Blender uses 'None' instead, indicating that a polygonal mesh is exported.
   This is necessary for USD to understand the custom normals;
   otherwise the mesh is always rendered smooth.

Vertex Velocities
   Currently only fluid simulations (not meshes in general) have explicit vertex velocities.
   This is the most important case for exporting velocities, though,
   as the baked mesh changes topology all the time, and
   thus computing the velocities at import time in a post-processing step is hard.

Coordinate System Orientation
   Blender uses the Z axis as up axis. Since USD supports both Y up and Z up,
   the USD files written by Blender always use Z up.

Materials
   Very simple versions of the materials are exported, using only
   the :ref:`render-materials-settings-viewport-display` color, metallic, and roughness.

   When there are multiple materials, the mesh faces are stored as geometry subset
   and each material is assigned to the appropriate subset.
   If there is only one material this is skipped. Note that the geometry subsets are not time-sampled,
   so it may break when an animated mesh changes topology.

Hair
   Only the parent strands are exported, and only with a constant color.
   No UV coordinates, and no information about the normals.

Camera
   Only perspective cameras are exported.

Lights
   USD does not directly support spot lights, so those are not exported.

Particles
   Particles are only written when they are alive, which means that they are always visible.
   There is currently no code that deals with marking them as invisible outside their lifespan.

   Objects instanced by particle system are exported by suffixing the object name with
   the particle's persistent ID, giving each particle transform a unique name.

Instancing/Referencing
   This is still an experimental feature that can be enabled when exporting to USD.
   When enabled, instanced object meshes are written to USD as references to the original mesh.
   The first copy of the mesh is written for real, and the following copies are referencing the first.
   Which mesh is considered 'the first' is chosen more or less arbitrarily.
