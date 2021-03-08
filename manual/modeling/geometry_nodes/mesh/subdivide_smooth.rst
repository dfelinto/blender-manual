.. index:: Geometry Nodes; Subdivision Smooth
.. _bpy.types.GeometryNodeSubdivisionSmooth:

****************
Subdivide Smooth
****************

.. figure:: /images/modeling_modifiers_nodes_subdivide-smooth.png
   :align: right

   The Subdivide Node.

The *Subdivide Smooth* node adds new faces to mesh geometry using a Catmull-Clark subdivision method.


Inputs
======

Geometry
   Standard geometry input.

Level
   The number of subdivisions to apply to the input geometry.
Creases
   Control how smooth edges should be with :ref:`modifiers-generate-subsurf-creases`.
Boundary Smooth
   Controls if open boundaries and corners are smooth.
Smooth UVs
   Controls if subdivision smooth is applied to UVs.

Outputs
=======

Geometry
   Standard geometry output.
