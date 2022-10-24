.. _bpy.types.ShaderNodeCameraData:

****************
Camera Data Node
****************

.. figure:: /images/node-types_ShaderNodeCameraData.webp
   :align: right
   :alt: Camera Data Node.

The *Camera Data* node is used to get information about the position of
the object relative to the camera. This could be used for example to change
the shading of objects further away from the camera, or make custom fog effects.


Inputs
======

This node has no inputs.


Properties
==========

This node has no properties.


Outputs
=======

View Vector
   A normalized vector, in camera space, from the camera to the shading point.
View Z Depth
   The distance each pixel is away from the camera.
View Distance
   Distance from the camera to the shading point.
