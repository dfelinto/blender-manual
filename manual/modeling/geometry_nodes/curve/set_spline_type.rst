.. index:: Geometry Nodes; Set Spline Type
.. _bpy.types.GeometryNodeCurveSplineType:

********************
Set Spline Type Node
********************

.. figure:: /images/modeling_geometry-nodes_curve_spline-type_node.png
   :align: right

   The Set Spline Type node.

Sets the spline type for the splines in the curve component that
are in the selection.


Inputs
======

Curve
   Standard geometry input with a curve component.

Selection
   The splines whose spline types will be changed.


Properties
==========

Spline Type
   The type to convert the splines in the selection to.
   Read the :ref:`Spline Types <curve-spline-types>` page for more details
   on the different spline types.

   :Bézier:
      Convert to a Bézier spline.

      .. note::

         When converting from a NURBS spline to a Bézier spline,
         at least six points are needed.
         When the number of points is not a multiple of three
         a full conversion is not possible and the spline has to be truncated.
   :NURBS:
      Convert to a NURBS spline.
   :Poly:
      Convert to a poly spline.


Outputs
=======

Curve
   Standard curve output.
