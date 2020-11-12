.. _bpy.types.ShaderNodeUVMap:

***********
UV Map Node
***********

.. figure:: /images/render_shader-nodes_input_uv-map_node.png
   :align: right

   UV Map Node.

The *UV Map* node is used to retrieve specific UV maps.
Unlike the :doc:`Texture Coordinate Node </render/shader_nodes/input/texture_coordinate>`
which only provides the active UV map,
this node can retrieve any UV map belonging to the object using the material.


Inputs
======

This node has no inputs.


Properties
==========

From Instancer :guilabel:`Cycles Only`
   See the :ref:`From Instancer <cycles-nodes-input-texture-coordinate-from-instancer>`
   option of the :doc:`Texture Coordinate Node </render/shader_nodes/input/texture_coordinate>`.

UV Map
   UV map to use.


Outputs
=======

UV
   UV mapping coordinates from the specified UV map.
