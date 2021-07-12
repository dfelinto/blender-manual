.. _bpy.ops.mesh.inset:
.. _tool-mesh-inset_faces:

***********
Inset Faces
***********

.. reference::

   :Mode:      Edit Mode
   :Tool:      :menuselection:`Toolbar --> Inset Faces`
   :Menu:      :menuselection:`Face --> Inset Faces`
   :Shortcut:  :kbd:`I`

This tool takes the currently selected faces and creates an inset of them,
with adjustable thickness and depth. Think of it as like creating an edge loop,
but relative to the selected edges, even in complex meshes.

The tool is modal, such that when you activate it,
you may adjust the thickness with your mouse position.
You may also adjust the depth of the inset during the modal operation by holding :kbd:`Ctrl`.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_face_inset-faces_before.png
          :width: 320px

          Selection to inset.

     - .. figure:: /images/modeling_meshes_editing_face_inset-faces_after.png
          :width: 320px

          Selection with inset.


Options
=======

.. figure:: /images/modeling_meshes_editing_face_inset-faces_options.png
   :align: right

   Inset operator options.

Boundary :kbd:`B`
   Determines whether open edges will be inset or not.
Offset Even
   Scale the offset to give a more even thickness.
Offset Relative
   Scale the offset by lengths of surrounding geometry.
Edge Rail
   Created vertices slide along the original edges of the inner geometry, instead of the normals.
Thickness
   Set the size of the offset.
Depth :kbd:`Ctrl`
   Raise or lower the newly inset faces to add depth.
Outset :kbd:`O`
   Create an outset rather than an inset.
   Causes the geometry to be created surrounding selection (instead of within).
Select Outer
   Toggle which side of the inset is selected after the operation.
Individual :kbd:`I`
   By default the Inset tool operates on the region around selected faces,
   but with this option each selected face can be inset on its own.
Interpolate
   Interpolate mesh data: e.g. UVs, vertex colors, weights, etc.
