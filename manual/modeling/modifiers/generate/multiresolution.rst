.. index:: Modeling Modifiers; Multiresolution Modifier
.. _bpy.types.MultiresModifier:

************************
Multiresolution Modifier
************************

The *Multiresolution* modifier (often shortened to "Multires") gives you the ability to subdivide a mesh similarly
to the :doc:`Subdivision Surface </modeling/modifiers/generate/subdivision_surface>` modifier,
but also allows you to edit the new subdivision levels in :doc:`Sculpt Mode </sculpt_paint/sculpting/introduction>`.

.. note::

   *Multiresolution* is the only modifier that cannot be repositioned in the stack after any modifier that will
   change geometry or other object data (i.e. all *Generate*, some *Modify* and some *Simulate* modifiers
   cannot come before the *Multiresolution* one).


Options
=======

.. figure:: /images/modeling_modifiers_generate_multiresolution_panel.png
   :align: right
   :width: 300px

   The Multiresolution modifier.


Levels Viewport
   Set the level of subdivisions to show in Object Mode.
Sculpt
   Set the level of subdivisions to use in Sculpt Mode.
Render
   Set the level of subdivisions to show when rendering.

Sculpt Base Mesh
   Makes sculpt-mode tools deform the base mesh instead of the displaced mesh,
   while previewing the displacement of higher subdivision levels. This allows you to
   see the propagation of strokes in real-time, which enables to use complex tools like
   Cloth or Pose in much higher resolutions without surface noise and artifacts.

Optimal Display
   When rendering the wireframe of this object, the wires of the new subdivided edges will be skipped
   (only displays the edges of the original geometry).


Subdivisions
------------

.. _bpy.ops.object.multires_subdivide:

Subdivide
   Creates a new level of subdivision using the subdivision type specified by *Subdivision Type* (see below).

Simple
   Creates a new level of subdivision using a simple interpolation by subdividing edges without any smoothing.
Linear
   Creates a new level of subdivision using linear interpolation of the current sculpted displacement.

.. _bpy.ops.object.multires_unsubdivide:

Unsubdivide
   Rebuild a lower subdivision level of the current base mesh.

.. _bpy.ops.object.multires_higher_levels_delete:

Delete Higher
   Deletes all subdivision levels that are higher than the current one.


Shape
-----

.. _bpy.ops.object.multires_reshape:

Reshape
   Copies vertex coordinates from another mesh.

   To use it, first select a different mesh object with matching topology and vertex indices,
   then :kbd:`Shift` select the object you wish to copy vertex coordinates to, and click *Reshape*.

.. _bpy.ops.object.multires_base_apply:

Apply Base
   Modifies the original unsubdivided mesh to match the form of the subdivided mesh.


Generate
--------

.. _bpy.ops.object.multires_rebuild_subdiv:

Rebuild Subdivisions
   Rebuilds all possible subdivisions levels to generate a lower resolution base mesh.
   This is used to create an optimized multiresolution version of a pre-existing sculpt.
   This option is only available when no subdivision level have been created through the modifier.

.. _bpy.ops.object.multires_external_save:

Save External
   Saves displacements to an external ``.btx`` file.


Advanced
--------

Quality
   How precisely the vertices are positioned (relatively to their theoretical position),
   can be lowered to get a better performance when working on high-poly meshes.

UV Smooth
   How to handle UVs during subdivision.

   Smooth, Keep Corners
      UV islands are smoothed, but their boundary remain sharp.
   Sharp
      UV remain unchanged.

Boundary Smooth
   Controls how open boundaries (and corners) are smoothed.

   All
      Smooth boundaries, including corners.
   Keep Corners
      Smooth boundaries, but corners are kept sharp.

Use Creases
   Use the :ref:`modifiers-generate-subsurf-creases` values stored in edges to control how smooth they are made.

Use Custom Normals
   Interpolates existing :ref:`modeling_meshes_normals_custom` of the resulting mesh.
