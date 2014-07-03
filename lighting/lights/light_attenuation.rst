
Light Attenuation
=================


Description
-----------


.. figure:: /images/25-Manual-Lighting-Falloff-hilite.jpg
   :width: 312px
   :figwidth: 312px

   Lamp panel, falloff options highlighted


There are two main controls for light falloff for :guilabel:`Point` and :guilabel:`Spot` lamps.

- The lamp :guilabel:`Falloff` type drop-down list, and
- The :guilabel:`Sphere` button.


Falloff types
-------------


Lin/Quad Weighted
~~~~~~~~~~~~~~~~~


.. figure:: /images/25-Manual-Lighting-Falloff-linquad.jpg
   :width: 308px
   :figwidth: 308px

   Lamp panel with Lin/Quad Weighted Falloff options highlighted


When this setting is chosen, two sliders are shown,
:guilabel:`Linear` and :guilabel:`Quadratic`\ ,
which control respectively the "linearness" and "quadraticness" of the falloff curve.

This lamp falloff type is in effect allowing the mixing of the two light attenuation profiles
(linear and quadratic attenuation types).


Linear
______

This slider input field can have a value between **0.0** and **1.0**\ .
A value of **1.0** in the :guilabel:`Linear` field and **0.0** in the
:guilabel:`Quadratic` field in effect means that the light from this source is completely
linear. This means that at the number of Blender Units distance specified in the
:guilabel:`Distance` field,
this light source's intensity will be half the value it was originally.

When the :guilabel:`Quadratic` slider is set to **0.0**\ , the formula for working out the
attenuation at a particular range for full linear attenuation is:

``I = E × (D / (D + L × r))``

Where

- ``I`` is the calculated Intensity of light.
- ``E`` is the current :guilabel:`Energy` slider setting.
- ``D`` is the current setting of the :guilabel:`Dist` field.
- ``L`` is the current setting of the :guilabel:`Linear` slider.
- ``r`` is the distance from the lamp where the light intensity gets measured.


Quadratic
_________


.. figure:: /images/Manual_-_Light_-_Example_-_Default_Lin-Quad_Weighted.jpg
   :width: 250px
   :figwidth: 250px

   Lamp with Lin/Quad Weighted falloff default settings


This slider input field can have a value between **0.0** and **1.0**\ . A value of **1.0**
in the :guilabel:`Quadratic` field and **0.0** in the :guilabel:`Linear` field means that
the light from this source is completely quadratic.

Quadratic attenuation type lighting is considered a more accurate representation of how light
attenuates (in the real world). In fact, fully quadratic attenuation is selected by default
for :guilabel:`Lin/Quad Weighted` lamp fallout
(see *Lamp with* :guilabel:`Lin/Quad Weighted` *falloff default settings*\ ).

Here again,
the light intensity is half when it reaches the :guilabel:`Distance` value from the lamp.
Comparing the quadratic falloff to the linear falloff,
the intensity decays much slower at distances lower than the set :guilabel:`Distance`\ ,
but it attenuates much quicker after :guilabel:`Distance` is reached.


When the :guilabel:`Linear` slider is set to **0.0**\ , the formula for working out the
attenuation at a particular range for full quadratic attenuation is:

``I = E × (D``\ :sup:`2` ``/ (D``\ :sup:`2` ``+ Q × r``\ :sup:`2`\ ``))``

Where

- ``I`` is the calculated Intensity of light.
- ``E`` is the current :guilabel:`Energy` slider setting.
- ``D`` is the current setting of the :guilabel:`Dist` field.
- ``Q`` is the current setting of the :guilabel:`Quad` slider.
- ``r`` is the distance from the lamp where the light intensity gets measured.


Mixing "Linear" and "Quad"
__________________________

If both the :guilabel:`Linear` and :guilabel:`Quad` slider fields have values greater than
**0.0**\ , then the formula used to calculate the light attenuation profile changes to this:

``I = E × (D / (D + L × r)) × (D``\ :sup:`2` ``/ (D``\ :sup:`2` ``+ Q × r``\ :sup:`2`\ ``))``

Where

