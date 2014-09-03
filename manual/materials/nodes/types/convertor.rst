
Material Convertor Nodes
************************

As the name implies, these nodes convert the colors in the material in some way.


ColorRamp Node
==============

.. figure:: /images/26-Manual-Material-Convertor-Node-ColorRamp.jpg

   ColorRamp node


The ColorRamp Node is used for mapping values to colors with the use of a gradient. It works exactly the same way as a :doc:`Colorband for textures and materials </materials/properties/ramps>`, using the Factor value as a slider or index to the color ramp shown, and outputting a color value and an alpha value from the output sockets.

By default,
the ColorRamp is added to the node map with two colors at opposite ends of the spectrum.
A completely black black is on the left
(Black as shown in the swatch with an Alpha value of 1.00)
and a whitewash white is on the right.

To select a color, :kbd:`LMB` click on the thin vertical line/band within the colorband.
The example picture shows the black color selected, as it is highlighted white.
The settings for the color are shown above the colorband as (left to right): color swatch,
Alpha setting, and interpolation type.


Inputs
------

:guilabel:`Fac`:
   Factor. The degree of node's influence in node tree. The value can be provided by another node or set manually.


Outputs
-------

:guilabel:`Color`
   Value of the color, combined by the node.
:guilabel:`Alpha`
   Value of the alpha, combined by the node.


Controls
--------

.. figure:: /images/26-Material-Convertor-Node-ColorRamp-Addpoint-Buticon.jpg

   Add a new mark to the center of the colorband with the default color (neutral gray).


.. figure:: /images/26-Material-Convertor-Node-ColorRamp-Deletepoint-Buticon.jpg

   Remove the currently selected mark from the colorband.


.. figure:: /images/26-Material-Convertor-Node-ColorRamp-Flip-Buticon.jpg

   Flip the colorband.


.. figure:: /images/26-Manual-Material-Convertor-Node-ColorRamp-Interpolation.jpg

   Modes of interpolation between marker's values color ramp


:guilabel:`Interpolation`
   Various modes of interpolation between marker's values can be chosen in the Interpolation menu:

   :guilabel:`Ease`
      Ease by quadratic equation.
   :guilabel:`Cardinal`
      Cardinal.
   :guilabel:`Linear`
      Linear (default).  A smooth, consistent transition between colors.
   :guilabel:`B-Spline`
      B-Spline.
   :guilabel:`Constant`
      Constant.


.. figure:: /images/26-Manual-Material-Convertor-Node-Colorband.jpg

   Colorband


:guilabel:`Colorband`
   Contain a gradient through a sequence of many colors (with alpha), each color acting across a certain position in the spectrum.


.. figure:: /images/26-Material-Convertor-Node-ColorRamp-Numberpoint-Buticon.jpg

   The number of the active mark.


.. figure:: /images/26-Material-Convertor-Node-ColorRamp-Pospoint-Buticon.jpg

   :guilabel:`Pos`.  The position of the active color mark in the colorband (range 0.0–1.0).  The position of the color marks can also be changed by :kbd:`lmb` dragging them in the colorband.


.. figure:: /images/26-Manual-Material-Convertor-Node-ColorSwatch.jpg

   Color swatch to color selection for a mark


Color :guilabel:`Selector`
   Allows set color and alpha values for each marker.


See more details about node controls' functions :doc:`here </materials/properties/ramps>`.


RGB to BW Node
==============

.. figure:: /images/26-Manual-Material-Convertor-Node-RGB-to-BW.jpg

   RGB to BW node


This node converts a color image to black-and-white.


Inputs
------

:guilabel:`Color`:
   Input color value. Includes a color swatch, allowing you to select the color directly on the node.


Outputs
-------

:guilabel:`Value`
   Black-and-white value of the input color, converted by the node.


Math Node
=========

.. figure:: /images/26-Manual-Material-Convertor-Node-Math.jpg

   Math node


This node performs the selected math operation on an image or buffer.
All common math functions are supported. If only an image is fed to one Value socket, the math
function will apply the other Value consistently to every pixel in producing the output Value.
Select the math function by clicking the up-down selector where the "Add" selection is shown.


Inputs
------

:guilabel:`Value`
   Input value 1 (upper). The value can be provided by another node or set manually.
:guilabel:`Value`
   Input value 2 (lower). The value can be provided by another node or set manually.


Outputs
-------

:guilabel:`Value`
   Output value, converted by the node.


Controls
--------

:guilabel:`Clamp`
   Clamps the result between 0 and 1.

:guilabel:`Operation`
   Selector the math function for conversion.

   :guilabel:`Add`
      Add the two inputs
   :guilabel:`Subtract`
      Subtract input 2 from input 1
   :guilabel:`Multiply`
      Multiply the two inputs
   :guilabel:`Divide`
      Divide input 1 by input 2
   :guilabel:`Sine`
      The sine of input 1 (degrees)
   :guilabel:`Cosine`
      The cosine of input 1 (degrees)
   :guilabel:`Tangent`
      The tangent of input 1 (degrees)
   :guilabel:`Arcsine`
      The arcsine (inverse sine) of input 1 (degrees)
   :guilabel:`Arccosine`
      The arccosine (inverse cosine) of input 1 (degrees)
   :guilabel:`Arctangent`
      The arctangent (inverse tangent) of input 1 (degrees)
   :guilabel:`Power`
      Input 1 to the power of input 2 (input1^input2)
   :guilabel:`Logarithm`
      Log base input 2 of input 1
   :guilabel:`Minimum`
      The minimum of input 1 and input 2
   :guilabel:`Maximum`
      The maximum of input 1 and input 2
   :guilabel:`Round`
      Rounds input 1 to the nearest integer
   :guilabel:`Less Than`
      Test if input 1 is less than input 2, returns 1 for true, 0 for false
   :guilabel:`Greater Than`
      Test if input 1 is greater than input 2, returns 1 for true, 0 for false
   :guilabel:`Modulo`
      Division of input 1 by input 2 with remainder.
   :guilabel:`Absolute`
      Always return non-negative value from any operation input 2 between input 1.


