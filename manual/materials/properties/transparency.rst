
Transparency
************

.. admonition:: Reference
   :class: refbox

   | Mode:     All Modes
   | Panel:    Shading/Material Context → Transparency


Materials in Blender can be set to be transparent,
so that light can pass through any objects using the material.
Transparency is controlled using an "alpha" channel, where each pixel has an additional value,
range 0-1, in addition to its RGB color values. If alpha=0, then the pixel is transparent,
and the RGB values for the surface contribute nothing to the pixel's appearance; for alpha=1,
the surface is fully opaque,
and the color of the surface determines the final color of the pixel.


.. figure:: /images/Doc_2.6_Materials_Properties_Transparency.jpg

   Transparency Panel


In Blender, there are three ways in which the transparency of a material can be set:
Mask, Z-Buffer and Ray-trace. Each of these is explained in more detail below.
The :doc:`Material Preview </materials/properties/preview>` option with a sphere object
gives a good demonstration of the capabilities of these three options.


Common Options
==============

The following property controls are available for all transparency options:

Alpha
   Sets the transparency of the material by setting all pixels in the alpha channel to the given value.
Fresnel
   Sets the power of the Fresnel effect.
   The Fresnel effect controls how transparent the material is,
   depending on the angle between the surface normal and the viewing direction.
   Typically, the larger the angle, the more opaque a material becomes
   (this generally occurs on the outline of the object).
Specular -
   Controls the alpha/falloff for the specular color.
Blend
   Controls the blending between transparent and non-transparent areas. Only used if Fresnel is greater than 0.


Mask

----


This option simply masks the Background.  It uses the alpha channel to mix the color of each
pixel on the active object plane with the color of the corresponding background pixel,
according to the alpha channel of the pixel. Thus for alpha = 1,
the object color is seen - the object is completely opaque; but if alpha = 0,
only the background is seen - the object is transparent
(but note that any other object behind the active object disappears).

This is useful for making textures of solid or semi-transparent objects from photographic
reference material - a mask is made with alpha opaque for pixels within the object,
and transparent for pixels outside the object.

See :doc:`Mask Transparency </materials/properties/mask_transparency>`.


Z Buffer
========

This uses the alpha buffer for transparent faces.
The alpha value of each pixel determines the mix of the basic color of the material,
and the color of the pixel is determined from the objects/background behind it.
Only basic settings are available with this option; it does not calculate refractions.


Raytraced Transparency
======================

Uses ray tracing to calculate refractions. Ray tracing allows for complex refractions,
falloff, and blurring,
and is used for simulating the refraction of light rays through a transparent material,
like a lens.

Note that the RayTrace option is only available in the Blender Render and Cycles render
engines, but not in the Game Engine.

A ray is sent from the camera and travels through the scene until it encounters an object.
If the first object hit by the ray is non-transparent,
then the ray takes the color of the object.

If the object is transparent, then the ray continues its path through it to the next object,
and so on, until a non-transparent object is finally encountered which gives the whole chain
of rays its color. Eventually,
the first transparent object inherits the colors of its background,
proportional to its :guilabel:`Alpha` value
(and the Alpha value of each transparent Material hit in between).

But while the ray travels through the transparent object,
it can be deflected from its course according to the Index of Refraction (IOR)
of the material. When you actually look through a plain sphere of glass,
you will notice that the background is upside-down and distorted:
this is all because of the Index of Refraction of glass.


.. note:: Enable Raytracing

   To get ray-traced transparency, you need to:

   - enable ray tracing in your Render settings.  This is done in the Render context  → Shading Panel. Ray tracing is enabled by default.
   - set your Alpha value to something other than 1.0.
   - in order for the background material to receive light passing through your transparent object, :guilabel:`Receive Transparent` must be turned on for that material in the Material → Shadow panel.


Options
=======

.. figure:: /images/Manual-2.5-Material-RaytracedTransp-Panel.jpg

   The Transparency Panel.


In addition to the common options given above, the following property controls are available:

