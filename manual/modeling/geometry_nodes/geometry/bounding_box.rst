.. index:: Geometry Nodes; Bounding Box
.. _bpy.types.GeometryNodeBoundBox:

************
Bounding Box
************

.. figure:: /images/modeling_geometry-nodes_geometry_bounding-box_node.png
   :align: right

   The Bounding Box node.

The *Bounding Box* node creates a cube with the minimum volume that encapsulates the geometry of the input.
The node also can output the vector positions of the bounding dimensions.


Inputs
======

Geometry
   Standard geometry input.


Properties
==========

This node has no properties.


Outputs
=======

Geometry
   The resulting box or cube to encapsulate the input geometry.

Min
   The coordinates corresponding to the cubes -X, -Y, -Z position values,
   i.e. how far the box extends in each of the negative axes directions.

Max
   The coordinates corresponding to the cubes +X, +Y, +Z position values.
   i.e. how far the box extends in each of the positive axes directions.


Example
=======

.. figure:: /images/modeling_geometry-nodes_geometry_bounding-box_example.png

   Bounding Box node used to create a cube that encapsulates the geometry a monkey mesh.
