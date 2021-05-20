.. index:: Geometry Nodes; Curve to Mesh
.. _bpy.types.GeometryNodeCurveToMesh:

*************
Curve to Mesh
*************

.. figure:: /images/modeling_geometry-nodes_curve_curve-to-mesh_node.png
   :align: center

   The Curve to Mesh node.

The Curve to Mesh node converts all splines of a curve to a mesh.
Optionally, a profile curve can be provided to give the curve a custom shape.

.. tip::

   The output mesh has auto smooth set and sharp edges from the profile curve tagged automatically.
   If any splines in the profile curve are Bezier splines and any of the control points use *Free* or
   *Vector* handles, the corresponding edges will be shaded sharp.


Inputs
======

Curve
   Standard geometry input.
   All non-curve components are ignored.

Profile Curve
   If a profile curve is provided, it will be extruded along all splines.
   Otherwise the generated mesh will just be a chain of edges.


Properties
==========

This node has no properties.


Outputs
=======

Mesh
   Standard geometry output.
