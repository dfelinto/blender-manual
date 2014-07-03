

..    TODO/Review: {{review|copy=X|text=Partially}} .


Cloth Simulation
================


+--------------------------------------+-------------------------------------------------+--------------------------------------+
+.. figure:: /images/Cloth-example1.jpg|.. figure:: /images/Cloth-oncarvedwood.jpg       |.. figure:: /images/Cloth-example2.jpg+
+   :width: 150px                      |   :width: 150px                                 |   :width: 150px                      +
+   :figwidth: 150px                   |   :figwidth: 150px                              |   :figwidth: 150px                   +
+                                      |                                                 |                                      +
+   Cloth example.                     |   Cloth on carved wooden men (made by motorsep).|   Cloth example.                     +
+--------------------------------------+-------------------------------------------------+--------------------------------------+


Cloth simulation is one of the hardest aspects of CG,
because it is a deceptively simple real-world item that is taken for granted,
yet actually has very complex internal and environmental interactions.
After years of development,
Blender has a very robust cloth simulator that is used to make clothing, flags, banners,
and so on. Cloth interacts with and is affected by other moving objects,
the wind and other forces, as well as a general aerodynamic model,
all of which is under your control.


Description
-----------


A piece of cloth is any mesh, open or enclosed, that has been designated as cloth. The
:guilabel:`Cloth` panels are located in the :guilabel:`Physics` sub-context and consist of
three panels of options. Cloth is either an open or closed mesh and is mass-less,
in that all cloth is assumed to have the same density, or mass per square unit.

Cloth is commonly modeled as a mesh grid primitive, or a cube, but can also be, for example, a teddy bear. However, Blender's :doc:`Softbody system <physics/soft_body>` provides better simulation of closed meshes; Cloth is a specialized simulation of fabrics.

Once the object is designated as Cloth, a Cloth :doc:`modifier <modifiers>` will be added to the object's modifier stack automatically. As a :doc:`modifier <modifiers>` then, it can interact with other modifiers, such as :guilabel:`Armature` and :guilabel:`Smooth`\ . In these cases, the ultimate shape of the mesh is computed in accordance with the order of the modifier stack. For example, you should smooth the cloth *after* the modifier computes the shape of the cloth.

So you edit the Cloth settings in two places: use the F7 Physics buttons to edit the
properties of the cloth and use the Modifier stack to  edit the Modifier properties related to
display and interaction with other modifiers.

You can :guilabel:`Apply` the cloth modifier to freeze, or lock in,
the shape of the mesh at that frame, which removes the modifier. For example,
you can drape a flat cloth over a table, let the simulation run, and then apply the modifier.
In this sense, you are using the simulator to save yourself a lot of modeling time.

Results of the simulation are saved in a cache, so that the shape of the mesh,
once calculated for a frame in an animation, does not have to be recomputed again.
If changes to the simulation are made,
you have full control over clearing the cache and re-running the simulation. Running the
simulation for the first time is fully automatic and no baking or separate step interrupts the
workflow.

Computation of the shape of the cloth at every frame is automatic and done in the background;
thus you can continue working while the simulation is computed. However it is CPU-intensive
and depending on the power of your PC and the complexity of the simulation,
the amount of CPU needed to compute the mesh varies, as does the lag you might notice.


 .. admonition:: Don't jump ahead
   :class: note

   If you set up a cloth simulation but Blender has not computed the shapes for the duration of the simulation, and if you jump ahead a lot of frames forward in your animation, the cloth simulator may not be able to compute or show you an accurate mesh shape for that frame, if it has not previously computed the shape for the previous frame(s).


Workflow
--------

A general process for working with cloth is to:

- Model the cloth object as a general starting shape.
- Designate the object as a "cloth" in the :guilabel:`Physics` tab of the :guilabel:`Properties` window.
- Model other deflection objects that will interact with the cloth. Ensure the Deflection modifier is last on the modifier stack, after any other mesh deforming modifiers.
- Light the cloth and assign materials and textures, UV-unwrapping if desired.
- If desired, give the object particles, such as steam coming off the surface.
- Run the simulation and adjust Options to obtain satisfactory results. The timeline window's VCR controls are great for this step.
- Optionally age the mesh to some point in the simulation to obtain a new default starting shape.
- Make minor edits to the mesh on a frame-by-frame basis to correct minor tears.


