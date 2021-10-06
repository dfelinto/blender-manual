.. index:: Geometry Nodes; Attribute Curve Map
.. _bpy.types.GeometryNodeAttributeCurveMap:

************************
Attribute Curve Map Node
************************

.. figure:: /images/modeling_geometry-nodes_attribute_attribute-curve-map_node.png
   :align: center

   The Attribute Curve Map node.

The *Attribute Curve Map* node maps an attribute to a new attribute based on a curve.


Inputs
======

Geometry
   Standard geometry input.

Attribute
   Source attribute name.

Result
   Result attribute name.


Properties
==========

Data Type
   Determines as which type the source attribute is interpreted.
   This also changes how many curves can be modified below.

Curve
   For the curve controls see: :ref:`Curve widget <ui-curve-widget>`.


Outputs
=======

Geometry
   Standard geometry output.
