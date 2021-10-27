.. index:: Geometry Nodes: Volume to Mesh
.. _bpy.types.GeometryNodeVolumeToMesh:

*******************
Volume to Mesh Node
*******************

.. figure:: /images/modeling_geometry-nodes_volume_volume-to-mesh_node.png
   :align: center

   The Volume to Mesh node.

The *Volume to Mesh* node generates a mesh on the "surface" of a volume.
The surface is defined by a threshold value.
All voxels with a larger value than the threshold are considered to be inside.


Inputs
======

Geometry
   Standard geometry inputs.

Voxel Amount
   Specifies the approximate resolution of the final mesh.
   The voxel size is adapted to the size of the entire volume.

Voxel Size
   Use a fixed resolution that does not change when the volume changes.

Threshold
   Voxels with a larger value are considered to be inside the mesh.

Adaptivity
   Reduces the final face count by simplifying geometry where detail is not needed.


Properties
==========

Resolution Mode
   Mode for how the resolution of the final mesh is controlled.

   :Grid:
      This makes the resolution dependent on the resolution of the grid that is converted.
      Higher resolution grids result in a higher resolution mesh.
      In many cases, that is the most efficient mode.
   :Voxel Amount:
      Specifies the approximate resolution of the final mesh.
      The voxel size is adapted to the size of the entire volume.
   :Voxel Size:
      Use a fixed resolution that does not change when the volume changes.


Outputs
=======

Geometry
   Standard geometry output.
