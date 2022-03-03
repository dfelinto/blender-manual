.. index:: Geometry Nodes; Field at Index
.. _bpy.types.GeometryNodeFieldAtIndex:

*******************
Field at Index Node
*******************

.. figure:: /images/modeling_geometry-nodes_field-at-index_node.png
   :align: right
   :alt: Field at Index Node.

The *Field at Index* node allows accessing data of other elements in the context geometry.
It is similar to the :doc:`/modeling/geometry_nodes/attribute/transfer_attribute` in *Index*
mode. The main difference is that this node does not require a geometry input, because the geometry
from the :ref:`field context <field-context>` is used.


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
   The :ref:`attribute domain <attribute-domains>` used for accumulation
   and for evaluation of the *Value* input. If the


Output
======

Value
   The value of the input field at the given index.