- ``I`` is the calculated Intensity of light.
- ``E`` is the current :guilabel:`Energy` slider setting.
- ``D`` is the current setting of the :guilabel:`Dist` field.
- ``L`` is the current setting of the :guilabel:`Linear` slider.
- ``Q`` is the current setting of the :guilabel:`Quad` slider.
- ``r`` is the distance from the lamp where the light intensity gets measured.


Zeroing both "Linear" and "Quad"
________________________________

If both the :guilabel:`Linear` and :guilabel:`Quadratic` sliders have **0.0** as their
values, the light intensity will not attenuate with distance.
This does not mean that the light will not get darker—it will,
but only because the energy the light has is spread out over a wider and wider distance.
The total amount of energy in the spread-out light will remain the same, though.
The light angle also affects the amount of light you see.
It is in fact the behavior of light in the deep space vacuum.

If what you want is a light source that doesn't attenuate and gives the same amount of light
intensity to each area it hits,
you need a light with properties like the :guilabel:`Constant` lamp :guilabel:`Falloff` type.

Also, when the :guilabel:`Linear` and :guilabel:`Quad` sliders are both **0.0** values the
:guilabel:`Distance` field ceases to have any influence on the light attenuation,
as shown by the equation above.


Graphical Summary
_________________

Below is a graph summarizing the lin/quad attenuation type,
showing attenuation with or without the :guilabel:`Sphere` option (described later).


.. figure:: /images/Manual-Part-V-DistanceGraph.jpg
   :width: 610px
   :figwidth: 610px


Custom Curve
~~~~~~~~~~~~

The :guilabel:`Custom Curve` lamp :guilabel:`Falloff` type is very flexible.

Most other lamp falloff types work by having their light intensity start at its maximum
(when nearest to the light source) and then with some predetermined pattern decrease their
light intensity when the distance from the light source increases.

When using the :guilabel:`Custom Curve` Lamp Falloff type,
a new panel is created called :guilabel:`Falloff Curve`\ . This :guilabel:`Falloff Curve`
profile graph allows the user to alter how intense light is at a particular point along a
light's attenuation profile (i.e. at a specific distance from the light source).

The :guilabel:`Falloff Curve` profile graph has two axes,
the "\ ``Distance``\ " axis and the "\ ``Intensity``\ " axis.
Distance axis
   It represents the position at a particular point along a light source's attenuation path. The far left is at the position of the light source and the far right is the place where the light source's influence would normally be completely attenuated. I say "normally would" because the :guilabel:`Falloff Curve` can be altered to do the exact opposite if required.
Intensity axis
   It represents the intensity at a particular point along a light source's attenuation path. Higher intensity is represented by being higher up the intensity axis, while lower intensity light is represented by being lower down on the intensity axis.

Altering the :guilabel:`Falloff Curve` profile graph is easy. Just :kbd:`lmb` click on a
part of the graph you want to alter and drag it where you want it to be.
If when you click you are over or near one of the tiny black square handles,
it will turn white, indicating that this  handle is now selected,
and you will be able to drag it to a new position.
If when you click on the graph you are not near a handle,
one will be created at the point that you clicked, which you can then drag where you wish.
You can also create handles at specific parts of the graph,
clicking with :kbd:`lmb` while holding :kbd:`ctrl` key;
it will create a new handle at the point you have clicked.

In the example below (the default for the :guilabel:`Falloff Curve` Profile Graph),
the graph shows that the intensity of the light starts off at its maximum
(when near the light), and linearly attenuates as it moves to the right
(further away from the light source).


+----------------------------------------------------------------+----------------------------------------------------------------------------------+
+.. figure:: /images/25-Manual-Lighting-Falloff-CustomDefault.jpg|.. figure:: /images/Manual_-_Light_-_Example_-_Default_Custom_Curve.jpg           +
+   :width: 306px                                                |   :width: 250px                                                                  +
+   :figwidth: 306px                                             |   :figwidth: 250px                                                               +
+                                                                |                                                                                  +
+   Default Falloff Curve panel graph.                           |   Render showing the Custom Curve lamp falloff type effect with default settings.+
+----------------------------------------------------------------+----------------------------------------------------------------------------------+


If you want to have a light attenuation profile that gets more intense as it moves away from
the light source, you could alter the graph as below:


