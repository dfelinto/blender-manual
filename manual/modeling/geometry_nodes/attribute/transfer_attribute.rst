.. index:: Geometry Nodes; Transfer Attribute
.. _bpy.types.GeometryNodeTransferAttribute:

***********************
Transfer Attribute Node
***********************

.. figure:: /images/modeling_geometry-nodes_attribute_transfer-attribute_node.png
   :align: center

   Transfer Attribute node.

The *Transfer Attribute* node retrieves values from a source geometry and provides them as a field,
so they can be used anywhere.


Inputs
======

Source
   The geometry to retrieve the attribute from.

   .. note::

      This node only supports instances in the source geometry when the *Mapping*
      method is set to *Index*.

Attribute
   A field to evaluate on the *Source* geometry for use with the transfer method.

Source Position
   The position to start from when finding the closest location on the source mesh or point cloud.
   Used in the *Nearest Face Interpolated* and *Nearest* modes. By default, this is the same as
   if the :doc:`/modeling/geometry_nodes/input/position` was connected.

Index
   Which index to use when retrieving the data from the input field in *Index* mode.
   By default, the :doc:`index </modeling/geometry_nodes/input/input_index>` is used, meaning that
   the data from the source attribute is copied directly to the output. However, a different
   index can be connected, resulting in a "shuffling" of the values.
   Indices that are either too large or below 0 are clamped.

   .. tip::

      To retrieve a single attribute value instead of a field, a single integer input
      or the :doc:`/modeling/geometry_nodes/input/integer` can be connected to this socket.


Properties
==========

Domain
   The :ref:`attribute domain <attribute-domains>` that the attribute is transferred from, or in other words, 
   the domain used to evaluate the *Attribute* input. For example, it is possible to transfer data from the
   faces of one geometry to the points of another.

Mapping
   How elements from the destination geometry are mapped to the output.

   :Index:
      Copy the attribute data from the value at the input index.
      In this mode, the source geometry can consist of a mesh, point cloud, or curve. The matching
      component type from the context will be chosen if possible, otherwise a component will be chosen
      in that order.

   :Nearest Face Interpolated:
      Transfer the attribute from the nearest point from anywhere on the surface.
      Non-face attributes are interpolated across the surface (edge attributes are not supported yet).
      Loose points and edges are ignored.

   :Nearest:
      Transfer the attribute from the nearest element (with a domain chosen by the *Domain* input).
      No interpolation is done.


Outputs
=======

Attribute
   The data retrieved from the *Source* geometry, mapped based on the node's settings and inputs.


Examples
========

.. figure:: /images/modeling_geometry-nodes_attribute_transfer-attribute_example.png
   :align: center

   Transferring the position of vertices from a different object's geometry,
   assuming that they have the same number of points.
