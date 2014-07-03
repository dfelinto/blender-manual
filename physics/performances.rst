
Simulation performance adjustments
==================================


OpenMP (Mac OSX)
----------------


How to use the distributed applescript to optimize simulation performance on OSX


Suboptimal baking performance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Often you will encounter suboptimal baking performance with openMP (OMP)
multithreaded simulations, especially fluids.

This is due how the domain splitting distributes threads to cells which are sometimes
not "filled" whereas calculations, resulting in lot of threads not giving any speedboost.
This is almost dependent on the resolution the simulation and object density.

If you have such an "undersaturated" simulation, it helps a lot to just reduce the OMP threads
to a low number instead of letting OMP just use all available cores.


Solution
~~~~~~~~


For OSX openMP-enabled Blender you can now use a delivered applescript to tune the
OMP-threads used. This makes usage of the terminal obsolete.

The default is for now set to 4 cores.

If you leave the input field empty, the script gets the corecount of your logical cpu-cores
(including HyperTrading)
This is the same what openMP would pull without the environment variable set.


Steps to use the applescript
~~~~~~~~~~~~~~~~~~~~~~~~~~~~


- In your Blenderfolder open the "set_simulation_threads" applescript

.. figure:: /images/Thread_Applescript.jpg


- Set the threadcount you want to use (leave empty to let OMP get all available cores)

.. figure:: /images/Thread_Setting.jpg


- Press o.k. to set the new value, a messagebox will show you the new setting accepted.

.. figure:: /images/Thread_Information.jpg


- Close and reopen Blender to take over the setting.
- Watch your baking progress or simulation framerates and perhaps repeat steps 1- 4 to get the optimal value.