+-----------------------------------------------------------------+------------------------------------------------------------------------------+
+.. figure:: /images/25-Manual-Lighting-Falloff-CustomReversed.jpg|.. figure:: /images/Manual_-_Lights_-_Lamps_-_Falloff_Curve_Reverse_Render.jpg+
+   :width: 310px                                                 |   :width: 250px                                                              +
+   :figwidth: 310px                                              |   :figwidth: 250px                                                           +
+                                                                 |                                                                              +
+   Falloff Curve for reversed attenuation.                       |   Falloff Curve for reversed attenuation rendered.                           +
+-----------------------------------------------------------------+------------------------------------------------------------------------------+


You are obviously not just limited to simple changes such as reversing the attenuation
profile, you can have almost any profile you desire.

Here is another example of a different :guilabel:`Falloff Curve` profile graph,
along with its resultant render output:


+---------------------------------------------------------------+------------------------------------------------------------------------------------+
+.. figure:: /images/25-Manual-Lighting-Falloff-CustomOscill.jpg|.. figure:: /images/Manual_-_Lights_-_Lamps_-_Falloff_Curve_Render.jpg              +
+   :width: 310px                                               |   :width: 250px                                                                    +
+   :figwidth: 310px                                            |   :figwidth: 250px                                                                 +
+                                                               |                                                                                    +
+   Oscillating attenuation profile.                            |   Render showing the effects of a "wavelet" profile graph on the light attenuation.+
+---------------------------------------------------------------+------------------------------------------------------------------------------------+


Inverse Square
~~~~~~~~~~~~~~


.. figure:: /images/Manual_-_Light_-_Example_-_Inverse_Square.jpg
   :width: 300px
   :figwidth: 300px

   Render showing the Inverse Square lamp falloff type effect with default settings.


This lamp falloff type attenuates its intensity according to inverse square law,
scaled by the :guilabel:`Distance` value. Inverse square is a sharper, realistic decay,
useful for lighting such as desk lamps and street lights.
This is similar to the old :guilabel:`Quad` option (and consequently, to the new
:guilabel:`Lin/Quad Weighted` option with :guilabel:`Linear` to **0.0** and :guilabel:`Quad`
to **1.0**\ ), with slight changes.


Inverse Linear
~~~~~~~~~~~~~~


.. figure:: /images/Manual_-_Light_-_Example_-_Inverse_Linear.jpg
   :width: 300px
   :figwidth: 300px

   Render showing the Inverse Linear lamp falloff type effect with default settings.


This lamp falloff type attenuates its intensity linearly,
scaled by the :guilabel:`Dist` value. This is the default setting, behaving the same as the
default in previous Blender versions without :guilabel:`Quad` switched on, and consequently,
like the new :guilabel:`Lin/Quad Weighted` option with :guilabel:`Linear` to **1.0** and
:guilabel:`Quad` to **0.0**\ . This isn't physically accurate,
but can be easier to light with.


Constant
~~~~~~~~


.. figure:: /images/Manual_-_Light_-_Example_-_Constant.jpg
   :width: 300px
   :figwidth: 300px

   Render showing the Constant lamp falloff type effect with default settings.


This lamp falloff type does not attenuate its intensity with distance.
This is useful for distant light sources like the sun or sky,
which are so far away that their falloff isn't noticeable.
:guilabel:`Sun` and :guilabel:`Hemi` lamps always have constant falloff.


Sphere
------


.. figure:: /images/25-Manual-Lighting-Falloff-PointSphere.jpg
   :width: 300px
   :figwidth: 300px

   Screenshot of the 3D view window, showing the Sphere light clipping circle.


The :guilabel:`Sphere` option restricts the light illumination range of a :guilabel:`Lamp` or
:guilabel:`Spot` lamp, so that it will completely stop illuminating an area once it reaches
the number of Blender Units away from the Lamp, as specified in the :guilabel:`Dist` field.

When the :guilabel:`Sphere` option is active,
a dotted sphere will appear around the light source,
indicating the demarcation point at which this light intensity will be null.


The :guilabel:`Sphere` option adds a term to the chosen attenuation law, whatever it is:

``I' = I × (D - r) / D`` *if* ``r < D; 0`` *otherwise*

Where:

