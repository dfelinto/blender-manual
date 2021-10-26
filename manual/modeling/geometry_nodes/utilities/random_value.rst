.. index:: Geometry Nodes; Random Value
.. _bpy.types.GeometryNodeRandomValue:

*****************
Random Value Node
*****************

.. figure:: /images/modeling_geometry-nodes_utilities_random-value_node.png
   :align: right

   Random Value Node

The *Random Value* node outputs a white noise like value as a *Float*, *Integer*, *Vector*, or *Boolean* field.


Inputs
======

Min
   The minimum value of the range where random values are sampled from.
   This input is only available for *Float*, *Integer*, and *Vector* types.
 
Max
   The maximum value of the range where random values are sampled from.
   This input is only available for *Float*, *Integer*, and *Vector* types.
 
Probability
   The probability ratio for the random *Boolean* output to be *True*.
   This input is only available for *Boolean* types.

ID
   An ID to drive the random number generator seed.

Seed
   A field to seed the random number generator.


Properties
==========

Data Type
   :Float: The output will be a *Float* field.
   :Integer: The output will be a *Integer* field.
   :Vector: The output will be a *Vector* field.
   :Boolean: The output will be a *Boolean* field.


Outputs
=======

Value
   Random values as a field.
