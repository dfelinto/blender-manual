.. index:: Geometry Nodes; Join Geometry
.. _bpy.types.GeometryNodeJoinGeometry:

******************
Join Geometry Node
******************

The *Join Geometry* node merges separately generated geometries into a single one.
If the geometry inputs contain different types of data, the output will also contain different data types.

.. figure:: /images/node-types_GeometryNodeJoinGeometry.webp
   :alt: Join Geometry node.

   Join Geometry node.

.. note::

   The node cannot handle the case when more than one geometry input has a volume component.


Materials
=========

When multiple mesh inputs contain different materials, the material slots from each mesh geometry
are merged so that the output mesh will contain all the input materials.


Attributes
==========

When merging attributes from multiple geometry inputs, the highest complexity data type is chosen
for the output attribute. In other words, if a ``weight`` attribute has a Boolean type on one geometry input
and a vector data type on another geometry, the ``weight`` attribute on the output geometry will have
a vector data type. The same heuristic is used for attribute domains, the domain with the most information
will be used for the output.

.. warning::

   Like other geometry nodes, this node always outputs generic typed attributes. So instead of a
   :term:`Vertex Group` attribute, it will create a "Float" attribute on the result, and it will
   create a generic 2D vector attribute instead of a special "UV Map" attribute. Some other areas
   of Blender don't properly handle generic attributes in version 3.0.

   Custom face corner normals are also not transferred currently.

Inputs
======

Geometry
   Geometry that will be joined. Multiple inputs are allowed.
   When the node is muted, only the first link will be passed through.


Properties
==========

This node has no properties.


Output
======

Geometry
   Standard geometry output.
