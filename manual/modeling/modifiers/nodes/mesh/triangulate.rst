.. index:: Nodes; Mesh; Triangulate
.. _bpy.types.GeometryNodeTriangulate:

***********
Triangulate
***********

The *Triangulate* node converts all faces in a mesh (quads and polygons) to triangular faces.
It fulfills the exact same function as the :ref:`Triangulate <bpy.ops.mesh.quads_convert_to_tris>` tool in Edit Mode.

.. list-table::

   * - .. figure:: /images/modeling_modifiers_generate_triangulate_before.png
          :width: 320px

          Mesh before Triangulate modifier.

     - .. figure:: /images/modeling_modifiers_generate_triangulate_after.png
          :width: 320px

          Mesh after Triangulate modifier.


Options
=======

.. figure:: /images/modeling_modifiers_nodes_triangulate.png
   :align: right

   Triangulate Node.

Quad Method
   Beauty
      Split the quads in nice triangles, slower method.
   Fixed
      Split the quads on their 1st and 3rd vertices.
   Fixed Alternate
      Split the quads on their 2nd and 4th vertices.
   Shortest Diagonal
      Split the quads based on the diagonal distance between their vertices.

Polygon Method
   Beauty
      Arrange the new triangles nicely, slower method.
   Clip
      Split the polygons using an ear-clipping algorithm
      (gives similar results to the tessellation used for the viewport rendering).

Inputs
======

Geometry
   Source geometry to triangulate.

Minimum Vertices
   Minimum number of vertices a face must have to be triangulated.
   For example, setting this value to 5, will prevent triangulation of :term:`Quads <Quad>`
   and only triangulate :term:`N-gons <N-gon>`.


Outputs
=======

Geometry
   The triangulated geometry.
