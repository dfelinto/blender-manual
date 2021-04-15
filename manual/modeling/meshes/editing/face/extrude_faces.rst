.. _bpy.ops.mesh.extrude_indiv:
.. _bpy.ops.view3d.edit_mesh_extrude_individual_move:
.. _bpy.ops.view3d.edit_mesh_extrude_move_normal:

*************
Extrude Faces
*************

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Face --> Extrude Faces`
   :Shortcut:  :kbd:`E`

*Extrude Faces* duplicate faces, while keeping the new geometry connected with the original vertices.

.. list-table::

   * - .. figure:: /images/modeling_meshes_tools_extrude-region_vert.png
          :width: 320px

          Single vertex extruded.

     - .. figure:: /images/modeling_meshes_tools_extrude-region_edge.png
          :width: 320px

          Single edge extruded.

This tool is of paramount importance for creating new geometry.
It allows you to create parallelepipeds from rectangles and cylinders from circles,
as well as easily creating such things as tree limbs.

The axis on which faces are extruded along can be set interactively.
Faces are extruded by default along their averaged normal.
The extrusion can be limited to a single axis by specifying an axis;
see :doc:`/scene_layout/object/editing/transform/control/axis_locking`.

The extrude tools differentiate in how the new geometry is connected in itself.
Only the border loop gets extruded.
The inner region of the selection gets moved unchanged with the extrusion.

.. list-table::

   * - .. figure:: /images/modeling_meshes_tools_extrude-region_face-before.png
          :width: 200px

          Selected face.

     - .. figure:: /images/modeling_meshes_tools_extrude-region_face-after.png
          :width: 200px

          During extrude.

     - .. figure:: /images/modeling_meshes_tools_extrude-region_face-after-zaxis.png
          :width: 200px

          Set to Z axis.

Flip Normals
   Only the *normals* of the new faces created from the extrusion will be flipped.

Dissolve Orthogonal Edges
   Removes and connects edges whose faces form a flat surface and intersect new edges.

Orientation
   Aligns the transformation axes to a specified orientation constraint.
   See :doc:`Transform Orientations </editors/3dview/controls/orientation>` for more information.

Proportional Editing
   The extruded face will affect nearby geometry.
   See :doc:`Proportional Editing </editors/3dview/controls/proportional_editing>` for a full reference.

   .. note::

      Even with the *Proportional Size* set to it's minimum,
      it will extrude the selected face as well as the new geometry and they will be layered on top of each other.
