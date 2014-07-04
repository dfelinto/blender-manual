
..    TODO/Review: {{review
   |im=
   The second image is from 2.4
   }} .


Sun: Sky & Atmosphere
=====================

.. figure:: /images/25-Manual-Lighting-Lamps-Sun-SkyAtmoPanel.jpg
   :width: 304px
   :figwidth: 304px

   Sky & Atmosphere panel


This panel allows you to enable an effect that simulates various properties of real sky and
atmosphere: the scattering of sunlight as it crosses the kilometers of air overhead.
For example, when the Sun is high, the sky is blue (and the horizon, somewhat whitish).
When the Sun is near the horizon, the sky is dark blue/purple, and the horizon turns orange.
The dispersion of the atmosphere is also more visible when it is a bit foggy:
the farther away an object is,
the more "faded" in light gray it is… Go out into the countryside on a nice hot day,
and you will see.

To enable this effect, you have to use a :guilabel:`Sun` light source. If, as usual,
the *position* of the lamp has no importance, its *rotation* is crucial:
it determines which hour it is. As a starting point,
you should reset rotation of your :guilabel:`Sun` (with :kbd:`alt-R`, or typing **0**
in each of the three :guilabel:`Rotation` fields :guilabel:`X` / :guilabel:`Y` / :guilabel:`Z` in
the :guilabel:`Transform Properties` panel - :kbd:`N`). This way,
you'll have a nice mid-day sun (in the tropics).

Now, there are two important angles for the :guilabel:`Sky/Atmosphere` effect:
the "incidence" angle (between the light direction and the X-Y plane),
which determines the "hour" of the day (as you might expect,
the default rotation - straight down - is "mid-day",
a light pointing straight up is "midnight", and so on…).
And the rotation around the Z axis determines the position of the sun around the camera.


.. figure:: /images/Manual-Lighting-Lamps-Sun-PositionForSkyAtmosphere.jpg
   :width: 610px
   :figwidth: 610px

   The dashed "light line" of the Sun lamp crossing the camera focal point.


In fact, to have a good idea of where the sun is in your world,
relative to the camera in your 3D view, you should always try to have the dashed "light line"
of the lamp crossing the center of the camera (its "focal" point), as shown in
(*The dashed "light line" of the* :guilabel:`Sun` *lamp crossing the camera focal point*).
This way, in camera view (:kbd:`pad0`, center window in the example picture),
you will see where the "virtual" sun created by this effect will be.

It is important to understand that the *position* of the sun has no importance for the
effect: only its *orientation* is relevant.
The position just might help you in your scene design.


Options
=======

:guilabel:`Sun & Sky Presets`:

- :guilabel:`Classic`:
- :guilabel:`Desert`:
- :guilabel:`Mountain`:


Sky
---

:guilabel:`Sky`
   This button enables the sky settings: it will create a "sky", with a "sun" if visible, and mix it with the background as defined in :guilabel:`World` settings.

:guilabel:`Turbidity`
   This is a general parameter that affects sun view, sky and atmosphere;
   it's an atmosphere parameter where low values describe clear sky, and high values shows more foggy sky.
   In general, low values give a clear, deep blue sky, with "little" sun; high values give a more reddish sky,
   with a big halo around the sun.
   Note that this parameter is one which can really modify the "intensity" of the sun lighting. See examples below.


Here are its specific controls:
:guilabel:`Blending`

- The first drop-down list shows you a menu of various mix methods. The one selected will be used to blend the sky and sun with the background defined in the :guilabel:`World` settings. The mixing methods are the same as described e.g. in the :doc:`Mix Compositing Node <composite_nodes/types/color#mix_node>` page.
- :guilabel:`Factor`

          Controls how much the sky and sun effect is applied to the World background.

:guilabel:`Color space`
   These buttons allows you to select which color space the effect uses, with the following choices:

   - :guilabel:`CIE`
   - :guilabel:`REC709`
   - :guilabel:`SMPTE`
   - :guilabel:`Exposure`

          This numeric field allows you to modify the exposure of the rendered Sky and Sun (**0.0** for no correction).

:guilabel:`Horizon`

- :guilabel:`Brightness`

          Controls brightness of colors at the horizon. Its value should be in the range **0.0** to **10.0**; values near zero means no horizontal brightness, and large values for this parameter increase horizon brightness. See examples below.

- :guilabel:`Spread`

          Controls spread of light at the horizon. Its value should be in the range **0.0** to **10.0**; values low in the range result in less spread of light at horizon, and values high in the range result in horizon light spread in through all the sky.

