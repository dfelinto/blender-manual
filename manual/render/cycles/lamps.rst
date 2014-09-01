
Lamps
*****

Next to lighting from the background and any object with an emission shader,
lamps are another way to add light into the scene.
The difference is that they are not directly visible in the rendered image,
and can be more easily managed as objects of their own type.

Type
   Currently **Point**, **Spot**, **Area** and **Sun** lamps are supported. Hemi lamps are not supported,
   and will be rendered as point and sun lamps respectively, but they may start working in the future,
   so it's best not to enable them to preserve compatibility.

Size
   Size of the lamp in Blender Units; increasing this will result in softer shadows and shading.

Cast Shadow
   By disabling this option, light from lamps will not be blocked by objects in-between.
   This can speed up rendering by not having to trace rays to the light source.


Point Lamp
==========

Point lamps emit light equally in all directions.
By setting the :guilabel:`Size` larger than zero, they become spherical lamps,
which give softer shadows and shading. The strength of point lamps is specified in Watts.


Spot Lamp
=========

Spot lamps emit light in a particular direction, inside a cone.
By setting the :guilabel:`Size` larger than zero, they can cast softer shadows and shading.
The size parameter defines the size of the cone,
while the blend parameter can soften the edges of the cone.


Area Lamp
=========

Area lamps emit light from a square or rectangular area with a Lambertian distribution.


Sun Lamp
========

Sun lamps emit light in a given direction. Their position is not taken into account;
they are always located outside of the scene, infinitely far away,
and will not result in any distance falloff.

Because they are not located inside the scene, their strength uses different units,
and should typically be set to lower values than other lights.
