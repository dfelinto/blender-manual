
..    TODO/Review: {{review|}} .


Animating Cameras
=================

As of Blender 2.5, :doc:`Everything is animatable <introduction/whats_new_in_this_series#animation_system>`\ . Read more about keyframes :doc:`Here <animation/keyframes>`\ .


Example
-------

As an example, we are going to create a nice and impressive camera effect,
which you can see e.g. in the first part of the Lord of the Ring: the *transtrav*\ .
Basically, the idea is to combine a forward zoom with a backward traveling (or conversely),
both controlled such as the point of interest keeps its scale in the image,
while its environment scales up or down,
depending whether it is nearer or more far from the camera…

Create a scene with a ground, and some objects laying on it.

Add a camera, place it as you like for the beginning of the transtrav
(your "key" object should be more or less at the center of the picture,
it's easier to handle!). As we are going to do a "forward" transtrav,
you should use a quite long lens at start. Go to frame **10**\ ,
and insert a keyframe for both the location (and optionally the rotation)
of the camera and its focal length.

Now, go to frame **140**\ , and move forward your camera to your key object.
Insert another keyframe for its position, and adjust its focal length until your key object
have the same visual dimensions as at the beginning. Add a key to both attributes.

This won't give you a fully perfect transtrav - to get such one,
you would have to dive into trigonometric maths… But the result is visually quite satisfying.


FIXME(Tag Unsupported:vimeo;
<vimeo>15837189</vimeo>
)


