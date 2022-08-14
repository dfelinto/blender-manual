
***************************
Universal Scene Description
***************************

Exporting to USD Files
======================

Universal Scene Description (USD) files can contain complex layering, overriding, and references to other files.
Blender's USD Exporter takes a much simpler approach. When exporting, all visible, supported objects in
the scene are exported, optionally limited by their selection state. Blender does not (yet) support exporting
invisible objects, USD layers, variants, skeletal animation, etc.

The following objects can be exported to USD:

- Meshes (of different kinds, see below).
- Cameras (perspective cameras only at the moment, not orthogonal ones).
- Light (all types except area lights).
- Hair (exported as curves, and limited to parent strands).
- Volume (both static and animated volumes).

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

   Shot from `Spring <https://cloud.blender.org/films/spring/>`__ exported to USD and opened in USDView.


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
   Exports material information of the object.
   By default the exporter approximates the :doc:`/render/shader_nodes/shader/principled`
   node tree by converting it to USD's Preview Surface format.
   If *To USD Preview Surface* is disabled, the material is set to the viewport materials of meshes.

   Additional material properties are set in the *Material* grouping of options.

   When a mesh has multiple materials assigned, a geometry subset is created for each material.
   The first material (if any) is always applied to the mesh itself as well
   (regardless of the existence of geometry subsets),
   because the Hydra viewport does not support materials on subsets.
   See `USD issue #542 <https://github.com/PixarAnimationStudios/USD/issues/542>`__
   for more information.

Use Settings for
   Determines the whether to use *Viewport* or *Render* visibility of collection, modifiers,
   or any other property that can be set for both the *Viewport* and *Render*.


Materials
---------

Additional options when *Materials* are enabled for export.

To USD Preview Surface
   When exporting materials, approximate a :doc:`/render/shader_nodes/shader/principled`
   node tree to by converting it to USD's Preview Surface format.
   If disabled, the material is set to the viewport materials of meshes.

   .. warning::

      Not all nodes are supported; currently only Diffuse,
      Principle, Image Textures, and UVMap nodes are support.

Export Textures
   Export textures referenced by shader nodes to a "textures"
   folder which in the same directory as the USD file.

Overwrite Textures
   Allow overwriting existing texture files when exporting textures.


File References
---------------

Relative Paths
   Use relative paths to reference external files (i.e. textures, volumes) in the exported USD file,
   otherwise use absolute paths.


Experimental
------------

Instancing
   As this is an experimental option. When unchecked,
   duplicated objects are exported as real objects, so a particle system with
   100 particles that is displayed with 100 meshes will have 100 individual meshes
   in the exported file. When checked, duplicated objects are exported as
   a reference to the original object. If the original object is not part of the export,
   the first duplicate is exported as real object and used as reference.


Exporter Limitations
====================

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


Importing USD Files
===================

`USD <https://graphics.pixar.com/usd/docs/index.html>`__ files typically represent the scene as
a hierarchy of primitives, or `prims <https://graphics.pixar.com/usd/docs/USD-Glossary.html#USDGlossary-Prim>`__.
Individual prims contain data to describe scene entities, such as geometry, lights, cameras and transform hierarchies.
Blender's USD importer converts USD prims to a hierarchy of Blender objects. Like the USD exporter,
the importer does not yet handle more advanced USD concepts, such as layers and references.

The following USD data types can be imported as Blender objects:

- Cameras
- Curves
- Lights
- Materials
- Meshes
- Volume

For more information on how the various data types are handled,
see the following descriptions of the `Import Options`_.


Xform and Scope Primitives
--------------------------

USD provides an ``Xform`` prim type, containing transform data, which can be
used to represent transform hierarchies and to organize the scene.
Such ``Xform`` prims are imported as Blender empty objects.

USD also supports ``Scope`` primitives, which are entities
that do not contain transform data, but which serve to group other element of the scene.
Blender doesn't have an exact counterpart to the concept of a scope,
so such primitives are imported as Blender empties located at the origin.
This is an imperfect representation, because empty objects have a transform and ``Scopes`` do not,
but this approach nonetheless helps preserve the structure of the scene hierarchy.


