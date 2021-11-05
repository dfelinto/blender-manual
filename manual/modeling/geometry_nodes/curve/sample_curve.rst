.. index:: Geometry Nodes; Sample Curve
.. _bpy.types.GeometryNodeSampleCurve:

*****************
Sample Curve Node
*****************

.. figure:: /images/modeling_geometry-nodes_curve_sample-curve_node.png
   :align: right

   Sample Curve node.

The *Sample Curve* calculates a point on a curve at a certain distance from the start of the curve,
specified by the length or factor inputs. It also outputs data retrieved from that position on the curve.
The sampled values are linearly interpolated from the values at the evaluated curve points
at each side of the sampled point.

.. note::

   When the curve contains multiple splines, the sample position is found based on the total accumulated length,
   including the lengths of all previous splines. The order of the splines is the same order as
   displayed in the :doc:`Spreadsheet Editor </editors/spreadsheet>`.


Inputs
======

Curve
   Standard geometry input with a curve component.

Factor
   The portion of the total length used to determine the sample position.

Length
   A length in distance units used to determine how far along the curve to travel before sampling.


Properties
==========

Mode
   How to find endpoint positions for the trimmed spline.
   The option acts the same as it does in the :doc:`/modeling/geometry_nodes/curve/curve_tilt`.

   :Factor:
      Find the endpoint positions using a factor of each spline's length.
      The input values should be between 0 or 1.
   :Length:
      Find the endpoint positions using a length from the start of each spline.
      The input values should be between 0 and the length of the splines.


Outputs
=======

Position
   The position at the sample along the spline.

Tangent
   The normalized :doc:`curve tangent </modeling/geometry_nodes/curve/curve_tangent>` at the sample.

   .. tip::

      This output can be combined with the :doc:`/modeling/geometry_nodes/utilities/align_euler_to_vector`
      to create a rotation that lines up with direction of the curve. Including the *Normal* output
      in a second align node after can align the other rotation axis.

Normal
   The normalized :doc:`curve normal </modeling/geometry_nodes/input/normal>` at the sample.


Examples
========

.. figure:: /images/modeling_geometry-nodes_curve_sample-curve_example.png
   :align: center

Here, the *Count* mode of the :doc:`/modeling/geometry_nodes/curve/resample_curve` is recreated,
except a mesh is used for the result instead of a curve. The Z axis of the position can be used
as the sample factor because the position is between zero and one for the entire line.
