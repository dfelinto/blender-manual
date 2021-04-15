.. _bpy.ops.transform.shrink_fatten:
.. _tool-mesh-shrink-fatten:

*************
Shrink Fatten
*************

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Tool:      :menuselection:`Toolbar --> Shrink/Fatten`
   :Menu:      :menuselection:`Mesh --> Transform --> Shrink Fatten`
   :Shortcut:  :kbd:`Alt-S`

This tool moved selected vertices/edges/faces along their own normal
(perpendicular to the face), which, on "standard normal meshes", will shrink/fatten them.

This transform tool does not take into account the pivot point or transform orientation.

Offset Even :kbd:`S`, :kbd:`Alt`
   Scale the offset to give it a more even thickness.
   A greater offset factor is obtained vertices, which share faces, forming a more acute angle.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_mesh_transform_shrink-fatten_before.png
          :width: 200px

          Mesh before shrink/flatten.

     - .. figure:: /images/modeling_meshes_editing_mesh_transform_shrink-fatten_inflate-positive.png
          :width: 200px

          Inflated using a positive value.

     - .. figure:: /images/modeling_meshes_editing_mesh_transform_shrink-fatten_inflate-negative.png
          :width: 200px

          Shrunk using a negative value.
