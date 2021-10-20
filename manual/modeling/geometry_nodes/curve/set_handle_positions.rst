.. index:: Geometry Nodes; Set Handle Positions
.. _bpy.types.GeometryNodeSetCurveHandlePositions:

*************************
Set Handle Positions Node
*************************

.. figure:: /images/modeling_geometry-nodes_curve_set-handle-positions_node.png
   :align: right

   Set Handle Positions node.

The *Set Handle Positions* node sets the positions for the handles of :ref:`Bézier curves <curve-bezier>`.
They can be used to alter the generated shape of the curve.
The input node for this data is the :doc:`/modeling/geometry_nodes/curve/curve_handle_position`.
See the :ref:`Bézier curves <curve-bezier-handle-type>` page for more details.

.. note::

   When the position is changed, *Auto* handle types will be converted to *Aligned*, and *Vector* handle
   types will be converted to *Free*.

.. note::

   The left and right handles cannot be changed at the same time with this node. That is because it would
   break the alignment for left and right handles at the same control point.


Inputs
======

Geometry
   Standard geometry input, containing a curve.

Selection
   Whether or not to change the handle position on each control point.
   True values mean the resolution will be changed, false values mean
   the resolution will remain the same.

Position
   The new handle position.

.. note::

   The handle positions are the global position of the handle, they are not relative to
   the position of the corresponding control point.


Properties
==========

Left / Right
   Whether to set the handle position of the left or right handle.
   The *Left* handle is closer to the start of the spline, and the *Right* handle is closer to the end.


Outputs
=======

Geometry
   Standard geometry output.
