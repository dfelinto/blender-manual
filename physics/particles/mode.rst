
Particle Mode
=============

Using :guilabel:`Particle Mode` you can edit the key-points (key-frames) and paths of :guilabel:`Baked` :doc:`Hair <physics/particles/hair>`\ , :doc:`Particle <physics/particles>`\ , :doc:`Cloth <physics/cloth>`\ , and :doc:`Soft Body <physics/soft_body>` simulations. (You can also edit and style hair before baking).

Since working in particle mode is pretty easy and very similar to working with vertices in the
3D window, we will show how to set up a particle system and then give a reference of the
various functions.


Ways to use Particle Mode
-------------------------


.. admonition:: Only Frames Baked to Memory are Editable!
   :class: nicetip

   If you cannot edit the particles, check that you are not baking to a :doc:`Disk Cache <physics/particles/cache_and_bake>`\ .


**Setup for Hair Particles**

- Create a :guilabel:`Hair` particle system - With your object selected, click the :guilabel:`Particle System` icon in the Properties panel.  Create a new particle system by clicking the :guilabel:`Plus`\ .
- Give it an initial velocity in the :guilabel:`Normal` direction (first check the :guilabel:`Advanced` box, then modify the :guilabel:`Velocity` sub-panel), or adjust the :guilabel:`Hair Length`\ .
- Create a simulation - Place the camera at a good position (\ :menuselection:`popup --> View --> Cameras --> Active Camera` ... or

FIXME(Template Unsupported: Shortcut/Keypress;
{{Shortcut/Keypress|pad0}}
)). Check the :guilabel:`Hair Dynamics` box.  Select :menuselection:`popup --> Render --> Render OpenGL Animation` in :guilabel:`Render Engine` mode.


.. figure:: /images/Blender2.6_particle_mode.jpg
   :width: 120px
   :figwidth: 120px

   Editing hair strands in Particle Mode


.. figure:: /images/Animated_editing_particles_in_particle_mode.gif

   Editing a baked particle simulation's particle paths in Particle Mode


**Setup for Particle, Cloth, and Soft Body Simulations**

- Use :guilabel:`Emitter` particles, or a cloth/soft-body simulation
- Create a simulation - set up objects and or emitters, set your time range (use a small range if you are just starting out and experimenting), set up the simulation how you want it, using :kbd:`Alt+A` to preview it.

 **Bake the Simulation**

- Once you are happy with the general simulation, :doc:`bake <physics/particles/cache_and_bake>` the simulation from object mode. The simulation must be baked to enable editing. (remember to bake to memory, a disk cache will not be editable in :guilabel:`Particle Mode`\ )

**Edit the Simulation**

- Switch to :guilabel:`Particle Edit` from the :guilabel:`Mode dropdown menu` in the bottom menu bar of the :guilabel:`3D View` to edit the particle's paths/key-frames.  You may need to press :kbd:`t` from within the 3D viewport to see the :guilabel:`Particle Edit` panel. Move to the frame you want to edit and use the various :guilabel:`Particle Edit` tools to edit your simulation. Work slowly, previewing your changes with :kbd:`Alt+A`\ , and save often so that you can go back to the previous version should something happen, or that you do not like the latest changes you have made.

To be able to clearly see what you are working on:

- Turn on the :guilabel:`Particle Edit Properties` (\ *PEP*\ ) panel with :kbd:`N`\ .
- Select :guilabel:`Point select mode`

.. figure:: /images/Icon-library_3D-Window_PointSelectMode.jpg


 in the header of the 3D window. This will display key points along the particle path.


.. admonition:: Brush Size
   :class: nicetip

   Press :kbd:`F` to resize the brush while working


Using Particle Mode
===================


Selecting Points
----------------


- Single: :kbd:`Rmb`\ .
- All: :kbd:`A`\ .
- Linked: Move the mouse over a keypoint and press :kbd:`L`\ .
- Border select: :kbd:`B`\ .
- First/last: :kbd:`W` → :guilabel:`Select First`\ /\ :guilabel:`Select Last`\ .

You may also use the :guilabel:`Select` Menu.


.. admonition:: Selections
   :class: nicetip

   Selections are extremely useful for modifying only the particles that you want. Hover over a particle path and press :kbd:`L` to link-select it, hover over the next and press :kbd:`L` to add that path to the selection. To remove a path, hold shift and press :kbd:`L`\ . To Deselect all press :kbd:`A`\ .

   The method to select individual points is the same as in edit mode. click to select,
   shift+click to add/remove a point from the selection


.. admonition:: Beware of Undo!
   :class: nicetip

   Using :guilabel:`Undo` in :guilabel:`Particle Mode` can have strange results. Remember to save often!


Moving keypoints or particles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


- To move selected keypoints press :kbd:`G`\ , or use one of the various other methods to grab vertices.
- To move a particle root you have to turn off :guilabel:`Keep` :guilabel:`Root` in the :guilabel:`Tool Bar`\ .
- You can do many of the things like with vertices, including scaling, rotating and removing (complete particles or single keys).
- You may not duplicate or extrude keys or particles, but you can subdivide particles which adds new keypoints (\ :kbd:`W` → :guilabel:`Subdivide`\ /\ :kbd:`pad2`\ ).
- Alternatively you can rekey a particle (\ :kbd:`W` → :guilabel:`Rekey`\ /\ :kbd:`pad1`\ ) and choose the number of keys.

