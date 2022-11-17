.. index:: Geometry Nodes; Distribute Points in Volume
.. _bpy.types.GeometryNodeDistributePointsInVolume:

***************************
Distribute Points in Volume
***************************

.. figure:: /images/node-types_GeometryNodeDistributePointsInVolume.png
   :align: center
   :alt: Distribute Points in Volume node.


The *Distribute Points in Volume* node creates points inside of volume grids.
The node has two basic modes of operation: distributing points randomly, or in
a regular grid. Both methods operate on all of the float grids in the volume.


Inputs
======

Volume
   Standard volume geometry input.

Density
   Number of points to sample per unit volume.

Spacing
   Spacing between grid points.

Threshold
   Minimum value of a volume cell to contain a grid point


Properties
==========

Distribution Method
   :Random:
      Distribute points randomly inside of the volume. The local point count is implicitly
      defined as a product of of the global from the *Density* input and the local voxel value.
      This method creates a distribution that is not stable as the input volume deforms.
   :Grid:
      Distribute the points in a grid pattern inside of the volume. At each grid point, the voxel
      value is used to determine whether to add a point.


Outputs
=======

Points
   Standard point cloud geometry output.
