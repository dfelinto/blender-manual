.. index:: Geometry Nodes; Mesh to Volume
.. _bpy.types.GeometryNodeMeshToVolume:

*******************
Mesh to Volume Node
*******************

.. figure:: /images/node-types_GeometryNodeMeshToVolume.png
   :align: right
   :alt: Mesh to Volume node.

The *Mesh to Volume* node creates a fog volumes based on the shape of a mesh.
The volume is created with a grid of the name `"density"`.


Inputs
======

Mesh
   Standard Mesh input.

Density
   Value of voxels inside the generated fog volume.

Voxel Amount
   Specify the approximate number of voxels along the diagonal.

Voxel Size
   Specify the voxel side length.

Exterior Band Width
   The maximum distance of the included voxels to the surface on the outside of the mesh.

Interior Band Width
   The maximum distance of the included voxels to the surface on the inside of the mesh.
   Activating *Fill Volume* is similar to increasing the interior band width to a high number.

Fill Volume
   The entire enclosed volume or otherwise only the voxels close to the surface
   will get a density greater than zero.
   This setting is only used when the mesh object is :term:`Manifold`.


Properties
==========

Resolution
   How the voxel size is specified.

   :Amount:
      Specify the approximate number of voxels along the diagonal.

   :Size:
      Specify the voxel side length. It is recommended to be careful when tweaking this value,
      because small changes can have a large effect on the processing time.


Outputs
=======

Volume
   The generated volume grid.