- ``I'`` is the required Intensity of light (with the :guilabel:`Sphere` option activated).
- ``I`` is the intensity of light calculated by the chosen attenuation law (without the :guilabel:`Sphere` option).
- ``D`` is the current setting of the :guilabel:`Dist` field.
- ``r`` is the distance from the lamp where the light intensity gets measured.

See the graphic at the end of the description of the :guilabel:`Lin/Quad Weighted` attenuation
option.


+-------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
+.. figure:: /images/Manual_-_Light_-_Constant_Falloff_-_Sphere_Active_-_Lighted_Plane.jpg              |.. figure:: /images/Manual_-_Light_-_Constant_Falloff_-_Sphere_Deactivated_-_Lighted_Plane.jpg              +
+   :width: 300px                                                                                       |   :width: 300px                                                                                            +
+   :figwidth: 300px                                                                                    |   :figwidth: 300px                                                                                         +
+                                                                                                       |                                                                                                            +
+   Render showing the light attenuation of a Constant falloff light type with the Sphere option active.|   Render showing the light attenuation of a Constant falloff light type with the Sphere option deactivated.+
+-------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+


Examples
--------


Distance
~~~~~~~~

In this example, the :guilabel:`Lamp` has been set pretty close to the group of planes.
This causes the light to affect the front, middle and rear planes more dramatically.
Looking at (\ *Various* :guilabel:`Dist`\ *ance settings*\ ),
you can see that as the :guilabel:`Dist` is increased,
more and more objects become progressively brighter.


+-----------------------------------------------------------+------------------------------------------------------------+-------------------------------------------------------------+
+.. figure:: /images/Manual-Part-V-LampRender-Distance10.jpg|.. figure:: /images/Manual-Part-V-LampRender-Distance100.jpg|.. figure:: /images/Manual-Part-V-LampRender-Distance1000.jpg+
+                                                           |                                                            |                                                             +
+   Distance: 10.                                           |   Distance: 100.                                           |   Distance: 1000.                                           +
+-----------------------------------------------------------+------------------------------------------------------------+-------------------------------------------------------------+
+Various :guilabel:`Distance` settings (shadows disabled).                                                                                                                             +
+-----------------------------------------------------------+------------------------------------------------------------+-------------------------------------------------------------+


The :guilabel:`Distance` parameter is controlling where the light is falling - at a linear
rate by default - to half its original value from the light's origin.
As you increase or decrease this value, you are changing where this half falloff occurs. You
could think of :guilabel:`Distance` as the surface of a sphere and the surface is where the
light's intensity has fallen to half its strength in all directions.
Note that the light's intensity continues to fall even after :guilabel:`Distance`\ .
:guilabel:`Distance` just specifies the distance where half of the light's energy has weakened.

Notice in (\ :guilabel:`Distance`\ *:* **1000**\ ) that the farthest objects are very bright.
This is because the falloff has been extended far into the distance,
which means the light is very strong when it hits the last few objects. It is not until
**1000** units that the light's intensity has fallen to half of its original intensity.

Contrast this with (\ :guilabel:`Distance`\ *:* **10**\ ),
where the falloff occurs so soon that the farther objects are barely lit.
The light's intensity has fallen by a half by time it even reaches the tenth object.

You may be wondering why the first few planes appear to be dimmer? This is because the surface
angle between the light and the object's surface normal is getting close to oblique.
That is the nature of a :guilabel:`Lamp` light object. By moving the light infinitely far away
you would begin to approach the characteristics of the :guilabel:`Sun` lamp type.


Inverse Square
~~~~~~~~~~~~~~

:guilabel:`Inverse Square` makes the light's intensity falloff with a non-linear rate, or specifically, a quadratic rate. The characteristic feature of using :guilabel:`Inverse Square` is that the light's intensity begins to fall off very slowly but then starts falling off very rapidly. We can see this in the (\ :guilabel:`Inverse Square` *selected*\ ) images.


+-------------------------------------------------------------------+--------------------------------------------------------+---------------------------------------------------------+
+.. figure:: /images/Manual-Part-V-LampRender-Quad10.jpg            |.. figure:: /images/Manual-Part-V-LampRender-Quad100.jpg|.. figure:: /images/Manual-Part-V-LampRender-Quad1000.jpg+
+                                                                   |                                                        |                                                         +
+   Inverse Square with 10.                                         |   Inverse Square with 100.                             |   Inverse Square with 1000.                             +
+-------------------------------------------------------------------+--------------------------------------------------------+---------------------------------------------------------+
+:guilabel:`Inverse Square` selected (with the specified distances).                                                                                                                   +
+-------------------------------------------------------------------+--------------------------------------------------------+---------------------------------------------------------+


