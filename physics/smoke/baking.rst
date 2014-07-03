..    TODO/Review: {{review}} .

Baking Smoke Simulations
========================


If you want to render an animation, you need to bake your smoke first.
Baking is simply calculating a simulation. To bake the smoke, the file must be saved.
The calculations are stored in a cache file which can be named. On occasion,
Baking may crash Blender. [See troubleshooting]

By scrubbing through the timeline or running the animation in the viewport via
:kbd:`alt-A` you already did some realtime-baking to the memory.
But for rendering the animation, the baked data must be on disk. And before you can bake,
you need to save your Blendfile.

Next select the domain cube and go to the physics tab where you open the Smoke Cache section.
Give your cache a file name by entering it into the text box and hitting :kbd:`enter`\ .
By hitting Bake your simulation data is computed and stored to disk. Notice that the
scrubbing-bug in the timeline is gone now? At this point you should be able to render the
animation.


+-----------------------------------------------+----------------------------------------+----------------------------------+
+.. figure:: /images/Smoke_cache.jpg            |.. figure:: /images/Smoke_cache_name.jpg|.. figure:: /images/Smoke_bake.jpg+
+   :width: 200px                               |   :width: 200px                        |   :width: 200px                  +
+   :figwidth: 200px                            |   :figwidth: 200px                     |   :figwidth: 200px               +
+                                               |                                        |                                  +
+   Go to the cache section of your smoke domain|   The files on disk need a name        |   Finally we're ready to bake    +
+-----------------------------------------------+----------------------------------------+----------------------------------+


