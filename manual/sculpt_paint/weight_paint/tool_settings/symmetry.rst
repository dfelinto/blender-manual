
********
Symmetry
********

.. admonition:: Reference
   :class: refbox

   :Mode:      Vertex Paint Mode
   :Tool:      :menuselection:`Toolbar --> Tool --> Symmetry`

Mirror
   Mirror the brush strokes across the selected local axes.
   Note that if you want to alter the directions the axes point in,
   you must rotate the model in Edit Mode and not in Object Mode.

Radial X, Y, Z
   These settings allow for radial symmetry in the desired axes.
   The number determines how many times the stroke will be repeated
   within 360 degrees around the central axes.

.. _bpy.types.Mesh.use_mirror_vertex_group_x:

Vertex Group X
   Use the X Mirror option for mirrored painting on groups that have symmetrical names,
   like with extension ".R"/ ".L" or "_R" / "_L". If a group has no mirrored counterpart,
   it will paint symmetrically on the active group itself.
   You can read more about the naming convention in
   :ref:`Editing Armatures: Naming conventions <armature-editing-naming-conventions>`.
   The convention for armatures/bones apply here as well.

Topology Mirror
   Use topology-based mirroring, for when both sides of a mesh have matching mirrored topology.
   See :ref:`here <bpy.types.Mesh.use_mirror_topology>` for more information.
