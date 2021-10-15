.. index:: Geometry Nodes; Points to Volume
.. _bpy.types.GeometryNodePointsToVolume:

*********************
Points to Volume Node
*********************

.. figure:: /images/modeling_geometry-nodes_volume_points-to-volume_node.png
   :align: center

   The Points to Volume node.

The *Points to Volume* node generates a fog volume sphere around every point in the input geometry.
The new volume grid is named "density".


Inputs
======

Geometry
   Standard geometry input.

Density
   Value of voxels inside the generated fog volume.

Voxel Amount
   Specify the approximate number of voxels along the diagonal.

Voxel Size
   Specify the voxel side length.

Radius
   Specify the radius of the sphere generated at each point.


Properties
==========

Resolution
   How the voxel size is specified.


Outputs
=======

Geometry
   Standard geometry output.
