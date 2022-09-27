.. _bpy.ops.mesh.subdivide:

*********
Subdivide
*********

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Edge --> Subdivide`

Subdividing splits selected edges and faces by cutting them in half or more,
adding new vertices, and subdividing accordingly the faces involved.
It adds resolution to the mesh by divide faces or edges into smaller units.

This process follows a few rules, depending on the settings:

- When only one edge of a face is selected (Triangle mode),
  triangles are subdivided into two triangles, and quads, into three triangles.
- When two edges of a face are selected:

  - If the face is a triangle, a new edge is created between the two new vertices,
    subdividing the triangle in a triangle and a quad.
  - If the face is a quad, and the edges are neighbors,
    there have *three* possible behaviors to divide the quad,
    depending on the setting of *Quad Corner Type* (see below for details).
  - If the face is a quad, and the edges are opposite,
    the quad is just subdivided in two quads by the edge linking the two new vertices.

- When three edges of a face are selected:

  - If the face is a triangle, this means the whole face is selected and
    it is then subdivided in four smaller triangles.
  - If the face is a quad, first the two opposite edges are subdivided as described above.
    Then, the "middle" edge is subdivided, affecting its new "sub-quad" as described above for only one edge.
- When a face of a :term:`Quad` is selected, the face is subdivided into four smaller quads.
- When a face of an :term:`N-gon` is selected,
  the individual edges will be subdivided but the face will stay unsubdivided.


Options
=======

These options are available in the *Tool* panel after running the tool:

Number of Cuts
   Specifies the number of cuts per edge to make.
   By default this is 1, cutting edges in half. A value of 2 will cut it into thirds, and so on.
Smoothness
   Displaces subdivisions to maintain approximate curvature.
   The effect is similar to the way the :doc:`/modeling/modifiers/generate/subdivision_surface`
   might deform the mesh.

   .. list-table::

      * - .. figure:: /images/modeling_meshes_editing_edge_subdivide_smooth-before.png
             :width: 200px

             Mesh before subdividing.

        - .. figure:: /images/modeling_meshes_editing_edge_subdivide_smooth-none.png
             :width: 200px

             Subdivided with no smoothing.

        - .. figure:: /images/modeling_meshes_editing_edge_subdivide_smooth-after.png
             :width: 200px

             Subdivided with smoothing of 1.

Quad/Tri Mode
   Forces subdivide to create triangles or quads instead of n-gons (see examples below).
   This mode doesn't allow the use of *Straight Cut* on quad corners.
Quad Corner Type
   Controls the way quads with only two adjacent selected edges are subdivided.

   Fan
      The quad is subdivided in a fan of four triangles,
      the common vertex being the one opposite to the selected edges.
   Inner Vertices
      The selected edges are subdivided, then an edge is created between
      the two new vertices, creating a small triangle.
      This edge is also subdivided,
      and the "inner vertex" thus created is linked by another edge to the one opposite
      to the original selected edges. All this results in a quad subdivided in a triangle and two quads.
   Path
      First an edge is created between the two opposite ends of the selected edges,
      dividing the quad in two triangles. Then, the same goes for the involved triangle as described above.
   Straight Cut
      The selected edges are subdivided, then an edge is created between
      the two new vertices, creating a small triangle and n-gon.

   .. list-table::

      * - .. figure:: /images/modeling_meshes_editing_edge_subdivide_two-edges-quad-fan2.png
             :width: 200px

             Fan cut type.

        - .. figure:: /images/modeling_meshes_editing_edge_subdivide_two-edges-quad-innervert.png
             :width: 200px

             Inner Vertices cut type.

        - .. figure:: /images/modeling_meshes_editing_edge_subdivide_two-edges-quad-path.png
             :width: 200px

             Path cut type.

Fractal
   Displaces the vertices in random directions after the mesh is subdivided.

   .. list-table::

      * - .. figure:: /images/modeling_meshes_editing_edge_subdivide_fractal-before.png
             :width: 200px

             Plane before subdivision.

        - .. figure:: /images/modeling_meshes_editing_edge_subdivide_fractal-none.png
             :width: 200px

             Regular subdivision.

        - .. figure:: /images/modeling_meshes_editing_edge_subdivide_fractal-after1.png
             :width: 200px

             Same mesh with fractal added.

Along Normal
   Causes the vertices to move along their normals, instead of random directions.

   .. figure:: /images/modeling_meshes_editing_edge_subdivide_fractal-along-normal.png
      :width: 200px

      Along normal set to 1.

Random Seed
   Changes the random seed of the *Fractal* noise function, producing a different result for each seed value.

   .. figure:: /images/modeling_meshes_editing_edge_subdivide_fractal-after2.png
      :width: 200px

      Same mesh with a different seed value.


Examples
========

Below are several examples illustrating the various possibilities of the *Subdivide*
and *Subdivide Multi* tools. Note the selection after subdivision.

.. figure:: /images/modeling_meshes_editing_edge_subdivide_before.png
   :width: 300px

   The sample mesh.


One Edge
--------

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_edge_subdivide_one-edge.png
          :width: 250px

          One Edge.

     - .. figure:: /images/modeling_meshes_editing_edge_subdivide_one-edge-tri.png
          :width: 250px

          Quad/Tri Mode.


Two Tri Edges
-------------

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_edge_subdivide_two-edges-tri.png
          :width: 250px

     - .. figure:: /images/modeling_meshes_editing_edge_subdivide_two-edges-tri-tri.png
          :width: 250px

          Quad/Tri Mode.


Two Opposite Quad Edges
-----------------------

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_edge_subdivide_two-edges-opposite.png
          :width: 250px

     - .. figure:: /images/modeling_meshes_editing_edge_subdivide_two-edges-opposite-tri.png
          :width: 250px

          Quad/Tri Mode.


Two Adjacent Quad Edges
-----------------------

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_edge_subdivide_two-edges-quad-fan2.png
          :width: 250px

          Fan cut type.

     - .. figure:: /images/modeling_meshes_editing_edge_subdivide_two-edges-quad-fan.png
          :width: 250px

          Quad/Tri Mode.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_edge_subdivide_two-edges-quad-innervert.png
          :width: 250px

          Inner vertices cut type.

     - .. figure:: /images/modeling_meshes_editing_edge_subdivide_two-edges-quad-innervert-tri.png
          :width: 250px

          Quad/Tri Mode.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_edge_subdivide_two-edges-quad-path.png
          :width: 250px

          Path cut type.

     - .. figure:: /images/modeling_meshes_editing_edge_subdivide_two-edges-quad-path-tri.png
          :width: 250px

          Quad/Tri Mode.


Three Edges
-----------

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_edge_subdivide_three-edges.png
          :width: 250px

     - .. figure:: /images/modeling_meshes_editing_edge_subdivide_three-edges-tri.png
          :width: 250px

          Quad/Tri Mode.


Tri
---

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_edge_subdivide_three-edges-tri2.png
          :width: 250px

     - .. figure:: /images/modeling_meshes_editing_edge_subdivide_three-edges-tri-tri.png
          :width: 250px

          Quad/Tri Mode.


Quad/Four Edges
---------------

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_edge_subdivide_four-edges.png
          :width: 250px

     - .. figure:: /images/modeling_meshes_editing_edge_subdivide_four-edges-tri.png
          :width: 250px

          Quad/Tri Mode.


Multiple Cuts
-------------

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_edge_subdivide_tri-multi.png
          :width: 250px

          Triangle with two cuts.

     - .. figure:: /images/modeling_meshes_editing_edge_subdivide_quad-multi.png
          :width: 250px

          Quad with two cuts.
