.. _bpy.ops.mesh.symmetry_snap:

****************
Snap to Symmetry
****************

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Snap to Symmetry`

The Snap to Symmetry tool lets you snap a mesh vertices to their mirrored neighbors.

Useful when dealing with meshes which are mostly symmetrical,
but have vertices which have been moved enough that Blender
does not detect them as mirrored (when X Mirror option is enabled for example).

This can be caused by accident when editing without X Mirror enabled. Sometimes models
imported from other applications are asymmetrical enough that mirror fails too.

Direction
   Specify the axis and direction to snap. Can be any of the three axes,
   and either positive to negative, or negative to positive.
Threshold
   Specify the search radius to use when finding matching vertices.
Factor
   Support for blending mirrored locations from one side to the other (0.5 is an equal mix of both).
Center
   Snap vertices along the center axis to zero.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_mesh_snap-symmetry_before.png
          :width: 320px

          Before Snap to Symmetry.

     - .. figure:: /images/modeling_meshes_editing_mesh_snap-symmetry_after.png
          :width: 320px

          After Snap to Symmetry.
