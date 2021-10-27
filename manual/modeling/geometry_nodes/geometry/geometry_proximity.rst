.. index:: Geometry Nodes; Geometry Proximity
.. _bpy.types.GeometryNodeGeometryProximity:

***********************
Geometry Proximity Node
***********************


.. figure:: /images/modeling_geometry-nodes_geometry_geometry-proximity_node.png
   :align: right

   The Geometry Proximity node.

The *Geometry Proximity* node finds the closest location on the target.


Inputs
======

Target
   Standard geometry input.

Source Position
   The given position to find the closest location on the target.

Properties
==========

Target Geometry
   :Points: Calculate the proximity to the target's points (faster than the other modes).
   :Edges: Calculate the proximity to the target's edges.
   :Faces: Calculate the proximity to the target's faces.


Outputs
=======

Position
   Closest location in the target.

Distance
   Distance (as floating-point value) from the source position to the closest location in the target.
