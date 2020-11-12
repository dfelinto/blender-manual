.. _bpy.ops.mesh.fill:
.. _modeling-meshes-editing-fill:

****
Fill
****

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Face --> Fill`
   :Hotkey:    :kbd:`Alt-F`

The *Fill* option will create *triangular* faces from any group of selected edges
or vertices, as long as they form one or more complete perimeters.

Beauty
   Arrange the new triangles nicely.

.. figure:: /images/modeling_meshes_editing_face_fill_example.png
   :width: 300px

   Filled using fill.

Note, unlike creating n-gons, *Fill* supports holes.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_face_fill_holes.png
          :width: 320px

          A closed perimeter of edges with holes.

     - .. figure:: /images/modeling_meshes_editing_face_fill_holes-filled.png
          :width: 320px

          Filled using fill.
