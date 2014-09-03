..    TODO/Review: {{review|text=todo: review the viscosity table commented text}} .


Fluid Domain
************

The Domain Object
=================

The bounding box of the object serves as the boundary of the simulation.
**All fluid objects must be in the domain.** Fluid objects outside the domain will not bake.
No tiny droplets can move outside this domain;
it's as if the fluid is contained within the 3D space by invisible force fields.
There can be only a single fluid simulation domain object in the scene.

**The shape of the object does not matter because it will** *always* **be treated like a box**
(The lengths of the bounding box sides can be different).
So, usually there won't be any reason to use another shape than a box.
If you need obstacles or other boundaries than a box to interfere with the fluid flow,
you need to insert additional obstacle objects *inside* the domain boundary.

This object will be *replaced* by the fluid during the simulation.


.. tip:: Baking is done on the Domain object

   When you calculate the fluid simulation, **you bake the simulation on the domain object**.
   For this reason all the baking options are visible only when selecting the Domain Object.

   For baking options, please refer to
   FIXME(TODO: Internal Link;
   [[#Baking|the baking section]]
   ) in this page.


Options
-------

.. figure:: /images/Fluid_domainpanel.jpg

   The fluid simulation options with Domain selected


Bake button
   For baking options please refer to FIXME(TODO: Internal Link; [[#Baking|the baking section]]) in this page.

Resolution

   Render resolution
      The granularity at which the actual fluid simulation is performed.
      This is probably the most important setting for the simulation as it
      determines the amount of details in the fluid, the memory and disk usage as well as computational time.


+------------------------------------------+-------------------------------------------+
+.. figure:: /images/Manual-Fluid-70res.jpg|.. figure:: /images/Manual-Fluid-200res.jpg+
+   :width: 270px                          |   :width: 270px                           +
+   :figwidth: 270px                       |   :figwidth: 270px                        +
+                                          |                                           +
+   10cm mug at Resolution 70.             |   10cm mug at Resolution 200.             +
+------------------------------------------+-------------------------------------------+


      Note that the amount of required memory quickly increases: a resolution of 32 requires ca. 4MB,
      64 requires ca. 30MB, while 128 already needs more than 230MB. Make sure to set the resolution low enough,
      depending on how much memory you have, to prevent Blender from crashing or freezing. Remember also that many
      operating systems limit the amount of memory that can be allocated by a single *process*, such as Blender,
      even if the *machine* contains much more than this. Find out what limitations apply to your machine.



.. note:: Resolution and Real-size of the Domain

   Be sure to set the resolution appropriate to the real-world size of the domain (see the *Realworld-size* in the
   FIXME(TODO: Internal Link; [[#Domain Wold|Domain Wold panel]])).
   If the domain is not cubic, the resolution will be taken for the longest side.
   The resolutions along the other sides will be reduced according to their lengths
   (therefore, a non-cubic domain will need less memory than a cubic one, resolutions being the same).


   Preview resolution

      This is the resolution at which the preview surface meshes will be generated.
      So it does not influence the actual simulation.
      Even if "there is nothing to see" in the preview,
      there might be a thin fluid surface that cannot be resolved in the preview.

Display quality

   How to display a baked simulation in the 3d view (menu *Viewport Display*) and for rendering (menu *Render Display*):


  Geometry
     use the original geometry (before simulation).
   Preview
      use the preview mesh.
   Final
      use the final high definition mesh.

   When no baked data is found, the original mesh will be displayed by default.

   After you have baked a domain, it is displayed (usually) in the Blender window as the preview mesh.
   To see the size and scope of the original domain box, select :guilabel:`Geometry` in the left dropdown.

Time

   Start
      It is the simulation start time (in seconds).

      This option makes the simulation computation in Blender start later in the simulation.
      The domain deformations and fluid flow prior to the start time are not saved.

      For example, if you wanted the fluid to appear to already have been flowing
      for 4 seconds before the actual first frame of data, you would enter 4.0 here.

   End
      It is the simulation ending time (in seconds).


.. tip:: Start and end times have nothing to do with how many frames are baked

   If you set *Start* time to 3.0, and *End* time to 4.0, you will simulate 1 second of fluid motion.
   That one second of fluid motion will be spread across however-many frames are set in the :guilabel:`Anim` panel
   (:guilabel:`Scene` context → :guilabel:`Render` sub-context → :guilabel:`Anim` and :guilabel:`Output` panel).

   This means, for example, that if you have Blender set to make 250 frames at 25 fps, the fluid
   will look like it had already been flowing for 3 seconds at the start of the simulation,
   *but* will play in slow motion (one-tenth normal speed),
   since the 1 second fluid sim plays out over the course of 10 video seconds. To correct this,
   change the end time to 13.0 (3.0 + 10.0) to match the 250 frames at 25 fps. Now,
   the simulation will be real-time,
   since you set 10 seconds of fluid motion to simulate over 10 seconds of animation.
   Having these controls in effect gives you a "speed control" over the simulation.


Generate Speed Vector
   If this button is clicked, no speed vectors will be exported.
   So by default, speed vectors are generated and stored on disk.
   They can be used to compute image based motion blur with the compositing nodes.

Reverse fluid frames
   The simulation is calculated backward

*Bake* directory
   For baking options please refer to FIXME(TODO: Internal Link; [[#Baking|the baking section]]) in this page.


Domain World
============

.. figure:: /images/Fluid_domainworld.jpg

   The Domain World options.


Viscosity
   The "thickness" of the fluid and actually the force needed to move an object of a certain surface area through it
   at a certain speed. You can either enter a value directly or use one of the presets in the drop down (such as
   honey, oil, or water).

   For manual entry, please note that the normal real-world viscosity (the so-called dynamic viscosity)
   is measured in Pascal-seconds (Pa.s), or in Poise units (P, equal to 0.1 Pa.s, pronounced "\ *pwaz* ",
   from the Frenchman Jean-Louis Poiseuille, who discovered the laws on "the laminar flow of viscous fluids"),
   and commonly centiPoise units (cP, equal to 0.001 Pa.s, "\ *sentipwaz* "). Blender, on the other hand,
   uses the kinematic viscosity (which is dynamic viscosity in Pa.s, divided by the density in kg.m\ :sup:`-3`,
   unit ``m``:sup:`2` ``.s``:sup:`-1`).
   The table below gives some examples of fluids together with their dynamic and kinematic viscosities.

   Manual entries are specified by a floating point number and an exponent.
   These floating point and exponent entry fields (scientific notation)
   simplify entering very small or large numbers. The viscosity of water at room temperature is 1.002 cP,
   ou 0.001002 Pa.s; the density of water is about 1000 kg.m\ :sup:`-3`, which gives us a kinematic viscosity of
   0.000001002 m\ :sup:`2`.s\ :sup:`-1` - so the entry would be 1.002 times 10 to the minus six (``1.
   002?10``:sup:`-6` in scientific notation). Hot Glass and melting iron is a fluid, but very thick;
   you should enter something like ``1.0?10``:sup:`0` (= 1.0) as its kinematic viscosity
   (indicating a value of ``1.0?10``:sup:`6` cP).

   Note that the simulator is not suitable for non-fluids, such as materials that do not "flow".
   Simply setting the viscosity to very large values will not result in rigid body behavior,
   but might cause instabilities.


.. note:: Viscosity varies

   The default values in Blender are considered typical for those types of fluids and "look right" when animated. However, actual viscosity of some fluids, especially sugar-laden fluids like chocolate syrup and honey, depend highly on temperature and concentration. Oil viscosity varies by SAE rating. Glass at room temperature is basically a solid, but glass at 1500 degrees Celsius flows (nearly) like water.


..    Comment: <!--

   There's still some things that aren't correct in this table, I think.
   Let me put as clear as I can:
   *The dynamic viscosity international unit is the Pascal-seconds (Pa.s). There are also Poise (P = 0.1 Pa.s), and centiPoise (cP = 0.001 Pa.s).
   *The kinematic viscosity international unit is in m^2.s^-1.
   *The density international unit is in kg.m^-3.
   Which implies that a Pascal corresponds to 1 kg.m^-1.s^-2,
   or else you cannot divide Pa.s by kg.m^-3 to obtain m^2.s^-1 !

   So if I take the kinematics values given bellow,
   and try to get the corresponding dynamic values, I have:
   *water: density: about 1000 (kg.m^-3); kinematic viscosity: 1×10^-6 (m^2.s^-1)
   → dynamic viscosity is 1000 × 1×10^-6 = 1×10^-3 Pa.s, hence 1 cP.
   → COHERENT
   *Oil:   density: more or less like water, so about 1000; Kinematic viscosity: 5×10^-5
   → dynamic viscosity is 1000 × 5×10^-5 = 1×10^-2 Pa.s, hence 50 cP, and not 500 cP
   → NOT COHERENT, unless Oil SAE 50 is ten times heavier than water!
   *Honey: density: about 1250 (kg.m^-3); kinematic viscosity: 2×10^-3
   → dynamic viscosity is 1250 × 2×10^-3 = 2.5 Pa.s, hence 2500 cP, and not 1×10^4 cP
   → NOT COHERENT, unless honey is five times heavier than water!
   *And so on, chocolate syrup density should be of 1×10^4 kg.m^-3 (ten times water density),
   ketchup density should be of 1×10^3 kg.m^-3 (same as water density, coherent I think),
   melting glass density should be of 1×10^12 kg.m^-3 (a thousand million times water density,
   it's more like black hole!)

   So, either the values in the tables are wrong (one way or the other),
   or the law to pass from dynamic viscosity to kinematic viscosity is just a "trick",
   an approximation, only working with fluids around water viscosity...

   Don't know, I'm not a physicist, but there definitively something wrong here,
   so if someone who knows better about this matter could check and correct it, it would be nice!
   --Mont29, 2009/08

   --> .


+---------------------------------+--------------------------+---------------------------------+--------------------------------------------------------------+
+Blender Viscosity Unit Conversion|Fluid                     |dynamic viscosity (in cP)        |kinematic viscosity (Blender, in m\ :sup:`2`.s\ :sup:`-1`)    +
+---------------------------------+--------------------------+---------------------------------+--------------------------------------------------------------+
+Water (20- C)                    |1.002×10\ :sup:`0` (1.002)|1.002×10\ :sup:`-6` (0.000001002)                                                               +
+---------------------------------+--------------------------+---------------------------------+--------------------------------------------------------------+
+Oil SAE 50                       |5.0×10\ :sup:`2` (500)    |5.0×10\ :sup:`-5` (0.00005)                                                                     +
+---------------------------------+--------------------------+---------------------------------+--------------------------------------------------------------+
+Honey (20- C)                    |1.0×10\ :sup:`4` (10,000) |2.0×10\ :sup:`-3` (0.002)                                                                       +
+---------------------------------+--------------------------+---------------------------------+--------------------------------------------------------------+
+Chocolate Syrup                  |3.0×10\ :sup:`4` (30,000) |3.0×10\ :sup:`-3` (0.003)                                                                       +
+---------------------------------+--------------------------+---------------------------------+--------------------------------------------------------------+
+Ketchup                          |1.0×10\ :sup:`5` (100,000)|1.0×10\ :sup:`-1` (0.1)                                                                         +
+---------------------------------+--------------------------+---------------------------------+--------------------------------------------------------------+
+Melting Glass                    |1.0×10\ :sup:`15`         |1.0×10\ :sup:`0` (1.0)                                                                          +
+---------------------------------+--------------------------+---------------------------------+--------------------------------------------------------------+


Realworld-size
   Size of the domain object in the real world in meters.
   If you want to create a mug of coffee, this might be 10 cm (0.1 meters), while a swimming pool might be 10m.
   The size set here is for the longest side of the domain bounding box.

Optimization

   Gridlevel
      How many adaptive grid levels to be used during simulation - setting this to -1 will perform automatic selection.

   Compressibility
      If you have problems with large standing fluid regions at high resolution, it might help to reduce this number (note that this will increase computation times).


Domain Boundary
===============

.. figure:: /images/Blender_fluids_domain_boundary.jpg
   :width: 300px
   :figwidth: 300px

   The Domain Boundary panel


This box has all the slip and surface options.


FIXME(Template Unsupported: Doc:2.6/Manual/Physics/Fluid/split_type;
{{Doc:2.6/Manual/Physics/Fluid/split_type}}
)

*Surface*

   Surface Smoothing
      Amount of smoothing to be applied to the fluid surface.
      1.0 is standard, 0 is off, while larger values increase the amount of smoothing.

   Subdivisions
      Allows the creation of high-res surface meshes directly during the simulation
      (as opposed to doing it afterwards like a subdivision modifier).
      A value of 1 means no subdivision, and each increase results in one further subdivision of each fluid voxel.
      The resulting meshes thus quickly become large, and can require large amounts of disk space.
      Be careful in combination with large smoothing values -
      this can lead to long computation times due to the surface mesh generation.

   *Hide fluid surface*



Domain Particles
================

.. figure:: /images/Blender_fluids_domain_particles.jpg
   :width: 300px
   :figwidth: 300px

   The Domain Particles panel


Here you can add particles to the fluid simulated, to enhance the visual effect.

Tracer Particles
   Number of tracer particles to be put into the fluid at the beginning of the simulation.
   To display them create another object with the :guilabel:`Particle` fluid type,
   explained below, that uses the same bake directory as the domain.

Generate Particles
   Controls the amount of fluid particles to create (0=off, 1=normal, >1=more).
   To use it, you have to have a surface subdivision value of at least 2.


.. figure:: /images/Manual-FluidSimParts.jpg
   :width: 600px
   :figwidth: 600px

   An example of the effect of particles can be seen here - the image to the left was simulated without,
   and the right one with particles and subdivision enabled.


Baking
======

.. figure:: /images/Fluid_domainpanel.jpg

   The fluid simulation options with Domain selected


Bake Button
-----------

Perform the actual fluid simulation. Blender will continue to work normally,
except there will be a status bar in the top of the window, next to the render pulldown.
Pressing :kbd:`Esc` or the "x" next to the status bar will abort the simulation.
Afterwards two "\ ``.bobj.gz`` " (one for the :guilabel:`Final` quality,
one for the :guilabel:`Preview` quality), plus one "\ ``.bvel.gz`` "
(for the :guilabel:`Final` quality) will be in the selected output directory for each frame.


Bake directory
--------------

**REQUIRED!**

Directory and file prefix to store baked surface meshes.

This is similar to the animation output settings, only selecting a file is a bit special:
when you select any of the previously generated surface meshes (e.g.
"\ ``test1_fluidsurface_final_0132.bobj.gz`` "), the prefix will be automatically set
("\ ``test1_`` " in this example).
This way the simulation can be done several times with different settings,
and allows quick changes between the different sets of surface data.

The default value is "\ ``/tmp/`` ", which is probably *not* what you want. Choose an
appropriate directory-name and file prefix so that these files will be stored in an
appropriate location *and* named in such a way that two different fluid-simulations won't
conflict with one another (if you're intending to specify only a directory-name here, i.e.
without a filename-prefix, don't forget the trailing "\ ``/`` ").


Notes
-----

Unique domain
   Because of the possibility of spanning and linking between scenes,
   there can only be one domain in an entire .blend file.

Selecting a Baked Domain
   After a domain has been baked, it changes to the fluid mesh.
   To re-select the domain so that you can bake it again after you have made changes,
   go to any frame and select (:kbd:`Rmb`) the fluid mesh.
   Then you can click the :guilabel:`BAKE` button again to recompute the fluid flows inside that domain.

Baking always starts at Frame #1
   The fluid simulator disregards the :guilabel:`Sta` setting in the :guilabel:`Anim` panel,
   it will always bake from frame 1.
   If you wish the simulation to start later than frame 1, you must key the fluid objects in your domain
   to be inactive until the frame you desire to start the simulation. See
   FIXME(TODO: Internal Link; [[#Animating Fluid Property Changes|below]]) for more information.

Baking always ends at the :guilabel:`End` Frame set in the :guilabel:`Anim` panel
   If your frame-rate is 25 frames per second,
   and ending time is 4.0 seconds, then you should (if your start time is 0)
   set your animation to end at frame ``4.0 × 25 = 100``

Freeing the previous baked solutions
   Deleting the content of the "Bake" directory is a destructive way to achieve this.
   Be careful if more than one simulation uses the same bake directory
   (be sure they use different filenames, or they will overwrite one another)!

Reusing Bakes
   Manually entering (or searching for) a previously saved (baked)
   computational directory and filename mask will switch the fluid
   flow and mesh deformation to use that which existed during the old bake.
   Thus, you can re-use baked flows by simply pointing to them in this field.

Baking processing time
   Baking takes a **lot** of compute power (hence time).
   Depending on the scene, it might be preferable to bake overnight.

   If the mesh has modifiers, the rendering settings are used for exporting the mesh to the fluid solver.
   Depending on the setting, calculation times and memory use might exponentially increase.
   For example, when using a moving mesh with :guilabel:`Subsurf` as an obstacle,
   it might help to decrease simulation time by switching it off, or to a low subdivision level.
   When the setup/rig is correct, you can always increase settings to yield a more realistic result.


..    Comment: <!--

   ===="St"/"Ad"/"Bn"/"Par" Buttons====
   Till now, we were in the {{Literal|St}}andard buttons.
   Clicking another one of these buttons will show other "panels" (groups of controls:
   {{Literal|Ad}}vanced, {{Literal|Bn}} for boundary, and {{Literal|Par}}ticle)
   of more advanced options, that often are fine set at the defaults.

   Standard
   :The settings in this set are already been described above...

   Advanced
   :Gravity vector
   ::Strength and direction of the gravity acceleration and any lateral (x,y plane) force. The main component should be along the negative z-axis (in ``m.s<sup>-2</sup>``).
   ::''Please Note:'' All of the x,y,z values should not be zero, or the fluid won't flow! Imagine a droplet floating in the nothingness of deep space... It must be some small number in at least one direction.

   --> .

