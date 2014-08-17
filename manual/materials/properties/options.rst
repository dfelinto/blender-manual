
Options
*******

.. figure:: /images/Doc_2.6_Materials_Properties_Options.jpg

   Material Options Panel


This panel provides a series of control options concerning how objects using this material
will appear in the rendered image. All controls are default "Off" unless otherwise stated.

**Traceable** (default On)
   Include this material and the geometry that uses it in ray-tracing calculations. See :doc:`Transparency <materials/properties/transparency>` for details of ray-tracing.

**Full Oversampling**
   Force this material to render full shading/textures for all :doc:`anti-aliasing <render/oversampling_(antialiasing)>` samples.

**Sky**
   Render this material with zero alpha, but with :doc:`sky background <lighting/lamps/sun/sky_and_atmosphere>` in place (scanline only)

**Use Mist**
   Use :doc:`mist <world/mist>` on this material (see "World Settings" for more details)

**Invert Z depth**
Render material's faces with an inverted Z buffer (scanline only)

**Z Offset**
   Give faces an artificial Z offset for Z transparency.

**Light Group**
   Limit lighting to lamps in this :doc:`light group <lighting/lights/lights_in_other_contexts>`.

**Exclusive**
   Uses the :doc:`light group <lighting/lights/lights_in_other_contexts>`  exclusively - these lamps are excluded from other scene lighting

**Local**
   When linked in, uses local :doc:`light group <lighting/lights/lights_in_other_contexts>`  with the same name.


**Face Textures**
   Replace object's base color with color from :doc:`UV map <textures/mapping/uv>` image textures.

**Face Textures Alpha**
   Replace object's base alpha with alpha from :doc:`UV map <textures/mapping/uv>` image textures.

**Vertex Color Paint**
   Replace object's base color with :doc:`vertex paint <materials/vertex_paint>` colors (multiply with 'texture face' face assigned textures)

**Vertex Color Light**
   Add :doc:`vertex paint <materials/vertex_paint>` colors as additional lighting. (This can be used to produce good incandescence effects).

**Object Color**
   Modulate the result with a per object color

**UV Project** (default On)
   Use to ensure UV interpolation is correct for camera projections (use with :doc:`UV project <modifiers/modify/uv_project>` modifier).

**Pass Index**
   Index number for the IndexMA render pass.


