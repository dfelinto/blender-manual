.. index:: Geometry Nodes; Instances

*********
Instances
*********

.. figure:: /images/modeling_geometry-nodes_instances.png
   :align: center

   The three types of instances.

In addition to storing real data like a mesh or a curve, a geometry can store instances,
which themselves can reference more geometry, or an object, or a collection. The purpose
of instancing is to allow including much more geometry in the result, without duplicating
the actual data. This is because renderer like :doc:`Cycles </render/cycles/index>`
can handle the same geometry data in many different locations better than when the data
is duplicated.

Each instance keeps track of which geometry it corresponds to, and a :term:`Transform`.
Instances can also store the ``id`` attribute, used for correct motion blur when instances
move in an animation.

The main node used to create instances in geometry nodes
is the :doc:`/modeling/geometry_nodes/instances/instance_on_points`.


.. warning::

   Currently instancing from geometry nodes cannot be mixed with instancing from the
   :doc:`/scene_layout/object/properties/instancing/index` panel in the property editor.


.. _geometry-nodes_nested-instancing:

Nested Instancing
=================

Since instances can store a geometry, and a geometry can contain instances, nested instancing is possible.
In other words, it is possible to instance an instance, or even a collection of instances.
By default, the :doc:`/modeling/geometry_nodes/instances/instance_on_points` will create
nested instances by instancing on the points real geometry and instanced geometry.

.. figure:: /images/modeling_geometry-nodes_instances-nested.png
   :align: center

   A node group that creates nested instancing by chaining
   :doc:`instance on points </modeling/geometry_nodes/instances/instance_on_points>` nodes.

Here, nested instancing is used to distribute geometry that contains both a mesh
and instances. The output geometry contains a "real" mesh, and a group of instances.
Each instance contains a sphere mesh and many instances of a cone geometry.

.. figure:: /images/modeling_geometry-nodes_instances-nested-tree.png
   :align: center
   :width: 50%

   The tree of instanced geometry for the example above.

What makes this method helpful is that the output geometry only contains three unique meshes:
the plane, the sphere, and the cone. This would make the performance much better if the meshes
were more complicated.

.. warning::

   Only eight levels of nested instancing are supported for rendering and the viewport currently.
   Though deeper trees of instances can be made inside geometry nodes, they must be realized at the
   end of the node tree.

.. _geometry-nodes_instance-processing:

Instance Processing
===================

Almost all nodes that process geometry do so by processing each unique
geometry in their input's tree of instances separately. For example,
if a :doc:`/modeling/geometry_nodes/mesh/subdivision_surface` was placed at
the end of the example above, it would only have to subdivide three meshes,
rather than each instance of a mesh. Another important example is processing with
the output of the :doc:`/modeling/geometry_nodes/text/string_to_curves`,
where each unique character only has to be processed once.

This method can improve performance a lot, but it means that the result of an operation
will be the same for every instance of a certain geometry. In order to have unique results
for every instance, the :doc:`/modeling/geometry_nodes/instances/realize_instances`
node can be used.
