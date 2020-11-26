.. index:: Nodes; Mesh; Point Instance
.. _bpy.types.GeometryNodePointInstance:

**************
Point Instance
**************

.. figure:: /images/modeling_modifiers_nodes_point-instance.png
   :align: right

   Point Instance Node.

The *Point Instance* node instances an element to each of the points present in the
input geometry. It works for both point cloud and mesh vertices.

.. note::
   This node only works if it the modifier belongs to a point cloud object.


Inputs
======

Geometry
   Source points to use as reference for instancing.
Object
   The object to instance.


Outputs
=======

Geometry
   The points with the information of what to instance.

   The geometry of the instanced elements is not outputed directly.
   Instead it is only generated in the viewport or at rendering time.
