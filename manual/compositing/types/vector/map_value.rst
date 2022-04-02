.. _bpy.types.CompositorNodeMapValue:

**************
Map Value Node
**************

.. figure:: /images/compositing_node-types_CompositorNodeMapValue.webp
   :align: right
   :alt: Map Value Node.

   Map Value Node.

Map Value node is used to scale, offset and clamp values.


Inputs
======

Value
   Standard Value input. (Value refers to each vector in the set.)


Properties
==========

Offset
   Factor added to the input value.
Size
   Scales (multiply) the input value.
Use Minimum, Maximum
   Enable this to activate their related operation.
Min, Max
   Defines a range between minimum and maximum to :term:`Clamp` the input value to.


Outputs
=======

Value
   Standard value output.


Example
=======

Z-Depth Map
-----------

This is particularly useful in achieving a depth of field effect,
where the Map Value node is used to map a Z value
(which can be 20 or 30 or even 500 depending on the scene) to the range between (0 to 1),
suitable for connecting to a Blur node.


Multiplying Values
------------------

The Map Value node can also be used to multiply values to achieve a desired output value.
In the mini-map to the right, the Time node outputs a value between 0.0 and 1.0 evenly scaled over 30 frames.
The *first* Map Value node multiplies the input by 2,
resulting in an output value that scales from 0.0 to 2.0 over 30 frames.
The *second* Map Value node subtracts 1 from the input,
giving working values between (-1.00 to 1.0), and multiplies that by 150,
resulting in an output value between (-150 to 150) over a 30-frame sequence.

.. figure:: /images/compositing_types_vector_map-value_example.png

   Using Map Value to multiply.
