.. index:: Nodes; Point Separate
.. _bpy.types.GeometryNodeAttributeCompare:

*****************
Attribute Compare
*****************

This node reads two input attributes as floats and allows for basic element-wise comparison operations.
Like the :doc:`Attribute Math </modeling/modifiers/nodes/attribute/attribute_math>` node, it is also 
possible to switch to using single values for inputs. This node can be combined with the 
:doc:`Point Separate </modeling/modifiers/nodes/point/point_separate>` node for more flexibility
for which points to separate out.


.. figure:: /images/modeling_modifiers_nodes_attribute_compare.png

   The attribute compare node.

Inputs
======

Geometry
   The geometry that is modified.

A
   The first input to the math operation.
   Depending on the *Type* input, this is either an attribute name or an input of the specified data type.

B
   The second input to the math operation.
   Depending on the *Type* input, this is either an attribute name or an input of the specified data type.

Epsilon
    For the *Equal* and *Not Equal* operations, this value is used as a threshold for deciding whether
    two inputs are equal.

Result
   Name of the attribute where the computed result it stored.
   If an attribute with this name does not exist yet, a new attribute with a boolean data type is added.
   If it does exist, the values of the existing attribute are overridden.

Properties
==========

Operation
   The math function to execute.

   .. note::
      For operations besides "Equal" and "Not Equal", the input attributes are converted implicitly 
      to the float data type. For the equality operations on vectors, the distance between the vector inputs are used.

Type A / Type B
   Contols whether to use an attribute or a single value of the specified data type as an input.
