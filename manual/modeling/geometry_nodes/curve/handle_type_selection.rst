.. index:: Geometry Nodes; Handle Type Selection
.. _bpy.types.GeometryNodeCurveHandleTypeSelection:

**************************
Handle Type Selection Node
**************************

.. figure:: /images/modeling_geometry-nodes_curve_handle-type-selection_node.png
   :align: center

   The Handle Type Selection node.

Creates a selection based on the handle types of the control points.


Inputs
======

This node has no inputs.


Properties
==========

Mode
   Whether to consider left and/or right handles.
   When both are selected, the outputted value is true
   if either of the handles are of the chosen type.

   :Left:
      Consider the left handle.
   :Right:
      Consider the right handle.

Handle Type
   Handle type for which the selection will be true.
   Read the :ref:`Bézier curves <curve-bezier-handle-type>` page for more details
   on the different handle types.


Outputs
=======

Selection
   Boolean field set to true wherever the handle type matches.
