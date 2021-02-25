.. index:: Geometry Nodes; Collection Info
.. _bpy.types.GeometryNodeCollectionInfo:

***************
Collection Info
***************

.. figure:: /images/modeling_modifiers_nodes_collection-info.png
   :align: right

   Collection Info Node.

The *Collection Info* node gets information from collections.
This can be useful to make an external collection to control parameters in the geometry node tree.


Inputs
======

Collection
   Collection to get the properties from.


Properties
==========

Transform Space
   The transformation of the geometry outputs.

   Original
      Output the geometry relative to the collection offset.
   Relative
      Join the input collection geometry with the modified object,
      maintaining the relative position between the objects in the scene.


Outputs
=======

Geometry
   Geometry of the collection in world space with all its modifiers applied.
