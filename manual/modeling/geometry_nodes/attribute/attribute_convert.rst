.. index:: Geometry Nodes; Attribute Convert
.. _bpy.types.GeometryNodeAttributeConvert:

*****************
Attribute Convert
*****************

.. figure:: /images/modeling_geometry-nodes_attribute_attribute-convert_panel.png
   :align: right

   The Attribute Convert node.

This node reads one input attribute and converts the data type and domain to the result attribute.
The data type conversion is determined by a set of built-in implicit conversion rules.
These rules are also used when connecting sockets with different data types. Additional information can be found
in the :doc:`Node Socket </interface/controls/nodes/parts>` section of the manual.

.. note::

   The data conversion rules are not editable. When converting a vector to a float,
   the implicit rule may not be desired. In this case it is recommended to
   use :doc:`Attribute Math </modeling/geometry_nodes/attribute/attribute_math>` nodes
   together with :doc:`Attribute Combine </modeling/geometry_nodes/attribute/attribute_combine_xyz>`
   and :doc:`Attribute Separate </modeling/geometry_nodes/attribute/attribute_separate_xyz>` nodes to
   achieve the desired result.


Inputs
======

Geometry
   Standard geometry input.

Attribute
   Name of the attribute that is to be converted.

Result
   Name of the attribute where the computed result it stored.
   If an attribute with this name does not exist yet, a new attribute is added.
   If it does exist, the values of the attribute are overridden.


Properties
==========

Domain
   This determines which domain is to be used to save the result attribute.
   Where the source attribute resides on a different domain, the data is interpolated.

   The *Auto* domain mode chooses the domain based on the following rules.

   #. If the result attribute already exists, use that domain.
   #. If the result attribute doesn't exist, use the source attribute domain.
   #. Otherwise use the default domain (points).

Data Type
   This determines the data type of the result attribute.


Output
======

Geometry
   Standard geometry output.
