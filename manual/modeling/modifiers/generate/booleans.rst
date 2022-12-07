.. index:: Modeling Modifiers; Boolean Modifier
.. _bpy.types.BooleanModifier:

****************
Boolean Modifier
****************

The *Boolean* modifier performs operations on meshes that are otherwise too complex
to achieve with as few steps by editing meshes manually. It uses one of
the three available Boolean operations to create a single mesh out of two mesh objects:

.. figure:: /images/modeling_modifiers_generate_booleans_union-intersect-difference-examples.png

   The Union, Intersection and Difference between a Cube and a UV Sphere,
   with the modifier applied to the sphere and using the cube as target.

This modifier needs a second mesh object, or collection of mesh objects,
to be the target (the second operand) of the operation.

.. warning::

   Only :term:`Manifold` meshes are guaranteed to give proper results,
   other cases (especially "opened" meshes, :term:`Non-manifold` but without any self-intersections)
   will usually work well, but might give odd glitches and artifacts in some cases.

.. tip::

   If you have marked your objects to show the edges
   (in :menuselection:`Properties --> Object Properties --> Viewport Display`, enable *Wireframe*),
   you will see the edge creation process while you are moving your objects around. Depending on your mesh topology,
   you can also enable X-Ray and Transparency and see the topology being created in real-time.


Options
=======

.. figure:: /images/modeling_modifiers_generate_booleans_panel.png
   :align: center
   :width: 300px

   The Boolean modifier.

Operation
   :Intersect:
      Everything inside both the target mesh and the modified mesh is kept.
      If the target is a collection, then only the inside of *all* meshes is kept.
   :Union:
      The target mesh or collection is added to the modified mesh,
      removing any interior faces.
   :Difference:
      The target mesh, or collection of meshes, is subtracted from the modified mesh
      (everything *outside* of the target mesh or collection is kept).

Operand Type
   Choose the type of the operand (target).

   :Object:
      The target is a mesh object.

   :Collection:
      The target is a collection.
      When the target is a collection and the Solver is Fast,
      the Intersect operation is not allowed.

Object
   The name of the target mesh object.

Collection
   The name of the target collection (may be empty if Solver is Exact,
   which can be useful in combination with the Self option).

Solver
   Algorithm used to calculate the Boolean intersections.

   :Fast:
      Uses a mathematically simple solver which offers the best performance;
      however, this solver lacks support for overlapping geometry.
   :Exact:
      Uses a mathematically complex solver which offers the best results
      and has full support for overlapping geometry;
      however, this solver is much slower than the *Fast Solver*.


Solver Options
--------------

Materials :guilabel:`Exact Solver`
   Method for setting materials on the new faces.

   :Index Based:
      Set the material on new faces based on the order of the material slot lists.
      If a material doesn't exist on the modifier object,
      the face will use the same material slot or the first if the object doesn't have enough slots.
   :Transfer:
      Transfer materials from non-empty slots to the result mesh, adding new materials as necessary.
      For empty slots, fall back to using the same material index as the operand mesh.

Self Intersection :guilabel:`Exact Solver`
   Correctly calculates cases when one or both operands have self-intersections,
   this involves more calculations making it slower.

Hole Tolerant :guilabel:`Exact Solver`
   Optimizes the Boolean output for :term:`Non-manifold` geometry
   at the cost of increased computational time.
   Because of the performance impact, this option should only be enabled
   when the *Exact* solver demonstrates errors with non-manifold geometry.

Overlap Threshold :guilabel:`Fast Solver`
   Maximum distance between two faces to consider them as overlapping.
   This helps solve the limitation of this solver,
   if the Boolean result seems unexpected try using the exact solver.
