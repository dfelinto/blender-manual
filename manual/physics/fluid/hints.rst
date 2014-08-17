..    TODO/Review: {{review}} .

Fluid Hints
***********

Some useful hints about fluid simulation in Blender:


- Don't be surprised, but you'll get whole bunch of mesh (.bobj.gz) files after a simulation. One set for preview, and another for final. Each set has a .gz file for each frame of the animation. Each file contains the simulation result - so you'll need them.


- Currently these files will not be automatically deleted, so it is a good idea to e.g. create a dedicated directory to keep simulation results. Doing a fluid simulation is similar to clicking the :guilabel:`ANIM` button - you currently have to take care of organizing the fluid surface meshes in some directory yourself. If you want to stop using the fluid simulation, you can simply delete all the ``*fluid*.bobj.gz`` files.


- Before running a high resolution simulation that might take hours, check the overall timing first by doing lower resolution runs.


- Fluid objects must be completely inside the bounding box of the domain object. If not, baking may not work correctly or at all. Fluid and obstacle objects can be meshes with complex geometries. Very thin objects might not appear in the simulation, if the chosen resolution is too coarse to resolve them (increasing it might solve this problem).


- Note that fluid simulation parameters, such as inflow velocity or the active flag can be animated with :guilabel:`Fluidsim` Ipos (see above).


- Don't try to do a complicated scene all at once. Blender has a powerful compositor that you can use to combine multiple animations.

   For example, to produce an animation showing two separate fluid flows while keeping your domain small,
   render one .avi using the one flow.
   Then move the domain and render another .avi with the other flow using an alpha channel (in a separate B&W .avi?).
   Then, composite both .avi's using the compositor's add function. A third .
   avi is usually the smoke and mist and it is laid on top of everything as well.
   Add a rain sheet on top of the mist and spray and you'll have quite a storm brewing! And then lightning flashes,
   trash blowing around, all as separate animations, compositing the total for a truly spectacular result.



- If you're having trouble, or something isn't working as you think it should - let me know: send the .blend file and a problem description to ``nils at thuerey dot de``. Please check these wiki pages and the `blenderartists-forum <http://blenderartists.org/forum/>`__ before sending a mail!

