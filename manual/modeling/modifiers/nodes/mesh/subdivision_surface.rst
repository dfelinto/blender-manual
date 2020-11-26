.. index:: Nodes; Mesh; Subdivision Surface
.. _bpy.types.GeometryNodeSubdivisionSurface:

*******************
Subdivision Surface
*******************

The *Subdivision Surface* node deform the geometry using Catmull-Clark
deformation.

.. figure:: /images/modeling_modifiers_nodes_subdivision-surface.png
   :align: right

   Subdivision Surface Node.

Inputs
======

Geometry
   Source geometry to sub-divide.
Level
   To which degree the geometry will be deformed.
Creases
   Control how smooth edges should be with :ref:`modifiers-generate-subsurf-creases`.
Boundary Smooth
  Controls if open boundaries and corners are smooth.
Smooth UVs
  Controls if subdivision smooth is apllied to UVs.


Outputs
=======

Geometry
   The subdivided geometry.
