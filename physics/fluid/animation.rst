..    TODO/Review: {{review}} .

Animating the fluid properties
==============================


A new type of Ipo Curve, :guilabel:`FluidSim`\ , is available for fluid domain objects.
Unlike most other animatable values in Blender,
:guilabel:`FluidSim` Ipos cannot be keyframed by simply using the :kbd:`I` key;
you must manually set values by clicking in the Ipo window. In order to set a keyframe, you
must select the property you wish to animate in the Ipo window and :kbd:`ctrl-Lmb` click
to set the keyframe to the desired location in the Ipo window.


.. admonition:: Enter Properties
   :class: nicetip

   Note that you do not have to be exact on where you click; we recommend that after you set the control point, open the :guilabel:`Transform Properties` panel (\ :kbd:`N`\ ) and round the X value to a whole frame number, and then set the Y value that you wish.


The fluid domain has several channels that control the fluid over time:

:guilabel:`Fac-Visc`
   A multiplicative factor in the fluid's viscosity coefficient. It must be set before baking, and changes the viscosity of the fluid over time, so you can turn water into wi… oil, for example!

:guilabel:`Fac-Tim`
   Changes the speed of the simulation; like the Speed Control in the VSE can speed up or slow down a video, this curve can speed up or slow down the fluid motion during a frame sequence. If the value for :guilabel:`Fac-Tim` is less than or equal to zero, time (and the fluid) stands still; the fluid freezes. For values between 0.0 and 1.0, the fluid runs slower and will look thicker. 1.0 is normal fluid motion, and values greater than 1.0 will make the fluid flow faster, possibly appearing thinner.

:guilabel:`GravX`\ /\ :guilabel:`GravY`\ /\ :guilabel:`GravZ`
   The XYZ vector for gravity changes; aka inertia of the fluid itself (think drinking a cup of coffee while driving NASCAR at Talladega, or sipping an espresso on the autobahn, or watering the plants on the Space Shuttle). Changes in these curves make the fluid slosh around due to external forces.

The :guilabel:`Fluid`\ , :guilabel:`Obstacle`\ , :guilabel:`Inflow`\ ,
:guilabel:`Outflow` and :guilabel:`Particle` objects can use the following channels:

:guilabel:`VelX`\ /\ :guilabel:`VelY`\ /\ :guilabel:`VelZ`
   Spurts of water from the garden hose can be simulated via these curves, to mimic changes in pressure and/or direction. It also can be used to simulate the effect of wind on a stream of water, for example.

:guilabel:`Active`
   When Active transitions from 0.0 to something greater than 0 (such as between 0.1 and 1.0), the object's function (designated as an :guilabel:`Inflow`\ , or :guilabel:`Outflow`\ , etc.) resumes its effect. Crossing down to 0.0 and then at some point, back up, re-establishes the effect and the resulting fluid sim. Use this for dripping, or any kind of intermittent inflow. This active status also works for objects designated as :guilabel:`Outflow` and :guilabel:`Obstacle`\ , so you can also simulate (for example) a drain plugging up.

You can also control the force settings of :guilabel:`Control` objects:

:guilabel:`AttrForceStr`\ , :guilabel:`AttrForceRa`
   These curves control the values of the attraction force settings.

:guilabel:`VelForceStr`\ , :guilabel:`VelForceRa`
   These curves control the values of the velocity force settings.

