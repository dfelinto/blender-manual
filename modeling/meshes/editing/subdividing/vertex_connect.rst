
..    TODO/Review: {{review|}} .


Vertex Connect
==============


.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     Mesh → Vertices → Connect
   | Hotkey:   :kbd:`J`


This tool joins selected vertices by edges, The main difference between this and creating
edges is that faces are split by the newly joined vertices.

When many vertices are selected, faces will be split by their selected vertices.

+--------------------------------------------------------+-------------------------------------------------------+
+.. figure:: /images/bmesh_connect_verts_multi_before.jpg|.. figure:: /images/bmesh_connect_verts_multi_after.jpg+
+   :width: 200px                                        |   :width: 200px                                       +
+   :figwidth: 200px                                     |   :figwidth: 200px                                    +
+                                                        |                                                       +
+   Before                                               |   After                                               +
+--------------------------------------------------------+-------------------------------------------------------+


When there are only 2 vertices selected, a cut will be made across unselected faces,
a little like the knife tool; however this is limited to straight cuts across connected faces.

+-------------------------------------------------------+------------------------------------------------------+
+.. figure:: /images/bmesh_connect_verts_pair_before.jpg|.. figure:: /images/bmesh_connect_verts_pair_after.jpg+
+   :width: 200px                                       |   :width: 200px                                      +
+   :figwidth: 200px                                    |   :figwidth: 200px                                   +
+                                                       |                                                      +
+   Before                                              |   After                                              +
+-------------------------------------------------------+------------------------------------------------------+
