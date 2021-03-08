.. index:: Geometry Nodes; Attribute Proximity
.. _bpy.types.GeometryNodeAttributeProximity:

*******************
Attribute Proximity
*******************

.. figure:: /images/modeling_modifiers_nodes_attribute-proximity.png
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
   Faces 
      Calculate the closest point anywhere on the faces of the target geometry's mesh.
   Edges 
      Calculate the closest point anywhere on the edges of the target geometry's mesh.
   Points
      Calculate the closest point or vertex on the target geometry. This mode is usually fastest.

Output
======

Geometry
   Standard geometry output.


Examples
========
The different modes of the node: faces, edges and points. 
In this example the geometry nodes modifier is added on the plane.
Note that the plane is subdivided and the cube is not. 

.. figure:: /images/modeling_modifiers_nodes_attribute-proximity-faces.png
   :align: left
   :width: 205px

   Target Geometry mode: Faces.

.. figure:: /images/modeling_modifiers_nodes_attribute-proximity-edges.png
   :align: left
   :width: 205px

   Target Geometry mode: Edges.

.. figure:: /images/modeling_modifiers_nodes_attribute-proximity-points.png
   :width: 205px

   Target Geometry mode: Points.


Be sure to set the mode to Points when the Target is a point cloud.

.. figure:: /images/modeling_modifiers_nodes_attribute-proximity-pointcloud-target.png
   :align: left
   :width: 680px

   Attribute Proximity node with a point cloud as Target.