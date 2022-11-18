.. index:: Geometry Nodes; Sample Nearest
.. _bpy.types.GeometryNodeSampleNearest:

*******************
Sample Nearest Node
*******************

.. figure:: /images/node-types_GeometryNodeSampleNearest.webp
   :align: center
   :alt: Sample Nearest node.

The *Sample Nearest* node retrieves the :doc:`index </modeling/geometry_nodes/input/input_index>` 
of the geometry element in its input geometry that is closest to the input position.
This node is similar to the :doc:`/modeling/geometry_nodes/geometry/geometry_proximity`,
but it outputs the index of the closest element instead of its distance from the current location.


Inputs
======

Geometry
   The geometry to sample.

   .. note::

      This node only supports point cloud and mesh inputs.

Sample Position
   The position to start from when finding the closest location on the target geometry.
   By default, this is the same as if the :doc:`/modeling/geometry_nodes/input/position` was connected.


Properties
==========

Domain
   The :ref:`attribute domain <attribute-domains>` to consider the distance from.


Outputs
=======

Index
   The :doc:`index </modeling/geometry_nodes/input/input_index>` of the closest geometry element of the chosen domain.


Examples
========

.. figure:: /images/modeling_geometry-nodes_sample_nearest-example.png
   :align: center

   Combining this node with the :doc:`/modeling/geometry_nodes/geometry/sample_index` gives a setup that
   can retrieve the closest attribute value from another geometry. This is the same behavior as the
   *Transfer Attribute* node in versions of Blender before 3.4.
