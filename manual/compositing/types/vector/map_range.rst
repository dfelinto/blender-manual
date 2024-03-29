.. index:: Compositor Nodes; Map Range
.. _bpy.types.CompositorNodeMapRange:

**************
Map Range Node
**************

.. figure:: /images/compositing_node-types_CompositorNodeMapRange.webp
   :align: right
   :alt: Map Range Node.

This node converts (maps) an input value range into a destination range.
By default, values outside the specified input range will be proportionally mapped as well.
This node is similar to *Map Value* node but provides a more intuitive way to specify the desired output range.


Inputs
======

Value
   The input value to be remapped.
From Min
   The lower bound of the range to remap from.
From Max
   The higher bound of the range to remap from.
To Min
   The lower bound of the target range.
To Max
   The higher bound of the target range.


Properties
==========

Clamp
   Clamps values to Min/Max of the destination range.


Outputs
=======

Value
   Standard value output.


Usage
=====

One important use case is to easily map the original range of the Z-depth channel
to a more usable range (i.e: 0.0 - 1.0) for use as a matte for colorization or filtering operations.