Vector Math Node
================

.. figure:: /images/26-Manual-Material-Convertor-Node-VectorMath.jpg

   Vector Math node


This node performs the selected math operation on vectors.
Select the math function by clicking the up-down selector where the "Add" selection is shown.


Inputs
------

:guilabel:`Vector`
   Input vector 1 (upper). The value can be provided by another node or set manually.
:guilabel:`Vector`
   Input vector 2 (lower). The value can be provided by another node or set manually.


Outputs
-------

:guilabel:`Vector`
   Output vector, converted by the node.
:guilabel:`Value`
   Output value, converted by the node.


Controls
--------

:guilabel:`Operation`
   Selector the math function for conversion.

   :guilabel:`Add`
      Adding input 1 and 2.
   :guilabel:`Subtract`
      Subtracting input 1 and 2.
   :guilabel:`Average`
      Averaging input 1 and 2.
   :guilabel:`Dot Product`
      Algebraic operation that takes two equal-length sequences of vectors 1 and 2 and returns a single number. Result - scalar.
   :guilabel:`Cross Product`
      Geometric binary operation on two vectors 1 and 2 in three-dimensional space. It results in a vector which is perpendicular to both and therefore normal to the plane containing them. Result - vector.
   :guilabel:`Normalize`
      Normalizing input 1 and 2.


Squeeze Value Node
==================

.. figure:: /images/26-Manual-Material-Convertor-Node-SqueezeValue.jpg

   Squeeze Value node


This node is used primarily in conjunction with the Camera Data node used.
The camera data generate large output values,
both in terms of the depth information as well as the extent in the width.
With the squeeze Node high output values to an acceptable material for the node degree,
ie to values between 0.0 - 1.0 scaled down.


Inputs
------

:guilabel:`Value`
   Any numeric value. The value can be provided by another node or set manually.
:guilabel:`Width`
   Determines the curve between sharp S-shaped (width = 1) and stretched (Width = 0.1). Negative values reverse the course. The value can be provided by another node or set manually.
:guilabel:`Center`
   The center of the output value range. This input value is replaced by the output value of 0.5. The value can be provided by another node or set manually.


Outputs
-------

:guilabel:`Value`
   A value between 0 and 1, converted by the node.


Separate RGB Node
=================

.. figure:: /images/26-Manual-Material-Convertor-Node-SeparateRGB.jpg

   Separate RGB node


This node separates an image into its red, green, blue channels - traditional primary colors,
also broadcast directly to most computer monitors.


Inputs
------

:guilabel:`Image`
   Input color value. Includes a color swatch, allowing you to select the color directly on the node.


Outputs
-------

:guilabel:`R`
   Value of the red color channel, separated out by the node.
:guilabel:`G`
   Value of the green color channel, separated out by the node.
:guilabel:`B`
   Value of the blue color channel, separated out by the node.


Combine RGB Node
================

.. figure:: /images/26-Manual-Material-Convertor-Node-CombineRGB.jpg

   Combine RGB node


This node combines a color (image) from separated red, green, blue channels.


Inputs
------

:guilabel:`R`
   Input value of red color channel. The value can be provided by another node or set manually.
:guilabel:`G`
   Input value of green color channel. The value can be provided by another node or set manually.
:guilabel:`B`
   Input value of blue color channel. The value can be provided by another node or set manually.


Outputs
-------

:guilabel:`Image`
   Output value of the color, combined by the node.


Separate HSV Node
=================

.. figure:: /images/26-Manual-Material-Convertor-Node-SeparateHSV.jpg

   Separate HSV node


This node separates an image into image maps for the hue, saturation, value channels.
Three values, often considered as more intuitive than the RGB system
(nearly only used on computers)

Use and manipulate the separated channels for different purposes; i.e.
to achieve some compositing/color adjustment result. For example,
you could expand the Value channel (by using the multiply node)
to make all the colors brighter. You could make an image more relaxed by diminishing
(via the divide or map value node) the Saturation channel.
You could isolate a specific range of colors
(by clipping the Hue channel via the Colorramp node) and change their color
(by the Add/Subtract mix node).


Inputs
------

:guilabel:`Color`
   Input color value. Includes a color swatch, allowing you to select the color directly on the node.


Outputs
-------

:guilabel:`H`
   Value of the hue color channel, separated out by the node (in some way, choose a «color» of the rainbow).
:guilabel:`S`
   Value of the saturation color channel, separated out by the node (the *quantity* of hue in the color (from desaturate - shade of gray - to saturate - brighter colors)).
:guilabel:`V`
   Value of the value color channel, separated out by the node (the **luminosity** of the color (from 'no light' - black - to 'full light' - 'full' color, or white if Saturation is 0.0)).


Combine HSV Node
================

.. figure:: /images/26-Manual-Material-Convertor-Node-CombineHSV.jpg

   Combine HSV node


This node combines a color from separated hue, saturation, value color channels.


Inputs
------

:guilabel:`H`
   Input value of hue color channel. The value can be provided by another node or set manually.
:guilabel:`S`
   Input value of saturation color channel. The value can be provided by another node or set manually.
:guilabel:`V`
   Input value of value color channel. The value can be provided by another node or set manually.


Outputs
-------

:guilabel:`Color`
   Output value of the color, combined by the node.


