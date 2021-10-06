.. index:: Geometry Nodes; Attribute Proximity
.. _bpy.types.GeometryNodeAttributeProximity:

************************
Attribute Proximity Node
************************

.. figure:: /images/modeling_geometry-nodes_attribute_attribute-proximity_node.png
   :align: right
   :width: 200px

   The Attribute Proximity node.

For each point in the input geometry, this node finds the closest position on the target.
Both the positions and the distances to them can be stored in attributes.


Inputs
======

Geometry
   Standard geometry input.

Target
   Standard geometry input.

Distance
   The name of the float attribute where the computed distance is stored.
   A new attribute with that name is added if it does not exist yet.
   If it does exist, the values of the existing attribute are overridden.

Position
   The name of the attribute where the computed location is stored.
   A new attribute with that name is added if it does not exist yet.
   If it does exist, the values of the existing attribute are overridden.


Properties
==========

Target Geometry
   :Faces:
      Calculate the closest point anywhere on the faces of the target's mesh geometry.
   :Edges:
      Calculate the closest point anywhere on the edges of the target's mesh geometry.
   :Points:
      Calculate the closest point or vertex on the target geometry. This mode is usually the fastest.


Output
======

Geometry
   Standard geometry output.


Examples
========

The different modes of the node: faces, edges and points.
In this example the geometry nodes modifier is added on the plane.
Note that the plane is subdivided and the cube is not.

.. figure:: /images/modeling_geometry-nodes_attribute_attribute-proximity_faces.png
   :align: left
   :width: 205px

   Target Geometry mode: faces.

.. figure:: /images/modeling_geometry-nodes_attribute_attribute-proximity_edges.png
   :align: left
   :width: 205px

   Target Geometry mode: edges.

.. figure:: /images/modeling_geometry-nodes_attribute_attribute-proximity_points.png
   :width: 205px

   Target Geometry mode: points.

Be sure to set the mode to points when the target is a point cloud.

.. figure:: /images/modeling_geometry-nodes_attribute_attribute-proximity_pointcloud-target.png
   :align: left
   :width: 680px

   Attribute Proximity node with a point cloud as target.
