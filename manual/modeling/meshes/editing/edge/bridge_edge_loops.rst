.. _bpy.ops.mesh.bridge-edge-loops:
.. _modeling-meshes-editing-bridge-edge-loops:

*****************
Bridge Edge Loops
*****************

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Edge --> Bridge Edge Loops`

*Bridge Edge Loops* connects multiple edge loops with faces.

Connect Loops
   :Open Loop: Loops connected with open ends.
   :Closed Loop: Tries to connect to a circular loop (where the start and end are merged).
   :Loop Pairs: Connects each even count of loops individually.
Merge
   Merges edge loops rather than creating a new face.
Merge Factor
   Which edge loop the edges are merged to, a value of 0.5 will merge at a half-way point.
Twist
   Determines which vertices in both loops are connected to each other.
Number of Cuts
   The number of intermediate edge loops used to bridge the distance between two loops.
Interpolation
   Linear, Blend Path, Blend Surface
Smoothness
   Smoothness of the *Blend Path* and *Blend Surface*.
Profile Factor
   How much intermediary new edges are shrunk/expanded.
Profile Shape
   The shape of the new edges.
   See the :ref:`Proportional Editing <3dview-transform-control-proportional-edit-falloff>` page
   for a description of each option.


Examples
========

Simple example showing two closed edge loops.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_edge_bridge-edge-loops_simple-before.png
          :width: 320px

          Input.

     - .. figure:: /images/modeling_meshes_editing_edge_bridge-edge-loops_simple-after.png
          :width: 320px

          Bridge result.

Example of the Bridge tool between edge loops with different numbers of vertices.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_edge_bridge-edge-loops_uneven-before.png
          :width: 320px

          Input.

     - .. figure:: /images/modeling_meshes_editing_edge_bridge-edge-loops_uneven-after.png
          :width: 320px

          Bridge result.

Example using the Bridge tool to cut holes in face selections and connect them.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_edge_bridge-edge-loops_faces-before.png
          :width: 320px

          Input.

     - .. figure:: /images/modeling_meshes_editing_edge_bridge-edge-loops_faces-after.png
          :width: 320px

          Bridge result.

Example showing how Bridge tool can detect multiple loops and connect them in one step.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_edge_bridge-edge-loops_multi-before.png
          :width: 320px

          Input.

     - .. figure:: /images/modeling_meshes_editing_edge_bridge-edge-loops_multi-after.png
          :width: 320px

          Bridge result.

Example of the subdivision option and surface blending with UVs.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_edge_bridge-edge-loops_advanced-before.png
          :width: 320px

          Input.

     - .. figure:: /images/modeling_meshes_editing_edge_bridge-edge-loops_advanced-after.png
          :width: 320px

          Bridge result.
