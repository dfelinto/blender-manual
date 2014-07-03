
Skin Modifier
=============


.. admonition:: Reference
   :class: refbox

   | Mode:     Any mode
   | Panel:    :guilabel:`Modifiers`


The :guilabel:`Skin` modifier uses vertices and edges to create a skinned surface,
using a per-vertex radius to better define the shape.

It is a quick way to generate base meshes for sculpting and/or smooth organic shapes with
arbitrary topology.

Note that faces in the input are ignored by the Skin modifier.

Options
-------


.. figure:: /images/Doc-skin-ui.jpg
   :width: 300px
   :figwidth: 300px

   Skin modifier UI.


:guilabel:`Create Armature`
   Create an armature for your object.
:guilabel:`Branch Smoothing`
   Smooth the intersection vertices.

:guilabel:`Selected Vertices`
:guilabel:`Mark Loose`
   Mark the selected vertices as loosing points. Loosing defines points which merge their faces with each other to fill gaps.
:guilabel:`Clear Loose`
   Take the Loose away. The initial behavior.

:guilabel:`Mark Root`
   Defines the root points of the object. These are the center of the object.

:guilabel:`Equalize Radii`
   Makes the skin radii of selected vertices equal on each axis.


Example
-------


- Select the cube. :kbd:`Tab` into edit mode and :menuselection:`[Alt][M] --> At Center` to merge all vertices at one point. :kbd:`E` then :kbd:`Z` to extrude the vertex along the Z axis.

.. admonition:: Skin Node Set Flag
   :class: note

   One of the mesh's vertices must be set to :guilabel:`Root`\ .  If you by accident delete the default root vertex, select a vertex, hit the :guilabel:`Skin Node Set Flag` button, and in the :guilabel:`Mesh Tools` menu set the new vertex to root.


.. figure:: /images/Skin-header-00.jpg

   Simple creature, made with only the Skin modifier.


- In the modifiers' menu, add a :guilabel:`Skin` modifier.
- :kbd:`Tab` into edit mode and start extruding.  To see the actual "Z spheres", :kbd:`Z` to change to wireframe mode.  These spheres are actual meshes with a lot of polygons, so performance issues might occur on older computers.
- Try to get  sketch results similar to the picture (Simple creature, made with only the Skin modifier.), through extruding the vertices of the object.
- Use :kbd:`Ctrl-A` to change the size of the different regions within the creature.
- Use :guilabel:`Mark Loose` at regions like the neck, to merge these faces more together.
- To get smoother results, activate :guilabel:`Smooth Shading` and use :kbd:`Ctrl-3` on the object.


External links
==============


- `Skin Modifier Development at Blender Nation <http://www.blendernation.com/2011/03/11/skin-modifier-development/>`__ — An early demonstration of the skin modifier by Nicholas Bishop (March 2011)
- Ji, Zhongping; Liu, Ligang; Wang, Yigang (2010). `B-Mesh: A Fast Modeling System for Base Meshes of 3D Articulated Shapes <http://www.math.zju.edu.cn/ligangliu/CAGD/Projects/BMesh/>`__\ , Computer Graphics Forum 29(7), pp. 2169-2178. — The work this modifier is based on (\ `direct link to PDF <http://www.math.zju.edu.cn/ligangliu/CAGD/Projects/BMesh/Paper/BMesh.pdf>`__\ )
- `Related thread on Blender artists <http://blenderartists.org/forum/showthread.php?209551-B-mesh-modeling-tools-papers-better-than-zsfere>`__


