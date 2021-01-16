.. _bpy.types.ShaderNodeTexSky:

****************
Sky Texture Node
****************

.. figure:: /images/render_shader-nodes_textures_sky_node.png
   :align: right

   Sky Texture Node.

The *Sky Texture* node adds a procedural Sky texture.


Inputs
======

Vector
   Texture coordinate to sample texture at;
   defaults to Generated texture coordinates if the socket is left unconnected.


Properties
==========

Sky Type
   Sky model to use.

   Preetham
      Based on the 1999 `paper <https://doi.org/10.1145/311535.311545>`__ by Preetham et al.
   Hosek/Wilkie
      Based on the 2012 `paper <https://cgg.mff.cuni.cz/projects/SkylightModelling/>`__ by Hosek and Wilkie.
   Nishita
      Improved version of the 1993
      `model <https://www.scratchapixel.com/lessons/procedural-generation-virtual-worlds/simulating-sky/simulating-colors-of-the-sky>`__
      by Nishita et al.

Sun Direction
   Sun direction vector.

Turbidity
   Atmospheric turbidity.

   - 2: Arctic like
   - 3: clear sky
   - 6: warm/moist day
   - 10: hazy day

Ground Albedo
   Amount of light reflected from the planet surface back into the atmosphere.

Sun Disc
   Enable/Disable sun disc lighting.

Sun Size
   Angular diameter of the sun disc (in degrees).

Sun Intensity
   Multiplier for sun disc lighting.

Sun Elevation
   Rotation of the sun from the horizon (in degrees).

Sun Rotation
   Rotation of the sun around the zenith (in degrees).

Altitude
   The distance in kilometers from sea level to the location of the camera.
   For example, if the camera is placed on a beach a value of 0 should be used.
   However, if the camera is in the cockpit of a flying airplane a value of 10 km will be more suitable.
   Note, this is limited to 60 km because the mathematical model only accounts
   for the first two layers of the earth's atmosphere (which ends around 60 km).

Air
   Density of air molecules.

   - 0 no air
   - 1 clear day atmosphere
   - 2 highly polluted day

Dust
   Density of dust and water droplets.

   - 0 no dust
   - 1 clear day atmosphere
   - 5 city like atmosphere
   - 10 hazy day

Ozone
   Density of ozone molecules;
   useful to make the sky appear bluer.

   - 0 no ozone
   - 1 clear day atmosphere
   - 2 city like atmosphere


Outputs
=======

Color
   Texture color output.


Examples
========

.. figure:: /images/render_shader-nodes_textures_sky_example.jpg
   :width: 200px

   Example of Sky Texture.

.. seealso::

   :doc:`/addons/lighting/sun_position` add-on
