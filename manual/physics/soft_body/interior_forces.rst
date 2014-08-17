
Interior Forces
***************

.. figure:: /images/Bsod-softbody-theory1.jpg
   :width: 200px
   :figwidth: 200px

   Image 1a: Vertices and forces along their connection edges.


To create a connection between the vertices of a Soft Body object there have to be forces that
hold the vertices together. These forces are effective along the edges in a mesh,
the connections between the vertices. The forces act like a spring. (*Image 1a*)
illustrates how a 3×3 grid of vertices (a mesh plane in Blender)
are connected in a Soft Body simulation.

But two vertices could freely rotate if you don't create additional edges between them.
Have you ever tried building a storage shelf out of 4 planks alone? Well - don't do it,
it will not be stable. The logical method to keep a body from collapsing would be to create
additional edges between the vertices. This works pretty well,
but would change your mesh topology drastically.


.. figure:: /images/Bsod-softbody-theory2.jpg
   :width: 200px
   :figwidth: 200px

   Image 1b: Additional forces with Stiff Quads enabled.


Luckily, Blender allows us to define additional *virtual* connections.
On one hand we can define virtual connections between the diagonal edges of a quad face
(:guilabel:`Stiff Quads`, *Image 1b*), on the other hand we can define virtual connections
between a vertex and any vertices connected to it's neighbours
(:guilabel:`Bending Stiffness`). In other words, the amount of bend that is allowed between a
vertex and any other vertex that is separated by two edge connections.


Edges Settings
**************

The characteristics of edges are set with the :guilabel:`Soft Body Edge` properties.

:guilabel:`Use Edges`
   Allow the edges in a Mesh Object to act like springs.

:guilabel:`Pull`
   The spring stiffness for edges (how much the edges are allowed to stretch). A low value means very weak springs
   (a very elastic material), a high value is a strong spring (a stiffer material) that resists being pulled apart.
   0.5 is latex, 0.9 is like a sweater, 0.999 is a highly-starched napkin or leather.
   The Soft Body simulation tends to get unstable if you use a value of 0.999,
   so you should lower this value a bit if that happens.
:guilabel:`Push`
   How much the Softbody resist being scrunched together,
   like a compression spring. Low values for fabric, high values for inflated objects and stiff material.
:guilabel:`Damp`
   The friction for edge springs. High values (max of 50) dampen the :guilabel:`Push` / :guilabel:`Pull` effect and calm down the cloth.
:guilabel:`Plastic`
   Permanent deformation of the object after a collision. The vertices take a new position without applying the modifier.
:guilabel:`Bending`
   This option creates virtual connections between a vertex and the vertices connected to it's neighbors. This includes diagonal edges. Damping also applies to these connections.
:guilabel:`Length`
   The edges can shrink or been blown up. This value is given in percent, 0 disables this function. 100% means no change, the body keeps 100% of his size.

:guilabel:`Stiff Quads`
   For quad faces, the diagonal edges are used as springs. This stops quad faces to collapse completely on collisions (what they would do otherwise).
:guilabel:`Shear`
   Stiffness of the virtual springs created for quad faces.


Preventing Collapse
===================

To show the effect of the different edge settings we will use two cubes (blue: only quads, red: only tris) and let them fall without any goal onto a plane (how to set up collision is shown on the page :doc:`Collisions <physics/soft_body/collisions>`).


+--------------------------------------------------------+--------------------------------------------------------+--------------------------------------------------------+
+.. figure:: /images/Blender3D_QuadVSTri-SB-0001-2.49.jpg|.. figure:: /images/Blender3D_QuadVSTri-SB-0036-2.49.jpg|.. figure:: /images/Blender3D_QuadVSTri-SB-0401-2.49.jpg+
+   :width: 200px                                        |   :width: 200px                                        |   :width: 200px                                        +
+   :figwidth: 200px                                     |   :figwidth: 200px                                     |   :figwidth: 200px                                     +
+                                                        |                                                        |                                                        +
+   Image 3a: Frame 1 without Stiff Quads.               |   Image 3b: Frame 36.                                  |   Image 3c: Frame 401.                                 +
+--------------------------------------------------------+--------------------------------------------------------+--------------------------------------------------------+


In (*Image 3*), the default settings are used (without :guilabel:`Stiff Quads`).
The "quad only" cube will collapse completely, the cube composed of tris keeps it's shape,
though it will deform temporarily because of the forces created during collision.


+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
+.. figure:: /images/Blender3D_QuadVSTri-SB-SQ-0001-2.49.jpg|.. figure:: /images/Blender3D_QuadVSTri-SB-SQ-0036-2.49.jpg|.. figure:: /images/Blender3D_QuadVSTri-SB-SQ-0401-2.49.jpg+
+   :width: 200px                                           |   :width: 200px                                           |   :width: 200px                                           +
+   :figwidth: 200px                                        |   :figwidth: 200px                                        |   :figwidth: 200px                                        +
+                                                           |                                                           |                                                           +
+   Image 4a: Frame 1 with Stiff Quads.                     |   Image 4b: Frame 36.                                     |   Image 4c: Frame 401.                                    +
+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+


In (*Image 4*), :guilabel:`Stiff Quads` is activated (for both cubes).
Both cubes keep their shape, there is no difference for the red cube,
because it has no quads anyway.


+----------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
+.. figure:: /images/Blender3D_QuadVSTri-SB-BS-0001-2.49.jpg                                   |.. figure:: /images/Blender3D_QuadVSTri-SB-BS-0036-2.49.jpg|.. figure:: /images/Blender3D_QuadVSTri-SB-BS-0401-2.49.jpg+
+   :width: 200px                                                                              |   :width: 200px                                           |   :width: 200px                                           +
+   :figwidth: 200px                                                                           |   :figwidth: 200px                                        |   :figwidth: 200px                                        +
+                                                                                              |                                                           |                                                           +
+   Image 5a: Frame 1 with Bending Stiffness.                                                  |   Image 5b: Frame 36.                                     |   Image 5c: Frame 401.                                    +
+   `Blend file <http://wiki.blender.org/index.php/Media:Blender3D Quads-BE-Stiffness.blend>`__|                                                           |                                                           +
+----------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+


The second method to stop an object from collapsing is to change it's :guilabel:`Bending
Stiffness`. This includes the diagonal edges (Damping also applies to these connections).

In (*Image 5*), :guilabel:`Be` is activated with a strength setting of 1.
Now both cubes are more rigid.


+------------------------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------------+
+.. figure:: /images/Blender3D_QuadVSTri-Bending-001-2.49.jpg|.. figure:: /images/Blender3D_QuadVSTri-Bending-101-2.49.jpg|.. figure:: /images/Blender3D_QuadVSTri-Bending-high-101-2.49.jpg+
+   :width: 200px                                            |   :width: 200px                                            |   :width: 200px                                                 +
+   :figwidth: 200px                                         |   :figwidth: 200px                                         |   :figwidth: 200px                                              +
+                                                            |                                                            |                                                                 +
+   Image 6a: Two planes going to collide.                   |   Image 6b: No bending stiffness, Frame 101.               |   Image 6c: High bending stiffness (10), Frame 101.             +
+------------------------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------------+


Bending stiffness can also be used if you want to make a subdivided plane more plank like.
Without :guilabel:`Be` the faces can freely rotate against each other like hinges
(*Image 6b*).
There would be no change in the simulation if you activated :guilabel:`Stiff Quads`,
because the faces are not deformed at all in this example.

Bending stiffness on the other hand prevents the plane from being - well - bent.
