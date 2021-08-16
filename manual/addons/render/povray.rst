.. todo: excluded sections in boxes (install instruction, tutorials) in the Wiki, maybe add after page split?

***********
POV-Ray 3.7
***********

POV-Ray is an SDL based (Scene Description Language) render engine with a long history
that makes it very stable and feature rich.
The latest version of POV-Ray 3.7 can be found at the `project site <http://www.povray.org/download/>`__.


Features
========

Some key features of the exporter include:

- Geometry import and export with their modifiers, keyed and physics animation
- Add POV-Ray specific non-mesh primitives (never show tessellation)
- Instances
- Hair particles
- Smoke simulations
- Atmospheric media (volume fog)
- HDRI environment mapping
- Aperture depth of field
- Material properties such as filtering, emission, translucency, subsurface scattering,
  glass fog (tinted absorption), blurry/glossy reflections...
- Procedural textures (emulated from Blender and POV-Ray native)
- Image textures
- Texture influence channels: Alpha, Diffuse, Bump, Specular, Mirror (uses same channel as specular)
- Global illumination: Radiosity (indirect lighting), photons caustics (reflect/refract), mesh lights
- Custom POV-Ray code input giving access to any POV-Ray feature not supported by the exporter.


.. rubric:: POV-Ray 3.7 features

Volumetrics and media (scattering/absorption), blurry reflections (uberPOV), ghosting for motion blur (uberPOV),
micropolygon displacement (HGPOV), etc.


Activation
==========

- Of course, don't forget to `download <http://www.povray.org/download/>`__ and install POV-Ray itself!
- Open Blender and go to Preferences then the Add-ons tab.
- Click Render then POV-3.7 to enable the script.


Usage
=====

Quick Start
-----------

#. Choose POV-Ray 3.7 from render engine selector. Then you can render as usual with the *Render* button.
#. The image will be rendered according to parameters set in the Properties.

Main global render settings for instance can be changed in the Render tab.
But there are also properties for environment, material (textures), object, etc. all accessible in other tabs
depending on the selected object (geometry, camera, light...).


POV-Ray Branches
----------------

Below is a comparison of some features of the two engines available to this exporter:

.. |tick|  unicode:: U+2713
.. |cross| unicode:: U+2717
.. |none|  unicode:: U+2014

