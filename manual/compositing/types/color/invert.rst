.. _bpy.types.CompositorNodeInvert:
.. Editors Note: This page gets copied into:
.. - :doc:`</render/cycles/nodes/types/color/invert>`

.. --- copy below this line ---

***********
Invert Node
***********

.. figure:: /images/compositing_node-types_CompositorNodeInvert.png
   :align: right

   Invert Node.

The *Invert Node* inverts the colors in the input image, producing a negative.


Inputs
======

Factor
   Controls the amount of influence the node exerts on the output image.
Color
   Standard color input.


Properties
==========

In the compositing context this node has the following properties.

RGB
   De/activation of the color channel inversion.
Alpha
   De/activation of the alpha channel inversion.


Outputs
=======

Color
   Standard color output.


Example
=======

.. figure:: /images/compositing_types_input_mask_example.png

   The Invert node is used to invert the mask.
