.. index:: Geometry Nodes; Field at Index
.. _bpy.types.GeometryNodeFieldAtIndex:

*******************
Field at Index Node
*******************

.. figure:: /images/node-types_GeometryNodeFieldAtIndex.webp
   :align: right
   :alt: Field at Index Node.

The *Field at Index* node allows accessing data of other elements in the context geometry.
It is similar to the :doc:`/modeling/geometry_nodes/attribute/transfer_attribute` in *Index*
mode. The main difference is that this node does not require a geometry input, because the geometry
from the :ref:`field context <field-context>` is used.

This node is also similar to the :doc:`/modeling/geometry_nodes/utilities/interpolate_domain` node,
except that the value to retrieve from the specified domain is specified by an index rather than
an automatic domain interpolation.


Inputs
======

Index
   The :doc:`index </modeling/geometry_nodes/input/input_index>` of the element in the selected domain
   to retrieve data from, i.e. "the fourth face", or "the first control point".

Value
   The field to retrieve data from.


Properties
==========

Domain
   The :ref:`attribute domain <attribute-domains>` used for for evaluation of the *Value* input.
   This is useful because it can be a different domain than the domain from the
   :ref:`field context <field-context>`, i.e. to choose a vertex for each face.


Output
======

Value
   The value of the input field at the given index.
