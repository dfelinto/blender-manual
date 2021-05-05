.. index:: Modifiers; F-Curve Modifiers
.. index:: F-Curve Modifiers

.. _bpy.types.FCurveModifiers:
.. _bpy.types.FModifier:

*****************
F-Curve Modifiers
*****************

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Sidebar region --> Modifiers --> Modifiers`

F-Curve modifiers are similar to object modifiers, in that they add non-destructive effects,
that can be adjusted at any time, and layered to create more complex effects.
Like object modifiers, F-curve modifiers are evaluated from the top down.
In other words, the top modifier is calculated first and consequent modifiers are calculated in order.
Modifiers can be moved by dragging the modifier box from the top right.

Modifiers can be muted or hidden by toggling the checkbox in the modifier's panel header.
They can be removed using the delete button in the modifier's panel header.


Adding a Modifier
=================

.. figure:: /images/editors_graph-editor_fcurves_sidebar_modifiers_panel.png

   Modifiers panel.

The F-curve modifier panel is located in the Sidebar region.
Select a curve by selecting one of its curve points, or by selecting the channel list.
Click on the *Add Modifier* menu to select a modifier.


Types of Modifiers
==================

.. index:: F-Curve Modifiers; Generator Modifier
.. _bpy.types.FModifierGenerator:

Generator Modifier
------------------

Generator creates a polynomial function.
These are basic mathematical formulas that represent lines, parabolas,
and other more complex curves, depending on the values used.

Mode
   Method used to represent the equation.

   :Expanded Polynomial:   Equation in the form :math:`y = x^1 + x^2 + ... + x^n`.
   :Factorized Polynomial: Equation in the form :math:`y = (Ax + B)(Cx + D)`.

Additive
   This option causes the modifier to be added to the curve, instead of replacing it by default.

Order
   Specify the order of the polynomial, or the highest power of ``X`` for this polynomial.
   (Number of coefficients: 1.)

   Change the Coefficient values to change the shape of the curve.

   .. seealso::

      `The Wikipedia Page <https://en.wikipedia.org/wiki/Polynomial>`__
      for more information on polynomials.

Influence
   Controls the percentage of affect the modifier has on the F-curve.


Restrict Frame Range
^^^^^^^^^^^^^^^^^^^^

Start/End
   The frame the modifier's affect starts/ends.
Blend In, Out
   The number of frames, relative the start/end values above, the modifier takes to fade in/out.


.. index:: F-Curve Modifiers; Built-in Function Modifier
.. _bpy.types.FModifierFunctionGenerator:

Built-in Function Modifier
--------------------------

These are additional formulas, each with the same options to control their shape.
Consult mathematics reference for more detailed information on each function:

Type
   The built-in function to use.

   :Sine: `Sine <https://en.wikipedia.org/wiki/Sine>`__.
   :Cosine: `Cosine <https://en.wikipedia.org/wiki/Trigonometric_functions>`__.
   :Tangent: `Tangent <https://en.wikipedia.org/wiki/Trigonometric_functions>`__.
   :Square Root: The square root of the value.
   :Natural Logarithm: The natural log of the value.
   :Normalized Sine: :math:`sin(x)/x`.

Additive
   This option causes the modifier to be added to the curve, instead of replacing it by default.

Amplitude
   Adjusts the Y scaling.
Phase Multiplier
   Adjusts the X scaling.
Phase Offset
   Adjusts the X offset.
Value Offset
   Adjusts the Y offset.

Influence
   Controls the percentage of affect the modifier has on the F-curve.


Restrict Frame Range
^^^^^^^^^^^^^^^^^^^^

Start/End
   The frame the modifier's affect starts/ends.
Blend In, Out
   The number of frames, relative the start/end values above, the modifier takes to fade in/out.


.. index:: F-Curve Modifiers; Envelope Modifier
.. _bpy.types.FModifierEnvelope:
.. _bpy.types.FModifierEnvelopeControlPoint:

Envelope Modifier
-----------------

Allows you to adjust the overall shape of a curve with control points.

Reference
   Set the Y value the envelope is centered around.
Min
   Lower distance from Reference Value for ``1:1`` default influence.
Max
   Upper distance from Reference Value for ``1:1`` default influence.

Add Control Point
   Add a set of control points. They will be created at the current frame.

Point
   Frame
      Set the frame number for the control point.
   Min
      Specifies the lower control point's position.
   Max
      Specifies the upper control point's position.

Influence
   Controls the percentage of affect the modifier has on the F-curve.


