.. index:: Nodes; Boolean

*******
Boolean
*******

The *Boolean Node* allows boolean operations between two *Geometry* inputs.


.. figure:: /images/modeling_modifiers_nodes_boolean.png

   Boolean modifier node.


Options
=======

Mode
   Intersect
      Everything inside both the geometry A and the geometry B is kept.

   Union
      The geometry A is added to the geometry B, removing any interior faces.

   Difference
      The geometry B is subtracted from the geometry A (everything outside of the geometry B is kept).
