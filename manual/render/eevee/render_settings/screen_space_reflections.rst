.. _bpy.types.SceneEEVEE.ssr:

************************
Screen Space Reflections
************************

If this effect is enabled, all Materials will use the depth buffer and
the previous frame color to create more accurate reflection than reflection probes.

If a *Reflection Plane* is near a reflective surface,
it will be used as the source for tracing rays more efficiently and fix the partial visibility problem.

.. figure:: /images/render_eevee_render-settings_screen-space-reflections_planar-reflection-combo.jpg

However, the reflected color will not contain the following effects:
Subsurface scattering, volumetrics, screen space reflections, screen space refractions.

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Render --> Screen Space Reflections`

Refractions
   Screen space refractions work the same way as screen space reflections and use the same parameters.
   But they are not enabled by default on all surfaces.
   Enabling it will have a small performance cost.
   You need to enable them in :menuselection:`Material Properties --> Settings`.
   Materials using screen space refractions will not cast screen space reflections.

Half Resolution Trace
   Use half resolution ray tracing. Only cast a ray for every fourth pixel.
   Enabling this option drastically reduces video memory usage and increases performance at the cost of quality.

Trace Precision
   Increases precision of the ray trace but introduces more noise and lowers the maximum trace distance.
   Increased precision also increases performance cost.

Thickness
   How thick to consider the pixels of the depth buffer during the tracing.
   Higher values will stretch the reflections and add flickering. Lower values may make the ray miss surfaces.

Edge Fading
   Smoothly fade out the reflected and refracted pixels if they are close to a screen edge.
   The unit is in screen percentage.

Clamp
   Clamp the reflected color intensity to remove noise and :term:`Fireflies`.

.. seealso:: :ref:`Limitations <eevee-limitations-reflections>`.