.. list-table::
   :header-rows: 1
   :class: valign
   :widths: 50 25 25

   * - Feature/Engine/Support
     - POV-Ray
     - UberPOV
   * - Full Spectral Resolution
     - |cross|
     - |tick| (under development)
   * - Supersampling
     - |tick|
     - |tick|
   * - Alpha Mapping
     - |tick|
     - |tick|
   * - Bump Mapping
     - |tick|
     - |tick|
   * - Normal Mapping
     - |cross|
     - |cross|
   * - Displacement Mapping
     - |cross|
     - |cross|
   * - Motion Blur
     - |cross|
     - |tick|
   * - Subsurface Scattering (SSS)
     - |tick|
     - |tick|
   * - Volumetric Scattering (Medium)
     - |tick|
     - |tick|
   * - Blurred Reflections
     - |tick| (very tricky)
     - |tick|
   * - Clay Render
     - |tick|
     - |tick|
   * - Depth of Field
     - |tick|
     - |tick|
   * - Material Layering
     - |tick|
     - |tick|
   * - Thin Film Coating
     - |tick|
     - |tick|
   * - Dispersion
     - |tick|
     - |tick|
   * - Anisotropy
     - |cross|
     - |cross|
   * - Thin Film Interference
     - |tick|
     - |tick|
   * - Complex IOR Files
     - |cross|
     - |cross|
   * - Coating Thickness Absorption
     - |tick|
     - |tick|
   * - Custom Reflectance 90
     - |tick|
     - |tick|
   * - Custom Fresnel Curve
     - |tick| (tricky)
     - |tick| (tricky)
   * - Sigma Texture
     - |tick|
     - |tick|
   * - Sun-Pool Caustics
     - |tick|
     - |tick|
   * - Ambient Occlusion
     - |cross| (tricky)
     - |tick| (under development)
   * - Lens Shift
     - |tick|
     - |tick|
   * - Diaphragm Circular/Polygonal
     - |tick|
     - |tick|
   * - Per-Object Texture Coordinates
     - |tick|
     - |tick|
   * - Texture Projection Modes
     - |tick|
     - |tick|
   * - Front/Camera Mapping
     - |tick| (tricky)
     - |tick| (tricky)
   * - Multiple UV Channels
     - |cross|
     - |cross|
   * - Texture Tone Mapping
     - |tick| (tricky)
     - |tick| (tricky)
   * - Procedural Textures
     - |tick|
     - |tick|
   * - Texture Layering
     - |tick|
     - |tick|
   * - Synthesis Texture Layering
     - |tick|
     - |tick|
   * - Point Lighting
     - |tick|
     - |tick|
   * - Mesh Lighting
     - |tick|
     - |tick|
   * - Image-based Lighting
     - |tick|
     - |tick|
   * - Physical Sun/Sky
     - |tick| (tricky)
     - |tick| (tricky)
   * - HDRI Support
     - |tick|
     - |tick|
   * - IES Texture Support
     - |cross|
     - |cross|
   * - Instance Support
     - |tick|
     - |tick|
   * - Resume/Merge Render
     - |tick|
     - |tick|
   * - Interactive Render
     - |tick|
     - |tick|
   * - Vignetting / Bloom / Glare (Post)
     - |tick| (tricky)
     - |tick| (tricky)
   * - Camera Response Function (CRF) (Post)
     - |cross|
     - |cross|
   * - Color Balance (Post)
     - |cross|
     - |cross|
   * - Multithreading
     - |tick|
     - |tick|
   * - Region Rendering
     - |tick|
     - |tick|
   * - Passive Emitter
     - |tick|
     - |tick|
   * - Invisible Emitter
     - |tick|
     - |tick|
   * - Invisible Object
     - |tick|
     - |tick|
   * - Shadowless Object
     - |tick|
     - |tick|
   * - Shadowless Point Lights
     - |tick|
     - |tick|
   * - Bucket Rendering
     - |tick|
     - |tick|


Exported UI Properties
======================

Render Properties
-----------------

Radiosity
^^^^^^^^^

In POV-Ray, "Radiosity" is diffuse interreflection which has nothing to do with vertex color based radiosity.
In fact, it is more similar to final gathering of irradiance samples and provides a noise free indirect light.

Some presets to radiosity are included, their names and settings are those of
the ``rad_def`` include file shipped with POV-Ray, they set up the properties
so you don't need to include the ``rad_def.inc`` in the exported pov-file,
it's one of the many examples of what an interface like Blender can bring to
all POV-Ray users who are not used to have one.

.. seealso::

   More details on `POV-Ray Wiki <https://wiki.povray.org/content/HowTo:Use_radiosity>`__.


Anti-Aliasing
^^^^^^^^^^^^^

Three sampling methods are supported:

- Non-recursive
- Recursive
- Stochastic (Monte Carlo)
  Only available for UberPOV.


Sampling Depth
""""""""""""""

Values must be comprised between 1 and 9.
Higher values increase render time and may even introduce some undesired blur.


Anti-Alias Threshold
""""""""""""""""""""

In the simple, non-recursive method, POV-Ray initially traces one ray per pixel.
If the color of a pixel differs from its neighbors (to the left or above) by at least the set threshold value,
then the pixel is supersampled by casting a given, fixed number of additional rays.
The default threshold is 0.3 but it may be changed using this ``Antialias_Threshold=n.n`` option.

.. seealso::

   More details on
   `POV-Ray Wiki <https://wiki.povray.org/content/Reference:Tracing_Options#Anti-Aliasing_Options>`__.

.. tip:: Depth of Field Without Anti-Aliasing

   Using no anti-aliasing when camera depth of field is on will speed up rendering and
   often provide decent enough images.


Bounding Method
^^^^^^^^^^^^^^^

Also called acceleration, it is set to automatic BSP (Binary Space Partitioning) by the exporter
as it's generally the most efficient (POV-Ray 3.7 only) but other acceleration methods are available in POV-Ray.

.. seealso::

   More details on `POV-Ray Wiki <https://wiki.povray.org/content/Reference:Tracing_Options#BSP_Bounding>`__.


Command Line Switches
^^^^^^^^^^^^^^^^^^^^^