:guilabel:`Sun`

- :guilabel:`Brightness`

          Controls the sun brightness. Its value should be in the range **0.0** to **10.0**; with low values the sky has no sun and with high values the sky only has sun.

- :guilabel:`Size`

          Controls the size of sun. Its values should be in the range **0.0** to **10.0**, but note that low values result in large sun size, and high values result in small sun size. Note that the overall brightness of the sun remains constant (set by :guilabel:`Brightness`), so the larger the sun (the smaller :guilabel:`Size`), the more it "vanishes" in the sky, and *vice versa*.

- :guilabel:`Back Light`

          For "Back Scatter Light", result on sun's color, high values result in more light around the sun. Its values range is **-1.0** to **1.0**. Negative values result in less light around sun.


Atmosphere
----------

:guilabel:`Atmosphere`
   This button enables the atmosphere settings. It will not modify the background, but it tries to simulate the effects of an atmosphere: scattering of the sunlight in the atmosphere, its attenuation, …

:guilabel:`Intensity`

- :guilabel:`Sun`

          Sets sun intensity. Its values are in range **0.0** to **10.0**. High values result in  bluer light on far objects.

- :guilabel:`Distance`

          This factor is used to convert Blender units into an understandable unit for atmosphere effect, it starts from **0** and high values result in more yellow light in the scene.

:guilabel:`Scattering`

- :guilabel:`Inscattering`

          This factor can be used to decrease the effect of light inscattered into atmosphere between the camera and objects in the scene. This value should be **1.0** but can be changed to create some nice, but not realistic, images.

- :guilabel:`Extinction`

          This factor can be use to decrease the effect of extinction light from objects in the scene. Like :guilabel:`Inscattering` factor, this parameter should be **1.0** but you can change it; low values result in less light extinction. Its value is in the range **0.0** to **1.0**.


Examples
========

First, let's see what happens when we modify the orientation of the sun:


+------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
+.. figure:: /images/Manual-Lighting-Lamps-Sun-SkyAtmosphere-MidDay.jpg                                                                                      |.. figure:: /images/Manual-Lighting-Lamps-Sun-SkyAtmosphere-MidNight.jpg    +
+   :width: 200px                                                                                                                                            |   :width: 200px                                                            +
+   :figwidth: 200px                                                                                                                                         |   :figwidth: 200px                                                         +
+                                                                                                                                                            |                                                                            +
+   With sun right overhead (mid-day).                                                                                                                       |   With sun deep "under the Earth" (midnight).                              +
+------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
+.. figure:: /images/Manual-Lighting-Lamps-Sun-SkyAtmosphere-EarlyTwilight.jpg                                                                               |.. figure:: /images/Manual-Lighting-Lamps-Sun-SkyAtmosphere-LateTwilight.jpg+
+   :width: 200px                                                                                                                                            |   :width: 200px                                                            +
+   :figwidth: 200px                                                                                                                                         |   :figwidth: 200px                                                         +
+                                                                                                                                                            |                                                                            +
+   Sun slightly above the horizon (start of twilight).                                                                                                      |   Sun slightly below the horizon (end of twilight).                        +
+------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
+Variations in :guilabel:`Sun` orientation, :guilabel:`Sun Size` to **5.0**, all other settings to default.                                                                                                                               +
+------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
+`The 2.4 .blend file of these examples <http://wiki.blender.org/index.php/Media:Manual-Lighting-Lamps-Sun-SkyAtmosphere-Examples-SunOrientation.blend>`__.                                                                               +
+------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+


And now, the effects of various settings (examples created with `this 2.4 .blend file <http://wiki.blender.org/index.php/Media:Manual-Lighting-Lamps-Sun-SkyAtmosphere-Examples-Settings.blend>`__):


+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------+
+.. figure:: /images/Manual-Lighting-Lamps-Sun-SkyAtmosphere-Turbidity2.0.jpg |.. figure:: /images/Manual-Lighting-Lamps-Sun-SkyAtmosphere-Turbidity2.3.jpg +
+   :width: 200px                                                             |   :width: 200px                                                             +
+   :figwidth: 200px                                                          |   :figwidth: 200px                                                          +
+                                                                             |                                                                             +
+   Turbidity: 2.0.                                                           |   Turbidity: 2.3.                                                           +
+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------+
+.. figure:: /images/Manual-Lighting-Lamps-Sun-SkyAtmosphere-Turbidity5.0.jpg |.. figure:: /images/Manual-Lighting-Lamps-Sun-SkyAtmosphere-Turbidity10.0.jpg+
+   :width: 200px                                                             |   :width: 200px                                                             +
+   :figwidth: 200px                                                          |   :figwidth: 200px                                                          +
+                                                                             |                                                                             +
+   Turbidity: 5.0.                                                           |   Turbidity: 10.0.                                                          +
+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------+
+Variations in :guilabel:`Turbidity` parameter, all other settings to default.                                                                              +
+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------+


