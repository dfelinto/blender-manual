.. _bpy.ops.mesh.intersect:

*****************
Intersect (Knife)
*****************

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Face --> Intersect (Knife)`

The Intersect tool lets you cut intersections into geometry.
It is a bit like the Boolean tool, but, does not calculate interior/exterior geometry.
Faces are split along the intersections, leaving new edges selected.

Source
   Self Intersect
      Operate on the overlapping geometry of the mesh.
   Selected/Unselected
      Operate between the selected and unselected geometry.

Separate Mode
   All
      Splits the geometry at the new edge.
   Cut
      Keep each side of the intersection separate without splitting the faces in half.
   Merge
      Merge all the geometry from the intersection.

Solver
   Algorithm used to calculate the intersections.

   Fast
      Uses a mathematically simple solver which offers the best performance;
      however, this solver lacks support for overlapping geometry.

      Merge Threshold
         Tolerance for close faces to be considered touching.
         It may be useful to increase this when some intersections aren't detected that should be and
         when extra geometry is being created because edges aren't detected as overlapping.

         .. warning::

            A threshold approaching the size of faces may cause very slow calculation,
            in general keep this value small.

   Exact
      Uses a mathematically complex solver which offers the best results
      and has full support for overlapping geometry;
      however, this solver is much slower than the *Fast Solver*.
