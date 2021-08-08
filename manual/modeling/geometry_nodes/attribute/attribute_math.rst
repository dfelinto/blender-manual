.. index:: Geometry Nodes; Attribute Math
.. _bpy.types.GeometryNodeAttributeMath:

**************
Attribute Math
**************

Modify an attribute with a math operation.

.. figure:: /images/modeling_geometry-nodes_attribute_attribute-math_node.png
   :align: right

   The Attribute Math Node.


Inputs
======

Geometry
   Standard geometry input.

A, B, C
   The first and second input to the math operation.
   This is either an attribute name or numeric value.

Result
   Name of the attribute where the computed result is stored.
   A new attribute with that name is added if it does not exist yet.
   If it does exist, the values of the existing attribute are overridden.


Properties
==========

Operation
   The mathematical operator to be applied to the input values:

   Functions
      :Add: The sum of the two values.
      :Subtract: The difference between the two values.
      :Multiply: The product of the two values.
      :Divide: The division of the first value by the second value.
      :Multiply Add: The sum of the product of the two values with *Addend*.
      :Power: The *Base* raised to the power of *Exponent*.
      :Logarithm: The log of the value with a *Base* as its base.
      :Square Root: The square root of the value.
      :Inverse Square Root: One divided by the square root of the value.
      :Absolute:
         The input value is read without regard to its sign.
         This turns negative values into positive values.
      :Exponent:
         Raises `Euler's number <https://en.wikipedia.org/wiki/E_(mathematical_constant)>`__
         to the power of the value.

   Comparison
      :Minimum: Outputs the smallest of the input values.
      :Maximum: Outputs the largest of two input values.
      :Less Than:
         Outputs 1.0 if the first value is smaller than the second value. Otherwise the output is 0.0.
      :Greater Than:
         Outputs 1.0 if the first value is larger than the second value. Otherwise the output is 0.0.
      :Sign:
         Extracts the sign of the input value. All positive numbers
         will output 1.0. All negative numbers will output -1.0. And 0.0 will output 0.0.
      :Compare: Outputs 1.0 if the difference between the two input values is less than or equal to *Epsilon*.
      :Smooth Minimum: `Smooth Minimum <https://en.wikipedia.org/wiki/Smooth_maximum>`__.
      :Smooth Maximum: `Smooth Maximum <https://en.wikipedia.org/wiki/Smooth_maximum>`__.

   Rounding
      :Round: Rounds the input value to the nearest integer.
      :Floor: Rounds the input value down to the nearest integer.
      :Ceil: Rounds the input value up to the nearest integer.
      :Truncate: Outputs the integer part of the *value*.
      :Fraction: `Fraction <https://en.wikipedia.org/wiki/Rational_function>`__.
      :Modulo: Outputs the remainder once the first value is divided by the second value.
      :Wrap:
         Outputs a value between *Min* and *Max* based on the absolute difference between
         the input value and the nearest integer multiple of *Max* less than the value.
      :Snap: Rounds the input value down to the nearest integer multiple of *Increment*.
      :Ping-pong: The output value is moved between 0.0 and the *Scale* based on the input value.

   Trigonometric
      :Sine:
         The `Sine <https://en.wikipedia.org/wiki/Sine>`__ of the input value.
      :Cosine:
         The `Cosine <https://en.wikipedia.org/wiki/Trigonometric_functions>`__ of the input value.
      :Tangent:
         The `Tangent <https://en.wikipedia.org/wiki/Trigonometric_functions>`__ of the input value.
      :Arcsine:
         The `Arcsine <https://en.wikipedia.org/wiki/Inverse_trigonometric_functions>`__ of the input value.
      :Arccosine:
         The `Arccosine <https://en.wikipedia.org/wiki/Inverse_trigonometric_functions>`__ of the input value.
      :Arctangent:
         The `Arctangent <https://en.wikipedia.org/wiki/Inverse_trigonometric_functions>`__ of the input value.
      :Arctan2:
         Outputs the `Inverse Tangent <https://en.wikipedia.org/wiki/Inverse_trigonometric_functions>`__
         of the first value divided by the second value measured in radians.
      :Hyperbolic Sine:
         The `Hyperbolic Sine <https://en.wikipedia.org/wiki/Hyperbolic_functions>`__ of the input value.
      :Hyperbolic Cosine:
         The `Hyperbolic Cosine <https://en.wikipedia.org/wiki/Hyperbolic_functions>`__ of the input value.
      :Hyperbolic Tangent:
         The `Hyperbolic Tangent <https://en.wikipedia.org/wiki/Hyperbolic_functions>`__ of the input value.

   Conversion
      :To Radians: Converts the input from degrees to radians.
      :To Degrees: Converts the input from radians to degrees.

   .. note::

      Attributes are converted implicitly to the float data type.

A, B, C
   :Attribute: The input is a text field that expects an attribute name.
   :Float: The input is a number field.


Output
======

Geometry
   Standard geometry output.