Creating Cloth Simulations
==========================

This section discusses how to use those options to get the effect you want.
First, enable :guilabel:`Cloth`\ . Set up for the kind of cloth you are simulating.
You can choose one of the presets to have a starting point.

As you can see, the heavier the fabric,
the more stiff it is and the less it stretches and is affected by air.


Cloth Panel
===========

:guilabel:`Presets`
   Contains a number of preset cloth examples, and allows you to add your own.

:guilabel:`Quality`
   Set the number of simulation steps per frame. Higher values result in better quality, but is slower.


Material
--------

:guilabel:`Mass`
   The mass of the cloth material.
:guilabel:`Structural`
   Overall stiffness of the cloth.
:guilabel:`Bending`
   Wrinkle coefficient. Higher creates more large folds.


Damping
-------

:guilabel:`Spring`
   Damping of cloth velocity. Higher = more smooth, less jiggling.
:guilabel:`Air`
   Air normally has some thickness which slows falling things down.


Pinning
-------


.. figure:: /images/Clothscreeny2.jpg
   :width: 200px
   :figwidth: 200px

   Cloth in action.


The first thing you need when pinning cloth is a :doc:`Vertex Group <modeling/meshes/vertex_groups>`\ . There are several ways of doing this including using the Weight Paint tool to paint the areas you want to pin (see the :doc:`Weight paint <modeling/meshes/weight_paint>` section of the manual).

Once you have a vertex group set, things are pretty straightforward; all you have to do is
press the :guilabel:`Pinning of cloth` button in the :guilabel:`Cloth` panel and select which
vertex group you want to use, and the stiffness you want it at.

:guilabel:`Stiffness`
   Target position stiffness. You can leave the stiffness as it is; the default value of 1 is fine.


..    Comment: <!--
   Note that if you move the cloth object ''after'' you have already run some simulations,
   you must unprotect and clear the cache; otherwise, Blender will use the position of the
   current/cached mesh's vertices when trying to represent where they are.
   Editing the shape of the mesh, after simulation, is also discussed below.
   You may disable the cloth and edit the mesh as a normal mesh editing process.
   This is jumping ahead and not clear and not true at this point.
   --[[User:Roger|Roger]] 18:42, 27 April 2008 (UTC)

   Finally, use the {{Literal|Timeline}} window Play button,
   or press {{Shortcut|alt|A}} in the 3D View to run the simulation.
   Your cloth will fall and interact with Deflection objects as it would in the real world.
   <!--this is jumping ahead and not clear and not true at this point.
   --[[User:Roger|Roger]] 18:42, 27 April 2008 (UTC)
   --> .


Collisions
==========

In most cases, a piece of cloth does not just hang there in 3D space,
it collides with other objects in the environment. To ensure proper simulation,
there are several items that have to be set up and working together:

- The :guilabel:`Cloth` object must be told to participate in :guilabel:`Collision`\ s.
- Optionally (but recommended) tell the cloth to collide with itself.
- Other objects must be visible to the :guilabel:`Cloth` object *via* shared layers.
- The other objects must be mesh objects.
- The other objects may move or be themselves deformed by other objects (like an armature or shape key).
- The other mesh objects must be told to deflect the cloth object.
- The blend file must be saved in a directory so that simulation results can be saved.
- You then :guilabel:`Bake` the simulation. The simulator computes the shape of the cloth for a frame range.
- You can then edit the simulation results, or make adjustments to the cloth mesh, at specific frames.
- You can make adjustments to the environment or deforming objects, and then re-run the cloth simulation from the current frame forward.


Collision Settings
------------------


.. figure:: /images/Cloth_collisionpanel.jpg
   :width: 200px
   :figwidth: 200px

   Cloth Collisions panel.


