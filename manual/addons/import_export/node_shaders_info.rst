
*******************************
Import & Export of Node Shaders
*******************************

While Blender now only supports the advanced node-based shading model for its materials,
most :abbr:`IO (Input/Output)` formats only support a basic shading model,
similar to the legacy fixed pipeline of old GPUs.

Blender features a way to convert between those, which any add-on can use, but it is currently pretty basic still.
Especially for exporting from Blender materials, the node system must follow some strict requirements.

.. note::

   Currently, only the
   :doc:`OBJ </addons/import_export/scene_obj>` and
   :doc:`FBX </addons/import_export/scene_fbx>`
   IO add-ons uses that method.

.. tip::

   The :doc:`glTF </addons/import_export/scene_gltf2>` format
   uses a more detailed conversion to and from shader nodes.

.. note::

   The wrapper is designed to be as symmetrical as possible
   (i.e. it is expected to give reproducible results across several import/export cycles).

.. figure:: /images/addons_import-export_node-shaders-info_example.png
   :align: center

   A typical setup of shader nodes that is can be exported.


Supported Node Setup
====================

This is especially important for exporting, importing will simply re-generate a similar setup.

Note that the features listed below are those supported by the wrapper.
Each add-on may have its own way to adapt them to its material system, some may not be handled by it, etc.

Principled BSDF
   The main shader must be a :doc:`Principled BSDF </render/shader_nodes/shader/principled>`.
   Only parameters defined there, and textures linked to it, will be exported.

   Currently handled parameters:

   - Base color
   - Specular intensity
   - Specular tint *(no texture support)*
   - Roughness
   - Metallic
   - IOR
   - Transmission
   - Alpha

Normal Map
   If linked to the Normal input of the Principled BSDF node,
   the :doc:`Normal Map </render/shader_nodes/vector/normal_map>` node is also supported
   (including its texture obviously).

Textures
   Only :doc:`Image </render/shader_nodes/textures/image>` textures using a UV mapping are supported.
   You may also use a :doc:`Mapping </render/shader_nodes/vector/mapping>` node to move/rotate/scale it.
