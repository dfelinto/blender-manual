.. index:: Nodes; Boolean
.. _bpy.types.GeometryNodeBoolean:

*******
Boolean
*******

The *Boolean Node* allows cutting, subtracting, and joining the mesh component of its two *Geometry* inputs.

The node acts with the same method as the *exact* mode of the 
:doc:`boolean modifier </modeling/modifiers/generate/booleans>`.


.. figure:: /images/modeling_modifiers_nodes_boolean.png

   The Boolean node.


Options
=======

Mode
   Intersect
      Produce a new mesh containing only the volume inside of both geometry A and geometry B.

   Union
      The two input geometries are joined, then any interior faces are removed.

   Difference
      Geometry B is subtracted from geometry A (everything outside of geometry B is kept).
