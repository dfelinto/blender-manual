.. _bpy.ops.mesh.solidify:

**************
Solidify Faces
**************

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Face --> Solidify Faces`

This takes a selection of faces and solidifies them by extruding them
uniformly to give volume to a :term:`Non-manifold` surface.
This is also available as a :doc:`Modifier </modeling/modifiers/generate/solidify>`.
After using the tool, you can set the offset distance in the :ref:`ui-undo-redo-adjust-last-operation` panel.

Thickness
   Amount to offset the newly created surface.
   Positive values offset the surface inward relative to the normals direction.
   Negative values offset outward.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_face_solidify-faces_before.png
          :width: 200px

          Mesh before solidify operation.

     - .. figure:: /images/modeling_meshes_editing_face_solidify-faces_after.png
          :width: 200px

          Solidify with a positive thickness.

     - .. figure:: /images/modeling_meshes_editing_face_solidify-faces_after2.png
          :width: 200px

          Solidify with a negative thickness.
