
Layers
======

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object` mode
   | Panel:    :guilabel:`Relations` (\ :guilabel:`Object` context)
   | Menu:     :menuselection:`Object --> Move to Layer...`
   | Hotkey:   :kbd:`M`


3D scenes often become exponentially more confusing as they grow more complex.
Sometimes the artist also needs precise control over how individual objects are lit,
and does not want lights for one object to affect nearby objects.
For this and other reasons below, objects can be placed into one or more "layers".
Using object layers, you can:

- Selectively display objects from certain layers in your 3D view, by selecting those layers in the :guilabel:`3D View` header bar. This allows you to speed up interface redrawing, reduce virtual-world clutter, and help improve your workflow.
- Control :doc:`which lights illuminate an object <lighting/lights/what_light_affects>`\ , by making a light illuminate only the objects on its own layer(s).
- Control which forces affect which :doc:`particle systems <physics/particles>`\ , since particles are only affected by forces and effects on the same layer.
- Control which layers are rendered (and hence, which objects), and which properties/channels are made available for compositing by using :doc:`render layers <render/post_process/layers>`\ .

Armatures can also become very complex, with different types of bones, controllers, solvers,
custom shapes, and so on. Since armatures are usually located close together,
this can quickly become cluttered. Therefore, Blender also provides layers just for armatures.
Armature layers are very similar to object layers, in that you can divide up an armature (rig)
across layers and only display those layers you wish to work on.

:doc:`Read more about armature layers » <rigging/armatures/visualization#armature_layers>`


Working with Layers
===================

3D layers differ from the layers you may know from 2D graphics applications as they have no
influence on the drawing order and are there (except for the special functions listed above)
mainly to allow you to organize your scene.

When rendering, Blender only renders the selected layers.
If all your lights are on a layer that is *not selected*\ ,
you won't see anything in your render except for objects lit by ambient lighting.

:doc:`Groups and Parenting <modeling/objects/groups_and_parenting>` are other ways to logically group related sets of objects. Please refer to the relevant sections for more information.


Viewing layers
--------------

Blender provides twenty layers whose visibility can be toggled with the small unlabeled
buttons in the header (see *3D Viewport layer buttons*\ ). To select a single layer,
click the appropriate button with :kbd:`lmb`\ ; to select more than one,
use :kbd:`shift-lmb` - doing this on an already active layer will deselect it.


.. figure:: /images/Manual-3Dinteraction-Navigating-Layers-layer-buttons.jpg
   :width: 600px
   :figwidth: 600px

   3D Viewport layer buttons.


To select layers via the keyboard, press :kbd:`1` to :kbd:`0`
(on the main area of the keyboard) for layers 1 through 10 (the top row of buttons),
and :kbd:`alt-1` to :kbd:`alt-0` for layers 11 through 20 (the bottom row).
The :kbd:`shift` key for multiple (de)selection works for these shortcuts too.

You can select or deselect all Scene Layer buttons at once by pressing the :kbd:`\`` key.


Locking to the scene
--------------------

By default, the lock button directly to the right of the layer buttons is enabled. This means that changes to the viewed layers affect all other 3D Views locked to the scene - see the :doc:`navigating the 3D view options page <3d_interaction/navigating>` for more information.


Multiple Layers
---------------

An object can exist on multiple layers. For example,
a lamp that only lights objects on a shared layer could "be" on layers 1, 2, and 3.
An object on layers 3 and 4 would be lit, whereas an object on layers 4 and 5 would not.
There are many places where layer-specific effects come into play,
especially lights and particles.


Moving objects between layers
-----------------------------

.. figure:: /images/Manual-3Dinteraction-Navigating-Layers-layer-selection.jpg

   Layer selection.


To move selected objects to a different layer,
press :kbd:`M` and then select the layer you want from the pop-up dialog.
Objects can also be on more than one layer at a time. To have an object on multiple layers,
hold :kbd:`shift` while clicking.


.. figure:: /images/Manual-3Dinteraction-Navigating-Layers-object-context.jpg

   Object context selection.


Another way to view or change a selected object layer is via the :guilabel:`Relations` panel,
in the :guilabel:`Object` context.


.. figure:: /images/Manual-3Dinteraction-Navigating-Layers-relations.jpg

   Layers in Object context, Relations panel.


You will then see the layer buttons in the :guilabel:`Relations` panel - as before the object
can be displayed on more than one layer by clicking :kbd:`shift-lmb`\ .


Example of object layer arrangement
-----------------------------------

As a suggestion, use the top row of layers for important parts of your scene,
and the bottom row for those you don't use or change often
(or for alternatives for the top row). In a staged set involving mainly two actors,
you might have the following objects on your layers:

- Lead Actors.
- Supporting Actors.
- Supporting Crew (background actors).
- Particles and effects (vortex, wind).
- Main Stage.
- Main backdrops and panels.
- Main props (tables, chairs).
- Little props, fillers, decorations, trappings.
- Cameras, Lights.
- Lead Actors' armatures.
- Supporting Actors' armatures.
- Crew armatures.
- Alternative clothing.
- Mesh WIP.
- Different stage setup, dimensions.
- Different backdrops that could be used.
- Other big props that might clog up the scene.
- Props WIP.
- Additional lighting.


