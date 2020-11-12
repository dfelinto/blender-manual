.. _bpy.types.SceneEEVEE.bloom:

*****
Bloom
*****

Bloom is a post-process effect that diffuses very bright pixels. This mimics lens artifacts of real cameras.
This allows a better sense of what the actual intensities of the pixels are.

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Render --> Bloom`

Threshold
   Filters out pixels under this level of brightness.

Knee
   Makes transition between under/over-threshold gradual.

Radius
   Bloom spread distance.

Color
   Color applied to the bloom effect.

Intensity
   Blend factor.

Clamp
   Maximum intensity a bloom pixel can have.
