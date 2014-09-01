
..    TODO/Review: {{review|partial=X}} .


Volumetric Lighting
*******************

According to Wikipedia, `volumetric lighting <http://en.wikipedia.org/wiki/Volumetric_lighting>`__
   « *is a technique used in 3D computer graphics to add lighting effects to a rendered scene. It allows the viewer to see beams of light shining through the environment; seeing sunbeams streaming through an open window is an example of volumetric lighting, also known as God rays. The term seems to have been introduced from cinematography and is now widely applied to 3D modeling and rendering especially in the field of 3D gaming.*
   *In volumetric lighting, the light cone emitted by a light source is modeled as a transparent object and considered as a container of a "volume": as a result, light has the capability to give the effect of passing through an actual three dimensional medium (such as fog, dust, smoke, or steam) that is inside its volume, just like in the real world.* »

A classic example is the search light with a visible halo/shaft of light being emitted from it
as the search light sweeps around.

By default Blender does not model this aspect of light.
For example when Blender lights something with a :guilabel:`Spot` light, you see the objects
and area on the floor lit but not the shaft/halo of light coming from the spotlight as it
progresses to its target and would get scattered on the way.

The halo/shaft of light is caused in the real world by light being scattered by particles in
the air,
some of which get diverted into your eye and that you perceive as a halo/shaft of light.
The scattering of light from a source can be simulated in Blender using various options,
but by default is not activated.

The only lamp able to create volumetric effects is the :doc:`Spot lamp </lighting/lamps/spot/halos>`
(even thought you might consider some of the :doc:`"Sky & Atmosphere" effects </lighting/lamps/sun/sky_and_atmosphere>`
of the :guilabel:`Sun` lamp as volumetric as well).


Example
=======

`Blend file of spotlight animation. <http://wiki.blender.org/index.php/Media:Manual - Shadow and Spot - Spotlight Animation.blend>`__


FIXME(Tag Unsupported:vimeo;
<vimeo>1827483</vimeo>
)


See also
********

- :doc:`Mist </world/mist>`
- :doc:`Smoke </physics/smoke>`
- :doc:`Volumetric Materials </materials/volumetric>`


