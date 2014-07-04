
Material Textures Influence
===========================

Not only can textures affect the color of a material,
they can also affect many of the other properties of a material. The different aspects of a
material that a texture influences are controlled in the :guilabel:`Influence` panel.

.. admonition:: Note
   :class: note

   Texture options for :guilabel:`Surface` and :guilabel:`Wire` materials and in some cases also for :guilabel:`Volume` and :guilabel:`Halo` materials.


Surface and Wire materials
--------------------------

.. figure:: /images/25-Manual-Textures-Influence-Surface.jpg
   :width: 308px
   :figwidth: 308px

   Texture Influence panel for a Surface material


Diffuse
_______

:guilabel:`Intensity`
   Amount texture affects affects diffuse reflectivity
:guilabel:`Color`
   Amount texture affect the basic color or RGB value of the material
:guilabel:`Alpha`
   Influences the opacity of the material. See :doc:`Use Alpha for Object Transparency <ls/textures/use_alpha_for_object_transparency>`. Also use :guilabel:`Z Transparency` for light and if combining multiple channels.
:guilabel:`Translucency`
   Influences the Translucency amount.


Specular
________

:guilabel:`Intensity`
   Amount texture affect specular reflectivity
:guilabel:`Color`
   Influences the :guilabel:`Specular` color, the color of the reflections created by the lamps on a glossy material.
:guilabel:`Hardness`
   Influences the specular hardness amount. A DVar of 1 is equivalent to a Hardness of 130, a DVar of 0.5 is equivalent to a Hardness of 65.


Shading
_______

:guilabel:`Ambient`
   Influences the amount of Ambient light the material receives.
:guilabel:`Emit`
   Influences the amount of light Emitted by the material.
:guilabel:`Mirror`
   Influences the mirror color. This works with environment maps and raytraced reflection.
:guilabel:`Ray Mirror`
   Influences the strength of raytraced mirror reflection.


Geometry
________

:guilabel:`Normal`
   Commonly called bump mapping, this alters the direction of the surface normal. This is used to fake surface imperfections or unevenness via bump mapping, or to create reliefs.
:guilabel:`Warp`
   :guilabel:`Warp` allows textures to influence/distort the texture coordinates of a next texture channel. The distortion remains active over all subsequent channels, until a new Warp has been set. Setting the factor at zero cancels out the effect.
:guilabel:`Displace`
   Influences the Displacement of vertices, for using :doc:`Displacement Maps <textures/influence/material/displacement>`.


Other Controls
~~~~~~~~~~~~~~

:guilabel:`Blend`
   Blending operation to perform. See :doc:`Texture Blending Modes <textures/influence/material/blending_modes>` for details.
:guilabel:`RGB to intensity`
   With this option enabled, an RGB texture (affects color) is used as an intensity texture (affects a value).
:guilabel:`Blend Color`
   If the texture is mapped to Col, what color is blended in according to the intensity of the texture? Click on the swatch or set the RGB sliders.
:guilabel:`Negative`
   The effect of the Texture is negated. Normally white means on, black means off, :guilabel:`Negative` reverses that.
:guilabel:`Stencil`
   The active texture is used as a mask for all following textures. This is useful for semitransparent textures and "Dirt Maps". Black sets the pixel to "untexturable".  The :guilabel:`Stencil` mode works similar to a layer mask in a 2D program. The effect of a stencil texture can not be overridden, only extended. You need an intensity map as input.
:guilabel:`DVar`
   Destination Value (not for RGB). The value with which the Intensity texture blends with the current value. Two examples:


- The :guilabel:`Emit` value is normally 0. With a texture mapped to :guilabel:`Emit` you will get maximal effect, because :guilabel:`DVar` is 1 by default. If you set :guilabel:`DVar` to 0 no texture will have any effect.


- If you want transparent material, and use a texture mapped to :guilabel:`Alpha`, nothing happens with the default settings, because the :guilabel:`Alpha` value in the :guilabel:`Material` panel is 1. So you have to set :guilabel:`DVar` to 0 to get transparent material (and of course :guilabel:`Z Transparency` also). This is a common problem for beginners. Or do it the other way round - set :guilabel:`Alpha` to 0 and leave :guilabel:`Dvar` on 1. Of course the texture is used inverted then.

:guilabel:`Bump Mapping`
   Settings for bump mapping.
   :guilabel:`Method`
   :guilabel:`Best Quality`, :guilabel:`Default`, :guilabel:`Compatible`, :guilabel:`Original`
   :guilabel:`Space`

      :guilabel:`Texture Space`, :guilabel:`Object Space`, :guilabel:`View Space`


Volume materials
----------------

.. figure:: /images/25-Manual-Textures-Influence-Volume.jpg
   :width: 308px
   :figwidth: 308px

   Texture Influence panel for Volume material


Special texture options for :guilabel:`Volume` materials

:guilabel:`Density`
   Causes the texture to affect the volume's density.
:guilabel:`Emission`
   Causes the texture to affect the volume's emission.
:guilabel:`Scattering`
   Amount the texture affects scattering.
:guilabel:`Reflection`
   Amount the texture affects brightness of out-scattered light
:guilabel:`Emission Color`
   Amount the texture affects emission color.
:guilabel:`Transmission`
   Amount the texture affects result color after light has been scattered/absorbed.
:guilabel:`Reflection Color`
   Amount the texture affects color of out-scattered light.


Halo materials
--------------

.. figure:: /images/25-Manual-Textures-Influence-Halo.jpg
   :width: 308px
   :figwidth: 308px

   Texture Influence panel for a Halo material


Special texture options for :guilabel:`Halo` materials

:guilabel:`Size`
   Amount the texture affects ray mirror.
:guilabel:`Hardness`
   Amount the texture affects hardness.
:guilabel:`Add`
   Amount the texture affects translucency.

