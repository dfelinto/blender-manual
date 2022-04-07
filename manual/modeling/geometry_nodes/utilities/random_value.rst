.. index:: Geometry Nodes; Random Value
.. _bpy.types.FunctionNodeRandomValue:

*****************
Random Value Node
*****************

.. figure:: /images/node-types_FunctionNodeRandomValue.webp
   :align: right
   :alt: Random Value node.

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
   An ID to drive the random number generator seed. By default, this input uses the same value
   as of the :doc:`/modeling/geometry_nodes/input/id`, which is the ``id`` attribute of the context
   geometry if it exists, and otherwise the :doc:`index </modeling/geometry_nodes/input/input_index>`.

Seed
   A field to :term:`Seed` the random number generator. This can be used to generate
   a different set of random values, even for two nodes with the same *ID* input.


Properties
==========

Data Type
   :Float: The output will be a *Float* field.
   :Integer: The output will be an *Integer* field.
   :Vector: The output will be a *Vector* field.
   :Boolean: The output will be a *Boolean* field.


Outputs
=======

Value
   Random values as a field.
