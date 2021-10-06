.. index:: Geometry Nodes; Triangulate
.. _bpy.types.GeometryNodeTriangulate:

****************
Triangulate Node
****************

.. figure:: /images/modeling_geometry-nodes_mesh_triangulate_node.png
   :align: right

   Triangulate Node.

The *Triangulate* node converts all faces in a mesh (quads and n-gons) to triangular faces.
It functions the same as the :ref:`Triangulate <bpy.ops.mesh.quads_convert_to_tris>` tool in Edit Mode.


Inputs
======

Geometry
   Standard geometry input.

Minimum Vertices
   Minimum number of vertices a face must have to be triangulated.
   For example, setting this value to 5, will prevent triangulation of :term:`Quads <Quad>`
   and only triangulate :term:`N-gons <N-gon>`.


Properties
==========

Quad Method
   :Beauty:
      Split the quads in nice triangles, slower method.
   :Fixed:
      Split the quads on their 1st and 3rd vertices.
   :Fixed Alternate:
      Split the quads on their 2nd and 4th vertices.
   :Shortest Diagonal:
      Split the quads based on the diagonal distance between their vertices.

N-gon Method
   :Beauty:
      Arrange the new triangles nicely, slower method.
   :Clip:
      Split n-gons using an ear-clipping algorithm
      (gives similar results to the tessellation used for the viewport rendering).


Outputs
=======

Geometry
   Standard geometry output.


Example
=======

.. list-table::

   * - .. figure:: /images/modeling_modifiers_generate_triangulate_before.png
          :width: 320px

          Mesh before triangulation.

     - .. figure:: /images/modeling_modifiers_generate_triangulate_after.png
          :width: 320px

          Mesh after triangulation.
