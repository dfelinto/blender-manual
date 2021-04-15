
*******
Extrude
*******

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Extrude`
   :Shortcut:  :kbd:`Alt-E`


Extrude Faces
=============

See :ref:`bpy.ops.view3d.edit_mesh_extrude_move_normal`.


Extrude Faces Along Normals
===========================

See :ref:`bpy.ops.view3d.edit_mesh_extrude_move_shrink_fatten`.


Extrude Individual Faces
========================

See :ref:`tool-mesh-extrude_individual`.


Extrude Manifold
================

See :doc:`/modeling/meshes/tools/extrude_manifold`.


Extrude Edges
=============

See :ref:`bpy.ops.mesh.extrude_edges_move`.


Extrude Vertices
================

See :ref:`bpy.ops.mesh.extrude_vertices_move`.


.. _bpy.ops.mesh.extrude_repeat:

Extrude Repeat
==============

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Extrude --> Extrude Repeat`

This tool behaves similar to the :doc:`/modeling/modifiers/generate/array`,
by extruding the selection along the Z axis of the view.
If the selection is not :term:`Manifold` it's extruded the specified number of times.

Offset X, Y, Z
   Distance between the instances.
Steps
   Number of instances.
Scale Offset
   Multiplication factor to increase or decrease the offset.


Spin
====

See :doc:`/modeling/meshes/tools/spin`.
