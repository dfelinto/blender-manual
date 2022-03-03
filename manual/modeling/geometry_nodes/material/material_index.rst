.. index:: Geometry Nodes; Material Index
.. _bpy.types.GeometryNodeInputMaterialIndex:

*******************
Material Index Node
*******************

.. figure:: /images/modeling_geometry-nodes_material_material-index_node.png
   :align: right
   :alt: Material Index node.

The *Material Index* node outputs which material in the list of materials of the geometry
each element corresponds to. Currently the node supports mesh data, where ``material_index``
is a built-in attribute on faces.

The node to set this data is
the :doc:`Set Material Index </modeling/geometry_nodes/material/set_material_index>` node.


Inputs
======

This node has no inputs.


Properties
==========

This node has no properties.


Outputs
=======

Material Index
   Standard integer value, with a minimum value of zero.
