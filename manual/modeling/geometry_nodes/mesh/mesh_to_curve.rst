.. index:: Geometry Nodes; Mesh to Curve
.. _bpy.types.GeometryNodeMeshToCurve:

******************
Mesh to Curve Node
******************

.. figure:: /images/node-types_GeometryNodeMeshToCurve.webp
   :align: right
   :alt: Mesh to Curve node.

The *Mesh to Curve* node generates a curve from a mesh.
The result is a poly spline, with a point for every selected vertex on the mesh.
Any intersection of more than two selected edges will cause a break in the spline.
Meaning that if a the mesh has grid-like topology and
a continuous spline is desired, the *Selection* input is very important.

Attributes will be transferred to the resulting curve, including named attributes.
If the mesh has attributes with the names of built-in curve attributes like ``radius`` and ``cyclic``,
they will be copied as well.


Inputs
======

Mesh
   Standard mesh input.

Selection
   A field input evaluated on the edge domain to determine whether each edge will be included in the result.

   .. tip::

      Using this input is more efficient than deleting parts of the geometry before or after the conversion.


Properties
==========

This node has no properties.


Outputs
=======

Curve
   Generated curve.
