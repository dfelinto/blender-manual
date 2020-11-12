.. _bpy.types.ShaderNodeCameraData:

****************
Camera Data Node
****************

.. figure:: /images/render_shader-nodes_input_camera-data_node.png
   :align: right

   Camera Data Node.

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
   A camera space vector from the camera to the shading point.
View Z Depth
   The distance each pixel is away from the camera.
View Distance
   Distance from the camera to the shading point.
