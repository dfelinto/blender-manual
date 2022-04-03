.. index:: Geometry Nodes; Curve to Mesh
.. _bpy.types.GeometryNodeCurveToMesh:

******************
Curve to Mesh Node
******************

.. figure:: /images/node-types_GeometryNodeCurveToMesh.webp
   :align: center
   :alt: The Curve to Mesh node.

   The Curve to Mesh node.

The Curve to Mesh node converts all splines of a curve to a mesh.
Optionally, a profile curve can be provided to give the curve a custom shape.

The node transfers attributes to the result. Attributes that are built-in on meshes but not curves,
like ``shade_smooth``, will be transferred to the correct domain as well.

.. tip::

   The output mesh has :ref:`auto smooth <auto-smooth>` set
   and :ref:`sharp edges <modeling_meshes_normals_sharp_edge>` from
   the profile curve tagged automatically. If any splines in the profile curve
   are Bézier splines and any of the control points use *Free* or *Vector* handles,
   the corresponding edges will be shaded sharp.


Inputs
======

Curve
   Standard geometry input.
   All non-curve components are ignored.

Profile Curve
   If a profile curve is provided, it will be extruded along all splines.
   Otherwise the generated mesh will just be a chain of edges.

Fill Caps
   If the profile spline is cyclic, fill the ends of the generated mesh with n-gons.
   The resulting mesh is :term:`Manifold`, the two new faces for each spline are
   simply connected to existing edges.


Properties
==========

This node has no properties.


Outputs
=======

Mesh
   Standard geometry output.
