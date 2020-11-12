.. _bpy.types.CompositorNodeColorBalance:

******************
Color Balance Node
******************

The Color Balance node can adjust the color and values of an image.

.. figure:: /images/compositing_node-types_CompositorNodeColorBalance.png

   Color Balance Node.


Inputs
======

Factor
   Controls the amount of influence the node exerts on the output image.
Color
   Standard image input.


Properties
==========

Two different correction formulas could be selected.

Lift/Gamma/Gain
   Lift
      Increases the value of dark colors.
   Gamma
      Adjusts midtones.
   Gain
      Adjusts highlights.

Offset/Power/Slope (ASC-CDL)
   Offset
      Summand. (Adjusts the overall brightness.)

      Basis
         Additional offset, allows to specify a negative Offset value.
   Power
      Over-all exponent. (Adjusts the midtones.)
   Slope
      Multiplier. (Adjusts the highlights.)


Outputs
=======

Color
   Standard output image.


Advanced
========

The Offset/Power/Slope Formula
------------------------------

*out* = (*i* × *s* + *o*)\ :sup:`p`

where:

- *out*: The color graded pixel code value.
- *i*: The input pixel code value (0 to 1) (black to white).
- *s*: Slope (any number 0 or greater, nominal value is 1.0).
- *o*: Offset (any number, the nominal value is 0).
- *p*: Power (any number greater than 0, nominal value is 1.0).
