
..    TODO/Review: {{review|}} .


Animating Lamps Properties
**************************

As of Blender 2.5, :doc:`Everything is animatable </introduction/whats_new_in_this_series#animation_system>`. Read more about keyframes :doc:`Here </animation/keyframes>`.


Example
=======

Let's illustrate this with a flying torch deep in a cave.

We won't detail the cave and torch creation - the first one is an deformed icosphere with :guilabel:`Subsurf` and :doc:`Displace modifiers </modifiers/deform/displace>`, and the second one, a cylinder scaled and subdivided several times in its length, with a :doc:`particle system </physics/particles>` to materialize its fire.

The torch will be the only light source of the scene. Add four :guilabel:`Lamp` lamps,
all using the same lamp datablock. Place them around the tip of the torch,
and parent them to it. Give them an orange color (e.g. ``(1.0, 0.8, 0.4)``),
a short :guilabel:`Distance` (**2.0**, but this depends on the size of your cave!),
and an :guilabel:`Inverse Square` falloff. Also let them cast ray shadows (soft shadows,
if you have enough computing power).

Right click on the :guilabel:`Energy` parameter and :guilabel:`Insert Keyframe` to create an
Fcurve, then open the graph editor to edit the keyframes. You can for example start at zero
(no energy, the scene is whole black), give a short and intense flash
(**10** over a few frames) to simulate a sort of lightning lighting the fire,
then back to very low (**0.25**),
and then a gently varying curve over the rest of the scene,
to simulate the irregularities of the flames.

You might also use the same animation to control the particle system emmission,
to synchronize the quantity of particles with the luminosity of the lamps.

Once your torch is flying, you should get something as shown below - you can download the blend file `here <http://wiki.blender.org/index.php/File:ManAnimationTechsLampExFlyingTorch.blend>`__.


FIXME(Tag Unsupported:vimeo;
<vimeo>15837328</vimeo>
)


