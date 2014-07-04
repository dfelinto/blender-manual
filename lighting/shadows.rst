
Shadows
=======

Light wouldn't even exist without its counterpart: shadows. Shadows are a darkening of a
portion of an object because light is being partially or totally blocked from illuminating the
object. They add contrast and volume to a scene;
there is nearly no place in the real world without shadows, so to get realistic renders,
you will need them. Blender supports the following kinds of shadows:

-

FIXME(Link Type Unsupported: #lamps;
[[#Lamps: Ray-traced Shadows|Ray-traced lamp shadows]]
)

-

FIXME(Link Type Unsupported: #lamps;
[[#Lamps: Buffered Shadows|Buffered lamp shadows]]
)

- :doc:`Ambient occlusion <lighting/ambient_occlusion>`
- :doc:`Indirect lighting <lighting/indirect_lighting>`

Ambient occlusion really isn't a shadow based on light *per se*, but based on geometry.
However, it does mimic an effect where light is prevented from fully and uniformly
illuminating an object, so it is mentioned here. Also,
it is important to mention ambient lighting,
since increasing :guilabel:`Ambient` decreases the effect of a shadow.

You can use a combination of ray-traced and buffer shadows to achieve different results.
Even within ray-traced shadows,
different lamps cast different patterns and intensities of shadow.
Depending on how you arrange your lamps,
one lamp may wipe out or override the shadow cast by another lamp.

Shadows is one of those trifectas in Blender,
where multiple things have to be set up in different areas to get results:

- The lamp has to cast shadows (ability and direction).
- An opaque object has to block light on its way (position and layer).
- Another object's material has to receive shadows (:guilabel:`Shadow` and :guilabel:`Receive Transparent` enabled).
- The render engine has to calculate shadows (:guilabel:`Shadow` for buffered shadows, :guilabel:`Shadow` and :guilabel:`Ray` for ray-traced shadows).

For example, the simple :guilabel:`Lamp`, :guilabel:`Area`, and :guilabel:`Sun` light has the ability to cast ray shadows, but not buffer shadows. The :guilabel:`Spot` light can cast both, whereas the :guilabel:`Hemi` light does not cast any. If a :guilabel:`Sun` lamp is pointing sideways, it will not cast a shadow from a sphere above a plane onto the plane, since the light is not traveling that way. All lamps able to cast shadows share some common options, described :doc:`here <lighting/shadows/properties>`.

Just to give you more shadow options (and further confuse the issue),
lamps and materials can be set to respectively **only** cast and receive shadows,
and not light the diffuse/specular aspects of the object. Also,
render layers can turn on/off the shadow pass,
and their output may or may not contain shadow information…


Lamps: Ray-traced Shadows
-------------------------

.. figure:: /images/25-Manual-Lighting-Shadow-Ray.jpg
   :width: 310px
   :figwidth: 310px

   Ray Shadow enabled for a lamp


Ray-traced shadows produce very precise shadows with very low memory use,
but at the cost of processing time.
This type of shadowing is available to all lamp types except :guilabel:`Hemi`.

As opposed to
FIXME(Link Type Unsupported: #lamps;
[[#Lamps: Buffered Shadows|buffered shadows]]
), ray-traced shadows are obtained by casting rays from a regular light source, uniformly and in all directions. The ray-tracer then records which pixel of the final image is hit by a ray light, and which is not. Those that are not are obviously obscured by a shadow.

Each light casts rays in a different way. For example,
a :guilabel:`Spot` light casts rays uniformly in all directions within a cone.
The :guilabel:`Sun` light casts rays from a infinitely distant point,
with all rays parallel to the direction of the :guilabel:`Sun` light.

For each additional light added to the scene, with ray-tracing enabled,
the rendering time increases. Ray-traced shadows require more computation than buffered
shadows but produce sharp shadow borders with very little memory resource usage.

To enable ray-traced shadows, three actions are required:

- Enable :guilabel:`Shadows` globally in the :guilabel:`Render` menu's :guilabel:`Shading` panel.
- Enable :guilabel:`Ray tracing` globally from the same panel.
- Enable ray-traced shadows for the light using the :guilabel:`Ray Shadow` button in the :guilabel:`Light` menu's :guilabel:`Shadow` panel. This panel varies depending on the type of light.
   - All lamps able to cast ray-traced shadows share some common options, described in :doc:`Ray-traced Properties <lighting/shadows/raytraced_properties>`.

Ray-traced shadows can be cast by the following types of lamp:

- :doc:`Point lamp <lighting/lamps/lamp>`
- :doc:`Spot lamp <lighting/lamps/spot>`
- :doc:`Area lamp <lighting/lamps/area>`
- :doc:`Sun lamp <lighting/lamps/sun>`


Lamps: Buffered Shadows
-----------------------

.. figure:: /images/25-Manual-Lighting-Shadow-SpotBufShad.jpg
   :width: 310px
   :figwidth: 310px

   Buffer Shadow enabled for a Spot lamp


.. figure:: /images/25-Manual-Lighting-Shadow-MatBufShad.jpg
   :width: 310px
   :figwidth: 310px

   Cast Buffer Shadows enabled for a material


:guilabel:`Buffered` shadows provide fast-rendered shadows at the expense of precision and/or quality. Buffered shadows also require more memory resources as compared to ray tracing. Using buffered shadows depends on your requirements. If you are rendering animations or can't wait hours to render a complex scene with soft shadows, buffer shadows are a good choice.

For a scanline renderer - and Blender's built-in engine *is*, among other things,
a scanline renderer - shadows can be computed using a *shadow buffer*.
This implies that an "image", as seen from the spot lamp's point of view, is "rendered" and
that the distance - in the image - for each point from the spot light is saved. Any point in
the "rendered" image that is farther away than any of those points in the spot light's image
is then considered to be in shadow. The shadow buffer stores this image data.

To enable buffered shadows these actions are required:

- Enable shadows globally from the :guilabel:`Scene` menu's :guilabel:`Gather` panel by selecting :guilabel:`Approximate`.
- Enable shadows for the light using the :guilabel:`Buffer Shadow` button in the :guilabel:`Lamp` menu's :guilabel:`Shadow` panel.
- Make sure the :guilabel:`Cast Buffer Shadows` options is enabled in each :guilabel:`Material` 's :guilabel:`Shadow` panel.


- The :doc:`Spot lamp <lighting/lamps/spot/buffered_shadows>` is the only lamp able to cast buffered shadows.


