.. _bpy.types.CompositorNodeHueCorrect:

****************
Hue Correct Node
****************

The *Hue Correct Node* is able to adjust the Hue, Saturation, and Value of an image,
with an input curve.

.. figure:: /images/compositing_node-types_CompositorNodeHueCorrect.png

   Hue Correct Node.


Inputs
======

Factor
   Controls the amount of influence the node exerts on the output image.
Image
   Standard image input.


Properties
==========

Level
   H (Hue), S (Saturation), V (Value)
Curve
   For the curve controls see: :ref:`Curve widget <ui-curve-widget>`.
   By default, the curve is a straight line, meaning there is no change.
   The spectrum allows you to raise or lower HSV levels for each range of pixel colors.
   To change an H, S, or V level, move the curve points up or down. Pixels with hue values each
   point in the horizontal position of the graph will be changed depending on the shape of the curve.


Outputs
=======

Image
   Standard image output.

.. TODO <2.8 explain all options