Now you must tell the :guilabel:`Cloth` object that you want it to participate in collisions.
For the cloth object, locate the :guilabel:`Cloth Collision` panel, shown to the right:
:guilabel:`Enable Collisions`
   :kbd:`Lmb` click this to tell the cloth object that it needs to move out of the way.

:guilabel:`Quality`
   A general setting for how fine and good a simulation you wish. Higher numbers take more time but ensure less tears and penetrations through the cloth.
:guilabel:`Distance`
   As another object gets this close to it (in Blender Units), the simulation will start to push the cloth out of the way.
:guilabel:`Repel`
   Repulsion force to apply when cloth is close to colliding.
:guilabel:`Repel Distance`
Maximum distance to apply repulsion force. Must be greater than minimum distance.
:guilabel:`Friction`
   A coefficient for how slippery the cloth is when it collides with the mesh object. For example, silk has a lower coefficient of friction than cotton.


Self-collisions
~~~~~~~~~~~~~~~

Real cloth cannot permeate itself, so you normally want the cloth to self-collide.

:guilabel:`Enable Self Collisions`
   Click this to tell the cloth object that it should not penetrate itself. This adds to simulation compute time, but provides more realistic results. A flag, viewed from a distance does not need this enabled, but a close-up of a cape or blouse on a character should have this enabled.

:guilabel:`Quality`
   For higher self-collision quality just increase the :guilabel:`Quality` and more self collision layers can be solved. Just keep in mind that you need to have at least the same :guilabel:`Collision Quality` value as the :guilabel:`Quality` value.

:guilabel:`Distance`
   If you encounter problems, you could also change the :guilabel:`Min Distance` value for the self-collisions. The best value is 0.75; for fast things you better take 1.0. The value 0.5 is quite risky (most likely many penetrations) but also gives some speedup.

Regression blend file: `Cloth selfcollisions <http://wiki.blender.org/index.php/Media:Cloth-regression-selfcollisions.blend>`__\ .


Shared Layers
-------------

Suppose you have two objects: a pair of Pants on layers 2 and 3,
and your Character mesh on layers 1 and 2.
You have enabled the Pants as cloth as described above.
You must now make the Character "visible" to the Cloth object,
so that as your character bends its leg, it will push the cloth.
This principle is the same for all simulations;
simulations only interact with objects on a shared layer. In this example,
both objects share layer 2.

To view/change an object's layers,
:kbd:`Rmb` click to select the object in :guilabel:`Object` mode in the 3D view.
:kbd:`M` to bring up the "Move Layers" popup,
which shows you all the layers that the object is on. To put the object on a single layer,
:kbd:`Lmb` click the layer button. To put the object on multiple layers,
:kbd:`shift-Lmb` the layer buttons. To remove an object from a selected layer,
simply :kbd:`shift-Lmb` the layer button again to toggle it.


Mesh Objects Collide
--------------------

If your colliding object is not a mesh object, such as a NURBS surface, or text object,
you must convert it to a mesh object. To do so, select the object in object mode,
and in the 3D View header, select :guilabel:`Object` → :guilabel:`Convert Object Type`
(\ :kbd:`alt-C`\ ), and select :guilabel:`Mesh` from the popup menu.


Cloth - Object collisions
-------------------------


.. figure:: /images/Manual-Panel-Collision.jpg
   :width: 200px
   :figwidth: 200px

   Collision settings.


The cloth object needs to be deflected by some other object. To deflect a cloth,
the object must be enabled as an object that collides with the cloth object.
To enable Cloth - Object collisions, you have to enable deflections on the collision object
(not on the cloth object).

In the :guilabel:`Buttons` window, :guilabel:`Object` context,
:guilabel:`Physics` sub-context, locate the :guilabel:`Collision` panel shown to the right. It
is also important to note that this collision panel is used to tell all simulations that this
object is to participate in colliding/deflecting other objects on a shared layer (particles,
soft bodies, and cloth).


 .. admonition:: Beware
   :class: note

   There are three different :guilabel:`Collision` panels, all found in the :guilabel:`Physics` sub-context. The first (by default), a tab beside the :guilabel:`Fields` panel, is the one needed here. The second panel, a tab in the :guilabel:`Soft Body` group, concern softbodies (and so has nothing to do with cloth). And we have already seen the last one, by default a tab beside the :guilabel:`Cloth` panel.


