
*************
Geometry Data
*************

This panel is used to manage any generic data attributes that a mesh could have.

.. warning::

   Clearing any data will result in the data loss of these values.

.. _bpy.ops.mesh.customdata_mask_clear:

Clear Sculpt-Mask Data
   Completely removes the mask data from the mesh. While not a huge benefit,
   this can speed-up sculpting if the mask is no longer being used.

.. _bpy.ops.mesh.customdata_skin_clear:
.. _bpy.ops.mesh.customdata_skin_add:

Add/Clear Skin Data
   Used to manage the skin data which is used by the :doc:`/modeling/modifiers/generate/skin`.
   This operator can be needed in case a Skin modifier is created but no skin data exist.

.. _bpy.ops.mesh.customdata_custom_splitnormals_clear:
.. _bpy.ops.mesh.customdata_custom_splitnormals_add:

Add/Clear Custom Split Normals Data
   Adds :ref:`Custom Split Normals <modeling_meshes_normals_custom>` data, if none exists yet.

.. _bpy.ops.mesh.customdata_bevel_weight_edge_add:
.. _bpy.ops.mesh.customdata_bevel_weight_edge_clear:

Add/Clear Edge Bevel Weight
   Adds a zero :ref:`Edge Bevel Weight <modeling-edges-bevel-weight>` value to all edges of the mesh.
   If edge bevel data does exist, this operator will delete all that data.

.. _bpy.ops.mesh.customdata_bevel_weight_vertex_add:
.. _bpy.ops.mesh.customdata_bevel_weight_vertex_clear:

Add/Clear Vertex Bevel Weight
   Adds a zero :ref:`Vertex Bevel Weight <modeling-vertex-bevel-weight>` value to all edges of the mesh.
   If edge bevel data does exist, this operator will delete all that data.

   .. _bpy.types.Mesh.use_customdata_edge_crease:
Store
   Edge Crease
      Save the :ref:`Edge Crease <modeling-edges-crease-subdivision>` with the mesh data.
