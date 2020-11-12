.. _bpy.ops.mesh.separate:
.. _object-separate:

********
Separate
********

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Separate`
   :Hotkey:    :kbd:`P`

At some point, you will come to a time when you need to cut parts away from a mesh to be separate.

To separate an object, the vertices (or faces) must be selected and then separated,
though there are several different ways to do this.

.. figure:: /images/modeling_meshes_editing_mesh_separate_example.png

   Suzanne dissected neatly.

Selection
   Separates the selected elements.
By Material
   Separates fragments based on the materials assigned to the different faces.
By Loose Parts
   Creates one object for every independent (disconnected) fragment of the original mesh.

.. seealso::

   :ref:`Joining objects <object-join>`.
