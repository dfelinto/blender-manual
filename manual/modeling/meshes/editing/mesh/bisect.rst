.. _bpy.ops.mesh.bisect:
.. _tool-mesh-bisect:

******
Bisect
******

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Tool:      :menuselection:`Toolbar --> Knife --> Bisect`
   :Menu:      :menuselection:`Mesh --> Bisect`

The Bisect tool is a quick way to cut a mesh in two along a custom plane.

Use :kbd:`LMB` click and drag to draw cut line.
Once the cut is done the :ref:`ui-undo-redo-adjust-last-operation` panel gives a few options.

Plane Point, Plane Normal
   The plane can be numerically adjusted for precise values.
Fill
   Cuts can optionally fill in the holes created,
   with materials, UV maps, and vertex colors based on the surrounding geometry.
Clear Inner, Clear Outer
   Cuts may remove geometry on one side.
Axis Threshold
   Cut along the straight plane or along the existing geometry below the distance from the plane.


Examples
========

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_mesh_bisect_example.png
          :width: 300px

          Example of a common use of bisect.

     - .. figure:: /images/modeling_meshes_editing_mesh_bisect_uv.jpg
          :width: 320px

          Example of bisect with the fill option enabled.
