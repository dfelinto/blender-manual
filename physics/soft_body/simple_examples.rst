
Simple examples
===============


some simple examples showing the power of softbody physics.


bouncing cube
-------------


change your start and end frames to 1 and 150.


.. figure:: /images/Manual-25-softbody-examples-timeline.jpg
   :width: 600px
   :figwidth: 600px

   The timeline


add a plane, and scale it 5 times. next go to the physics tab, and add a collision.
the default settings are fine for this example.

now add a cube, or use the default cube. Tab into edit mode and subdivide it thrice.
then add a bevel modifier to it, to smoothen the edges. to add a little more, press r twice,
and move your cursor a bit.

when finisht, your scene should look like this:


.. figure:: /images/Manual-25-softbody-examples-scene-ready.jpg
   :width: 400px
   :figwidth: 400px

   The scene, ready for softbody physics


Everything is ready to add the softbody physics. go to the physics tab and add 'softbody'.
uncheck the soft body goal , and check softbody self collision. under soft body edges,
increase the bending to 10.

playing tha animation with alt a will now give a slow animation of a bouncing cube.
to speed things up, we need to bake the softbody physics.

Under Soft Body Cache change start and end to your start and end frames.
in this case 1 and 150.
to test if everything is working, you can take a cache step of 5 or 10,
but for the final animation it's better to reduce it to 1, to cache everything.

when finisht, your physics panel should look like this:


.. figure:: /images/Manual-25-softbody-examples-physics-settings.jpg
   :width: 500px
   :figwidth: 500px

   The physics settings.


you can now bake the simulation, give the cube materials and textures and render the animation.


result
------


the rendered bouncing cube:


+--------------------------------------------------------+
+FIXME(Tag Unsupported:youtube;                          +
+<youtube width="640" height="360" >3PzgB9jw9iA</youtube>+
+)                                                       +
+--------------------------------------------------------+
