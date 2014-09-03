
..    TODO/Review: {{review|partial=X|text=examples?}} .


Texture Convertor Nodes
***********************

As the name implies, these nodes convert the colors in the material in some way.


Math

----


.. figure:: /images/Doc26-textureNodes_math.jpg

   math node


The math node performs one of several math functions on one or two inputs

Clamp
   Clamps the result between 0 and 1.

Add
   Add the two inputs
Subtract
   Subtract input 2 from input 1
Multiply
   Multiply the two inputs
Divide
   Divide input 1 by input 2
Sine
   The sine of input 1 (degrees)
Cosine
   The cosine of input 1 (degrees)
Tangent
   The tangent of input 1 (degrees)
Arcsine
   The arcsine (inverse sine) of input 1 (degrees)
Arccosine
   The arccosine (inverse cosine) of input 1 (degrees)
Arctangent
   The arctangent (inverse tangent) of input 1 (degrees)
Power
   Input 1 to the power of input 2 (input1^input2)
Logarithm
   log base input 2 of input 1
Minimum
   The minimum of input 1 and input 2
Maximum
   The maximum of input 1 and input 2
Round
   Rounds input 1 to the nearest integer
Less Than
   Test if input 1 is less than input 2, returns 1 for true, 0 for false
Greater Than
   Test if input 1 is greater than input 2, returns 1 for true, 0 for false


ColorRamp Node
==============

.. figure:: /images/Doc26-textureNodes-colorRamp.jpg

   ColorRamp Node


The ColorRamp Node is used for mapping values to colors with the use of a gradient. It works exactly the same way as a :doc:`Colorband for textures and materials </materials/properties/ramps>`, using the Factor value as a slider or index to the color ramp shown, and outputting a color value and an alpha value from the output sockets.

By default,
the ColorRamp is added to the node map with two colors at opposite ends of the spectrum.
A completely black black is on the left
(Black as shown in the swatch with an Alpha value of 1.00)
and a whitewash white is on the right. To select a color,
:kbd:`LMB` click on the thin vertical line/band within the colorband.
The example picture shows the black color selected, as it is highlighted white.
The settings for the color are shown above the colorband as (left to right): color swatch,
Alpha setting, and interpolation type.

To change the hue of the selected color in the colorband,
:kbd:`LMB` click on the swatch,
and use the popup color picker control to select a new color.
Press :kbd:`Enter` to set that color.

To add colors, hold :kbd:`Ctrl` down and :kbd:`LMB` click inside the gradient.
Edit colors by clicking on the rectangular color swatch, which pops up a color-editing dialog.
Drag the gray slider to edit Alpha values. Note that you can use textures for masks
(or to simulate the old "Emit" functionality)
by connecting the alpha output to the factor input of an RGB mixer.

To delete a color from the colorband, select it and press the Delete button.

When using multiple colors,
you can control how they transition from one to another through an interpolation mixer.
Use the interpolation buttons to control how the colors should band together: Ease, Cardinal,
Linear, or Spline.

Use the A: button to define the Alpha value of the selected color for each color in the range.


RGB to BW Node
==============

.. figure:: /images/Doc26-textureNodes-rgbToBw.jpg

   RGB to BW Node


This node converts a color image to black-and-white by computing the luminance of the rgb
values.


Value to Normal
===============

.. figure:: /images/Doc26-textureNodes-valueToNormal.jpg

   Value to Normal node


Computes a normal map based on greyscale values of an input

Val
   The texture to compute the normal map from

Nabla
   Size of derivative offset used for calculating normals.


Distance
========

.. figure:: /images/Doc26-textureNodes-distance.jpg

   Distance node. Coordinate 2 dropdown is displayed


Computes the distance between two 3d coordinates.

