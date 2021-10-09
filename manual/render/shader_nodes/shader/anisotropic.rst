.. _bpy.types.ShaderNodeBsdfAnisotropic:

****************
Anisotropic BSDF
****************

.. figure:: /images/render_shader-nodes_shader_anisotropic_node.png
   :align: right

   Anisotropic BSDF.

:guilabel:`Cycles Only`

The *Anisotropic* :abbr:`BSDF (Bidirectional Scattering Distribution Function)`
is used to add a glossy reflection, with separate control over U and V direction roughness.
The tangents used for shading are derived from the active UV map. If no UV map is available,
they are automatically generated using a sphere mapping based on the mesh bounding box.


Inputs
======

Color
   Color of the surface, or physically speaking, the probability that light is reflected for each wavelength.
Roughness
   Sharpness of the reflection; perfectly sharp at 0.0 and smoother with higher values.
Anisotropy
   Amount of anisotropy in the reflection; 0.0 gives a round highlight.
   Higher values give elongated highlights orthogonal to the tangent direction;
   negative values give highlights shaped along the tangent direction.
Rotation
   Rotation of the anisotropic tangent direction.
   Value 0.0 equals 0° rotation, 0.25 equals 90° and 1.0 equals 360° = 0°.
   This can be used to texture the tangent direction.
Normal
   Normal used for shading; if nothing is connected the default shading normal is used.
Tangent
   Tangent used for shading; if nothing is connected the default shading tangent is used.


Properties
==========

Distribution
   Microfacet distribution to use. *Sharp* results in perfectly sharp reflections like a mirror,
   while *Beckmann*, *GGX* and *Ashikhmin-Shirley* can use the *Roughness* input for blurry reflections.


Outputs
=======

BSDF
   Standard shader output.


Examples
========

.. list-table::

   * - .. figure:: /images/render_shader-nodes_shader_anisotropic_rot0.jpg

          Anisotropic rotation on 0.

     - .. figure:: /images/render_shader-nodes_shader_anisotropic_rot025.jpg

          Anisotropic rotation on 0.25 (90°).

.. figure:: /images/render_shader-nodes_shader_anisotropic_example.jpg

   Anisotropic shading with 0° rotation, 90° rotation and textured rotation of the tangent direction.
   `Example blend-file <https://en.blender.org/uploads/b/b7/Blender2.65_cycles_anisotropic.blend>`__.
