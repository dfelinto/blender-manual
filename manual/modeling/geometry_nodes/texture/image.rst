.. index:: Geometry Nodes; Texture
.. _bpy.types.GeoNodeImageTexture:

.. note::

   Unlike the other texure nodes, this node operates diffently 
   in Geometry Nodes compared to the equivalent Shader node. 
   When not connected the Vector input has an implicit Position attribute value.

.. _bpy.types.ShaderNodeTexImage:

******************
Image Texture Node
******************

.. figure:: /images/modeling_geometry-nodes_texture-nodes_image_texture_node.jpg
   :align: right

   Image Texture Node.

The *Image Texture*  node is used to add an image file as a texture. 
The image data is sampled with the input Vector and ouputs a Color and Alpha value.  


Inputs
======

Image
   The image socket can be used to connect to the Group Input node. 
   If this is not connected the image can be opened or selected from the node.

Vector
   Texture coordinate for texture look-up. If this socket is left unconnected,
   the Position attribute is used.
   
Frame
   If the Image supports animation, the frame can be set here. 
   This can be keyframed so that the image changes between frames.

Properties
==========

Interpolation
   Method to scale images up or down for sampling.

   :Linear: Regular quality interpolation.
   :Cubic: Smoother, better quality interpolation. For bump maps this should be used to get best results.
   :Closest: No interpolation, use only closest pixel for rendering pixel art.

Extension
   Extension defines how the image is extrapolated past the original bounds:

   :Repeat: Will repeat the image horizontally and vertically giving tiled-looking result.
   :Extend: Will extend the image by repeating pixels on its edges.
   :Clip: Clip to the original image size and set all the exterior pixels values to transparent black.


Outputs
=======

Color
   RGBA color from the image. If the image has alpha, the color is premultiplied with alpha if the Alpha output is used,
   and unpremultiplied or straight if the Alpha output is not used.
Alpha
   Alpha channel from image.
