.. index:: Geometry Nodes; Boolean
.. _bpy.types.GeometryNodeBoolean:

*******
Boolean
*******

The *Boolean Node* allows you to cut, subtract, and join the geometry of two inputs.
This node offers the same operations as the :doc:`Boolean modifier </modeling/modifiers/generate/booleans>`.

.. figure:: /images/modeling_modifiers_nodes_boolean.png

   The Boolean node.


Inputs
======

Geometry A, B
   Standard geometry input.


Properties
==========

Mode
   Intersect
      Produce a new geometry containing only the volume inside of both geometry A and geometry B.

   Union
      The two input pieces of geometry are joined, then any interior elements are removed.

   Difference
      Geometry B is subtracted from geometry A (everything outside of geometry B is kept).


Output
======

Geometry
   Standard geometry output.
