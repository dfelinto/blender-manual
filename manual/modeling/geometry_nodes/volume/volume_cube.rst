.. index:: Geometry Nodes: Volume Cube
.. _bpy.types.GeometryNodeVolumeCube:

****************
Volume Cube Node
****************

.. figure:: /images/node-types_GeometryNodeVolumeCube.png
   :align: right
   :alt: The Volume Cube node.

The *Volume Cube* generates a volume from scratch by evaluating an input field on every single
voxel in a rectangular prism. The *Density* field defines the output volume grid's value at every
voxel. The field can only depend on the :doc:`/modeling/geometry_nodes/input/position`.


Inputs
======

Density
   The value for the new grid at each voxel.

Background
   The value of the grid outside the rectangular prism controlled by the *Min* and *Max* inputs.
   The node can generate a more memory-efficient volume when the values of the *Density* input are
   the same as the background value.

Min
   One corner of the rectangular prism in which to fill evaluate the field.

Max
   The other corner of the rectangular prism in which to fill evaluate the field. 

Resolution X,Y,Z
   The number of voxels to evaluate the field in on each axis.

   .. note::
      Changing these values can have a significant impact on performance. For example, the default values
      of 32 mean the input field will be evaluated about 33 thousand times. Increasing the values to 100
      will give 1 million evaluations, and 1000 would give 1 billion.


Properties
==========

This node has no properties.


Outputs
=======

Volume
   Geometry containing the generated volume.
