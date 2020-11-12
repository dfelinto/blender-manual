.. _bpy.types.CompositorNodeValue:
.. Editors Note: This page gets copied into :doc:`</render/cycles/nodes/types/input/value>`

.. --- copy below this line ---

**********
Value Node
**********

.. figure:: /images/compositing_node-types_CompositorNodeValue.png
   :align: right

   Value Node.

The *Value Node* is a simple node to input numerical values to other nodes in the tree.


Inputs
======

This node has no input sockets.


Properties
==========

Single numerical value (floating point).


Outputs
=======

Value
   The value set in the node properties.


Example
=======

In the example below the *Value Node* is used to control multiple values at once,
this make the node a useful organizational tool.

.. figure:: /images/compositing_types_input_value_example.png

   Example of the *Value* node.

.. tip::

   From this you can also make different values proportional to each other by adding
   a :doc:`Math Node </compositing/types/converter/math>` in between the different links.
