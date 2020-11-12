.. _bpy.ops.mesh.select_similar:

**************
Select Similar
**************

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> Similar`
   :Hotkey:    :kbd:`Shift-G`

Select geometry that has similar certain properties to the ones selected,
based on a threshold that can be set in tool properties after activating the tool.
Tool options change depending on the selection mode:

Vertex Selection Mode:
   Normal
      Selects all vertices that have normals pointing in similar directions to those currently selected.
   Amount of Adjacent Faces
      Selects all vertices that have the same number of faces connected to them.
   Vertex Groups
      Selects all vertices in the same :doc:`vertex group </modeling/meshes/properties/vertex_groups/index>`.
   Amount of Connecting Edges
      Selects all vertices that have the same number of edges connected to them.

Edge Selection Mode:
   Length
      Selects all edges that have a similar length as those already selected.
   Direction
      Selects all edges that have a similar direction (angle) as those already selected.
   Amount of Faces Around an Edge
      Selects all edges that belong to the same number of faces.
   Face Angles
      Selects all edges that are between two faces forming a similar angle, as with those already selected.
   Crease
      Selects all edges that have a similar :ref:`Crease <modeling-edges-crease-subdivision>`
      value as those already selected.
   Bevel
      Selects all edges that have the same *Bevel Weight* as those already selected.
   Seam
      Selects all edges that have the same *Seam* state as those already selected.
      *Seam* is a mark used in :ref:`UV texturing <editors-uv-index>`.
   Sharpness
      Selects all edges that have the same *Sharp* state as those already selected.
      *Sharp* is a mark used by the :doc:`Edge Split Modifier </modeling/modifiers/generate/edge_split>`.

Face Selection Mode:
   Material
      Selects all faces that use the same material as those already selected.
   Area
      Selects all faces that have a similar area as those already selected.
   Polygon Sides
      Selects all faces that have the same number of edges.
   Perimeter
      Selects all faces that have a similar perimeter (added values of its edge lengths).
   Normal
      Selects all faces that have a similar normal as those selected.
      This is a way to select faces that have the same orientation (angle).
   Co-planar
      Selects all faces that are (nearly) in the same plane as those selected.
   Flat/Smooth
      Selects all faces with similar :doc:`face shading </modeling/meshes/editing/face/shading>`.
   Face-Map
      Selects all faces belonging to a :ref:`Face-Map <bpy.types.FaceMaps>`.
   Freestyle Face Marks
      Selects all faces with similar :ref:`Freestyle Face Marks <bpy.ops.mesh.mark_freestyle_face>`.


.. _bpy.ops.mesh.select_similar_region:

Face Regions
============

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> Similar --> Face Regions`

Select matching features on a mesh that has multiple similar areas based on the topology.