IOR
   Index of Refraction.  Sets how much a ray traveling through the material will be refracted,
   hence producing a distorted image of its background.  See
   FIXME(TODO: Internal Link; [[#IOR values for Common Materials|IOR values for Common Materials]]) below.
Filter
   Amount of filtering for transparent ray trace. The higher this value,
   the more the base color of the material will show. The material will still be transparent but it will start to take on the color of the material. Disabled (0.0) by default.
Falloff
   How fast light is absorbed as it passes through the material. Gives 'depth' and 'thickness' to glass.
Limit
   Materials thicker than this are not transparent.
   This is used to control the threshold after which the filter color starts to come into play.
Depth
   Sets the maximum number of transparent surfaces a single ray can travel through. There is no typical value.
   Transparent objects outside the :guilabel:`Depth` range will be rendered pitch black if viewed through the
   transparent object that the :guilabel:`Depth` is set for.  In other words,
   if you notice black areas on the surface of a transparent object,
   the solution is probably to increase its :guilabel:`Depth` value
   (this is a common issue with ray tracing transparent objects).
   You may also need to turn on transparent shadows on the background object.

Gloss
   Settings for the glossiness of the material.

   Amount
      The clarity of the refraction. Set this to something lower than zero to get a blurry refraction.
   Threshold
      Threshold for adaptive sampling. If a sample contributes less than this amount (as a percentage), sampling is stopped.
   Samples
      Number of cone samples averaged for blurry refraction.


Examples
========

Index of Refraction
-------------------

.. figure:: /images/Manual-2.5-Material-RaytracedTransp-IOR-Examples.jpg

   Influence of the IOR of an Object on the distortion of the background: spheres of Water, Glass and Diamond (top to bottom).


(*Influence of the IOR of an Object on the distortion of the background: spheres of Water, Glass  and Diamond (top to bottom).*). There are different values for typical materials: Air is **1.000** (no refraction), Alcohol is **1.329**, Glass is **1.517**, Plastic is **1.460**, Water is **1.333** and Diamond is **2.417**.


Fresnel
-------

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
+.. figure:: /images/Manual-2.5-Material-RayTraceTransp-FresnelExampel.jpg                                                                                                                                                                                                                                                                               |.. figure:: /images/Manual-2.5-Material-RayTraceTransp-FresnelExampelZTransp.jpg +
+   :width: 320px                                                                                                                                                                                                                                                                                                                                        |   :width: 320px                                                                 +
+   :figwidth: 320px                                                                                                                                                                                                                                                                                                                                     |   :figwidth: 320px                                                              +
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
+16 pieces of glass rotated in various directions demonstrate the angle-dependent Fresnel effect with ray-traced (left) and alpha buffered transparency (right).  Note that the major difference is the lack of IOR effect in the latter case.  (Download `.blend <http://wiki.blender.org/index.php/:File:Manual25-Material-FresnelExample.blend>`__.)                                                                                    +
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
+.. figure:: /images/Manual-2.5-Material-RayTraceTransp-FresnelSettings.jpg                                                                                                                                                                                                                                                                              |.. figure:: /images/Manual-2.5-Material-RayTraceTransp-FresnelSettingsZTransp.jpg+
+   :width: 320px                                                                                                                                                                                                                                                                                                                                        |   :width: 320px                                                                 +
+   :figwidth: 320px                                                                                                                                                                                                                                                                                                                                     |   :figwidth: 320px                                                              +
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
+Settings for Fresnel using ray-traced (left) and Z transparency (right).                                                                                                                                                                                                                                                                                                                                                                  +
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+


Note the specular highlight in the F4 glass tile
(which is facing midway between the light and the camera); the Fresnel effect can be seen in
row C and column 6 where the faces are turned away from the camera.

The amount of Fresnel effect can be controlled by either increasing the :guilabel:`Blend`
value or decreasing the :guilabel:`Alpha` value.


Depth
-----

.. figure:: /images/Manual-2.5-Material-Transp-3GlassesExample.jpg
   :width: 640px
   :figwidth: 640px

   A simple scene with three glasses on a surface, and three lamps.  Depth was set to 4, 8, 12, and 14, resulting in render times of 24 sec, 34 sec, 6 min, and 11 min respectively. (Download `.blend <http://wiki.blender.org/index.php/:File:Manual25-Material-3GlassesExample.blend>`__.)


Increasing :guilabel:`Depth` also considerably increases render time.
Each time a light ray passes through a surface,
the ray-tracing algorithm is called recursively.  In the example above,
each side of each glass has an exterior and an interior surface.
Light rays thus have to pass through four surfaces for each glass.

But not only that, at every point on a surface, some of the light can be reflected,
or mirrored off the surface in various directions.
This results in multiple rays needing to be calculated for each point
(often referred to as a **tree of rays** [http://www.cs.unc.edu/~rademach/xroads-RT/RTarticle.
html]). In each of the rendered images above there are 640×400=256 000 pixels.
By increasing :guilabel:`Depth`, at least one tree of rays is added to each pixel.

Be kind to your computer. Carefully placing objects in a scene to avoid overlapping
transparent objects is often an interesting alternative.


Hints
*****

Transparent shadows
===================

+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+
+.. figure:: /images/Manual25-Material-TranspShadow-Example-NoTraSha.jpg                     |.. figure:: /images/Manual25-Material-TranspShadow-Example-EnvLight.jpg  +
+   :width: 320px                                                                            |   :width: 320px                                                         +
+   :figwidth: 320px                                                                         |   :figwidth: 320px                                                      +
+                                                                                            |                                                                         +
+   No transparent shadows                                                                   |   No transparent shadows, environment lighting enabled                  +
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+
+.. figure:: /images/Manual25-Material-TranspShadow-Example-TraSha.jpg                       |.. figure:: /images/Manual25-Material-TranspShadow-Example-TraSha2.jpg   +
+   :width: 320px                                                                            |   :width: 320px                                                         +
+   :figwidth: 320px                                                                         |   :figwidth: 320px                                                      +
+                                                                                            |                                                                         +
+   Transparent shadows enabled, alpha set to 0.0                                            |   As previous, alpha set to 0.25                                        +
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+
+.. figure:: /images/Manual25-Material-TranspShadow-Example-TraSha-AO1.jpg                   |.. figure:: /images/Manual25-Material-TranspShadow-Example-TraSha-AO2.jpg+
+   :width: 320px                                                                            |   :width: 320px                                                         +
+   :figwidth: 320px                                                                         |   :figwidth: 320px                                                      +
+                                                                                            |                                                                         +
+   Transparent shadows with ambient occlusion set to multiply, distance 1 (radius of sphere)|   As previous, distance increased to 2 (diameter of sphere)             +
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+

By default, the shadows of transparent objects are rendered solid black,
as if the object was not transparent at all. But in reality,
the more transparent an object is, the lighter its shadow will be.

In Blender, transparent shadows are set on the materials that receive the shadows from the
transparent object.
This is enabled and disabled with the :guilabel:`Receive Transparent` button,
in the :guilabel:`Material` context → :guilabel:`Shadow` panel. The shadow's brightness is
dependent on the :guilabel:`Alpha` value of the shadow casting material.

Alternatives to transparent ray-traced shadows can be found in the :guilabel:`World` context,
namely the :guilabel:`Ambient Occlusion`, :guilabel:`Environment Lighting`,
and :guilabel:`Gather` panels.  Alternatively, a texture can be used to control the
:guilabel:`Intensity` value of the shadow-receiving material.


IOR values for Common Materials
===============================

The following list provides some index of refraction values to use when ray-traced
transparency is used for various liquids, solids (gems), and gases:

Acetone
   ``1.36``
Actinolite
   ``1.618``
Agalmatolite
   ``1.550``
Agate
   ``1.544``
Agate
   ``1.540``
Air
   ``1.000``
Alcohol
   ``1.329``
Alcohol, Ethyl (grain)
   ``1.36``
Alexandrite
   ``1.745``
Alexandrite
   ``1.750``
Almandine
   ``1.83``
Aluminum
   ``1.44``
Amber
   ``1.545``
Amblygonite
   ``1.611``
Amethyst
   ``1.540``
Ammolite
   ``1.600``
Anatase
   ``2.490``
Andalusite
   ``1.640``
Anhydrite
   ``1.571``
Apatite
   ``1.632``
Apophyllite
   ``1.536``
Aquamarine
   ``1.575``
Aragonite
   ``1.530``
Argon
   ``1.000281``
Asphalt
   ``1.635``
Axinite
   ``1.674 - 1.704``
Axinite
   ``1.675``
Azurite
   ``1.730``
Barite
   ``1.636``
Barytocalcite
   ``1.684``
Beer
   ``1.345``
Benitoite
   ``1.757``
Benzene
   ``1.501``
Beryl
   ``1.57 - 1.60``
Beryl, Red
   ``1.570 - 1.598``
Beryllonite
   ``1.553``
Brazilianite
   ``1.603``
Bromine (liq)
   ``1.661``
Bronze
   ``1.18``
Brownite
   ``1.567``
Calcite
   ``1.486``
Calspar
   ``1.486``
Cancrinite
   ``1.491``
Carbon Dioxide (gas)
   ``1.000449``
Carbon Disulfide
   ``1.628``
Carbon Tetrachloride
   ``1.460``
Carbonated Beverages
   ``1.34 - 1.356``
Cassiterite
   ``1.997``
Celestite
   ``1.622``
Cerussite
   ``1.804``
Ceylonite
   ``1.770``
Chalcedony
   ``1.544 - 1.553``
Chalk
   ``1.510``
Chalybite
   ``1.630``
Chlorine (gas)
   ``1.000768``
Chlorine (liq)
   ``1.385``
Chrome Green
   ``2.4``
Chrome Red
   ``2.42``
Chrome Tourmaline
   ``1.61 - 1.64``
Chrome Yellow
   ``2.31``
Chromium
   ``2.97``
Chrysoberyl
   ``1.745``
Chrysoberyl, Cat's eye
   ``1.746 - 1.755``
Chrysocolla
   ``1.500``
Chrysoprase
   ``1.534``
Citrine
   ``1.532 - 1.554``
Citrine
   ``1.550``
Clinohumite
   ``1.625 - 1.675``
Clinozoisite
   ``1.724``
Cobalt Blue
   ``1.74``
Cobalt Green
   ``1.97``
Cobalt Violet
   ``1.71``
Colemanite
   ``1.586``
Copper
   ``1.10``
Copper Oxide
   ``2.705``
Coral
   ``1.486``
Coral
   ``1.486 - 1.658``
Cordierite
   ``1.540``
Corundum
   ``1.766``
Cranberry Juice (25%)
   ``1.351``
Crocoite
   ``2.310``
Crystal
   ``2.000``
Cuprite
   ``2.850``
Danburite
   ``1.627 - 1.641``
Danburite
   ``1.633``
Diamond
   ``2.417``
Diopside
   ``1.680``
Dolomite
   ``1.503``
Dumortierite
   ``1.686``
Ebonite
   ``1.66``
Ekanite
   ``1.600``
Elaeolite
   ``1.532``
Emerald
   ``1.560 - 1.605``
Emerald Catseye
   ``1.560 - 1.605``
Emerald, Synth flux
   ``1.561``
Emerald, Synth hydro
   ``1.568``
Enstatite
   ``1.663``
Epidote
   ``1.733``
Ethanol
   ``1.36``
Ethyl Alcohol
   ``1.36``
Euclase
   ``1.652``
Fabulite
   ``2.409``
Feldspar, Adventurine
   ``1.532``
Feldspar, Albite
   ``1.525``
Feldspar, Amazonite
   ``1.525``
Feldspar, Labradorite
   ``1.565``
Feldspar, Microcline
   ``1.525``
Feldspar, Oligoclase
   ``1.539``
Flourite
   ``1.434``
Formica
   ``1.47``
Garnet, Andradite
   ``1.88 - 1.94``
Garnet, Demantoid
   ``1.880 - 1.9``
Garnet, Demantoid
   ``1.880``
Garnet, Grossular
   ``1.738``
Garnet, Hessonite
   ``1.745``
Garnet, Mandarin
   ``1.790 - 1.8``
Garnet, Pyrope
   ``1.73 - 1.76``
Garnet, Rhodolite
   ``1.740 - 1.770``
Garnet, Rhodolite
   ``1.760``
Garnet, Spessartite
   ``1.810``
Garnet, Tsavorite
   ``1.739 - 1.744``
Garnet, Uvarovite
   ``1.74 - 1.87``
Gaylussite
   ``1.517``
Glass
   ``1.51714``
Glass, Albite
   ``1.4890``
Glass, Crown
   ``1.520``
Glass, Crown, Zinc
   ``1.517``
Glass, Flint, Dense
   ``1.66``
Glass, Flint, Heaviest
   ``1.89``
Glass, Flint, Heavy
   ``1.65548``
Glass, Flint, Lanthanum
   ``1.80``
Glass, Flint, Light
   ``1.58038``
Glass, Flint, Medium
   ``1.62725``
Glycerine
   ``1.473``
Gold
   ``0.47``
Hambergite
   ``1.559``
Hauyne
   ``1.490 - 1.505``
Hauynite
   ``1.502``
Helium
   ``1.000036``
Hematite
   ``2.940``
Hemimorphite
   ``1.614``
Hiddenite
   ``1.655``
Honey, 13% water content
   ``1.504``
Honey, 17% water content
   ``1.494``
Honey, 21% water content
   ``1.484``
Howlite
   ``1.586``
Hydrogen (gas)
   ``1.000140``
Hydrogen (liq)
   ``1.0974``
Hypersthene
   ``1.670``
Ice
   ``1.309``
Idocrase
   ``1.713``
Iodine Crystal
   ``3.34``
Iolite
   ``1.522 - 1.578``
Iron
   ``1.51``
Ivory
   ``1.540``
Jade, Jadeite
   ``1.64 - 1.667``
Jade, Nephrite
   ``1.600 - 1.641``
Jadeite
   ``1.665``
Jasper
   ``1.540``
Jet
   ``1.660``
Kornerupine
   ``1.665``
Kunzite
   ``1.660 - 1.676``
Kyanite
   ``1.715``
Labradorite
   ``1.560 - 1.572``
Lapis Gem
   ``1.500``
Lapis Lazuli
   ``1.50 - 1.55``
Lazulite
   ``1.615``
Lead
   ``2.01``
Leucite
   ``1.509``
Magnesite
   ``1.515``
Malachite
   ``1.655``
Meerschaum
   ``1.530``
Mercury (liq)
   ``1.62``
Methanol
   ``1.329``
Milk
   ``1.35``
Moldavite
   ``1.500``
Moonstone
   ``1.518 - 1.526``
Moonstone, Adularia
   ``1.525``
Moonstone, Albite
   ``1.535``
Morganite
   ``1.585 - 1.594``
Natrolite
   ``1.480``
Nephrite
   ``1.600``
Nitrogen (gas)
   ``1.000297``
Nitrogen (liq)
   ``1.2053``
Nylon
   ``1.53``
Obsidian
   ``1.489``
Oil of Wintergreen
   ``1.536``
Oil, Clove
   ``1.535``
Oil, Lemon
   ``1.481``
Oil, Neroli
   ``1.482``
Oil, Orange
   ``1.473``
Oil, Safflower
   ``1.466``
Oil, vegetable (50- C)
   ``1.47``
Olivine
   ``1.670``
Onyx
   ``1.486``
Opal, Black
   ``1.440 - 1.460``
Opal, Fire
   ``1.430 - 1.460``
Opal, White
   ``1.440 - 1.460``
Oregon Sunstone
   ``1.560 - 1.572``
Oxygen (gas)
   ``1.000276``
Oxygen (liq)
   ``1.221``
Padparadja
   ``1.760 - 1.773``
Painite
   ``1.787``
Pearl
   ``1.530``
Periclase
   ``1.740``
Peridot
   ``1.635 - 1.690``
Peristerite
   ``1.525``
Petalite
   ``1.502``
Phenakite
   ``1.650``
Phosgenite
   ``2.117``
Plastic
   ``1.460``
Plexiglas
   ``1.50``
Polystyrene
   ``1.55``
Prase
   ``1.540``
Prasiolite
   ``1.540``
Prehnite
   ``1.610``
Proustite
   ``2.790``
Purpurite
   ``1.840``
Pyrite
   ``1.810``
Pyrope
   ``1.740``
Quartz
   ``1.544 - 1.553``
Quartz, Fused
   ``1.45843``
Rhodizite
   ``1.690``
Rhodochrisite
   ``1.600``
Rhodonite
   ``1.735``
Rock Salt
   ``1.544``
Rubber, Natural
   ``1.5191``
Ruby
   ``1.757 - 1.779``
Rum, White
   ``1.361``
Rutile
   ``2.62``
Sanidine
   ``1.522``
Sapphire
   ``1.757 - 1.779``
Sapphire, Star
   ``1.760 - 1.773``
Scapolite
   ``1.540``
Scapolite, Yellow
   ``1.555``
Scheelite
   ``1.920``
Selenium, Amorphous
   ``2.92``
Serpentine
   ``1.560``
Shampoo
   ``1.362``
Shell
   ``1.530``
Silicon
   ``4.24``
Sillimanite
   ``1.658``
Silver
   ``0.18``
Sinhalite
   ``1.699``
Smaragdite
   ``1.608``
Smithsonite
   ``1.621``
Sodalite
   ``1.483``
Sodium Chloride
   ``1.544``
Spessartite
   ``1.79 - 1.81``
Sphalerite
   ``2.368``
Sphene
   ``1.885``
Spinel
   ``1.712 - 1.717``
Spinel, Blue
   ``1.712 - 1.747``
Spinel, Red
   ``1.708 - 1.735``
Spodumene
   ``1.650``
Star Ruby
   ``1.76 - 1.773``
Staurolite
   ``1.739``
Steatite
   ``1.539``
Steel
   ``2.50``
Stichtite
   ``1.520``
Strontium Titanate
   ``2.410``
Styrofoam
   ``1.595``
Sugar Solution 30%
   ``1.38``
Sugar Solution 80%
   ``1.49``
Sulphur
   ``1.960``
Synthetic Spinel
   ``1.730``
Taaffeite
   ``1.720``
Tantalite
   ``2.240``
Tanzanite
   ``1.690-1.7``
Teflon
   ``1.35``
Thomsonite
   ``1.530``
Tiger eye
   ``1.544``
Topaz
   ``1.607 - 1.627``
Topaz, Blue
   ``1.610``
Topaz, Imperial
   ``1.605 - 1.640``
Topaz, Pink
   ``1.620``
Topaz, White
   ``1.630``
Topaz, Yellow
   ``1.620``
Tourmaline
   ``1.603 - 1.655``
Tourmaline
   ``1.624``
Tourmaline, Blue
   ``1.61 - 1.64``
Tourmaline, Catseye
   ``1.61 - 1.64``
Tourmaline, Green
   ``1.61 - 1.64``
Tourmaline, Paraiba
   ``1.61 - 1.65``
Tourmaline, Red
   ``1.61 - 1.64``
Tremolite
   ``1.600``
Tugtupite
   ``1.496``
Turpentine
   ``1.472``
Turquoise
   ``1.610``
Ulexite
   ``1.490``
Uvarovite
   ``1.870``
Wardite
   ``1.590``
Variscite
   ``1.550``
Water (0- C)
   ``1.33346``
Water (100- C)
   ``1.31766``
Water (20- C)
   ``1.33283``
Water (gas)
   ``1.000261``
Water (35- C, room temp)
   ``1.33157``
Whisky
   ``1.356``
Willemite
   ``1.690``
Witherite
   ``1.532``
Vivianite
   ``1.580``
Vodka
   ``1.363``
Wulfenite
   ``2.300``
Zincite
   ``2.010``
Zircon
   ``1.777 - 1.987``
Zircon, High
   ``1.960``
Zircon, Low
   ``1.800``
Zirconia, Cubic
   ``2.173 - 2.21``
