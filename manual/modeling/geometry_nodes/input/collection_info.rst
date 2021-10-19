.. index:: Geometry Nodes; Collection Info
.. _bpy.types.GeometryNodeCollectionInfo:

********************
Collection Info Node
********************

.. figure:: /images/modeling_geometry-nodes_input_collection-info_node.png
   :align: right

   Collection Info Node.

The *Collection Info* node gets information from collections.
This can be useful to control parameters in the geometry node tree with an external collection.

.. tip::
   A *Collection Info* node can be added quickly by dragging a collection into the node editor.


Inputs
======

Collection
   Collection to get the properties from.

Separate Children
   Output each child of the collection as a separate instance. The list of instances will be sorted alphabetically
   with the objects and child collections sorted together. This can be used with the *Pick Instance* option in the
   :doc:`/modeling/geometry_nodes/instances/instance_on_points` node to choose between collection children at each
   point.

Reset Children
   Remove the transform of each of the collection's children when converting them to instances. This is useful in
   order to keep child objects visually separate in the viewport, while keeping every instance located directly
   at the location of the point it was added for.


Properties
==========

Transform Space
   The transformation of the geometry outputs.

   :Original:
      Output the geometry relative to the collection offset.
   :Relative:
      Join the input collection geometry with the modified object,
      maintaining the relative position between the objects in the scene.


Outputs
=======

Geometry
   Geometry of the collection in world space with all its modifiers applied.
