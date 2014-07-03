
Transparency
============


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


In Blender, there are three ways in which the transparency of a material can be set:  Mask, Z-Buffer and Ray-trace.  Each of these is explained in more detail below.  The :doc:`Material Preview <materials/properties/preview>` option with a sphere object gives a good demonstration of the capabilities of these three options.


Common Options
--------------

The following property controls are available for all transparency options:

**Alpha**
    Sets the transparency of the material by setting all pixels in the alpha channel to the given value.
**Fresnel**
     Sets the power of the Fresnel effect. The Fresnel effect controls how transparent the material is, depending on the angle between the surface normal and the viewing direction. Typically, the larger the angle, the more opaque a material becomes (this generally occurs on the outline of the object).
**Specular** -
    Controls the alpha/falloff for the specular color.
**Blend**
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

See :doc:`Mask Transparency <materials/properties/mask_transparency>`\ .


Z Buffer
--------

This uses the alpha buffer for transparent faces.
The alpha value of each pixel determines the mix of the basic color of the material,
and the color of the pixel is determined from the objects/background behind it.
Only basic settings are available with this option; it does not calculate refractions.


Raytraced Transparency
----------------------

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


.. admonition:: Enable Raytracing
   :class: note


   To get ray-traced transparency, you need to:

   - enable ray tracing in your Render settings.  This is done in the Render context  → Shading Panel. Ray tracing is enabled by default.
   - set your Alpha value to something other than 1.0.
   - in order for the background material to receive light passing through your transparent object, :guilabel:`Receive Transparent` must be turned on for that material in the Material → Shadow panel.


Options
-------


.. figure:: /images/Manual-2.5-Material-RaytracedTransp-Panel.jpg

   The Transparency Panel.


In addition to the common options given above, the following property controls are available:

:guilabel:`IOR`
    Index of Refraction.  Sets how much a ray traveling through the material will be refracted, hence producing a distorted image of its background.  See
