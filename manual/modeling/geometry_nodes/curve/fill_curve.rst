.. index:: Geometry Nodes; Fill Curve
.. _bpy.types.GeometryNodeFillCurve:

***************
Fill Curve Node
***************

.. figure:: /images/modeling_geometry-nodes_curve_curve-fill_node.png
   :align: center

   The Fill Curve node.

The *Fill Curve* node generates a mesh using the constrained Delaunay triangulation algorithm
with the curves as boundaries. The mesh is only generated flat with a local Z of 0.


Inputs
======

Curve
   Standard geometry input with a curve component.


Properties
==========

Mode
   The type of geometry the output consists of.

   :Triangles:
      The output is made up of triangles.
   :N-gons:
      The output is made up of n-gons.


Outputs
=======

Mesh
   The filled in curves.
