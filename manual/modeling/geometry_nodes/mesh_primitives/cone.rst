.. index:: Geometry Nodes; Cone
.. _bpy.types.GeometryNodeMeshCone:

*********
Cone Node
*********

.. figure:: /images/node-types_GeometryNodeMeshCone.webp
   :align: right
   :alt: Cone node.

The *Cone* node generates a cone mesh that is optionally truncated.


Inputs
======

Vertices
   Number of points on the circle at the top and bottom.
   No geometry is generated if the number is below three.

Side Segments
   Number of edges running vertically along the side of the cone.
   No geometry is generated if the number is below one.

Fill Segments
   Number of concentric rings used to fill the round faces at the top and bottom.
   No geometry is generated if the number is below one.

Radius Top
   The distance of the vertices in the top circle from the Z axis.
   If this is zero, the vertices in the circle are merged into one.

Radius Bottom
   Same as *Radius Top* but for the bottom circle.

Depth
   Height of the generated cone.

.. note::

   If the top and bottom radii are zero, this node will output a single line.


Properties
==========

Fill Type
   How the circles at the top and bottom are filled with faces when their radius is larger than zero.

   :None: Do not fill the circles.
   :N-Gon: Fill the innermost segment of the circles with a single face.
   :Triangles: Fill the innermost segment of the circles with triangles connected to a new vertex on the Z axis.


Outputs
=======

Mesh
   Standard geometry output.

Top
   A boolean attribute field with a selection of the faces on the top of the cone. If the *Fill Type*
   property is set to none, then this will be a selection of the top edges instead. If *Radius Top*
   is zero, this will be a selection of the top vertex.

Side
   A boolean attribute field with a selection of the faces on the side of the cone.

Bottom
   A boolean attribute field with a selection of the faces on the bottom of the cone. If the *Fill Type*
   property is set to none, then this will be a selection of the bottom edges instead. If *Radius Bottom*
   is zero, this will be a selection of the top vertex.
