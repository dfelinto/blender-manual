.. _bpy.ops.mesh.extrude_faces_move:
.. _tool-mesh-extrude_individual:

************************
Extrude Individual Faces
************************

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Tool:      :menuselection:`Toolbar --> Extrude Region --> Extrude Individual`
   :Menu:      :menuselection:`Mesh --> Extrude --> Individual Faces`
   :Hotkey:    :kbd:`Alt-E`

This tool allows you to extrude a selection of multiple faces as individuals, instead of as a region.
The faces are extruded along their own normals, rather than their average.
This has several consequences: first, "internal" edges
(i.e. edges between two selected faces) are no longer deleted (the original faces are).

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_face_extrude-individual-faces_multi.png
          :width: 200px

          Selection of multiple faces.

     - .. figure:: /images/modeling_meshes_editing_face_extrude-individual-faces_multi-region.png
          :width: 200px

          Extruded using extrude region.

     - .. figure:: /images/modeling_meshes_editing_face_extrude-individual-faces_multi-individual.png
          :width: 200px

          Extruded using Extrude Individual.
