.. index:: Nodes; Transform
.. _bpy.types.GeometryNodeTransform:

*********
Transform
*********

The *Transform Node* allows to move, rotate or scale the geometry. It happens to the entire geometry at once, and not per element.
For example, you can't rotate individual point cloud points with this node.

.. figure:: /images/modeling_modifiers_nodes_transform.png
   :align: left

   Transform modifier node.


Inputs
=======

Geometry
    Geometry to transform.

Translation
    Translates the geometry in the local space.
Rotation
    Euler rotation in local space.
Scale
    Scale to transform the geometries in local space.


Output
=======

Geometry
    Transformed geometry.


.. note::
    The transformation happens in the local space of the object that owns the modifier.
