.. index:: Geometry Nodes; Boolean
.. _bpy.types.GeometryNodeBoolean:

************
Boolean Node
************

The *Boolean Node* allows you to cut, subtract, and join the geometry of two inputs.
This node offers the same operations as the :doc:`Boolean modifier </modeling/modifiers/generate/booleans>`.

.. figure:: /images/modeling_geometry-nodes_mesh_boolean_node.png

   The Boolean node.


Inputs
======

Geometry 1/2
   Standard geometry input.

Self Intersection
   Correctly calculates cases when one or both operands have self-intersections,
   this involves more calculations making it slower.

Hole Tolerant
   Optimizes the Boolean output for :term:`Non-manifold` geometry
   at the cost of increased computational time.
   Because of the performance impact, this option should only be enabled
   when the *Exact* solver demonstrates errors with non-manifold geometry.


Properties
==========

Operation
   :Intersect:
      Produce a new geometry containing only the volume inside of both geometry 1 and geometry 2.
   :Union:
      The two input pieces of geometry are joined, then any interior elements are removed.
   :Difference:
      Geometry 2 is subtracted from geometry 1 (everything outside of geometry 2 is kept).


Output
======

Geometry
   Standard geometry output.
