..    TODO/Review: {{review|text=check see-also and external links}} .


Fluid Appendix
**************

Limitations & Workarounds
=========================

- One domain per blender file (as of Version 2.42), but you can have multiple fluid objects.

   *Workaround:* For previews, move the domain around to encompass each fluid flow part, and then for final, scale up the size of the domain to include all fluid objects (but computation will take longer). This is actually a benefit, because it lets you control how much compute time is used, by varying the size and location of the domain.


- If the setup seems to go wrong, make sure all the normals are correct (hence, enter :guilabel:`Edit mode`, select all, and recalculate normals once in a while).


- Currently there's a problem with zero gravity simulation - simply select a very small gravity until this is fixed.


- If an object is initialized as :guilabel:`Volume`, it has to be closed and have an inner side (a plane won't work). To use planes, switch to :guilabel:`Shell`, or extrude the plane.


- Blender freezes after clicking :guilabel:`BAKE`. Pressing :kbd:`Esc` makes it work again after a while - this can happen if the resolution is too high and memory is swapped to hard disk, making everything horribly slow. Reducing the resolution should help in this case.


- Blender crashes after clicking :guilabel:`BAKE` - this can happen if the resolution is really high and more than 2GB are allocated, causing Blender to crash. Reduce the resolution. Many operating systems limit the total amount of memory that can be allocated by a *process*, such as Blender, even if the *machine* has more memory installed. Sux...


- The meshes should be closed, so if some parts of e.g. a fluid object are not initialized as fluid in the simulation, check that all parts of connected vertices are closed meshes. Unfortunately, the Suzanne (monkey) mesh in Blender is not a closed mesh (the eyes are separate).


- If the fluid simulation exits with an error message (stating e.g. that the "init has failed"), make sure you have valid settings for the domain object, e.g. by resetting them to the defaults.


- To import a single fluid surface mesh you can use this script: `.bobj.-Import-Script <http://www10.informatik.uni-erlangen.de/~sinithue/temp/bobj_import.py>`__.


- You may not be able to bake a fluid that takes more than 1GB, not even with the LargeAddressAware build - it might be a limitation of the current fluid engine.


- Note that first frame may well take only a few hundred MBs of RAM memory, but latter ones go over one GB, which may be why your bake fails after awhile. If so, try to bake one frame at the middle or end at full res so you'll see if it works.


- Memory used doubles when you set surface subdivision from 1 to 2.


- Using "generate particles" will also add memory requirements, as they increase surface area and complexity. Ordinary fluid-sim generated particles probably eat less memory.


See also
========

..    TODO/Review: {{WikiTask/Todo|check these links, make sure they are compatible with Blender 2.6}} .


- `Tutorial 1: Very Basic Introduction <http://wiki.blender.org/index.php/User:N t/SummerOfCode2005/Fluid Animation/Tutorial 1>`__
- `Tutorial 2: The Next Step <http://wiki.blender.org/index.php/User:N t/SummerOfCode2005/Fluid Animation/Tutorial 2>`__
- `Tutorial 1&2 Gui Changes for newer builds <http://wiki.blender.org/index.php/User:N t/SummerOfCode2005/Fluid Animation/Tutorial Changes>`__
- :doc:`Another BSoD fluid tutorial <ls/physics/bsod/fluid>`
- `Developer documentation (implementation, dependencies, ...) <http://wiki.blender.org/index.php/User:N t/SummerOfCode2005/Fluid Animation/Development>`__


External links
==============

..    TODO/Review: {{WikiTask/Todo|check these links, make sure they are compatible with Blender 2.6}} .


- `An Introduction to Fluid Simulations in Blender (video) <http://cg.tutsplus.com/tutorials/3d-art/an-introduction-to-fluid-simulations-in-blender/>`__ (`Blendernation link <http://www.blendernation.com/cgtuts-an-introduction-to-fluid-simulations-in-blender/>`__)

   Learn the basics of how to set up a fluid simulation in Blender with an obstacle.

- `Fluid Simulator Tutorial (video) <http://www.free3dtutorials.com/index.php?tutorials=0&software=11&id=269&page=>`__ (`Blendernation link <http://www.blendernation.com/2007/10/09/fluid-simulator-tutorial/>`__)

   Very easy to understand video-tutorial to fluid simulation newcomers. Also covers some of the most common pitfalls.

- `Guide on Blender Fluid Simulator's Parameters <http://www.pkblender.it>`__ (`Blendernation link <http://www.blendernation.com/2007/11/21/guide-on-blender-fluid-simulators-parameters/>`__)

