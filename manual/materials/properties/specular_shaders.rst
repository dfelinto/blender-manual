
Specular Shaders
****************

.. admonition:: Reference
   :class: refbox

   | Mode:     All Modes
   | Panel:    Shading/Material Context → Specular


Specular shaders create the bright highlights that one would see on a glossy surface,
mimicking the reflection of light sources. Unlike :doc:`diffuse shading </materials/properties/diffuse_shaders>`,
specular reflection is *viewpoint dependent*.
According to Snell's Law, light striking a specular surface will be reflected at an angle which mirrors the
incident light angle (with regard to the surface's normal), which makes the viewing angle very important.


.. tip:: Not a Mirror!

   It is important to stress that the *specular reflection*
   phenomenon discussed here is not the reflection we would see in a mirror,
   but rather the light highlights we would see on a glossy surface.
   To obtain true mirror-like reflections you would need to use the internal raytracer.
   Please refer to section :doc:`RENDERING </render>` of this manual.


Common Options
==============

Each specular shader share the following common options:

Specular Color
   The color of the specular highlight
Intensity
   The intensity, or brightness of the specular highlight. This has a range of [0-1].
Ramp
   Allows you to set a range of specular colors for :guilabel:`Material`,
   and define how the range will vary over a surface. See :doc:`Ramps </materials/properties/ramps>` for details.

As a result, a material has at least two different colors, a diffuse, and a specular one.
The specular color is normally set to pure white
(the same "pure white" as the reflected light source),
but it can be set to different values for various effects (e.g.
metals tend to have colored highlights).


Technical Details
-----------------

.. figure:: /images/Manual-Part-III-MatGen03.jpg

   Specular Reflection.


In reality, the quality of Diffuse and Specular reflection are generated during the same
process of light scattering, but are not the same.
Diffusion is actually subsurface scattering at a very small scale.

Imagine that a surface is made up of extremely microscopic semi-transparent,
reflective facets. The sharpness of Specular reflection is determined by the distribution of
the angle of these microfacets on the surface of an object.
The more deep and jagged these facets are,
the more the light spreads when it hits the surface.
When these facets are flatter against the "macrosurface",
the surface will have a tighter reflection, closer to a mirror.
This is a condensed explanation of the generally accepted microfacet theory of reflectance,
which is the basis of all modern BRDFs (Bi-directional Reflectance Distribution Functions),
or shading models.

Because these microfacets are transparent,
some light that hits them travels into the surface and diffuses.
The light that makes it back out is roughly Lambertian most of the time,
meaning that it spreads evenly in all directions.
It is also attenuated by the pigmentation in the surface,
hence creating what we perceive as diffuse, and the color of an object.

Note that at glancing angles, the reflectivity of a surface will always go to 1.

If it is difficult for you to understand this relationship, try to imagine a ball (say,
of centimeter scale): if you throw it against a wall of raw stones
(with a scale of roughness of a decimeter), it will bounce in a different direction each time,
and you will likely quickly lose it! On the other hand,
if you throw it against a smooth concrete wall (with a roughness of, say, a millimeter scale),
you can quite easily anticipate its bounce, which follow (more or less!)
the same law as the light reflection.


CookTorr
========

.. admonition:: Reference
   :class: refbox

   | Mode:     All Modes
   | Panel:    Shading/Material Context → Shaders


.. figure:: /images/Manual-2.5-Material-Shader-CookTorr.jpg
   :width: 320px
   :figwidth: 320px

   CookTorr Shader (Lambert 0.8)


CookTorr (Cook-Torrance)
is a basic specular shader that is most useful for creating shiny plastic surfaces.
It is a slightly optimized version of Phong.
Robert L. Cook (LucasFilm) and Kenneth E. Torrance (Cornell University) In their 1982 paper
`A Reflectance Model for Computer Graphics <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.83.7263&rep=rep1&type=pdf>`__ (PDF),
they described "a new reflectance model for rendering computer synthesized images"
and applied it to the simulation of metal and plastic.

Options
-------

**Hardness**
   Size of the specular highlight


Phong
=====

.. admonition:: Reference
   :class: refbox

   | Mode:     All Modes
   | Panel:    Shading/Material Context → Shaders


.. figure:: /images/Manual-2.5-Material-Shader-Phong.jpg
   :width: 320px
   :figwidth: 320px

   Phong Shader (Lambert 0.8)


Phong is a basic shader that's very similar to CookTorr,
but is better for skin and organic surfaces.
`Bui Tuong Phong <http://en.wikipedia.org/wiki/Bui_Tuong_Phong>`__ (1942-1975)
was a Vietnamese-born computer graphics pioneer that developed the first algorithm for simulating specular phenomenon.
`His model <http://en.wikipedia.org/wiki/Phong_reflection_model>`__
included components not only for specular lighting, but also diffuse and ambient lighting.

Options
-------

Hardness
   Size of the specular highlight.


.. tip:: Planet Atmosphere

   Because of its fuzziness, this shader is good for atmosphere around a planet.
   Add a sphere around the planet, slightly larger than the planet.
   For its material, use a phong specular shader.
   Set it to a very low alpha (.05), zero diffuse, low hardness (5) but high specularity (1).


Blinn
=====

.. admonition:: Reference
   :class: refbox

   | Mode:     All Modes
   | Panel:    Shading/Material Context → Shaders


.. figure:: /images/Manual-2.5-Material-Shader-Blinn.jpg
   :width: 320px
   :figwidth: 320px

   Blinn Shader (Oren-Nayar Int 0.8, Rough 0.5)


Blinn is a more 'physical' specular shader, often used with the Oren-Nayar diffuse shader.
It can be more controllable because it adds a fourth option, an *index of refraction* (IOR),
to the aforementioned three.
`James F. Blinn <http://en.wikipedia.org/wiki/Jim_Blinn>`__
worked at NASA's Jet Propulsion Laboratory and became widely known for his work
on Carl Sagan's TV documentary *Cosmos*.
The model he described in his 1977 paper
`Models of Light Reflection for Computer Synthesized Pictures <http://research.microsoft.com/pubs/73852/p192-blinn.pdf>`__
(PDF) included changes in specular intensity with light direction and more accurately positioned highlights on a surface.

Options
-------

Hardness
   Size of the specular highlight.
   The Blinn shader is capable of much tighter specular highlights than Phong or CookTorr.
IOR
   'Index of Refraction'.
   This parameter is not actually used to compute refraction of light rays through the material
   (a ray tracer is needed for that),
   but to correctly compute specular reflection intensity and extension via Snell's Law.


Toon
----


.. admonition:: Reference
   :class: refbox

   | Mode:     All Modes
   | Panel:    Shading/Material Context → Shaders


.. figure:: /images/Manual-2.5-Material-Shader-ToonSpec.jpg
   :width: 320px
   :figwidth: 320px

   Toon Specular Shader (Toon Diffuse, Int 0.8, Size & Smooth match)


The Toon specular shader matches the Toon diffuse shader. It is designed to produce the sharp,
uniform highlights of cartoon cels.

Options
-------

Size
   Size of the specular highlight.
Smooth
   Softness of the highlight's edge.

.. tip:: Alternative Method

   The Toon shader effect can also be accomplished in a more controllable way using ColorRamps.


WardIso
=======

.. admonition:: Reference
   :class: refbox

   | Mode:     All Modes
   | Panel:    Shading/Material Context → Shaders


.. figure:: /images/Manual-2.5-Material-Shader-WardIso.jpg
   :width: 320px
   :figwidth: 320px

   WardIso Shader


WardIso is a flexible specular shader that can be useful for metal or plastic.

Gregory J. Ward
   developed a relatively simple model that obeyed the most basic laws of physics.  In his 1992 paper,
   *Measuring and modeling anisotropic re?ection,* Ward introduced a Bidirectional Re?ectance Distribution Function
   (BRDF) since then widely used in computer graphics because the few parameters it uses are simple to control.
   His model could represent both isotropic surfaces (independent of light direction) and anisotropic surfaces
   (direction dependent). In Blender,
   the Ward specular shader is still called **Ward Isotropic** but is actually anisotropic.
   (`PDF <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.69.6812&rep=rep1&type=pdf>`__)



Options
-------

Slope
   Standard deviation for of surface slope.
   Previously known as the `root-mean-square <http://en.wikipedia.org/wiki/Root_mean_square>`__ or rms value,
   this parameter in effect controls the size of the specular highlight,
   though using a different method to that of the other specular shaders.
   It is capable of extremely sharp highlights.


