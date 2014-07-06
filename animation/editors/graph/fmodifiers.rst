
..    TODO/Review: {{review|im=examples}} .


F-Curve Modifiers
*****************

F-Curve modifiers are similar to object modifiers, in that they add non-destructive effects,
that can be adjusted at any time, and layered to create more complex effects.


Adding a Modifier
=================

The F-curve modifier panel is located in the Properties panel.
Select a curve by selecting one of its curve points, or by selecting the channel list.
Click on the :kbd:`Add Modifier` button and select a modifier.

To add spin to an object or group, select the object/group and add a keyframe to
the axis of rotation (x,y, or z)

Go to the Graph Editor.....make sure the f-curves properties panel is visible
(View > Properties)

>Add Modifier > (e.g.) Generator


Types of Modifiers
==================

Generator
---------

Generator creates a Factorized or Expanded Polynomial function.
These are basic mathematical formulas that represent lines, parabolas,
and other more complex curves, depending on the values used.

:guilabel:`Additive`
   This option causes the modifier to be added to the curve, instead of replacing it by default.
:guilabel:`Poly Order`
   Specify the order of the polynomial, or the highest power of 'x' for this polynomial. (number of coefficients - 1).

Change the Coefficient values to change the shape of the curve. See
FIXME(Link Type Unsupported: http;
[[http://en.wikipedia.org/wiki/Polynomial The Wikipedia Page]]
) for more information on polynomials.


Built-in Function
-----------------

These are additional formulas, each with the same options to control their shape.
Consult mathematics reference for more detailed information on each function.

- Sine
- Cosine
- Tangent
- Square Root
- Natural Logarithm
- Normalized Sine (sin(x)/x)

:guilabel:`Amplitude`
   Adjusts the Y scaling
:guilabel:`Phase Multiplier`
   Adjusts the X scaling
:guilabel:`Phase Offset`
   Adjusts the X offset
:guilabel:`Value Offset`
   Adjusts the Y offset


Envelope
--------

Allows you to adjust the overall shape of a curve with control points.

:guilabel:`Reference Value`
   Set the Y value the envelope is centered around.
:guilabel:`Min`
   Lower distance from Reference Value for 1:1 default influence.
:guilabel:`Max`
   Upper distance from Reference Value for 1:1 default influence.

:guilabel:`Add Point`
   Add a set of control points. They will be created at the current frame.
:guilabel:`Fra:`
   Set the frame number for the control point.
:guilabel:`Min`
   Specifies the lower control point's position.
:guilabel:`Max`
   specifies the upper control point's position.


Cycles
------

Cycles allows you add cyclic motion to a curve that has 2 or more control points.
The options can be set for before and after the curve.

:guilabel:`Cycle Mode`
   :guilabel:`Repeat Motion`
      Repeats the curve data, while maintaining their values each cycle.
   :guilabel:`Repeat with Offset`
      Repeats the curve data, but offsets the value of the first point to the value of the last point each cycle.
   :guilabel:`Repeat Mirrored`
      Each cycle the curve data is flipped across the X-axis.

:guilabel:`Before/After Cycles`
   Set the number of times to cycle the data. A value of 0 cycles the data infinitely.


Noise
-----

Modifies the curve with a noise formula.
This is useful for creating subtle or extreme randomness to animated movements,
like camera shake.

:guilabel:`Blend Type`
   :guilabel:`Replace`
      Adds a -.5 to .5 range noise function to the curve.
   :guilabel:`Add`
      Adds a 0 to 1 range noise function to the curve.
   :guilabel:`Subtract`
      Subtracts a 0 to 1 range noise function to the curve.
   :guilabel:`Multiply`
      Multiplies a 0 to 1 range noise function to the curve.

:guilabel:`Scale`
   Adjust the overall size of the noise. Values further from 0 give less frequent noise.
:guilabel:`Strength`
   Adjusts the Y scaling of the noise function.
:guilabel:`Phase`
   Adjusts the random seed of the noise.
:guilabel:`Depth`
   Adjusts how detailed the noise function is.


Python
------

Limits
------

Limit curve values to specified X and Y ranges.

:guilabel:`Minimum/Maximum X`
   Cuts a curve off at these frames ranges, and sets their minimum value at those points.
:guilabel:`Minimum/Maximum Y`
   Truncates the curve values to a range.


Stepped
-------

Gives the curve a stepped appearance by rounding values down within a certain range of frames.

:guilabel:`Step Size`
   Specify the number of frames to hold each frame
:guilabel:`Offset`
   Reference number of frames before frames get held. Use to get hold for '1-3' vs '5-7' holding patterns.
:guilabel:`Use Start Frame`
   Restrict modifier to only act before its 'end' frame
:guilabel:`Use End Frame`
   Restrict modifier to only act after its 'start' frame

