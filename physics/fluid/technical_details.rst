..    TODO/Review: {{review}} .

Fluid Technical Details
***********************

Physical correctness
====================

.. figure:: /images/Manual-Part-X-fluidsim-example3.jpg

   "My cup runneth over", created with Blender and Yafray.


Fluid animation can take a lot of time - the better you understand how it works,
the easier it will be to estimate how the results will look.
The algorithm used for Blender's fluid simulation is the *Lattice Boltzmann Method* (LBM);
other fluid algorithms include *Navier-Stokes* (NS)
solvers and *Smoothed Particle Hydrodynamics* (SPH) methods.
LBM lies somewhere between these two.

In general,
it is really hard for current computers to correctly simulate even a 1-meter tank of water.
For simulating a wave crashing through a city,
you would probably need one of the most expensive supercomputers you could get,
and it might still not work properly,
no matter which of the three algorithms above you're using. Therefore,
to achieve "the effect that you really want",
you'll need to resort to strategies very similar to what filmmakers have been doing
(quite successfully...) in "analogue" movies for many years: "\ *fake it!* "

A good fluid simulation is a *very important* part, but not the *only* part,
of achieving a satisfactory image.
Let Blender do the computational dirty-work of calculating the basic fluid simulation, then
create realism by adding carefully selected details that match the viewer's expectations for
"the real-life maelstrom that you have created".

For example, you can pretend to have a wave in a gigantic city by:
building a *smaller* model, modeling a *small* wave in the model at very high resolution,
and hope that nobody will notice the difference between a 100m and a 1m wave (they won't).
Texture the wave front with lots of noise and clouds affecting the color. Add lots of smoke
(mist) emitters on the various surfaces that the wave hits, timing each of them to emit at the
moment of impact in a direction incident to the surface and collision. Animate cars and trash
(and drowning people...) to float and bob on the wave front using the baked mesh. Use a string
of mist emitters pointing up positioned at the wave crest to simulate the mist that blows off
the top of the crest into the air. Consider exactly where you want to put the camera,
whether you want to use a zoom lens or a wide angle, and so on
(is the viewer to be "looking down upon the poor unfortunate actors",
or "drowning along with them"?). *This* is the kind of attention to detail,
above and beyond the fluid simulation itself, that will carry the shot.

For Blender's LBM solver, the following things will make the simulation harder to compute:

- Large domains.
- Long duration.
- Low viscosities.
- High velocities.

The viscosity of water is already really low, so especially for small resolutions,
the turbulence of water can not be correctly captured. If you look closely,
most simulations of fluids in computer graphics do not yet look like real water as of now.
Generally, don't rely on the physical settings too much
(such as physical domain size or length of the animation in seconds).
Rather try to get the overall motion right with a low resolution,
and then increase the resolution as much as possible or desired.


Acknowledgements
================

The integration of the fluid simulator was done as a Google Summer-of-Code project. More
information about the solver can be found at
`www.ntoken.com <http://graphics.ethz.ch/~thuereyn/ntoken3/Publications.html>`__.
These Animations were created with the solver before its integration into blender:
[http://www10.informatik.uni-erlangen.de/~sinithue/public/phd/nthuerey_050731_sgposter.avi
Adaptive Grids],
[http://www10.informatik.uni-erlangen.de/~sinithue/public/phd/nthuerey_050607_tr1rtlbm.
avi Interactive Animations]. Thanks to Chris Want for organizing the Blender-SoC projects, and
to Jonathan Merrit for mentoring this one! And of course thanks to Google for starting the
whole thing... SoC progress updates were posted here:
`SoC-Blenderfluid-Blog at PlanetSoC <http://www.planetsoc.com/blog/51>`__.

The solver itself was developed by Nils Thuerey with the help and supervision of the following
people: U. Ruede, T. Pohl, C. Koerner, M. Thies, M. Oechsner and T.
Hofmann at the Department of Computer Science 10 (System Simulation, LSS) in Erlangen,
Germany.


+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
+`http://www10.informatik.uni-erlangen.de/~sinithue/img/lsslogo.png <http://www10.informatik.uni-erlangen.de/>`__|`http://www10.informatik.uni-erlangen.de/~sinithue/img/unierlangenlogo.png <http://www.uni-erlangen.de/>`__+
+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+