With :guilabel:`Inverse Square` selected, the :guilabel:`Distance` field specifies where the light begins to fall off faster, roughly speaking; see the light attenuation
FIXME(TODO: Internal Link;
[[#Falloff types|description]]
) for more info.

In (\ :guilabel:`Inverse Square` *with* **10**\ ),
the light's intensity has fallen so quickly that the last few objects aren't even lit.

Both (\ :guilabel:`Inverse Square` *with* **100**\ ) and
(\ :guilabel:`Inverse Square` *with* **1000**\ ) appear to be almost identical and that is
because the :guilabel:`Distance` is set beyond the farthest object's distance which is at
about **40 BU** out. Hence, all the objects get almost the full intensity of the light.

As above, the first few objects are dimmer than farther objects because they are very close to
the light. Remember, the brightness of an object's surface is also based on the angle between
the surface normal of an object and the ray of light coming from the lamp.

This means there are at least two things that are controlling the surface's brightness:
intensity and the angle between the light source and the surface's normal.


Sphere
~~~~~~


.. figure:: /images/Manual-Part-V-LampRender-SphereView.jpg

   Clipping Sphere.


:guilabel:`Sphere` indicates that the light's intensity is null at the :guilabel:`Distance` distance and beyond, regardless of the chosen light's falloff. In (\ *Clipping Sphere*\ ) you can see a side view example of the setup with :guilabel:`Sphere` enabled and a distance of **10**\ .

Any objects beyond the sphere receive no light from the lamp.

The :guilabel:`Distance` field is now specifying both where the light's rays become null, and the intensity's ratio falloff setting. Note that there is no abrupt transition at the sphere: the light attenuation is progressive (for more details, see the descriptions of the
FIXME(TODO: Internal Link;
[[#Sphere|{{Literal|Sphere}} options]]
) and
FIXME(TODO: Internal Link;
[[#Falloff types|light attenuations]]
) above).


+--------------------------------------------------------------------------------------------------+---------------------------------------------------------+---------------------------------------------------------+
+.. figure:: /images/Manual-Part-V-LampRender-Sphere10.jpg                                         |.. figure:: /images/Manual-Part-V-LampRender-Sphere20.jpg|.. figure:: /images/Manual-Part-V-LampRender-Sphere40.jpg+
+                                                                                                  |                                                         |                                                         +
+   Sphere with 10.                                                                                |   Sphere with 20.                                       |   Sphere with 40.                                       +
+--------------------------------------------------------------------------------------------------+---------------------------------------------------------+---------------------------------------------------------+
+:guilabel:`Sphere` enabled with the specified distances, :guilabel:`Inverse Linear` light falloff.                                                                                                                    +
+--------------------------------------------------------------------------------------------------+---------------------------------------------------------+---------------------------------------------------------+


In (\ :guilabel:`Sphere` *with* **10**\ ), the clipping sphere's radius is **10** units,
which means the light's intensity is also being controlled by **10** units of distance.
With a linear attenuation,
the light's intensity has fallen very low even before it gets to the first object.

In (\ :guilabel:`Sphere` *with* **20**\ ),
the clipping sphere's radius is now **20 BU** and some light is reaching the middle objects.

In (\ :guilabel:`Sphere` *with* **40**\ ), the clipping sphere's radius is now **40** units,
which is beyond the last object. However, the light doesn't make it to the last few objects
because the intensity has fallen to nearly **0**\ .


Hints
-----

If a :guilabel:`Lamp` light is set to not cast shadows,
it illuminates through walls and the like.
If you want to achieve some nice effects like a fire,
or a candle-lit room interior seen from outside a window,
the :guilabel:`Sphere` option is a must. By carefully working on the :guilabel:`Distance`
value you can make your warm firelight shed only within the room,
while illuminating outside with a cool moonlight,
the latter achieved with a :guilabel:`Sun` or :guilabel:`Hemi` light or both.