Sky
---

+--------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
+.. figure:: /images/Manual-Lighting-Lamps-Sun-SkyAtmosphere-Sky-HorBright0.0.jpg      |.. figure:: /images/Manual-Lighting-Lamps-Sun-SkyAtmosphere-Sky-HorBright0.85.jpg+
+   :width: 200px                                                                      |   :width: 200px                                                                 +
+   :figwidth: 200px                                                                   |   :figwidth: 200px                                                              +
+                                                                                      |                                                                                 +
+   Horizon Brightness: 0.0.                                                           |   Horizon Brightness: 0.85.                                                     +
+--------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
+.. figure:: /images/Manual-Lighting-Lamps-Sun-SkyAtmosphere-Sky-HorBright1.04.jpg     |.. figure:: /images/Manual-Lighting-Lamps-Sun-SkyAtmosphere-Sky-HorBright1.13.jpg+
+   :width: 200px                                                                      |   :width: 200px                                                                 +
+   :figwidth: 200px                                                                   |   :figwidth: 200px                                                              +
+                                                                                      |                                                                                 +
+   Horizon Brightness: 1.04.                                                          |   Horizon Brightness: 1.13.                                                     +
+--------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
+Variations in :guilabel:`Horizon Brightness` parameter, all other settings to default.                                                                                  +
+--------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+


+----------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
+.. figure:: /images/Manual-Lighting-Lamps-Sun-SkyAtmosphere-Sky-HorSpread0.7.jpg  |.. figure:: /images/Manual-Lighting-Lamps-Sun-SkyAtmosphere-Sky-HorSpread1.2.jpg+
+   :width: 200px                                                                  |   :width: 200px                                                                +
+   :figwidth: 200px                                                               |   :figwidth: 200px                                                             +
+                                                                                  |                                                                                +
+   Horizon Spread: 0.7.                                                           |   Horizon Spread: 1.2.                                                         +
+----------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
+.. figure:: /images/Manual-Lighting-Lamps-Sun-SkyAtmosphere-Sky-HorSpread2.2.jpg  |.. figure:: /images/Manual-Lighting-Lamps-Sun-SkyAtmosphere-Sky-HorSpread5.0.jpg+
+   :width: 200px                                                                  |   :width: 200px                                                                +
+   :figwidth: 200px                                                               |   :figwidth: 200px                                                             +
+                                                                                  |                                                                                +
+   Horizon Spread: 2.2.                                                           |   Horizon Spread: 5.0.                                                         +
+----------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
+Variations in :guilabel:`Horizon Spread` parameter, all other settings to default.                                                                                 +
+----------------------------------------------------------------------------------+--------------------------------------------------------------------------------+


+----------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
+.. figure:: /images/Manual-Lighting-Lamps-Sun-SkyAtmosphere-Sky-SunBright0.2.jpg  |.. figure:: /images/Manual-Lighting-Lamps-Sun-SkyAtmosphere-Sky-SunBright0.5.jpg+
+   :width: 200px                                                                  |   :width: 200px                                                                +
+   :figwidth: 200px                                                               |   :figwidth: 200px                                                             +
+                                                                                  |                                                                                +
+   Sun Brightness: 0.2.                                                           |   Sun Brightness: 0.5.                                                         +
+----------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
+.. figure:: /images/Manual-Lighting-Lamps-Sun-SkyAtmosphere-Sky-SunBright0.75.jpg |.. figure:: /images/Manual-Lighting-Lamps-Sun-SkyAtmosphere-Sky-SunBright1.0.jpg+
+   :width: 200px                                                                  |   :width: 200px                                                                +
+   :figwidth: 200px                                                               |   :figwidth: 200px                                                             +
+                                                                                  |                                                                                +
+   Sun Brightness: 0.75.                                                          |   Sun Brightness: 1.0.                                                         +
+----------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
+Variations in :guilabel:`Sun Brightness` parameter, all other settings to default.                                                                                 +
+----------------------------------------------------------------------------------+--------------------------------------------------------------------------------+