Animations
----------

The importer supports two types of animation:

- **Animating transforms**: If a USD primitive has time-varying transform data,
  a :doc:`Transform Cache </animation/constraints/transform/transform_cache>` constraint
  will be added to the imported Blender object.
- **Animating geometry**: Animating mesh and curve geometry is supported by adding
  a :doc:`Mesh Sequence Cache </modeling/modifiers/modify/mesh_sequence_cache>` modifier to the imported data.
  Geometry attribute (`USD Primvar <https://graphics.pixar.com/usd/docs/USD-Glossary.html#USDGlossary-Primvar>`__)
  animation is currently supported only for Color Attributes and UVs.
  Note that USD file sequences (i.e. a unique file per frame) are not yet supported.


Materials
---------

If a USD mesh or geometry subset has a bound material, the importer will assign to
the Blender object a material with the same name as the USD material.
If a Blender material with the same name already exists in the scene,
the existing material will be assigned. Otherwise, a new material will be created.

If the USD material has
a `USD Preview Surface <https://graphics.pixar.com/usd/docs/UsdPreviewSurface-Proposal.html>`__ shader source,
the :ref:`render-materials-settings-viewport-display` color, metallic, and roughness are set to
the corresponding USD Preview Surface input values.

There is also an experimental *Import USD Preview* option to convert USD Preview Surface shaders
to Blender :doc:`Principled BSDF </render/shader_nodes/shader/principled>` shader nodes.
This option can be lossy, as it does not yet handle converting all shader settings and types,
but it can generate approximate visualizations of the materials.


Coordinate System Orientation
-----------------------------

If the imported USD is Y up, a rotation will be automatically applied to
root objects to convert to Blender's Z up orientation.


Import Options
==============

The following options are available when importing from USD:

Cameras
   Import cameras (perspective and orthographic).

Curves
   Import curve primitives, including USD basis and NURBS curves.
   (Note that support for Bézier basis is not yet fully implemented.)

Lights
   Import lights. Does not currently include USD dome, cylinder or geometry lights.

Materials
   Import materials. See also the experimental *Import USD Preview* option.

Meshes
   Import meshes.

Volumes
   Import USD OpenVDB field assets.

Path Mask
   Import only the subset of the USD scene rooted at the given primitive.

Scale
   Value by which to scale the imported objects in relation to the world's origin.

UV Coordinates
   Read mesh UV coordinates.

Color Attributes
   Convert the USD mesh ``displayColor`` values to Blender's Color Attributes.

Subdivision
   Create Subdivision Surface modifiers based on the USD ``SubdivisionScheme`` attribute.

Import Instance Proxies
   Create unique Blender objects for USD instances.

Visible Primitives Only
   Do not import invisible USD primitives. Only applies to primitives with a non-animated
   `visibility <https://graphics.pixar.com/usd/docs/USD-Glossary.html#USDGlossary-Visibility>`__ attribute.
   Primitives with animated visibility will always be imported.

Guide
   Include primitives with
   `purpose <https://graphics.pixar.com/usd/docs/USD-Glossary.html#USDGlossary-Purpose>`__ ``guide``.

Proxy
   Include primitives with purpose ``proxy``.

Render
   Include primitives with purpose ``render``.

Set Frame Range
   Update the scene's start and end frame to match those of the USD stage.

Relative Path
   Select the file relative to the blend-file.

Create Collection
   Add all imported objects to a new collection.

Light Intensity Scale
   Scale for the intensity of imported lights.

Material Name Collision
   Behavior when the name of an imported material conflicts with an existing material.

   :Make Unique: Import each USD material as a unique Blender material.
   :Reference Existing: If a material with the same name already exists, reference that instead of importing.


Experimental
------------

Import USD Preview
   Convert USD Preview Surface shaders to Principled BSDF shader networks.

Set Material Blend
   If the *Import USD Preview* option is enabled, the material blend method will automatically be set based on
   the ``opacity`` and ``opacityThreshold`` shader inputs, allowing for visualization of transparent objects.
