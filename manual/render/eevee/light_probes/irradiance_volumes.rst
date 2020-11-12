
******************
Irradiance Volumes
******************

Diffuse indirect lighting is stored in volumetric arrays.
These arrays are defined by the user using Irradiance Volume objects.
They control how arrays are placed in the world as well as their resolution.

Lighting is computed at the dot positions visible when the Irradiance Volume object is selected.

.. seealso::

   :doc:`Indirect Lighting </render/eevee/render_settings/indirect_lighting>`.

If Ambient Occlusion is enabled, it will be applied onto diffuse indirect lighting.
If both Ambient Occlusion and "Bent Normals" are enabled
the indirect lighting will be sampled from the least occluded direction and appear more correct.

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Object Data --> Probe`

Distance
   A probe object only influences the lighting of nearby surfaces.
   This influence zone is defined by the Distance parameter and object scaling.
   The influence distance varies a bit, depending on the probe type.

   For Irradiance Volumes, the influence inside the volume is always 100%.
   The influence decays only outside of the volume until
   the distance to the volume reaches the Distance parameter value (in local space).

Falloff
   Percentage of the influence distance during which the influence of a probe fades linearly.

Intensity
   Intensity factor of the recorded lighting.
   Making this parameter anything other than 1.0 is not physically correct. Use it for tweaking or artistic purposes.

Resolution
   Spatial resolution for Irradiance Volumes is determined per probe.
   The local volume is divided into a regular grid of the specified dimensions.
   One irradiance sample will be computed for each cell in this grid.

Clipping
   Defines the near and far clip distances when capturing the scene.

   .. warning::

      Clipping distances are applied at the samples positions and *not* at the grid origin.

Visibility Collection
   In some cases, it is useful to limit which objects appear in the light probe's captured lighting.
   For instance, an object that is too close to a capture point might be better excluded.
   This is what the visibility collection does.
   Only objects that are in this collection will be visible when this probes captures the scene.

   There is also an option to invert this behavior and effectively hide the objects in this collection.

   .. note::

      This is only a filtering option. That means that if an object is not visible at render time
      it won't be visible during the probe render.


Visibility
==========

For every grid point a small Variance Shadow Map is rendered.
This visibility cubemap is used to reduce light leaking behind occluders.
You can tweak the size of this map inside the render settings and
tweak the bias and blur factors per grid inside the Probe Properties tab.

   Bias
      Reduces self-shadowing.

   Bleed Bias
      Increases the "contrast" of the depth test result.

   Blur
      Amount of blur to apply when filtering the visibility shadow map.
      Does not increase runtime cost but has a small effect on baking time.


Blending
========

The lighting values from an Irradiance Volume will fade outwards until the volume bounds are reached.
They will fade into the world's lighting or another Irradiance Volume's lighting.

If multiple Irradiance Volumes overlap, smaller (in volume) ones will always have more priority.

If an object is not inside any Irradiance Volume, or if the indirect lighting has not been baked,
the world's diffuse lighting will be used to shade it.

.. tip::

   - When lighting indoor environments, try to align grids with the room shape.
   - Try not to put too much resolution in empty areas or areas with a low amount of lighting variation.
   - You can fix bad samples by adding a smaller grid near the problematic area.


Viewport Display
================

Influence
   Show the influence bounds in the 3D Viewport. The inner sphere is where the falloff starts.

Clipping
   Show the clipping distance in the 3D Viewport.