+------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
+.. figure:: /images/Manual-Lighting-Lamps-Sun-SkyAtmosphere-Sky-SunSize2.0.jpg|.. figure:: /images/Manual-Lighting-Lamps-Sun-SkyAtmosphere-Sky-SunSize4.0.jpg +
+   :width: 200px                                                              |   :width: 200px                                                               +
+   :figwidth: 200px                                                           |   :figwidth: 200px                                                            +
+                                                                              |                                                                               +
+   Sun Size: 2.0.                                                             |   Sun Size: 4.0.                                                              +
+------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
+.. figure:: /images/Manual-Lighting-Lamps-Sun-SkyAtmosphere-Sky-SunSize7.0.jpg|.. figure:: /images/Manual-Lighting-Lamps-Sun-SkyAtmosphere-Sky-SunSize10.0.jpg+
+   :width: 200px                                                              |   :width: 200px                                                               +
+   :figwidth: 200px                                                           |   :figwidth: 200px                                                            +
+                                                                              |                                                                               +
+   Sun Size: 7.0.                                                             |   Sun Size: 10.0.                                                             +
+------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
+Variations in :guilabel:`Sun Size` parameter, all other settings to default.                                                                                  +
+------------------------------------------------------------------------------+-------------------------------------------------------------------------------+


+-------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
+.. figure:: /images/Manual-Lighting-Lamps-Sun-SkyAtmosphere-Sky-BackLight-1.0.jpg                                  |.. figure:: /images/Manual-Lighting-Lamps-Sun-SkyAtmosphere-Sky-BackLight-0.33.jpg+
+   :width: 200px                                                                                                   |   :width: 200px                                                                  +
+   :figwidth: 200px                                                                                                |   :figwidth: 200px                                                               +
+                                                                                                                   |                                                                                  +
+   Back Light: -1.0.                                                                                               |   Back Light: -0.33.                                                             +
+-------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
+.. figure:: /images/Manual-Lighting-Lamps-Sun-SkyAtmosphere-Sky-BackLight0.33.jpg                                  |.. figure:: /images/Manual-Lighting-Lamps-Sun-SkyAtmosphere-Sky-BackLight1.0.jpg  +
+   :width: 200px                                                                                                   |   :width: 200px                                                                  +
+   :figwidth: 200px                                                                                                |   :figwidth: 200px                                                               +
+                                                                                                                   |                                                                                  +
+   Back Light: 0.33.                                                                                               |   Back Light: 1.0.                                                               +
+-------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
+Variations in :guilabel:`Back Light` parameter, :guilabel:`Sun Bright` to **2.5**, all other settings to default.                                                                                     +
+-------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+


Atmosphere
----------

For all renders below, :guilabel:`Hor.Bright` is set to **0.2**,
and :guilabel:`Sun Bright` to **2.0**.


+------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
+.. figure:: /images/Manual-Lighting-Lamps-Sun-SkyAtmosphere-Sky-SunIntensity1.0.jpg |.. figure:: /images/Manual-Lighting-Lamps-Sun-SkyAtmosphere-Sky-SunIntensity3.33.jpg+
+   :width: 200px                                                                    |   :width: 200px                                                                    +
+   :figwidth: 200px                                                                 |   :figwidth: 200px                                                                 +
+                                                                                    |                                                                                    +
+   Sun Intensity: 1.0.                                                              |   Sun Intensity: 3.33.                                                             +
+------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
+.. figure:: /images/Manual-Lighting-Lamps-Sun-SkyAtmosphere-Sky-SunIntensity6.66.jpg|.. figure:: /images/Manual-Lighting-Lamps-Sun-SkyAtmosphere-Sky-SunIntensity10.0.jpg+
+   :width: 200px                                                                    |   :width: 200px                                                                    +
+   :figwidth: 200px                                                                 |   :figwidth: 200px                                                                 +
+                                                                                    |                                                                                    +
+   Sun Intensity: 6.66.                                                             |   Sun Intensity: 10.0.                                                             +
+------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
+Variations in :guilabel:`Sun Intensity` parameter, all other settings to default.                                                                                        +
+------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+


