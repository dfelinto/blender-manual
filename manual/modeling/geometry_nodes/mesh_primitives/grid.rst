.. index:: Geometry Nodes; Grid
.. _bpy.types.GeometryNodeMeshGrid:

****
Grid
****

.. figure:: /images/modeling_geometry-nodes_mesh-primitives_plane_node.png
   :align: right

   Grid Node.

The *Grid* node generates a planar mesh on the XY plane.


Inputs
======

Size X
   Side length of the plane in the X direction.

Size Y
   Side length of the plane in the Y direction.

Vertices X
   Number of vertices in the X direction.
   If this is smaller than two, no mesh is generated.

Vertices Y
   Number of vertices in the Y direction.
   If this is smaller than two, no mesh is generated.

Outputs
=======

Geometry
   Standard geometry output containing the generated mesh.
