.. index:: Geometry Nodes; Set Handle Type
.. _bpy.types.GeometryNodeCurveSetHandles:

********************
Set Handle Type Node
********************

.. figure:: /images/modeling_geometry-nodes_curve_set-handles_node.png
   :align: right

   The Set Handle Type node.

Sets the handle type for the points on the Bézier curve that are in the selection.

The handle type of each control point can be retrueved with with the 
:doc:`/modeling/geometry_nodes/curve/set_handle_type`.

Inputs
======

Curve
   Bézier curve.

Selection
   The points whose handle types will be changed.


Properties
==========

Mode
   Whether to update left or right or both handles.
   When both are selected, both the left and the right
   handles will be updated.

   :Left:
      Update the left handles.
   :Right:
      Update the right handles.

Handle Type
   The handle type to switch to. See the :ref:`Bézier curves <curve-bezier-handle-type>`
   page for more details on the different handle types.


Outputs
=======

Curve
   Standard curve output.
