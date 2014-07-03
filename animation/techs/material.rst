
..    TODO/Review: {{review|}} .


Animating Material Attributes
=============================

As of Blender 2.5, :doc:`Everything is animatable <introduction/whats_new_in_this_series#animation_system>`\ . Read more about keyframes :doc:`Here <animation/keyframes>`\ .

Before reading this page, you should know about Blender's materials - if not, read :doc:`this chapter <materials>` first!

Animated materials can be a very powerful tool, for many different purposes. For example,
you can use them to simulate the color changes of a chameleon's skin,
a video screen lighting up, the surface of a river or lake, a light lighting up
(with an halo material), etc., etc.

The possibilities are nearly unlimited. For example,
you could keyframe the :guilabel:`Glossiness` of raytraced reflection/transparency,
which would enable the simulation of condensation spreading over a mirror or window…).


Example
-------

As an illustration, we'll create a simple "psychedelic" background. This obviously won't
demonstrate all possibilities of material animation - but I think this would need at least a
whole book!

Add a plane and a camera, such that the plane faces the camera and covers the whole view.

Add a material to the plane. As we won't use any light,
set its :guilabel:`Emit` value to **1.0**\ .

Create Fcurves for :guilabel:`R`\ , :guilabel:`G` and :guilabel:`B`\ ,
with a few random control points, all in the ``[0.0, 1.0]`` range.
Manage to have three different length between the first and last keyframes,
and enable the :guilabel:`Cyclic` extend mode (\ :kbd:`E-pad2`\ ). This way,
with the three curves cycling over various periods, you'll get a never-the-same color
animation! Unless you want to get a "time-tileable" animation, in which case you should manage
to get exactly the same color at start and end… You can also create an :guilabel:`Emit`
Fcurve, e.g. to create a fade in/out…

Now, let's add a bit of fun in this plain colored background.
Add a texture to the material and, in the :guilabel:`Texture` sub-context,
select a procedural texture (\ :guilabel:`DistortedNoise`\ , for example,
but any one will work - follow your taste!), and set it to your liking.

Back in the :guilabel:`Material` sub-context,
choose to what you want to map the texture - for this example,
I chose to map it to diffuse color in :guilabel:`Difference` mode, in a first texture channel,
and to emit value in :guilabel:`Mul`\ tiply mode, in a second texture channel.

Finally, animate the Z offset of the mapping of both channels
(define a first :guilabel:`OfsZ` Fcurve,
and use the copy/paste buttons to exactly copy it to the second texture channel's curve).
Here again, you can either have two different values for start and end,
or the same if you want a cyclic animation…

Usually, you will create a slow, linear variation of the Z offset (i.e.
a straight curve with low gradient), e.g.
a decay of **1.0** over **500** to **1000** frames,
but the only way to find the good value is to make preview renders!

You should get something similar to what shown below. You can download the blend file

`here <http://wiki.blender.org/index.php/File:ManAnimationTechsMaterialExPshychedelic.blend>`__\ .


FIXME(Tag Unsupported:vimeo;
<vimeo>15837405</vimeo>
)


