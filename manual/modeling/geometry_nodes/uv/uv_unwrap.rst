.. index:: Geometry Nodes; UV Unwrap
.. _bpy.types.GeometryNodeUVUnwrap:

**************
UV Unwrap Node
**************


.. figure:: /images/node-types_GeometryUVUnrwap.png
   :align: right
   :alt: UV Unwrap node.

The *UV Unwrap Node* generates a UV map islands based on a selection of seam edges.
The node implicitly performs a :doc:`Pack Islands </modeling/geometry_nodes/uv/pack_uv_islands>`
operation upon completion, because the results may not be generally useful otherwise.

.. seealso::

   The :ref:`bpy.ops.uv.unwrap` operator performs a similar operation in the UV editor.
   Unlike the Unwrap operator, the node doesn't perform aspect ratio correction,
   because it is trivial to implement with a :doc:`/modeling/geometry_nodes/vector/vector_math`.


Inputs
======

Selection
   Faces to participate in the unwrap operation.
   UVs that are part of any other face will not be affected.

Seam
   Edges to mark where the mesh is "cut" for the purposes of unwrapping.

Margin
   The distance to leave between UV islands.

Fill Holes
   Virtually fill holes in mesh before unwrapping, to better avoid overlaps and preserve symmetry.


Properties
==========

Method
   :Angle Based:
      This method gives a good 2D representation of a mesh
   :Conformal:
      Uses LSCM (Least Squares Conformal Mapping). This usually gives a less accurate UV
      mapping than Angle Based, but works better for simpler objects


Output
======

UV
   The generated UV coordinates between 0 and 1 for each face corner in the selected faces.
