.. _bpy.ops.view3d.edit_mesh_extrude_move_shrink_fatten:

***************************
Extrude Faces Along Normals
***************************

.. reference::

   :Mode:      Edit Mode
   :Tool:      :menuselection:`Toolbar --> Extrude Region --> Extrude Along Normals`
   :Menu:      :menuselection:`Mesh --> Extrude --> Extrude Faces Along Normals`
   :Shortcut:  :kbd:`Alt-E`

Extrusion and offset will be locked in to only move along the local normals of the selected mesh.

Flip Normals
   Only the *normals* of the new faces created from the extrusion will be flipped.

Dissolve Orthogonal Edges
   Removes and connects edges whose faces form a flat surface and intersect new edges.

Offset
   Amount to move geometry along the normals.

Offset Even
   The length of the new edges will be uniform.

Proportional Editing
   The extruded face will affect nearby geometry.
   See :doc:`Proportional Editing </editors/3dview/controls/proportional_editing>` for a full reference.
