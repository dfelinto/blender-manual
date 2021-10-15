.. index:: Geometry Nodes; Normal
.. _bpy.types.GeometryNodeInputNormal:

***********
Normal Node
***********

.. figure:: /images/modeling_geometry-nodes_input_normal_node.png
   :align: right

   Normal Node.

The *Normal Node* returns a vector for each evaluated point indicating the normal
direction. The output can depend on the attribute domain used in the node evaluating the field,
but the output is always a normalized `unit vector <https://en.wikipedia.org/wiki/Unit_vector>`.

   :Face: 
      On the face domain, the normal is the "up" direction of the face.

   :Mesh Vertices:
      For mesh vertices, the normal is an average of the surrounding face normals.
      If the vertex does not have any connected faces, the output is simply the normalized position
      of that vertex.

   :Edge:
      The normal output for each edge is the average of the edge's two vertex normals

   :Face Corner:
      The output for each face corner is the same as the face normal of the corresponding face.

   :Curve Control Points:
      The output of of this node when used for curve geometry is the evaluated normal of the curve,
      which depends on the twist method. The normal vector is always perpendicular to the direction
      of the curve's path at every point.

   .. warning::

      For NURBS and Bezier spline curves, keep in mind that the value retrieved from this node is the
      value at every control point, which may not correspond to the visible *evaluated* points. For
      NURBS splines the difference may be even more pronounced and the result may not be as expected.
      A :doc:`</modeling/geometry_nodes/curve/resample_curve>` node can be used to create a Poly spline,
      where there is a control point for every evaluated point.


Inputs
======

This node has no inputs.


Properties
==========

This node has no properties.


Outputs
=======

Normal
   Vector indicating the normal of each geometry element.
