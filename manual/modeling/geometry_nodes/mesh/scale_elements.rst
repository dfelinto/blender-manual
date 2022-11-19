.. index:: Geometry Nodes; Scale Elements
.. _bpy.types.GeometryNodeScaleElements:

*******************
Scale Elements Node
*******************

.. figure:: /images/node-types_GeometryNodeScaleElements.webp
   :align: right
   :alt: Scale Elements node.

The *Scale Elements Node* scales groups of connected edges and faces.
When multiple selected faces/edges share the same vertices, they are scaled together.
The center and scaling factor is averaged in this case.


Inputs
======

Mesh
   Standard geometry input.

Selection
   Whether to scale each edge or face.
   True values mean the element will be scaled, false means it will be unaffected.

Scale
   The factor used to scale elements or groups of elements.

Center
   Origin of the scaling for each element. If multiple elements are connected, their center is averaged.

Axis :guilabel:`Single Axis Mode Only`
   Axis in which to scale the element. This input is normalized internally, so the length does not matter.


Properties
==========

Domain
   The element type to transform.

   :Face: Scale individual faces or neighboring face islands.
   :Edge: Scale individual edges or neighboring edge islands.

Scale Mode
   :Uniform: Scale elements by the same factor in every direction.
   :Single Axis: Scale elements in a single direction defined by the *Direction* input.


Output
======

Mesh
   Standard geometry output.

Examples
========

.. figure:: /images/modeling_geometry-nodes_flip-faces_extrude.png
   :align: right

The node is useful when combined with the :doc:`/modeling/geometry_nodes/mesh/extrude_mesh`,
especially in *Individual* mode, where face islands don't need to be scaled together.
