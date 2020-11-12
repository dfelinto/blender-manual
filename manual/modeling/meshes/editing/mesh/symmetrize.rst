.. _bpy.ops.mesh.symmetrize:

**********
Symmetrize
**********

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Symmetrize`

The *Symmetrize* tool is a quick way to make a mesh symmetrical.
*Symmetrize* works by cutting the mesh at the pivot point of the object,
and mirroring over the geometry in the specified axis, and merges the two halves together
(if they are connected). Also the mesh data is copied from one side to the other:
e.g. UVs, vertex colors, vertex weights.

Direction
   Specify the axis and direction of the effect. Can be any of the three axes,
   and either positive to negative, or negative to positive.
Threshold
   The vertices in this range will be snapped to the plane of symmetry.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_mesh_symmetrize_example-1.png
          :width: 320px

          Mesh before Symmetrize.

     - .. figure:: /images/modeling_meshes_editing_mesh_symmetrize_example-2.png
          :width: 320px

          Mesh after Symmetrize.

.. seealso::

   See :doc:`Mirror </modeling/meshes/editing/mesh/mirror>`
   for information on mirroring, which allows you to flip geometry across an axis.
