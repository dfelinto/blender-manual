.. _bpy.ops.mesh.intersect_boolean:

*******************
Intersect (Boolean)
*******************

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Face --> Intersect (Boolean)`

Performs Boolean operations with the selection on the unselected geometry.
While the :doc:`/modeling/modifiers/generate/booleans` is useful for non-destructive edits,
access to these operations with a tool in Edit Mode can be useful to quickly perform edits.

Boolean Operation
   Intersect
      Opposite of *Difference* (everything *inside* of the target mesh is kept).
   Union
      The target mesh is added to the modified mesh.
   Difference
      The target mesh is subtracted from the modified mesh (everything *outside* of the target mesh is kept).

Solver
   Algorithm used to calculate the boolean intersections.

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

Swap
   Changes the order of the operations when using *Difference* to determine which side is kept.

Self
   Correctly calculates cases when one or both operands have self-intersections,
   this involves more calculations making it slower.
