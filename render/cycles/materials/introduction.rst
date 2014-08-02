
Introduction
************

Materials define the appearance of meshes, curves and other objects.
They consist of three shaders, defining the appearance of the surface of the mesh,
the volume inside the mesh, and displacement of the surface of the mesh.


.. figure:: /images/Manual_cycles_material_shaders.jpg


:ref:`Surface Shader <render-cycles-materials-volume>`
======================================================

The surface shader defines the light interaction at the surface of the mesh. One or more
:abbr:`BSDF (Bidirectional scattering distribution function)` s specify if incoming light is
reflected back, refracted into the mesh, or absorbed.

Emission defines how light is emitted from the surface,
allowing any surface to become a light source.


:ref:`Volume Shader <render-cycles-materials-volume>`
=====================================================

When the surface shader does not reflect or absorb light, it enters into the volume.
If no volume shader is specified, it will pass straight through to the other side of the mesh.

If it is defined,
a volume shader describes the light interaction as it passes through the volume of the mesh.
Light may be scattered, absorbed, or emitted at any point in the volume.

A material may have both a surface and a volume shader, or only one of either.
Using both may be useful for materials such as glass, water or ice,
where you want some of the light to be absorbed as it passes through the surface,
combined with e.g. a glass or glossy shader at the surface.


:ref:`Displacement <render-cycles-materials-displacement>`
==========================================================

The shape of the surface and the volume inside it may be altered by displacement shaders.
This way, textures can then be used to make the mesh surface more detailed.

Depending on the settings, the displacement may be virtual,
only modifying the surface normals to give the impression of displacement,
which is known as bump mapping, or a combination of real and virtual displacement.


Energy Conservation
===================

The material system is built with physics-based rendering in mind,
cleanly separating how a material looks and which rendering algorithm is used to render it.
This makes it easier to achieve realistic results and balanced lighting,
though there are a few things to keep in mind.

In order for materials to work well with global illumination, they should be,
speaking in terms of physics, energy conserving.
That means they cannot reflect more light than comes in.
This property is not strictly enforced, but if colors are in the range 0.0 to 1.0, and
:abbr:`BSDF (Bidirectional scattering distribution function)` s are only mixed together with the
Mix Shader node, this will automatically be true.

It is however possible to break this,
with color values higher than 1.0 or using the Add Shader node, but one must be careful when
doing this to keep materials behaving predictably under various lighting conditions.
It can result in a reflection adding light into the system at each bounce,
turning a :abbr:`BSDF (Bidirectional scattering distribution function)` into a kind of emitter.
