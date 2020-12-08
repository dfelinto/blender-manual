.. index:: Nodes; Mesh; Subdivision Surface
.. _bpy.types.GeometryNodeSubdivisionSurface:

*******************
Subdivision Surface
*******************

.. figure:: /images/modeling_modifiers_nodes_subdivision-surface.png
   :align: right

   Subdivision Surface Node.

The *Subdivision Surface* node deform the geometry using Catmull-Clark deformation.


Inputs
======

Geometry
   Standard geometry input.

Level
   To which degree the geometry will be deformed.
Creases
   Control how smooth edges should be with :ref:`modifiers-generate-subsurf-creases`.
Boundary Smooth
   Controls if open boundaries and corners are smooth.
Smooth UVs
   Controls if subdivision smooth is applied to UVs.


Properties
==========

This node has no properties.


Outputs
=======

Geometry
   Standard geometry output.