FIXME(TODO: Internal Link;
[[#IOR values for Common Materials|IOR values for Common Materials]]
) below.
:guilabel:`Filter`
    Amount of filtering for transparent ray trace. The higher this value, the more the base color of the material will show. The material will still be transparent but it will start to take on the color of the material. Disabled (0.0) by default.
:guilabel:`Falloff`
    How fast light is absorbed as it passes through the material. Gives 'depth' and 'thickness' to glass.
:guilabel:`Limit`
    Materials thicker than this are not transparent. This is used to control the threshold after which the filter color starts to come into play.
:guilabel:`Depth`
    Sets the maximum number of transparent surfaces a single ray can travel through. There is no typical value. Transparent objects outside the :guilabel:`Depth` range will be rendered pitch black if viewed through the transparent object that the :guilabel:`Depth` is set for.  In other words, if you notice black areas on the surface of a transparent object, the solution is probably to increase its :guilabel:`Depth` value (this is a common issue with ray tracing transparent objects).  You may also need to turn on transparent shadows on the background object.

:guilabel:`Gloss`
    Settings for the glossiness of the material.
   :guilabel:`Amount`
       The clarity of the refraction. Set this to something lower than zero to get a blurry refraction.
   :guilabel:`Threshold`
       Threshold for adaptive sampling. If a sample contributes less than this amount (as a percentage), sampling is stopped.
   :guilabel:`Samples`
       Number of cone samples averaged for blurry refraction.


Examples
--------


Index of Refraction
~~~~~~~~~~~~~~~~~~~


.. figure:: /images/Manual-2.5-Material-RaytracedTransp-IOR-Examples.jpg

   Influence of the IOR of an Object on the distortion of the background: spheres of Water, Glass and Diamond (top to bottom).


(\ *Influence of the IOR of an Object on the distortion of the background: spheres of Water, Glass  and Diamond (top to bottom).*\ ). There are different values for typical materials: Air is **1.000** (no refraction), Alcohol is **1.329**\ , Glass is **1.517**\ , Plastic is **1.460**\ , Water is **1.333** and Diamond is **2.417**\ .


Fresnel
~~~~~~~


+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
+.. figure:: /images/Manual-2.5-Material-RayTraceTransp-FresnelExampel.jpg                                                                                                                                                                                                                                                                               |.. figure:: /images/Manual-2.5-Material-RayTraceTransp-FresnelExampelZTransp.jpg +
+   :width: 320px                                                                                                                                                                                                                                                                                                                                        |   :width: 320px                                                                 +
+   :figwidth: 320px                                                                                                                                                                                                                                                                                                                                     |   :figwidth: 320px                                                              +
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
+16 pieces of glass rotated in various directions demonstrate the angle-dependent Fresnel effect with ray-traced (left) and alpha buffered transparency (right).  Note that the major difference is the lack of IOR effect in the latter case.  (Download `.blend <http://wiki.blender.org/index.php/:File:Manual25-Material-FresnelExample.blend>`__\ .)                                                                                  +
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
~~~~~


.. figure:: /images/Manual-2.5-Material-Transp-3GlassesExample.jpg
   :width: 640px
   :figwidth: 640px

   A simple scene with three glasses on a surface, and three lamps.  Depth was set to 4, 8, 12, and 14, resulting in render times of 24 sec, 34 sec, 6 min, and 11 min respectively. (Download `.blend <http://wiki.blender.org/index.php/:File:Manual25-Material-3GlassesExample.blend>`__\ .)


Increasing :guilabel:`Depth` also considerably increases render time.
Each time a light ray passes through a surface,
the ray-tracing algorithm is called recursively.  In the example above,
each side of each glass has an exterior and an interior surface.
Light rays thus have to pass through four surfaces for each glass.

But not only that, at every point on a surface, some of the light can be reflected,
or mirrored off the surface in various directions.
This results in multiple rays needing to be calculated for each point
(often referred to as a **tree of rays**\ [http://www.cs.unc.edu/~rademach/xroads-RT/RTarticle.
html]). In each of the rendered images above there are 640×400=256 000 pixels.
By increasing :guilabel:`Depth`\ , at least one tree of rays is added to each pixel.

Be kind to your computer. Carefully placing objects in a scene to avoid overlapping
transparent objects is often an interesting alternative.


Hints
=====


Transparent shadows
-------------------


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
namely the :guilabel:`Ambient Occlusion`\ , :guilabel:`Environment Lighting`\ ,
and :guilabel:`Gather` panels.  Alternatively, a texture can be used to control the
:guilabel:`Intensity` value of the shadow-receiving material.


IOR values for Common Materials
-------------------------------

The following list provides some index of refraction values to use when ray-traced
transparency is used for various liquids, solids (gems), and gases:


+--------------------------------------+----------------------------------------+--------------------------------------+----------------------------------------+
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++A                                   +|+E                                     +|+J                                   +|+S                                     ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Acetone               |1.36         +|+Ebonite                 |1.66         +|+Jade, Jadeite         |1.64 - 1.667 +|+Sanidine                |1.522        ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Actinolite            |1.618        +|+Ekanite                 |1.600        +|+Jade, Nephrite        |1.600 - 1.641+|+Sapphire                |1.757 - 1.779++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Agalmatolite          |1.550        +|+Elaeolite               |1.532        +|+Jadeite               |1.665        +|+Sapphire, Star          |1.760 - 1.773++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Agate                 |1.544        +|+Emerald                 |1.560 - 1.605+|+Jasper                |1.540        +|+Scapolite               |1.540        ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Agate                 |1.540        +|+Emerald Catseye         |1.560 - 1.605+|+Jet                   |1.660        +|+Scapolite, Yellow       |1.555        ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Air                   |1.000        +|+Emerald, Synth flux     |1.561        +|+K                                   +|+Scheelite               |1.920        ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Alcohol               |1.329        +|+Emerald, Synth hydro    |1.568        +|+Kornerupine           |1.665        +|+Selenium, Amorphous     |2.92         ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Alcohol, Ethyl (grain)|1.36         +|+Enstatite               |1.663        +|+Kunzite               |1.660 - 1.676+|+Serpentine              |1.560        ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Alexandrite           |1.745        +|+Epidote                 |1.733        +|+Kyanite               |1.715        +|+Shampoo                 |1.362        ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Alexandrite           |1.750        +|+Ethanol                 |1.36         +|+L                                   +|+Shell                   |1.530        ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Almandine             |1.83         +|+Ethyl Alcohol           |1.36         +|+Labradorite           |1.560 - 1.572+|+Silicon                 |4.24         ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Aluminum              |1.44         +|+Euclase                 |1.652        +|+Lapis Gem             |1.500        +|+Sillimanite             |1.658        ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Amber                 |1.545        +|+F                                     +|+Lapis Lazuli          |1.50 - 1.55  +|+Silver                  |0.18         ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Amblygonite           |1.611        +|+Fabulite                |2.409        +|+Lazulite              |1.615        +|+Sinhalite               |1.699        ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Amethyst              |1.540        +|+Feldspar, Adventurine   |1.532        +|+Lead                  |2.01         +|+Smaragdite              |1.608        ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Ammolite              |1.600        +|+Feldspar, Albite        |1.525        +|+Leucite               |1.509        +|+Smithsonite             |1.621        ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Anatase               |2.490        +|+Feldspar, Amazonite     |1.525        +|+M                                   +|+Sodalite                |1.483        ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Andalusite            |1.640        +|+Feldspar, Labradorite   |1.565        +|+Magnesite             |1.515        +|+Sodium Chloride         |1.544        ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Anhydrite             |1.571        +|+Feldspar, Microcline    |1.525        +|+Malachite             |1.655        +|+Spessartite             |1.79 - 1.81  ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Apatite               |1.632        +|+Feldspar, Oligoclase    |1.539        +|+Meerschaum            |1.530        +|+Sphalerite              |2.368        ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Apophyllite           |1.536        +|+Flourite                |1.434        +|+Mercury (liq)         |1.62         +|+Sphene                  |1.885        ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Aquamarine            |1.575        +|+Formica                 |1.47         +|+Methanol              |1.329        +|+Spinel                  |1.712 - 1.717++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Aragonite             |1.530        +|+G                                     +|+Milk                  |1.35         +|+Spinel, Blue            |1.712 - 1.747++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Argon                 |1.000281     +|+Garnet, Andradite       |1.88 - 1.94  +|+Moldavite             |1.500        +|+Spinel, Red             |1.708 - 1.735++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Asphalt               |1.635        +|+Garnet, Demantoid       |1.880 - 1.9  +|+Moonstone             |1.518 - 1.526+|+Spodumene               |1.650        ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Axinite               |1.674 - 1.704+|+Garnet, Demantoid       |1.880        +|+Moonstone, Adularia   |1.525        +|+Star Ruby               |1.76 - 1.773 ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Axinite               |1.675        +|+Garnet, Grossular       |1.738        +|+Moonstone, Albite     |1.535        +|+Staurolite              |1.739        ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Azurite               |1.730        +|+Garnet, Hessonite       |1.745        +|+Morganite             |1.585 - 1.594+|+Steatite                |1.539        ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++B                                   +|+Garnet, Mandarin        |1.790 - 1.8  +|+N                                   +|+Steel                   |2.50         ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Barite                |1.636        +|+Garnet, Pyrope          |1.73 - 1.76  +|+Natrolite             |1.480        +|+Stichtite               |1.520        ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Barytocalcite         |1.684        +|+Garnet, Rhodolite       |1.740 - 1.770+|+Nephrite              |1.600        +|+Strontium Titanate      |2.410        ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Beer                  |1.345        +|+Garnet, Rhodolite       |1.760        +|+Nitrogen (gas)        |1.000297     +|+Styrofoam               |1.595        ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Benitoite             |1.757        +|+Garnet, Spessartite     |1.810        +|+Nitrogen (liq)        |1.2053       +|+Sugar Solution 30%      |1.38         ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Benzene               |1.501        +|+Garnet, Tsavorite       |1.739 - 1.744+|+Nylon                 |1.53         +|+Sugar Solution 80%      |1.49         ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Beryl                 |1.57 - 1.60  +|+Garnet, Uvarovite       |1.74 - 1.87  +|+O                                   +|+Sulphur                 |1.960        ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Beryl, Red            |1.570 - 1.598+|+Gaylussite              |1.517        +|+Obsidian              |1.489        +|+Synthetic Spinel        |1.730        ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Beryllonite           |1.553        +|+Glass                   |1.51714      +|+Oil of Wintergreen    |1.536        +|+T                                     ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Brazilianite          |1.603        +|+Glass, Albite           |1.4890       +|+Oil, Clove            |1.535        +|+Taaffeite               |1.720        ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Bromine (liq)         |1.661        +|+Glass, Crown            |1.520        +|+Oil, Lemon            |1.481        +|+Tantalite               |2.240        ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Bronze                |1.18         +|+Glass, Crown, Zinc      |1.517        +|+Oil, Neroli           |1.482        +|+Tanzanite               |1.690-1.7    ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Brownite              |1.567        +|+Glass, Flint, Dense     |1.66         +|+Oil, Orange           |1.473        +|+Teflon                  |1.35         ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++C                                   +|+Glass, Flint, Heaviest  |1.89         +|+Oil, Safflower        |1.466        +|+Thomsonite              |1.530        ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Calcite               |1.486        +|+Glass, Flint, Heavy     |1.65548      +|+Oil, vegetable (50- C)|1.47         +|+Tiger eye               |1.544        ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Calspar               |1.486        +|+Glass, Flint, Lanthanum |1.80         +|+Olivine               |1.670        +|+Topaz                   |1.607 - 1.627++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Cancrinite            |1.491        +|+Glass, Flint, Light     |1.58038      +|+Onyx                  |1.486        +|+Topaz, Blue             |1.610        ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Carbon Dioxide (gas)  |1.000449     +|+Glass, Flint, Medium    |1.62725      +|+Opal, Black           |1.440 - 1.460+|+Topaz, Imperial         |1.605 - 1.640++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Carbon Disulfide      |1.628        +|+Glycerine               |1.473        +|+Opal, Fire            |1.430 - 1.460+|+Topaz, Pink             |1.620        ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Carbon Tetrachloride  |1.460        +|+Gold                    |0.47         +|+Opal, White           |1.440 - 1.460+|+Topaz, White            |1.630        ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Carbonated Beverages  |1.34 - 1.356 +|+H                                     +|+Oregon Sunstone       |1.560 - 1.572+|+Topaz, Yellow           |1.620        ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Cassiterite           |1.997        +|+Hambergite              |1.559        +|+Oxygen (gas)          |1.000276     +|+Tourmaline              |1.603 - 1.655++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Celestite             |1.622        +|+Hauyne                  |1.490 - 1.505+|+Oxygen (liq)          |1.221        +|+Tourmaline              |1.624        ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Cerussite             |1.804        +|+Hauynite                |1.502        +|+P                                   +|+Tourmaline, Blue        |1.61 - 1.64  ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Ceylonite             |1.770        +|+Helium                  |1.000036     +|+Padparadja            |1.760 - 1.773+|+Tourmaline, Catseye     |1.61 - 1.64  ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Chalcedony            |1.544 - 1.553+|+Hematite                |2.940        +|+Painite               |1.787        +|+Tourmaline, Green       |1.61 - 1.64  ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Chalk                 |1.510        +|+Hemimorphite            |1.614        +|+Pearl                 |1.530        +|+Tourmaline, Paraiba     |1.61 - 1.65  ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Chalybite             |1.630        +|+Hiddenite               |1.655        +|+Periclase             |1.740        +|+Tourmaline, Red         |1.61 - 1.64  ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Chlorine (gas)        |1.000768     +|+Honey, 13% water content|1.504        +|+Peridot               |1.635 - 1.690+|+Tremolite               |1.600        ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Chlorine (liq)        |1.385        +|+Honey, 17% water content|1.494        +|+Peristerite           |1.525        +|+Tugtupite               |1.496        ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Chrome Green          |2.4          +|+Honey, 21% water content|1.484        +|+Petalite              |1.502        +|+Turpentine              |1.472        ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Chrome Red            |2.42         +|+Howlite                 |1.586        +|+Phenakite             |1.650        +|+Turquoise               |1.610        ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Chrome Tourmaline     |1.61 - 1.64  +|+Hydrogen (gas)          |1.000140     +|+Phosgenite            |2.117        +|+U                                     ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Chrome Yellow         |2.31         +|+Hydrogen (liq)          |1.0974       +|+Plastic               |1.460        +|+Ulexite                 |1.490        ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Chromium              |2.97         +|+Hypersthene             |1.670        +|+Plexiglas             |1.50         +|+Uvarovite               |1.870        ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Chrysoberyl           |1.745        +|+I                                     +|+Polystyrene           |1.55         +|+V-W                                   ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Chrysoberyl, Cat's eye|1.746 - 1.755+|+Ice                     |1.309        +|+Prase                 |1.540        +|+Wardite                 |1.590        ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Chrysocolla           |1.500        +|+Idocrase                |1.713        +|+Prasiolite            |1.540        +|+Variscite               |1.550        ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Chrysoprase           |1.534        +|+Iodine Crystal          |3.34         +|+Prehnite              |1.610        +|+Water (0- C)            |1.33346      ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Citrine               |1.532 - 1.554+|+Iolite                  |1.522 - 1.578+|+Proustite             |2.790        +|+Water (100- C)          |1.31766      ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Citrine               |1.550        +|+Iron                    |1.51         +|+Purpurite             |1.840        +|+Water (20- C)           |1.33283      ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Clinohumite           |1.625 - 1.675+|+Ivory                   |1.540        +|+Pyrite                |1.810        +|+Water (gas)             |1.000261     ++
++----------------------+-------------+|+------------------------+-------------+|+----------------------+-------------+|+------------------------+-------------++
++Clinozoisite          |1.724        +|                                        |+Pyrope                |1.740        +|+Water (35- C, room temp)|1.33157      ++
++----------------------+-------------+|                                        |+----------------------+-------------+|+------------------------+-------------++
++Cobalt Blue           |1.74         +|                                        |+Q                                   +|+Whisky                  |1.356        ++
++----------------------+-------------+|                                        |+----------------------+-------------+|+------------------------+-------------++
++Cobalt Green          |1.97         +|                                        |+Quartz                |1.544 - 1.553+|+Willemite               |1.690        ++
++----------------------+-------------+|                                        |+----------------------+-------------+|+------------------------+-------------++
++Cobalt Violet         |1.71         +|                                        |+Quartz, Fused         |1.45843      +|+Witherite               |1.532        ++
++----------------------+-------------+|                                        |+----------------------+-------------+|+------------------------+-------------++
++Colemanite            |1.586        +|                                        |+R                                   +|+Vivianite               |1.580        ++
++----------------------+-------------+|                                        |+----------------------+-------------+|+------------------------+-------------++
++Copper                |1.10         +|                                        |+Rhodizite             |1.690        +|+Vodka                   |1.363        ++
++----------------------+-------------+|                                        |+----------------------+-------------+|+------------------------+-------------++
++Copper Oxide          |2.705        +|                                        |+Rhodochrisite         |1.600        +|+Wulfenite               |2.300        ++
++----------------------+-------------+|                                        |+----------------------+-------------+|+------------------------+-------------++
++Coral                 |1.486        +|                                        |+Rhodonite             |1.735        +|+Z                                     ++
++----------------------+-------------+|                                        |+----------------------+-------------+|+------------------------+-------------++
++Coral                 |1.486 - 1.658+|                                        |+Rock Salt             |1.544        +|+Zincite                 |2.010        ++
++----------------------+-------------+|                                        |+----------------------+-------------+|+------------------------+-------------++
++Cordierite            |1.540        +|                                        |+Rubber, Natural       |1.5191       +|+Zircon                  |1.777 - 1.987++
++----------------------+-------------+|                                        |+----------------------+-------------+|+------------------------+-------------++
++Corundum              |1.766        +|                                        |+Ruby                  |1.757 - 1.779+|+Zircon, High            |1.960        ++
++----------------------+-------------+|                                        |+----------------------+-------------+|+------------------------+-------------++
++Cranberry Juice (25%) |1.351        +|                                        |+Rum, White            |1.361        +|+Zircon, Low             |1.800        ++
++----------------------+-------------+|                                        |+----------------------+-------------+|+------------------------+-------------++
++Crocoite              |2.310        +|                                        |+Rutile                |2.62         +|+Zirconia, Cubic         |2.173 - 2.21 ++
++----------------------+-------------+|                                        |+----------------------+-------------+|+------------------------+-------------++
++Crystal               |2.000        +|                                        |                                      |                                        +
++----------------------+-------------+|                                        |                                      |                                        +
++Cuprite               |2.850        +|                                        |                                      |                                        +
++----------------------+-------------+|                                        |                                      |                                        +
++D                                   +|                                        |                                      |                                        +
++----------------------+-------------+|                                        |                                      |                                        +
++Danburite             |1.627 - 1.641+|                                        |                                      |                                        +
++----------------------+-------------+|                                        |                                      |                                        +
++Danburite             |1.633        +|                                        |                                      |                                        +
++----------------------+-------------+|                                        |                                      |                                        +
++Diamond               |2.417        +|                                        |                                      |                                        +
++----------------------+-------------+|                                        |                                      |                                        +
++Diopside              |1.680        +|                                        |                                      |                                        +
++----------------------+-------------+|                                        |                                      |                                        +
++Dolomite              |1.503        +|                                        |                                      |                                        +
++----------------------+-------------+|                                        |                                      |                                        +
++Dumortierite          |1.686        +|                                        |                                      |                                        +
++----------------------+-------------+|                                        |                                      |                                        +
+--------------------------------------+----------------------------------------+--------------------------------------+----------------------------------------+


