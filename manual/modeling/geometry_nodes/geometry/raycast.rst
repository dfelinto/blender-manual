.. index:: Geometry Nodes; Raycast
.. _bpy.types.GeometryNodeRaycast:

*******
Raycast
*******

.. figure:: /images/modeling_geometry-nodes_geometry_raycast_node.png
   :align: center

   Raycast node.

The *Raycast* node intersects rays from one geometry onto another.
A ray starts on each point of the input geometry.
It computes hit points on the target mesh and outputs normals, distances
and any surface attribute specified by the user.


Inputs
======

Geometry
   Rays are created at the geometry points.

Target Geometry
   Geometry that rays are tested against.

Ray Direction
   Direction of each ray from the starting position.

Ray Length
   Maximum distance a ray can travel before being considered "no hit".

Target Attribute
   An optional attribute of the *Target Geometry* that will be interpolated at the hit points.
   The resulting values are stored in the output attribute named by *Hit Attribute*.

Is Hit
   Boolean output attribute that is true for each ray which has hit the *Target Geometry*.

Hit Position
   Output attribute storing the intersection point with the target mesh.

Hit Normal
   Output attribute storing the surface normal vector at the hit location.

Hit Distance
   Output attribute storing distance from the ray origin to the hit point.

Hit Attribute
   Output Attribute storing interpolated values of the *Target Attribute* at the hit positions.


Properties
==========

Ray Direction
   :Attribute: The input is a text field that expects an attribute name.
   :Vector: The input is a vector of three float numbers.

Ray Length
   :Attribute: The input is a text field that expects an attribute name.
   :Float: The input is a number field.

Mapping
   How attributes of the target mesh are mapped to the attribute values on the result geometry.

   Interpolated
      Vertex and corner attributes are interpolated with a bilinear function.

   Nearest
      Chooses the attribute value of the closest vertex or face corner without interpolating.


Outputs
=======

Geometry
   Geometry that contains output attributes for each ray.
