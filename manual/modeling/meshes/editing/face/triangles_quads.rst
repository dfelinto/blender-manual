.. _bpy.ops.mesh.tris_convert_to_quads:
.. _mesh-faces-tristoquads:

******************
Triangles to Quads
******************

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Face --> Triangles to Quads`
   :Hotkey:    :kbd:`Alt-J`

This tool converts the selected triangles into quads by taking adjacent triangles and
removing the shared edge to create a quad, based on a threshold.
This tool can be applied on a selection of multiple triangles.

This means you can select the entire mesh and convert triangles that already form square shapes --
to be converted into quads, without having to concern yourself with individual faces.

Alternatively you can force this operation selecting a pairs of faces (see hint below for other ways of joining).

To create a quad, this tool needs at least two adjacent triangles.
If you have an even number of selected triangles,
it is also possible not to obtain only quads. In fact,
this tool tries to create most even rectangular quads from the given triangles,
which means some triangles could remain.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_face_triangles-quads_before.png
          :width: 320px

          Before converting tris to quads.

     - .. figure:: /images/modeling_meshes_editing_face_triangles-quads_after.png
          :width: 320px

          After converting tris to quads.

All the menu entries and hotkeys use the settings defined in the *Operator* panel:

Max Angle
   This value, between (0 to 180), controls the threshold for this tool to work on adjacent triangles.
   With a threshold of 0.0,
   it will only join adjacent triangles that form a perfect rectangle
   (i.e. right-angled triangles sharing their hypotenuses).
   Larger values are required for triangles with a shared edge that is small,
   relative to the size of the other edges of the triangles.
Compare UVs
   When enabled, it will prevent the union of triangles that are not also adjacent in the active UV map.
Compare Vertex Color
   When enabled, it will prevent the union of triangles that have no matching vertex color.
Compare Sharp
   When enabled, it will prevent the union of triangles that share an edge marked as sharp.
Compare Materials
   When enabled, it will prevent the union of triangles that do not have the same material assigned.

.. hint::

   When isolated groups of faces are selected, they can be combined
   with :ref:`Create Face <modeling-mesh-make-face-edge-dissolve>` or :ref:`bpy.ops.mesh.dissolve_faces`;
   this is not limited to quads.
