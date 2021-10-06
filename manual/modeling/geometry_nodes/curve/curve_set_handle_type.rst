.. index:: Geometry Nodes; Curve Set Handle Type
.. _bpy.types.GeometryNodeCurveSetHandles:

**************************
Curve Set Handle Type Node
**************************

.. figure:: /images/modeling_geometry-nodes_curve_set-handles_node.png
   :align: right

   The Curve Set Handle Type node.

Sets the handle type for the points on the Bézier curve that
are in the selection. 

Inputs
======

Curve
   Bézier curve.

Selection
   The points whose handle types will be changed.


Properties
==========

Mode
   Whether to update left and/or right handles.

   :Left:
      Update the left handles
   :Right:
      Update the right handles

Handle type
   The handle type to switch to.
   Read the :ref:`Bézier curves <curve-bezier-handle-type>` page for more details
   on the different handle types.


Outputs
=======

Curve
   The curve with the updated handle types.


