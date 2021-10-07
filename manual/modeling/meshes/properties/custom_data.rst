
*************
Geometry Data
*************

.. _bpy.ops.mesh.customdata_mask_clear:

Clear Sculpt-Mask Data
   Completely frees the mask data layer from the mesh. While not a huge benefit,
   this can speed-up sculpting if the mask is no longer being used.

.. _bpy.ops.mesh.customdata_skin_clear:
.. _bpy.ops.mesh.customdata_skin_add:

Add/Clear Skin Data
   Used to manage the skin data layer which is used by the :doc:`/modeling/modifiers/generate/skin`.
   This operator can be needed in case a Skin modifier is created but no skin data exist.


.. _bpy.ops.mesh.customdata_custom_splitnormals_clear:
.. _bpy.ops.mesh.customdata_custom_splitnormals_add:

Add/Clear Custom Split Normals Data
   Adds a :ref:`custom split normals <modeling_meshes_normals_custom>` data layer, if none exists yet.


.. _bpy.types.Mesh.use_customdata_vertex_bevel:

Store
   Vertex Bevel Weight
      Save the :ref:`Vertex Bevel Weight <modeling-vertex-bevel-weight>` with the mesh data.
      
   .. _bpy.types.Mesh.use_customdata_edge_bevel:

   Edge Bevel Weight
      Save the :ref:`Edge Bevel Weight <modeling-edges-bevel-weight>` with the mesh data.

   .. _bpy.types.Mesh.use_customdata_edge_crease:

   Edge Crease
      Save the :ref:`Edge Crease <modeling-edges-crease-subdivision>` with the mesh data..

   .. warning::

      Disabling any of these properties will result in the data loss of these values.
