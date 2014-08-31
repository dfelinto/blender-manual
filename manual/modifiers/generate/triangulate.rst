
Triangulate Modifier
********************

.. admonition:: Reference
   :class: refbox

   | Mode:     Object mode
   | Panel:    Properties Window → Context Button :guilabel:`Modifiers`

   .. figure:: /images/CZ_Modifier_ContextButton.jpg


Description
===========

The :guilabel:`Triangulate` modifier converts all faces in a mesh
(whether it be quads or N-gons) to triangular faces.
This modifier does the exact same function as the Ctrl+T triangulate in :guilabel:`Edit Mode`


.. figure:: /images/Triangulate-before.jpg
   :width: 300px
   :figwidth: 300px

   Mesh before Triangulate Modifier


.. figure:: /images/Triangulate-after.jpg
   :width: 300px
   :figwidth: 300px

   Mesh after Triangulate Modifier


Options
=======

:guilabel:`Quad Method`:
   :guilabel:`Beauty`
      Split the quads in nice triangles, slower method.

   :guilabel:`Fixed`
      Split the quads on the 1st and 3rd vertices.

   :guilabel:`Fixed Alternate`
      Split the quads on the 2nd and 4th vertices.

   :guilabel:`Shortest Diagonal`
      Split the quads based on the distance between the vertices.

:guilabel:`Ngon Method`:
   :guilabel:`Beauty`
      Arrange the new triangles nicely, slower method.
   :guilabel:`Scanfill`
      Split the ngons using a scanfill algorithm.