Restrict Frame Range
^^^^^^^^^^^^^^^^^^^^

Start/End
   The frame the modifier's affect starts/ends.
Blend In, Out
   The number of frames, relative the start/end values above, the modifier takes to fade in/out.


.. index:: F-Curve Modifiers; Cycles Modifier
.. _bpy.types.FModifierCycles:

Cycles Modifier
---------------

Cycles allows you add cyclic motion to a curve that has two or more control points.
The options can be set for before and after the curve.

.. note::

   The Cycles Modifier can only be the first modifier.

Before/After Mode
   :No Cycles: Do not repeat curve data before/after.
   :Repeat Motion:
      Repeats the curve data, while maintaining their values each cycle.
   :Repeat with Offset:
      Repeats the curve data, but offsets the value of the first point to the value of the last point each cycle.
   :Repeat Mirrored:
      Each cycle the curve data is flipped across the X axis.

Count
   Set the number of times to cycle the data. A value of 0 cycles the data infinitely.

Influence
   Controls the percentage of affect the modifier has on the F-curve.


Restrict Frame Range
^^^^^^^^^^^^^^^^^^^^

Start/End
   The frame the modifier's affect starts/ends.
Blend In, Out
   The number of frames, relative the start/end values above, the modifier takes to fade in/out.


Trivially Cyclic Curves
^^^^^^^^^^^^^^^^^^^^^^^

When the *Cycle Mode* for both ends is set to either *Repeat Motion* or
*Repeat with Offset*, and no other options of the modifier are
changed from their defaults, it defines a simple infinite cycle.

This special case receives some additional support from other areas of Blender:

- Automatic Bézier handle placement is aware of the cycle and adjusts to achieve a smooth transition.
- The :ref:`Cycle-Aware Keying <timeline-keying>` option can be enabled to take
  the cycle into account when inserting new keyframes.


.. index:: F-Curve Modifiers; Noise Modifier
.. _bpy.types.FModifierNoise:

Noise Modifier
--------------

Modifies the curve with a noise formula.
This is useful for creating subtle or extreme randomness to animated movements,
like camera shake.

Blend Type
   :Replace: Adds a -0.5 to 0.5 range noise function to the curve.
   :Add: Adds a 0 to 1 range noise function to the curve.
   :Subtract: Subtracts a 0 to 1 range noise function to the curve.
   :Multiply: Multiplies a 0 to 1 range noise function to the curve.

Scale
   Adjust the overall size of the noise. Values further from 0 give less frequent noise.
Strength
   Adjusts the Y scaling of the noise function.
Offset
   Offsets the noise in time.
Phase
   Adjusts the random seed of the noise.
Depth
   Adjusts how detailed the noise function is.

Influence
   Controls the percentage of affect the modifier has on the F-curve.


Restrict Frame Range
^^^^^^^^^^^^^^^^^^^^

Start/End
   The frame the modifier's affect starts/ends.
Blend In, Out
   The number of frames, relative the start/end values above, the modifier takes to fade in/out.


.. index:: F-Curve Modifiers; Limits Modifier
.. _bpy.types.FModifierLimits:

Limits Modifier
---------------

Limit curve values to specified X and Y ranges.

Minimum X, Y
   Cuts a curve off at these frames ranges, and sets their minimum value at those points.
Minimum X, Y
   Truncates the curve values to a range.

Influence
   Controls the percentage of affect the modifier has on the F-curve.


Restrict Frame Range
^^^^^^^^^^^^^^^^^^^^

Start/End
   The frame the modifier's affect starts/ends.
Blend In, Out
   The number of frames, relative the start/end values above, the modifier takes to fade in/out.


.. index:: F-Curve Modifiers; Stepped Interpolation Modifier
.. _bpy.types.FModifierStepped:

Stepped Interpolation Modifier
------------------------------

Gives the curve a stepped appearance by rounding values down within a certain range of frames.

Step Size
   Specify the number of frames to hold each frame.
Offset
   Reference number of frames before frames get held.
   Use to get hold for (1-3) vs (5-7) holding patterns.
Start Frame
   Restrict modifier to only act before its "end" frame.
End Frame
   Restrict modifier to only act after its "start" frame.

Influence
   Controls the percentage of affect the modifier has on the F-curve.


Restrict Frame Range
^^^^^^^^^^^^^^^^^^^^

Start/End
   The frame the modifier's affect starts/ends.
Blend In, Out
   The number of frames, relative the start/end values above, the modifier takes to fade in/out.
