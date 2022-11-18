.. index:: Geometry Nodes; Sample Nearest Surface
.. _bpy.types.GeometryNodeSampleNearestSurface:

***************************
Sample Nearest Surface Node
***************************

.. figure:: /images/node-types_GeometryNodeSampleNearestSurface.webp
   :align: center
   :alt: Sample Nearest Surface node.

The *Sample Nearest Surface* node finds values at the closest points on
the surface of a source mesh geometry. Non-face attributes are interpolated
across the surface. 

This node is similar to the :doc:`/modeling/geometry_nodes/geometry/geometry_proximity`,
but it gives the value of any attribute at the closest surface point, not just its position.

.. warning::
   Because the node samples the *surface* of a mesh rather than its edges or vertices,
   values from loose points and edges are ignored.


Inputs
======

Mesh
   The geometry to retrieve the attribute from.

Value
   A field to evaluate on the *Source* geometry for use with the transfer method.

Sample Position
   The position to start from when finding the closest location on the target mesh.
   By default, this is the same as if the :doc:`/modeling/geometry_nodes/input/position` was connected.


Properties
==========

Data Type
   The :ref:`data type <attribute-data-types>` to use for the retrieved values.


Outputs
=======

Value
   The data retrieved and interpolated from the *Source* geometry, mapped based on the node's settings and inputs.