How smoothly the hair and particle paths are displayed depends on the :guilabel:`Path Steps`
setting in the :guilabel:`Tool Bar`\ . Low settings produce blocky interpolation between points,
while high settings produce a smooth curve.


Mirroring particles
~~~~~~~~~~~~~~~~~~~


- If you want to create an X-Axis symmetrical haircut you have to do following steps:
  - Select all particles with :kbd:`A`\ .
  - Mirror the particles with :kbd:`ctrl-M`\ , or use the :guilabel:`Particle` → :guilabel:`Mirror` menu.
  - Turn on :guilabel:`X-Axis Mirror Editing` in the :guilabel:`Particle` menu.

It may happen that after mirroring two particles occupy nearly the same place.
Since this would be a waste of memory and rendertime,
you can :guilabel:`Remove doubles` either from the :guilabel:`Specials` (\ :kbd:`W`\ )
or the :guilabel:`Particle` menu.


Hiding/Unhiding
~~~~~~~~~~~~~~~

Hiding and unhiding of particles works similar as with vertices in the 3D window.
Select one or more keypoints of the particle you want to hide and press :kbd:`H`\ .
The particle in fact doesn't vanish, only the key points.

Hidden particles (i.e. particles whose keypoints are hidden)
don't react on the various brushes. But:

If you use :guilabel:`Mirror Editing` even particles with hidden keypoints may be moved,
if their mirrored counterpart is moved.

To un-hide all hidden particles press Alt+H.


Select Modes
~~~~~~~~~~~~


.. figure:: /images/Icon-library_3D-Window_ParticleSelectAndDisplayMode.jpg
   :width: 640px
   :figwidth: 640px


:guilabel:`Path`
    No keypoints are visible, you can select/deselect only all particles.
:guilabel:`Point`
    You see all of the keypoints.
:guilabel:`Tip`
    You can see and edit (including the brushes) only the tip of the particles, i.e. the last keypoint.


Brush
~~~~~

With the buttons you can select the type of "Comb" utility you want to use.
Below the brush types, their settings appear:

Common Options:
   :guilabel:`Radius`
      Set the radius if the brush.
   :guilabel:`Strength`
      Set the strength of the brush effect (not for Add brush).
   :guilabel:`Add/Sub Grow/Shrink`
      Sets the brush to add the effect or reverse it..

:guilabel:`None`
    No special tool, just edit the keypoints as "normal" vertices.
:guilabel:`Comb`
    Moves the keypoints (similar to "proportional editing").
:guilabel:`Smooth`
    Parallels visually adjacent segments.
:guilabel:`Add`
    Adds new particles.
   :guilabel:`Count`
      The number of new particles per step.
   :guilabel:`Interpolate`
      Interpolate the shape of new hairs from existing ones.
   :guilabel:`Steps`
      Amount of brush steps
   :guilabel:`Keys`
      How many keys to make new particles with.
:guilabel:`Length`
    Scales the segments, so it makes the hair longer(\ :guilabel:`Grow`\ ) or shorter(\ :guilabel:`Shrink`\ ).
:guilabel:`Puff`
   Rotates the hair around it's first keypoint (root). So it makes the hair stand up (\ :guilabel:`Add`\ ) or lay down (\ :guilabel:`Sub`\ ).
   :guilabel:`Puff Volume`
      Apply puff to unselected end-points, (helps maintain hair volume when puffing root)
:guilabel:`Cut`
    Scales the segments until the last keypoint reaches the brush.

:guilabel:`Weight`
    This is especially useful for softbody animations, because the weight defines the softbody :guilabel:`Goal`\ . A keypoint with a weight of 1 won't move at all, a keypoint with a weight of 0 subjects fully to softbody animation. This value is scaled by the :guilabel:`GMin`\ -\ :guilabel:`GMax` range of softbody goals...    Comment: <!-- Not more true, I think: '''Weight is only drawn for the complete hair (i.e. with the value of the tip), not for each keypoint, so it's a bit difficult to paint'''.--> .


Options
~~~~~~~

:guilabel:`Deflect Emitter`\ ,\ :guilabel:`Dist`
    Don't move keypoints through the emitting mesh. :guilabel:`Dist` is the distance to keep from the Emitter.
:guilabel:`Keep`
   :guilabel:`Length`
       Keep the length of the segments between the keypoints when combing or smoothing the hair. This is done by moving all the other keypoints.
   :guilabel:`Root`
       Keep first key unmodified, so you can't transplant hair.
:guilabel:`X Mirror`
   Enable mirror editing across the local x axis.

:guilabel:`Draw`
   :guilabel:`Path Steps`
       Drawing steps, sets the smoothness of the drawn path.
   :guilabel:`Show Children`
    Draws the children of the particles too. This allows to fine tune the particles and see their effects on the result, but it may slow down your system if you have many children.