Some command line arguments can be passed to POV-Ray. Arguments are separated by spaces.
Command line switches consist of a ``/`` (Slash), ``+`` (plus) or ``-`` (minus) sign, followed by
one or more alphabetic characters and possibly a numeric value.

.. seealso::

   More details on `POV-Ray Wiki <https://wiki.povray.org/content/Category:Command-Line_and_INI-File_Options>`__.


.. rubric:: Some Commonly Used Commands:

``-D``: Hide image while rendering
   Use this command line switch to not show the rendered image in POV-Ray
   (slightly faster and lighter on memory).
   The image will be sent back to Blender after completion
   (on Linux this is a hidden default switch to avoid OS-specific editor problems).

``+WT``: Limit the number of threads used
   Limits POV-Ray to using only one single render thread.
   (Likewise, ``+WT2`` would instruct POV-Ray to use two render threads.)
``+C``: Continue an interrupted render
   For "Continue trace" is able to recover the point at which your last render stopped and
   continue it from there (even if you switched off your computer).
``/EXIT``: Close POV-Ray after rendering the image
   There is an option in POV-Ray for Windows interface to do the same:
   The "On Completion" option to "Exit POV-Ray for Windows" (in the *Render* menu).

.. tip:: Fast Preview Renders

   When first setting up your scene, and for fast preview rendering, turn off anti-aliasing, depth of field,
   photons, Radiosity, expensive material features, and in the scene Shading panel, turn off shadows.
   (Other features might get turned off from this panel in future versions of the exporter.)

   Alternatively, use
   the `Quality <https://wiki.povray.org/content/Reference:Tracing_Options#Quality_Settings>`__ command line switches
   ``+q1`` to ``+q11``. These allow you to easily disable most of the CPU-intensive features.


Formatting
^^^^^^^^^^

The exported POV-Ray file can be customized:

- Different indentation characters to choose from.
- Option to add comments to POV-Ray file.
- Option to write long lists of coordinates in one line for easier browsing of the pov-file
  (and slightly faster parsing by the renderer).


Scene Properties
----------------

Color Management
^^^^^^^^^^^^^^^^

sRGB is supposed to be always used currently.


World Properties
----------------

Background
^^^^^^^^^^

Blender *World* gets exported:

- As POV-Ray ``background{}`` if flat colored.
- Using Blender's *Blend Sky* options triggers its export as a POV-Ray ``sky_sphere{}``.

(Sky texture currently appears a little different because of its mapping).


Atmospheric Media
^^^^^^^^^^^^^^^^^

(To create volume lights):

- Number of samples for media calculation
- Atmospheric media color


Object Properties
-----------------

Importance Sampling
^^^^^^^^^^^^^^^^^^^

It is a priority value between 0 and 1 that can be set per object in the *Object* properties tab
for Radiosity to cast more rays at objects that require them most.
Touch this rather carefully when trying to improve render times.


Data Properties
---------------

The script exports sky, lights, hair particles, smoke, fluids, meshes, blobs (metaballs).


Camera
^^^^^^

Depth of Field
""""""""""""""

It has to be enabled for below property to act:

The focal point of depth of field is based on Blender UI *Distance* field, or *Object* field.


Aperture
""""""""

Sets the blur amount (increase to get more).


Perturbation
""""""""""""

Normal map for camera plane, native POV procedural patterns can be used with variable:

- Strength
- Turbulence
- Scale


Lights
^^^^^^

No Shadows toggle button can be used to deactivate tracing of shadows for specific lights only.

.. tip:: For Realistic Light Attenuation

   Use Inverse square falloff, and a small falloff distance value with a higher light intensity
   will give the best results with POV-Ray's implementation of inverse square law. See this
   `discussion <http://news.povray.org/povray.general/thread/%3Cweb.4d77b443f36cbfe281c811d20%40news.povray.org%3E/>`__.


Smoke
^^^^^

A DF3-file (POV-Ray voxel format) is exported and used with a POV-Ray media container with
the same dimension and resolution as Blender smoke domain.


Hair
^^^^

A union of POV-Ray ``sphere_sweep`` is exported and used for each strand.
They can take the color of a texture applied to emitting object,
and shape of sphere sweep tries to emulate shape of strands.