Mesh Object Modifier Stack
--------------------------


.. figure:: /images/Manual-Simulation-Cloth-ColliderStack.jpg
   :width: 200px
   :figwidth: 200px

   Collision stack.


The object's shape deforms the cloth,
so the cloth simulation must know the "true" shape of that mesh object at that frame.
This true shape is the basis shape as modified by shape keys or armatures. Therefore,
the :guilabel:`Collision` modifier must be **after** any of those.
The image to the right shows the :guilabel:`Modifiers` panel for the Character mesh object
(not the cloth object).


Cloth Cache
===========

Cache settings for cloth are the same as with other dynamic systems. See :doc:`Particle Cache <physics/particles/cache_and_bake>` for details.


Bake Collision
--------------


.. figure:: /images/Manual-Simulation-Cloth-CollisionBake.jpg
   :width: 200px
   :figwidth: 200px

   After Baking.


After you have set up the deflection mesh for the frame range you intend to run the simulation
(including animating that mesh *via* armatures),
you can now tell the cloth simulation to compute (and avoid) collisions.
Select the cloth object and in the :guilabel:`Object` context,
:guilabel:`Physics` sub-context, set the :guilabel:`Start` and :guilabel:`End` settings for
the simulation frames you wish to compute, and click the :guilabel:`Bake` button.

You cannot change :guilabel:`Start` or :guilabel:`End` without clearing the bake simulation.
When the simulation has finished, you will notice you have the option to free the bake,
edit the bake and re-bake:

There's a few things you'll probably notice right away. First,
it will bake significantly slower than before,
and it will probably clip through the box pretty badly as in the picture on the right.


Editing the cached simulation=
------------------------------

The cache contains the shape of the mesh at each frame. You can edit the cached simulation,
after you've baked the simulation and pressed the :guilabel:`Bake Editing` button.
Just go to the frame you want to fix and :kbd:`Tab` into :guilabel:`Edit mode`\ .
There you can move your vertices using all of Blender's mesh shaping tools. When you exit,
the shape of the mesh will be recorded for that frame of the animation.
If you want Blender to resume the simulation using the new shape going forward,
:kbd:`Lmb` click '\ :guilabel:`Rebake from next Frame` and play the animation.
Blender will then pick up with that shape and resume the simulation.

Edit the mesh to correct minor tears and places where the colliding object has punctured the
cloth.

If you add, delete, extrude, or remove vertices in the mesh, Blender will take the new mesh as
the starting shape of the mesh back to the *first frame* of the animation,
replacing the original shape you started with,
up to the frame you were on when you edited the mesh. Therefore,
if you change the content of a mesh, when you :kbd:`Tab` out of :guilabel:`Edit mode`\ ,
you should unprotect and clear the cache ..    Comment: <!--''From next frame'' ???--> . so that Blender will
make a consistent simulation.


Troubleshooting
===============

If you encounter some problems with collision detection, there are two ways to fix them:


- The fastest solution is to increase the :guilabel:`Min Distance` setting under the :guilabel:`Cloth Collision` panel. This will be the fastest way to fix the clipping; however, it will be less accurate and won't look as good. Using this method tends to make it look like the cloth is resting on air, and gives it a very rounded look.


- A second method is to increase the :guilabel:`Quality` (in the first :guilabel:`Cloth` panel). This results in smaller steps for the simulator and therefore to a higher probability that fast-moving collisions get caught. You can also increase the :guilabel:`Collision Quality` to perform more iterations to get collisions solved.


- If none of the methods help, you can easily edit the cached/baked result in :guilabel:`Edit mode` afterwards.


- My Cloth is torn by the deforming mesh - he "Hulks Out": Increase its structural stiffness (\ :guilabel:`StructStiff` setting, :guilabel:`Cloth` panel), very high, like 1000.


 .. admonition:: :guilabel:`Subsurf` modifier
   :class: note

   A bake/cache is done for every subsurf level so please use **the equal** subsurf level for render and preview.


Examples
========

