
*******************
Reflection Cubemaps
*******************

Specular Indirect Lighting is stored in an array of cubemaps. These are defined by the Reflection Cubemap objects.
They specify where to sample the scene's lighting and where to apply it.

.. seealso::

   :doc:`Indirect Lighting </render/eevee/render_settings/indirect_lighting>`.

*Screen Space Reflections* are much more precise than reflection cubemaps.
If enabled, they have priority and cubemaps are used as a fall back if a ray misses.

If *Ambient Occlusion* is enabled, it will be applied in a physically plausible manner to specular indirect lighting.

.. note::

   The cube probes are encoded into tetrahedral maps. Some distortions may occur on the negative Z hemisphere.
   Those are more visible with higher roughness values.


Blending
========

The lighting values from a Reflection Cubemap will fade outwards until the volume bounds are reached.
They will fade into the world's lighting or another Reflection Cubemap's lighting.
If multiple Reflection Cubemaps overlap, smaller (in volume) ones will always have more priority.
If an object is not inside any Reflection Cubemap influence,
or if the indirect lighting has not been baked, the world's cubemap will be used to shade it.

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Object Data --> Probe`

Distance
   A probe object only influences the lighting of nearby surfaces.
   This influence zone is defined by the Distance parameter and object scaling.
   The influence distance varies is a bit, depending on the probe type.

   For Reflection Cubemaps the influence volume can either be a box or a sphere centered on the probe's origin.

Falloff
   Percentage of the influence distance during which the influence of a probe fades linearly.

Intensity
   Intensity factor of the recorded lighting.
   Making this parameter anything other than 1.0 is not physically correct.
   Use it for tweaking or artistic purposes.

Clipping
   Define the near and far clip distances when capturing the scene.

Visibility Collection
   Sometimes, it is useful to limit which objects appear in the light probe's captured lighting.
   For instance, an object that is too close to a capture point might be better excluded.
   This is what the visibility collection does.
   Only objects that are in this collection will be visible when this probe will capture the scene.

   There is also an option to invert this behavior and effectively hide the objects inside this collection.

   .. note::

      This is only a filtering option.
      That means if an object is not visible at render time it won't be visible during the probe render.


Custom Parallax
===============

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Object Data --> Custom Parallax`

By default, the influence volume is also the parallax volume.
The parallax volume is a volume on which is projected the recorded lighting.
It should roughly fit it surrounding area. In some cases it may be better to
adjust the parallax volume without touching the influence parameters.
In this case, just enable the *Custom Parallax* and
change the shape and distance of the parallax volume independently.


Viewport Display
================

Influence
   Show the influence bounds in the 3D Viewport. The inner sphere is where the falloff starts.

Clipping
   Show the clipping distance in the 3D Viewport.

Parallax
   Show the *Custom Parallax* shape in the 3D Viewport.
