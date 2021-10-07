.. index:: Geometry Nodes; Attribute Transfer
.. _bpy.types.GeometryNodeAttributeTransfer:

***********************
Attribute Transfer Node
***********************

.. figure:: /images/modeling_geometry-nodes_attribute_attribute-transfer_node.png
   :align: center

   Attribute Transfer node.

The *Attribute Transfer* node transfers an attribute from one geometry to another.


Inputs
======

Geometry
   Geometry to transfer the attribute to.

Source Geometry
   Geometry to transfer the attribute from.

Source
   Name of the attribute on the source geometry.

Destination
   Name of the attribute on the destination geometry.


Properties
==========

Domain
   Domain that the attribute is transferred to.
   For example, it is possible to transfer a point attribute from
   one geometry to the face domain of another geometry.
   In *Auto* mode, the node tries to guess the domain based on what domain the attribute belongs to.

Mapping
   How elements from the destination geometry are mapped to points on the source geometry.

   :Nearest Face Interpolated:
      Transfer the attribute from the nearest point on the surface.
      Non-face attributes are interpolated across the surface (edge attributes are not supported yet).
      Loose points and edges are ignored.
   :Nearest:
      Transfer the attribute from the nearest element.
      No interpolation is done.


Outputs
=======

Geometry
   Standard geometry output.
