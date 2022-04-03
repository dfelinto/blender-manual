.. index:: Geometry Nodes; Extrude Mesh
.. _bpy.types.GeometryNodeExtrudeMesh:

*****************
Extrude Mesh Node
*****************

.. figure:: /images/node-types_GeometryNodeExtrudeMesh.webp
   :align: right
   :alt: Extrude Mesh node.

   Extrude Mesh node.

The *Extrude Mesh Node* generates new vertices, edges, or faces, on selected geometry
and transforms them based on an offset.

The operations are similar to the :doc:`extrude tools </modeling/meshes/editing/mesh/extrude>`
in mesh edit mode, though there are some differences. Most importantly, the node never keeps the back-faces
of the extrusion in place, they are always removed. Attribute propagation rules may also be different.


Inputs
======

Mesh
   Standard geometry input.

Selection
   Whether to extrude each element.
   True values mean elements will be extruded, false values mean elements will remain unchanged.

Offset
   The amount to translate the new geometry on each axis. The default value of the "Offset" input
   is the mesh's :doc:`normals </modeling/geometry_nodes/input/normal>`. To change the distance,
   the *Scale* input can be used. However, when an input is computed for this directly, the length
   of the input vectors is used.

   .. tip::

      Because the default input is the mesh's normals, they may need to be calculated just for this node.
      If the extrusion is only in one direction anyway, a potential performance improvement is to connect
      a :doc:`/modeling/geometry_nodes/input/vector` instead.

Scale
   The factor used to scale elements or groups of elements.

Individual :guilabel:`Face Mode Only`
   Whether to extrude each face individually rather than extruding connected groups of faces together as regions.
   A quad side face will be generated on each side of every selected face.


Properties
==========

Mode
   :Vertices:
      This mode is quite simple, it just attaches new edges and vertices to the selected vertices.

   :Edges:
      Attach new quad faces to the selected edges. Vertices shared by the
      original selected vertices are also shared in the duplicated edges.

      .. note::

         Depending on the situation, the normals of the new faces may be arbitrary. If the selected
         edges only have one selected face, then the node can pick a consistent orientation for the
         new faces, but if there is more than one connected face, or no connected faces, the normals
         may have to be adjusted afterwards.

   :Faces:
      Extrudes contiguous regions of selected faces, or each selected face individually,
      depending on the *Individual* boolean input.

      When the *Individual* input is false, the node will find regions of connected faces and generate
      new "side" faces on the boundaries of those regions. If the whole mesh is selected and it is already
      a :term:`Manifold` shape, then result will just be that the whole mesh moves. Any vertices, edges
      or faces on the *inside* of the face regions are just moved, they are not duplicated.


Output
======

Mesh
   Standard geometry output.

Top
   A boolean field output containing the top new top geometry. The :ref:`domain <attribute-domains>`
   depends on the selected mode. In *Vertex* mode, this is a selection of the new vertices.
   In *Edge* mode, this is a selection of the duplicated edges
   and in *Face* mode, it is a selection of the new faces.

Side
   A boolean field output containing the "side" of the new geometry. In *Vertex* mode, it selects
   the new edges, in *Edge* mode, the new faces, and in *Face* mode, the new side faces are selected,
   which are all of the new faces that aren't in the *Top* selection.


Examples
========

.. figure:: /images/modeling_geometry-nodes_extrude-mesh_sphere-materials.png
   :align: center

Here, the selection outputs are used to set materials on certain faces of the mesh.
A :doc:`/modeling/geometry_nodes/utilities/random_value` node can be used to limit the
extrusion to a random set of faces.


Attribute Propagation
=====================

Attributes are transferred to the new elements with specific rules.
An attribute will never change domains on the resulting mesh.
The ``id`` attribute does not have any special handling.

Generally boolean attributes are propagated with "or", meaning any connected
"true" value that is mixed in for other types will cause the new value
to be "true" as well.

The following sectopms descrone

Vertex Mode
-----------

.. figure:: /images/modeling_geometry-nodes_extrude-mesh_attributes-vertex-new-edges.png
   :align: center
   :width: 400px

   The new edges created in vertex mode use the average value of all connected edges.

* New **vertices** have copied values from their original vertices
* New **edges** have the average value of any connected original edges.
  For boolean attributes, edges are selected if any connected edges were selected.

Edge Mode
---------

.. figure:: /images/modeling_geometry-nodes_extrude-mesh_attributes-edge-connecting-edges.png
   :align: center
   :width: 400px

   Attribute propagation for new connecting edges (the vertical yellow edge).
   The final value is a mix of the values from the two middle blue edges.
   The darker maroon edges lower on the image are not used.

* New **vertices** have copied values from their original vertices.
* Vertical connecting **edges** get the average value
  from any connected extruded edges. For booleans, the edges are selected if any connected extruded
  edges were selected. (*Propagation rules are shown in the figure above*.)
* Horizontal duplicate **edges** have copied values from their original edges.
* New **faces** get the average values of all faces connected to the selected edge.
  For booleans, faces are selected if any connected original faces were selected.
* New **face corners** get the averaged value of corresponding corners in all faces connected to selected edges.
  For booleans, corners are selected if one of those corners are selected.

Face Mode
---------

.. figure:: /images/modeling_geometry-nodes_extrude-mesh_attributes-face-connecting-edges.png
   :align: center
   :width: 400px

   Attribute propagation for new connecting edges (the vertical yellow edge).
   The final value is a mix of the values from the two middle blue edges.
   The values from the darker maroon edges between unselected faces and
   on top of the extruded region are not used.

* New **vertices** have copied values from their original vertices.
* Vertical connecting **edges** get the average value from any connected extruded edges,
  not including the edges "on top" of extruded regions. For booleans,
  the edges are selected if any of those connected edges were selected.
  (*Propagation rules are shown in the figure above*.)
* Horizontal duplicate **edges** have copied values from their original edges.
* New **faces** have copied values from the corresponding extruded faces.
* New **face corners** have copied values from the corresponding corresponding corners of extruded faces.

Individual Face Mode
--------------------

.. figure:: /images/modeling_geometry-nodes_extrude-mesh_attributes-face-individual-connecting-edges.png
   :align: center
   :width: 400px

   Attribute propagation for new connecting edge. Each edge uses the average values of the two neighboring
   edges on its extruded face.

* New **vertices** have copied values from their original vertices.
* Vertical connecting **edges** get the average value of the two neighboring edges on each extruded face.
  For booleans, the edges are selected when at least one neighbor on the extruded face was selected.
* Horizontal duplicate **edges** have copied values from their original edges.
* New side **faces** have copied values from their corresponding selected face.
* New **face corners** have copied values from the corresponding corners of selected faces.
