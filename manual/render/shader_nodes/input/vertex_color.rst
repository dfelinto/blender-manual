.. _bpy.types.ShaderNodeVertexColor:

*****************
Vertex Color Node
*****************

.. figure:: /images/render_shader-nodes_input_vertex-color_node.png
   :align: right

   Vertex Color node.

The *Vertex Color* node provides vertex colors as well as their alpha value.


Inputs
======

This node has no inputs.


Properties
==========

Vertex Color
   The target vertex color.
   The listed vertex colors are those of the mesh of the active object.
   If the active object has no mesh, a warning will be displayed.
   If the property is marked in red, it means the vertex color is not available in
   the mesh of the active object, but it may be available in other meshes of
   objects that share this material!


Outputs
=======

Color
   Vertex color.
Alpha
   Alpha value.
