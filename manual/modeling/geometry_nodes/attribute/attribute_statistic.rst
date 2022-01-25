.. index:: Geometry Nodes; Attribute Statistic
.. _bpy.types.GeometryNodeAttributeStatistic:

************************
Attribute Statistic Node
************************

.. figure:: /images/modeling_geometry-nodes_attribute_attribute-statistic_node.png
   :align: right

   The Attribute Statistic node.

The *Attribute Statistic* node evaluates a field on a geometry and outputs a statistic about the entire data set.


Inputs
======

Geometry
   Standard geometry input.

Attribute
   The attribute field to query a statistic from.

Selection
   A boolean field input for each element indicating whether to include its value in the statistics result
   If the boolean is false, the corresponding value from the *Attribute* input will be ignored.


Properties
==========

Data Type
   :Float:
      The output will be a single floating-point value.
   :Vector:
      The output will be a vector of three floating-point values.
      All calculations are elementwise.

Domain
   :Spline: Data is queried from each spline.
   :Face Corner: Data is queried from each face corner.
   :Corner: Data is queried from each face corner.
   :Edge: Data is queried from each edge.
   :Point: Data is queried from each point.


Outputs
=======

Mean
   The average value of all data.

Median
   The median value of all data.

Sum
   The sum value of all data.

Min
   The min value of all data.

Max
   The max value of all data.

Range
   The difference between the max and min value.

Standard Deviation
   How much values differ from the mean.
   A low standard deviation indicates that the values are grouped tightly together at the mean.
   A high standard deviation indicates that the values are spread out over a large range.

Variance
   The variance of all data, defined as the square of the standard deviation.