To start with cloth, the first thing you need, of course, is some fabric. So,
let's delete the default cube and add a plane. I scaled mine up along the Y axis,
but you don't have to do this. In order to get some good floppy and flexible fabric,
you'll need to subdivide it several times. I did it 8 times for this example.
So :kbd:`Tab` into :guilabel:`Edit mode`\ ,
and press :kbd:`W` → :guilabel:`Subdivide multi`\ , and set it to 8.

Now, we'll make this cloth by going to the :guilabel:`Object` context
(\ :kbd:`f7`\ ) → :guilabel:`Physics` sub-context.
Scroll down until you see the :guilabel:`Cloth` panel, and press the :guilabel:`Cloth` button.
Now, a lot of settings will appear, most of which we'll ignore for now.

That's all you need to do to set your cloth up for animating,
but if you hit :kbd:`alt-A`\ , your lovely fabric will just drop very un-spectacularly.
That's what we'll cover in the next two sections about pinning and colliding.


Using Simulation to Shape/Sculpt a Mesh
---------------------------------------

You can :guilabel:`Apply` the :guilabel:`Cloth` modifier at any point to freeze the mesh in
position at that frame. You can then re-enable the cloth,
setting the start and end frames from which to run the simulation forward.

Another example of aging is a flag.
Define the flag as a simple grid shape and pin the edge against the flagpole.
Simulate for 50 frames or so, and the flag will drop to its "rest" position.
Apply the :guilabel:`Cloth` modifier.
If you want the flag to flap or otherwise move in the scene,
re-enable it for the frame range when it is in camera view.


Smoothing of Cloth
------------------

Now, if you followed this from the previous section,
your cloth is probably looking a little blocky. In order to make it look nice and smooth like
the picture you need to apply a :guilabel:`Smooth` and/or :guilabel:`Subsurf` modifier in the
:guilabel:`Modifiers` panel under the :guilabel:`Editing` context (\ :kbd:`f9`\ ). Then,
in the same context, find the :guilabel:`Links and Materials` panel
(the same one you used for vertex groups) and press :guilabel:`Set Smooth`\ .

Now, if you hit :kbd:`alt-A`\ , things are starting to look pretty nice, don't you think?


Cloth on armature
-----------------

Cloth deformed by armature and also respecting an additional collision object: `Regression blend file <http://wiki.blender.org/index.php/Media:Cloth-regression-armature.blend>`__\ .


Cloth with animated vertex groups
---------------------------------

Cloth with animated pinned vertices: `Regression blend file <http://wiki.blender.org/index.php/Media:Cloth_anim_vertex.blend>`__\ . UNSUPPORTED: Starting with a goal of 0 and increasing it, but still having the vertex not pinned will not work (e.g. from goal = 0 to goal = 0.5).


Cloth with Dynamic Paint
------------------------

Cloth with Dynamic Paint using animated vertex groups: `Regression blend file <http://wiki.blender.org/index.php/Media:Cloth_dynamic_paint.blend>`__\ . UNSUPPORTED: Starting with a goal of 0 and increasing it, but still having the vertex not pinned will not work (e.g. from goal = 0 to goal = 0.5) because the necessary "goal springs" cannot be generated on the fly.


Using Cloth for Softbodies
--------------------------


.. figure:: /images/Cloth-Sb1.jpg
   :width: 200px
   :figwidth: 200px

   Using cloth for softbodies.


Cloth can also be used to simulate softbodies.
It's for sure not its main purpose but it works nonetheless.
The example image uses standard :guilabel:`Rubber` material, no fancy settings,
just :kbd:`alt-A`\ .

Blend file for the example image: `Using Cloth for softbodies <http://wiki.blender.org/index.php/Media:Cloth-sb1.blend>`__\ .


Cloth with Wind
---------------


.. figure:: /images/Cloth-flag2.jpg
   :width: 200px
   :figwidth: 200px

   Flag with wind applied.


Regression blend file for Cloth with wind and self collisions (also the blend for the image above): `Cloth flag with wind and selfcollisions <http://wiki.blender.org/index.php/Media:Cloth-flag2.blend>`__\ .