+------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
+.. figure:: /images/Manual-Lighting-Lamps-Sun-SkyAtmosphere-Sky-Inscattering0.1.jpg |.. figure:: /images/Manual-Lighting-Lamps-Sun-SkyAtmosphere-Sky-Inscattering0.33.jpg+
+   :width: 200px                                                                    |   :width: 200px                                                                    +
+   :figwidth: 200px                                                                 |   :figwidth: 200px                                                                 +
+                                                                                    |                                                                                    +
+   Inscattering: 0.1.                                                               |   Inscattering: 0.33.                                                              +
+------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
+.. figure:: /images/Manual-Lighting-Lamps-Sun-SkyAtmosphere-Sky-Inscattering0.66.jpg|.. figure:: /images/Manual-Lighting-Lamps-Sun-SkyAtmosphere-Sky-Inscattering1.0.jpg +
+   :width: 200px                                                                    |   :width: 200px                                                                    +
+   :figwidth: 200px                                                                 |   :figwidth: 200px                                                                 +
+                                                                                    |                                                                                    +
+   Inscattering: 0.66.                                                              |   Inscattering: 1.0.                                                               +
+------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
+Variations in :guilabel:`Inscattering` parameter, all other settings to default.                                                                                         +
+------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+


+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
+.. figure:: /images/Manual-Lighting-Lamps-Sun-SkyAtmosphere-Sky-Extinction0.0.jpg |.. figure:: /images/Manual-Lighting-Lamps-Sun-SkyAtmosphere-Sky-Extinction0.33.jpg+
+   :width: 200px                                                                  |   :width: 200px                                                                  +
+   :figwidth: 200px                                                               |   :figwidth: 200px                                                               +
+                                                                                  |                                                                                  +
+   Extinction: 0.0.                                                               |   Extinction: 0.33.                                                              +
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
+.. figure:: /images/Manual-Lighting-Lamps-Sun-SkyAtmosphere-Sky-Extinction0.66.jpg|.. figure:: /images/Manual-Lighting-Lamps-Sun-SkyAtmosphere-Sky-Extinction1.0.jpg +
+   :width: 200px                                                                  |   :width: 200px                                                                  +
+   :figwidth: 200px                                                               |   :figwidth: 200px                                                               +
+                                                                                  |                                                                                  +
+   Extinction: 0.66.                                                              |   Extinction: 1.0.                                                               +
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
+Variations in :guilabel:`Extinction` parameter, all other settings to default.                                                                                       +
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+


+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
+.. figure:: /images/Manual-Lighting-Lamps-Sun-SkyAtmosphere-Sky-Distance1.0.jpg|.. figure:: /images/Manual-Lighting-Lamps-Sun-SkyAtmosphere-Sky-Distance2.0.jpg+
+   :width: 200px                                                               |   :width: 200px                                                               +
+   :figwidth: 200px                                                            |   :figwidth: 200px                                                            +
+                                                                               |                                                                               +
+   Distance: 1.0.                                                              |   Distance: 2.0.                                                              +
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
+.. figure:: /images/Manual-Lighting-Lamps-Sun-SkyAtmosphere-Sky-Distance3.0.jpg|.. figure:: /images/Manual-Lighting-Lamps-Sun-SkyAtmosphere-Sky-Distance4.0.jpg+
+   :width: 200px                                                               |   :width: 200px                                                               +
+   :figwidth: 200px                                                            |   :figwidth: 200px                                                            +
+                                                                               |                                                                               +
+   Distance: 3.0.                                                              |   Distance: 4.0.                                                              +
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
+Variations in :guilabel:`Distance` parameter, all other settings to default.                                                                                   +
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+


Hints and limitations
=====================

To always have the :guilabel:`Sun` pointing at the camera center, you can use a :doc:`TrackTo constraint <constraints/tracking/track_to>` on the sun object, with the camera as target, and :guilabel:`-Z` as the "To" axis (use either :guilabel:`X` or :guilabel:`Y` as "Up" axis). This way, to modify height/position of the sun in the rendered picture, you just have to move it; orientation is automatically handled by the constraint. Of course, if your camera itself is moving, you should also add e.g. a :doc:`Copy Location constraint <constraints/transform/copy_location>` to your :guilabel:`Sun` lamp, with the camera as target - and the :guilabel:`Offset` option activated… This way, the sun light won't change as the camera moves around.

If you use the default :guilabel:`Add` mixing type,
you should use a very dark-blue world color, to get correct "nights"…

This effect works quite well with a :guilabel:`Hemi` lamp, or some ambient occlusion,
to fill in the :guilabel:`Sun` shadows.

Atmosphere shading currently works incorrectly in reflections and refractions and is only
supported for solid shaded surfaces. This will be addressed in a later release.


