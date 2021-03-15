.. index:: Geometry Nodes; Attribute Remove
.. _bpy.types.GeometryNodeAttributeRemove:

****************
Attribute Remove
****************

.. figure:: /images/modeling_modifiers_nodes_attribute-remove.png
   :align: right
   :width: 200px

   The Attribute Remove node.

The *Attribute Remove* node removes a number of given attributes from each element of the given Geometry.


Inputs
======

Geometry
   Standard geometry input.

Attribute (Multi-Input)
   The name of the attribute to remove.
   Multiple attribute can be removed at once by connecting multiple :ref:`String Input nodes<input-string-node>`.
   Built-in attributes and attributes that don't exist can't be removed.

Output
======

Geometry
   Standard geometry output.
