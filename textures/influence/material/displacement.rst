
Displacement Maps
=================

Description
~~~~~~~~~~~

Displacement mapping allows a texture input to manipulate the position of vertices on rendered geometry. Unlike :doc:`Normal or Bump mapping <textures/influence/material/bump_and_normal>`, where the shading is distorted to give an illusion of a bump (discussed on the previous page), Displacement Maps create real bumps, creases, ridges, etc in the actual mesh. Thus, the mesh deformations can cast shadows, occlude other objects, and do everything that changes in real geometry can do, but, on the other hand, requires a lot more vertices to work.


Options
~~~~~~~

In the :doc:`Influence panel <textures/influence/material>`, the strength of the displacement is controlled by the :guilabel:`Displace` and :guilabel:`Normal` sliders.

- If a texture provides only normal information (e.g. :guilabel:`Stucci`), vertices move according to the texture's normal data. The normal displacement is controlled by the :guilabel:`Normal` slider.
- If a texture provides only intensity information (e.g. :guilabel:`Magic`, derived from color), vertices move along the directions of their normals (a vertex has no normal itself, it's the resulting vector of the adjacent faces). White pixels move outward in the direction of the normal, black pixels move in the opposite direction. The amount of displacement is controlled with the :guilabel:`Displace` slider.

The two modes are not exclusive. Many texture types provide both information
(:guilabel:`Clouds`, :guilabel:`Wood`, :guilabel:`Marble`, :guilabel:`Image`).
The amount of each type can be mixed using the respective sliders.
Intensity displacement gives a smoother, more continuous surface,
since the vertices are displaced only outward.
Normal displacement gives a more aggregated surface,
since the vertices are displaced in multiple directions.

The depth of the displacement is scaled with an object's scale,
but not with the relative size of the data.
This means if you double the size of an object in object mode,
the depth of the displacement is also doubled, so the relative displacement appears the same.
If you scale inside :guilabel:`Edit Mode`, the displacement depth is not changed,
and thus the relative depth appears smaller.


Hints
~~~~~

Displacement maps move the rendered faces, not the physical mesh faces. So,
in 3D View the surface may appear smooth, but render bumpy. To give a detailed surface,
there has to be faces to displace and have to be very small.
This creates the trade-off between using memory and CPU time versus render quality.

From best to worst, displacement works with these object types using the methods listed to
control the render face size:

:doc:`Subdivision Surface <modifiers/generate/subsurf>` **Meshes**
   Rendered face size is controlled with render subsurf level. Displacement really likes smooth normals.
**Manually (** :guilabel:`Edit Mode` **)** :doc:`subdivided <modeling/meshes/advanced_tools#subdivide>` **meshes**
   Control render faces with number of subdivides.
   (This can be combined with the above methods.) Displaces exactly the same Simple Subsurf,
   but slows editing down because of the OpenGL overhead of drawing the extra faces.
   (You can't turn the edit subdivide level down this way).
:doc:`Meta Objects <modeling/metas>`
   Control render faces with render wiresize. Small wire == more faces.

The following are available, but currently don't work well.
It is recommended that you convert these to meshes before rendering.

**Open** :doc:`NURBS Surfaces <modeling/surfaces>`
   Control render faces with U/V :guilabel:`Surface Resolution`. Higher numbers give more faces. (Note normal errors).
**Closed NURBS Surfaces**
   Control with :guilabel:`Surface Resolution` controls. (Note the normal errors, and how implicit seam shows).
:doc:`Curves <modeling/curves>` **and** :doc:`Text <modeling/texts>`
   Control with :guilabel:`Surface Resolution` controls. Higher gives more render faces. (Note that the large flat surfaces have few render faces to displace).


.. admonition:: Displace Modifier
   :class: note

   If you want more control over your displacement,
   you'll probably want to use the :doc:`Displace Modifier <modifiers/deform/displace>`.
   This feature has lots of different options so that you can customize the displacement exactly to your liking.

