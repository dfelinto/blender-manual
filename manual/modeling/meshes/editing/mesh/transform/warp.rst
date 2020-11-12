
****
Warp
****

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Modes
   :Menu:      :menuselection:`Object/Mesh/Curve/Surface --> Transform --> Warp`

.. figure:: /images/modeling_meshes_editing_mesh_transform_warp_operator-panel.png
   :align: right

   Warp tool options.

The *Warp* transformation takes selected elements and
warps them around the 3D cursor by a certain angle.
Note that this transformation is always dependent on the location of the 3D cursor.
The Pivot Point is not taken into account.
The results of the *Warp* transformation are also view dependent.


Usage
=====

.. list-table:: In this example, a plane is warped around the 3D cursor by the indicated number of degrees.

   * - .. figure:: /images/modeling_meshes_editing_mesh_transform_warp_mesh.png

          Before.

     - .. figure:: /images/modeling_meshes_editing_mesh_transform_warp_mesh-90.png

          Warp Angle 90.

   * - .. figure:: /images/modeling_meshes_editing_mesh_transform_warp_mesh-180.png

          Warp Angle 180.

     - .. figure:: /images/modeling_meshes_editing_mesh_transform_warp_mesh-360.png

          Warp Angle 360.


Cursor Position & View
----------------------

The location of the 3D cursor can be used to alter the results of the *Warp* transformation.
As can be seen from the example in this section, the *Warp* radius
is dependent on the distance of the cursor from the selected elements.
The greater the distance, the greater the radius.

The result of the *Warp* transform is also influenced by your current view.
The example in this section shows the results of a 180 degree *Warp* transform applied
to the same Plane mesh when in different views.

.. list-table:: This image shows how the Warp transform is influenced by the location of the cursor.

   * - .. figure:: /images/modeling_meshes_editing_mesh_transform_warp_mesh.png

          Before.

     - .. figure:: /images/modeling_meshes_editing_mesh_transform_warp_mesh-180.png

          Warp Angle 180.

   * - .. figure:: /images/modeling_meshes_editing_mesh_transform_warp_mesh-cursor.png

          Before.

     - .. figure:: /images/modeling_meshes_editing_mesh_transform_warp_mesh-cursor-180.png

          Warp Angle 180.

.. list-table:: This image shows the influence of the current view.

   * - .. figure:: /images/modeling_meshes_editing_mesh_transform_warp_view-1.png

          Before.

     - .. figure:: /images/modeling_meshes_editing_mesh_transform_warp_view-2.png

          Warp Angle 180 in XZ view.

   * - .. figure:: /images/modeling_meshes_editing_mesh_transform_warp_view-3.png

          Warp Angle 180 in YZ view.

     - .. figure:: /images/modeling_meshes_editing_mesh_transform_warp_view-4.png

          Warp Angle 180 in User view.

.. note:: Warping text

   If you want to warp text, you will need to convert it from a text object to mesh
   using :ref:`object-convert-to`.


Example
=======

.. figure:: /images/modeling_meshes_editing_mesh_transform_warp_text.jpg

   Text wrapped around logo.

This was made by creating the Blender logo and text as separate objects.
The text was converted to a mesh and then warped around the Blender logo.
