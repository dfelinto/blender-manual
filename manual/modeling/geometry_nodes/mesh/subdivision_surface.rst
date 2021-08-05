.. index:: Geometry Nodes; Subdivision Surface
.. _bpy.types.GeometryNodeSubdivisionSurface:

*******************
Subdivision Surface
*******************

.. figure:: /images/modeling_geometry-nodes_mesh_subdivision-surface_node.png
   :align: right

   The Subdivision Surface Node.

The *Subdivision Surface* node adds new faces to mesh geometry using a Catmull-Clark subdivision method.


Inputs
======

Geometry
   Standard geometry input.

Level
   The number of subdivisions to apply to the input geometry.
Use Creases
   Controls how smooth edges should be with :ref:`modifiers-generate-subsurf-creases`.
Boundary Smooth
   Controls if open boundaries and corners are smooth.
Smooth UVs
   Controls if whether smoothing is applied to UVs.


Properties
==========

This node has no properties.


Outputs
=======

Geometry
   Standard geometry output.
