.. index:: Geometry Nodes; Realize Instances
.. _bpy.types.GeometryNodeRealizeInstances:

**********************
Realize Instances Node
**********************

.. figure:: /images/modeling_geometry-nodes_instances_realize-instances_node.png
   :align: right

   Realize Instances node.

The *Realize Instances* node makes any instances (efficient duplicates of the same geometry)
into real geometry data. This makes it possible to affect each instance individually,
whereas without this node, the exact same changes are applied to every instance of
the same geometry. However, performance can become much worse when the input
contains many instances of complex geometry, which is a fundamental limitation
when procedurally processing geometry.

.. note::

   If the input contains multiple volume instances, only the first volume component is moved to the output.


Attributes
==========

When merging attributes from multiple geometry inputs, the highest complexity data type is chosen
for the output attribute. In other words, if a ``weight`` attribute has a Boolean type on one geometry input
and a vector data type on another geometry, the ``weight`` attribute on the output geometry will have
a vector data type.

.. warning::

   Like other geometry nodes, this node always outputs generic typed attributes. So instead of a
   :term:`Vertex Group` attribute, it will create a "Float" attribute on the result, and it will
   create a generic 2D vector attribute instead of a special "UV Map" attribute. Some other areas
   of Blender don't properly handle generic attributes in version 3.0. 
   
   Custom face corner normals are also not transferred currently.

Inputs
======

Geometry
   Standard geometry input.


Properties
==========

This node has no properties.


Outputs
=======

Geometry
   Standard geometry output.
