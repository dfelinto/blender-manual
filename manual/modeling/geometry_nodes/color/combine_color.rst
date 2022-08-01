.. _bpy.types.FunctionNodeCombineColor:
.. index:: Geometry Nodes; Combine Color

******************
Combine Color Node
******************

.. figure:: /images/node-types_FunctionNodeCombineColor.png
   :align: right
   :alt: Combine Color Node.

The *Combine Color Node* combines an image from its composite color channels.
The node can combine multiple :term:`Color Models <Color Model>` depending on the Mode property.


Inputs
======

The outputs of this node depends on the Mode property (see below).

Alpha
   The color channel that that is responsible for the image's transparency.


Properties
==========

Mode
   The color model to output.

   :RGB: Combine the three inputs: Red, Green, and Blue color channels into a single color.
   :HSV: Combine the three inputs: Hue, Saturation, and Value color channels into a single color.
   :HSL: Combine the three inputs: Hue, Saturation, and Lightness color channels into a single color.


Output
======

Color
   Standard color output.
