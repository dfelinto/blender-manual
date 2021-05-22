
************
Introduction
************

Nodes can be used to change an object's geometry in a more complex way than regular modifiers.
To use them add a :doc:`Geometry Nodes Modifier </modeling/modifiers/generate/geometry_nodes>`.

.. figure:: /images/modeling_geometry-nodes_introduction_properties.png

   The properties of a Geometry Nodes modifier in the modifier stack.


Node Categories
===============

Attribute
   Nodes for working with data stored per object element, e.g. vertex groups.
Color
   Nodes for modifying color data passed through color sockets.
Geometry
   Nodes that can operate on different geometry types (volume, mesh).
Input
   Nodes used mainly as input to other nodes.
Mesh
   Nodes that only operate on meshes.
Mesh Primitives
   Nodes that create a primitive mesh, e.g. a cube.
Point
   Nodes that modify the object elements, e.g. vertices.
Utilities
   Nodes with general purpose for modifying data.
Vector
   Nodes for modifying vector quantities.
Volume
   Nodes for creating or working with volumes.


.. _bpy.ops.node.active_preview_toggle:

Node Data Previews
==================

The data values for :doc:`Attributes </modeling/geometry_nodes/attributes_reference>`
are shown in the :doc:`Spreadsheet editor </editors/spreadsheet>`.
You can also preview the attributes up to a certain node
by toggling the node preview with the button to the right of the node label.
