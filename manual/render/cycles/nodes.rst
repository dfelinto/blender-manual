
Nodes
*****

Materials, lights and backgrounds are all defined using a network of shading nodes.
These nodes output values, vectors, colors and shaders.


[[/Shaders|'''Shaders''']]
==========================

An important concept to understand when building node setups is that of the **shader
socket**. The output of all surface and volume shaders is a shader,
describing lighting interaction at the surface or of the volume,
rather than the color of the surface.

There are a few types of shaders available as nodes:


- :abbr:`BSDF (Bidirectional scattering distribution function)` shader describing light reflection, refraction and absorption at an object surface.
- **Emission** shader describing light emission at an object surface or in a volume.
- **Volume** shader describing light scattering inside a volume.
- **Background** shader describing light emission from the environment.

Each shader node has a color input, and outputs a shader.
These can then be mixed and added together using Mix and Add Shader nodes.
No other operations are permitted.
The resulting output can then be used by the render engine to compute all light interactions,
for direct lighting or global illumination.


[[/Textures|'''Textures''']]
============================

Each texture type in Cycles corresponds to a node,
with a texture coordinate and various parameters as input, and a color or value as output.
No texture datablocks are needed; instead node groups can be used for reusing texture setups.

For UV mapping and texture painting in the viewport, the Image texture node must be used.
When setting such a node as active, it will be drawn in Textured draw mode,
and can be painted on in texture paint mode.

The default texture coordinates for all nodes are Generated coordinates,
with the exception of Image textures that use UV coordinates by default.
Each node includes some options to modify the texture mapping and resulting color,
and these can be edited in the texture properties.


[[/More|'''More''']]
====================

Nodes for geometric data, texture coordinates,
layering shaders and non-physically based tricks.


[[/OSL|'''Open Shading Language''']]
====================================

Custom nodes can be written using the Open Shading Language.