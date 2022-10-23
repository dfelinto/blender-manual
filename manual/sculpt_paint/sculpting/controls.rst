
********
Controls
********

Auto-Masking
============

.. reference::

   :Mode:      Sculpt Mode
   :Tool:      :menuselection:`Header --> Auto-Masking`

These properties automatically mask geometry based on geometric features of the mesh.
Note, these properties are applied across all sculpt brushes, however, they can also be configured
per brush in the :ref:`Advanced Brush Settings <sculpt-tool-settings-brush-settings-advanced>`.
These properties can be accessed via a :ref:`bpy.types.UIPieMenu` by pressing :kbd:`Alt-A`.

.. _bpy.types.Sculpt.use_automasking_topology:

Topology
   Brush affects only vertices connected to the active vertex under the brush.

.. _bpy.types.Sculpt.use_automasking_face_sets:

Face Sets
   Affect only vertices that share face sets with active vertex.

.. _bpy.types.Sculpt.use_automasking_boundary_edges:

Mesh Boundary
   Does not affect non-manifold boundary edges.

.. _bpy.types.Sculpt.use_automasking_boundary_face_sets:

Face Sets Boundary
   Does not affect vertices which belong to a face set boundary.

.. _bpy.types.Brush.automasking_boundary_edges_propagation_steps:

Propagation Steps
   The distance where *Mesh Boundary Auto-Masking* is going to protect vertices from the fully masked edge.
