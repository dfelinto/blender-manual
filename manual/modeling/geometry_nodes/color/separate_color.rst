.. _bpy.types.FunctionNodeSeparateColor:
.. index:: Geometry Nodes; Separate Color

*******************
Separate Color Node
*******************

.. figure:: /images/node-types_FunctionNodeSeparateColor.png
   :align: right
   :alt: Separate Color Node.

The *Separate Color Node* splits an image into its composite color channels.
The node can output multiple :term:`Color Models <Color Model>` depending on the Mode property.


Inputs
======

Color
   Standard color input.


Properties
==========

Mode
   The color model to output.

   :RGB: Split the input colors into it's three outputs: Red, Green, and Blue color channels.
   :HSV: Split the input colors into it's three outputs: Hue, Saturation, and Value color channels.
   :HSL: Split the input colors into it's three outputs: Hue, Saturation, and Lightness color channels.


Outputs
=======

The outputs of this node depends on the Mode property (see above).

Alpha
   The color channel that that is responsible for the image's transparency.