Material Properties
-------------------

Emission
^^^^^^^^

.. tip:: Mesh Lights

   When used together with Radiosity, the Emit property will allow you to create light bulbs or any luminous form
   that really illuminates other objects.


SSS / SSLT
^^^^^^^^^^

Note that SSS in POV-Ray (called SSLT) is very sensitive and will give different results
if the mesh normals are smooth shaded or flat.


Translucency
^^^^^^^^^^^^

Illumination from the back of a surface.

.. seealso::

   More details on `POV-Ray Wiki <https://wiki.povray.org/content/Reference:Finish#Diffuse>`__.


IOR Mirror
^^^^^^^^^^

This option is for using one consistent IOR for ray-traced reflection and refraction and
not breaking the law of conservation of energy between the two.


Iridescence
^^^^^^^^^^^

(Newton's thin film coating.)


Caustics
^^^^^^^^

- Chromatic dispersion for refractive caustics
- Fast fake caustics (somewhat like Blender Ray Transparency)
- Refractive caustics using photons
- Reflective caustics using photons (high IOR or no mirror IOR for easier effect.)

.. tip:: Faster Photons

   To set up some caustics, try moving from the smallest photon depth value to a minimum at
   which you start to see the effect you are after. Check off the *Receive Photons* object property
   for any object that does not really need it.
   (A glass object casting caustics often doesn't need to receive any itself.)
   Then you can balance other parameters to tune photons distribution and smoothing (gathering).
   Don't set the global spacing too fine in scene settings,
   because then you can still make it finer on each object using its spacing multiplier.
   If your system has several threads, they can be used in the photons stage:
   one thread per light, so you can then make your scene lighting more complex without overhead.


Shaders
^^^^^^^

Emulation is attempted from Blender for:

- Specular and diffuse toon (no edges yet)
- Phong and Cook Torrance (both the same)
- Blinn (not perfectly matched)
- Ward isotropic
- Fresnel and Minnaert, started but not finished yet

.. tip:: Glass Like Materials

   When trying to achieve some glass like material, keep low diffuse value, dark or totally black to
   avoid a dull surface and keep a clear transparency.


Texture Properties
------------------

UV Coordinates
^^^^^^^^^^^^^^

Best with planar projection for now. (Silvio Falcinelli)


Texture Channels
^^^^^^^^^^^^^^^^

Texture influences currently exported are: Alpha, Diffuse, Bump, Specular, Mirror (uses same channel as specular).
(No other channel because of POV-Ray non-uniform syntax for them.)


Custom Gamma
^^^^^^^^^^^^

For image textures (read POV-Ray 3.7 docs before using since it generally needs not be used).

.. seealso::

   More details on
   `POV-Ray Wiki <https://wiki.povray.org/content/Documentation:Tutorial_Section_3.3#Gamma_Handling>`__.


Custom POV Code
===============

POV-Ray files are not just pure data files (unlike with most other renderers).
They are programs, with loops, functions, etc.
This means that no matter how many features this exporter could support,
POV-Ray will always have much more under the hood.


Video Tutorial
--------------

Here is a demonstration of the exporter by SMcA.
This video is currently being worked on and may get replaced in the future.

.. youtube:: PD4PmGLMyys


Step by Step
------------

You can add custom POV code directly in Blender's Text editor,
all you have to do is to make sure this POV code has directly or indirectly a ``#declare`` keyword,
followed by the name of your choice and the POV item you want to use.
(Current POV syntax is closer to C than Python, so anything that follows two slash character (``//``) is a comment.)


Adding POV Code Directly
^^^^^^^^^^^^^^^^^^^^^^^^

POV items can be anything but for now only the equivalent of Blender materials can be replaced with this method.
In POV-Ray, it is called ``texture {}`` don't get confused, it really includes all the material properties.

Though you can directly specify a ``texture {}`` block in POV-Ray files,
the ``#declare`` directive allows to assign it to a variable and reuse it more easily.
The exporter makes use of this feature by default, so you won't be able to use your custom texture,
unless you declare it. Here is an example:

.. code-block:: C

   #declare MyTexture =
   texture{
       pigment{
           brick color rgb< 0.99, 0.99, 0.99>  // color mortar
           color rgb< 0.75, 0.5, 0.30>*0.75  // color brick
           brick_size <0.25, 0.0525, 0.125> // format in X, Y and Z-direction
           mortar 0.01                      // size of the mortar
           scale 3
       } // end of pigment
       normal {wrinkles 0.75 scale 0.01}
       finish {ambient 0.15 diffuse 0.95 phong 0.2}
       rotate<0,0,0>  translate< 0.01, 0.00, 0.00>
   } // end of texture

#. Open the Text editor's Sidebar.
#. In the text view properties option, you can chose to render 3D View and/or text. Enable *Both*.
#. Syntax highlight detects ``pov/inc/mcr/ini`` extensions.
#. Some complete POV-Ray scenes are available to Templates header menu.
#. And an Insert menu to add just some POV code snippets at cursor's location.
#. Then you have to go into the material properties to the *Custom POV Code* field,
   and just type in the name of your declared item to use: "MyTexture" in the example given.
   Then you can render your image normally and the material will be replaced.

Blender and POV-Ray do not have the same coordinates systems: POV is Y up while Blender is Z up,
so it is to be expected that text generated content is not turned the same as exported UI items
since the exporter adds a transform matrix to all exported entities.
So if you want to specify orientations more intuitively by looking at the interface,
some transforms have to be specified at the end of your custom blocks, for instance as follows:

.. code-block:: C

   scale <-1, 1, 1>
   rotate <90, 0, -90>
   }


Adding POV Code from Include Files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In any POV-Ray scene you can use the ``#include`` directive to add items from an external POV-Ray file.
It's like the import function in Python. The files to be included have ``.inc`` as their name extension.
Then in the replacement field, you can type in any of the declared names available in the include file.
"Out of the box", POV-Ray ships with a lot of include files.
So you can use them for your textures, but you can also use them for some of their elements.
For instance a very often used include file is one that allows to call colors by their names
instead of numbers called ``colors.inc``, so the previous example could also be written:

.. code-block:: C

   #include "colors.inc"
   #declare MyTexture =
   texture{
       pigment{
           brick color White*0.99  // color mortar
           color rgb< 0.75, 0.5, 0.30>*0.75  // color brick
           brick_size <0.25, 0.0525, 0.125> // format in x, y and z- direction
           mortar 0.01                      // size of the mortar
           scale 3
       } // end of pigment
       normal {wrinkles 0.75 scale 0.01}
       finish {ambient 0.15 diffuse 0.95 phong 0.2}
       rotate<0,0,0>  translate< 0.01, 0.00, 0.00>
   } // end of texture

Some other POV-Ray specific objects are also available:
In POV-Ray a triangle mesh is just one primitive among many.
You can explore the POV-Ray language by modifying the output file and
with the same method, add these primitives by hand, or you can just pick some from the *Add* menu.


POV-Ray Primitives
------------------

The Add menu in the 3D Viewport allows you to add POV-Ray specific objects in addition to native Blender objects.

They are mathematically defined shapes as opposed to meshes.
The sphere, torus, cylinder or cone side will always be round and smooth when rendered,
no matter how close you get, and regardless of their appearance in the 3D Viewport, which is only a proxy.

These objects are the type of objects that get created when you import a POV-Ray file,
so that ideally, you could "exchange" data back and forth between POV-Ray and Blender.


Infinite Plane
^^^^^^^^^^^^^^

The rendered plane is actually infinite, but represented by a proxy in the 3D Viewport,
which is just very big, but still finite.
Please report if you would rather have a different default scale.

.. seealso::

   More details on `POV-Ray Wiki <https://wiki.povray.org/content/Reference:Plane>`__.


Box
^^^

Based on a mesh cube the object can be transformed using move/rotate/scale

.. seealso::

   More details on `POV-Ray Wiki <https://wiki.povray.org/content/Reference:Box>`__.


Sphere
^^^^^^

The sphere has a radius parameter, a location and a scale.

.. seealso::

   More details on `POV-Ray Wiki <https://wiki.povray.org/content/Reference:Sphere>`__.


Cylinder
^^^^^^^^

In POV-Ray, cylinders are defined by radius, base point and end point.
For convenience, move/rotate/scale can be used to the same effect.

.. seealso::

   More details on `POV-Ray Wiki <https://wiki.povray.org/content/Reference:Cylinder>`__.


Cone
^^^^

Cones have a basis radius and end radius.

.. seealso::

   More details on `POV-Ray Wiki <https://wiki.povray.org/content/Reference:Cone>`__.


Torus
^^^^^

Torus has a main radius and a section radius.

.. seealso::

   More details on `POV-Ray Wiki <https://wiki.povray.org/content/Reference:Torus>`__.


Parametric
^^^^^^^^^^

This is a surface generated from the combination of three mathematical equations.

.. seealso::

   More details on `POV-Ray Wiki <https://wiki.povray.org/content/Reference:Parametric>`__.


Rainbow
^^^^^^^

The rainbow is a view dependent effect.

.. seealso::

   More details on `POV-Ray Wiki <https://wiki.povray.org/content/Reference:Rainbow>`__.


Lathe
^^^^^

This object behaves like the Blender Screw modifier to create surfaces by revolving a spline
except instead of being tessellated beforehand, it follows the mathematical curvature of the spline
so you won't see any polygons no matter how close you zoom.

.. seealso::

   More details on `POV-Ray Wiki <https://wiki.povray.org/content/Reference:Lathe>`__.


Prism
^^^^^

This is a POV-Ray primitive that simply extrudes a shape.

.. seealso::

   More details on `POV-Ray Wiki <https://wiki.povray.org/content/Reference:Prism>`__.


Superquadric Ellipsoid
^^^^^^^^^^^^^^^^^^^^^^

A quite versatile tool that can provide quick models for cushion or star-shaped objects.

.. seealso::

   More details on `POV-Ray Wiki <https://wiki.povray.org/content/Reference:Superquadric_Ellipsoid>`__.


Height Field
^^^^^^^^^^^^

This is a displacement of a surface following a texture. Tessellation also happens at render time,
so you don't need to subdivide anything before.

.. seealso::

   More details on `POV-Ray Wiki <https://wiki.povray.org/content/Reference:Height_Field>`__.


Sphere Sweep
^^^^^^^^^^^^

This POV-Ray primitive sweeps a sphere a long as spline to create an interpolated form
that can have variations of radius along the spline. It is also used to export hair strands.

.. seealso::

   More details on `POV-Ray Wiki <https://wiki.povray.org/content/Reference:Sphere_Sweep>`__.


Blob Sphere
^^^^^^^^^^^

Like Blender metaballs.

.. seealso::

   More details on `POV-Ray Wiki <https://wiki.povray.org/content/Reference:Blob>`__.


Isosurfaces
^^^^^^^^^^^

In POV-Ray isosurfaces are objects that can combine and be deformed using pigments or equations.

.. seealso::

   More details on `POV-Ray Wiki <https://wiki.povray.org/content/Reference:Isosurface>`__.

Isosurface Box
   An isosurface component shaped as a box.
Isosurface Sphere
   An isosurface component shaped as a sphere.
Supertorus
   An isosurface shaped as a torus with deforming parameters equivalent to those of the superellipsoid.

Parameters (POV-Ray names):

``MajorRadius``, ``MinorRadius``
   Base radii for the torus.
``MajorControl``, ``MinorControl``
   Controls for the roundness of the supertorus. Use numbers in the range [0, 1].
``Accuracy``
   The accuracy parameter.
``MaxGradient``
   The max_gradient parameter.


Macro Based Primitives
^^^^^^^^^^^^^^^^^^^^^^

Two primitives are actually macros that generate a mesh from curves before render time:

- Polygon to Circle Blending
- Loft


Importing POV-Ray Files
=======================

#. From the same Add menu, you can also import POV-Ray files.
#. Or otherwise, clicking :menuselection:`File --> Import` from the Topbar menu.
#. You can then select one or several files.


.. reference::

   :Category:  Render
   :Description: POV-Ray 3.7 integration for Blender.
   :Location: :menuselection:`Render --> Engine --> POV-Ray 3.7`
   :File: render_povray folder
   :Author: Campbell Barton, Maurice Raybaud, Leonid Desyatkov, Bastien Montagne, Constantin Rahn, Silvio Falcinelli
   :License: GPL
   :Note: This add-on is bundled with Blender.
