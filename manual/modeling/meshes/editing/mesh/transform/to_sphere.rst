.. _bpy.ops.transform.tosphere:
.. _tool-transform-to_sphere:

*********
To Sphere
*********

.. admonition:: Reference
   :class: refbox

   :Mode:      Object and Edit Modes
   :Menu:      :menuselection:`Mesh --> Transform --> To Sphere`
   :Hotkey:    :kbd:`Shift-Alt-S`

The *To Sphere* transformation will give the selection spherical qualities.
The Fig. :ref:`fig-mesh-deform-to-sphere-monkey` below shows the results of applying
the *To Sphere* transformation to the monkey mesh.

.. _fig-mesh-deform-to-sphere-monkey:

.. figure:: /images/modeling_meshes_editing_mesh_transform_to-sphere_suzanne-spherical.png

   Monkey with increasing sphericity.

   The sequence above shows a monkey mesh with
   a 0, 0.25 (25%), 0.5 (50%) and 1 (100%) To Sphere transform applied.


Usage
=====

.. figure:: /images/modeling_meshes_editing_mesh_transform_to-sphere_operator-panel.png

   To Sphere Factor.

As can be seen in the below image, the result
will be smoother and more spherical when there are more mesh elements available to work with.

.. figure:: /images/modeling_meshes_editing_mesh_transform_to-sphere_cubes-spherical.png

   To Sphere applied to cubes with different subdivision levels.

   In this image sequence, To Sphere was applied to the entire cube
   at levels of 0, 0.25 (25%), 0.5 (50%) and 1 (100%) respectively.

The *To Sphere* transform will generate different results depending on the number
and arrangement of elements that were selected (as shown by the below image).

.. figure:: /images/modeling_meshes_editing_mesh_transform_to-sphere_other-spherical.png

   To Sphere applied to different selections.
