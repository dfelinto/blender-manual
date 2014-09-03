
Laplacian Deform
****************

.. admonition:: Reference
   :class: refbox

   | Mode:     Any mode
   | Panel:    :guilabel:`Modifiers`


Description
===========

The :guilabel:`Laplacian Deform` modifier allows you to pose a mesh while preserving geometric
details of the surface.


The user defines a set of 'anchor' vertices, and then moves some of them around.
The modifier keeps the rest of the anchor vertices in fixed positions, and calculates the best
possible locations of all the remaining vertices to preserve the original geometric details.


This modifier captures the geometric details with the uses of differential coordinates. The
differential coordinates captures the local geometric information how curvature and direction
of a vertex based on its neighbors.


.. note::

   You must define a :guilabel:`Anchors Vertex Group`. Without a vertex group modifier does nothing.


Options
=======

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
+:guilabel:`Anchors Vertex Group`                                                                                                                                                                                                              |.. figure:: /images/Apinzonf_Diagram_Deform_Modifier_Panel_00.jpg            +
+   A vertex group name, to define the group of vertices that user uses to transform the model. The weight of each vertex does not affect the behavior of the modifier; the method only takes into account vertices with weight greater than 0.|   :width: 369px                                                             +
+                                                                                                                                                                                                                                              |   :figwidth: 369px                                                          +
+                                                                                                                                                                                                                                              |                                                                             +
+                                                                                                                                                                                                                                              |   Bind button is disabled until the user select a valid Anchors Vertex Group+
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+


+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
+:guilabel:`Bind`                                                                                                                                                                                                                      |.. figure:: /images/Apinzonf_Diagram_Deform_Modifier_Panel_01.jpg            +
+   The :guilabel:`Bind` button is what tells the :guilabel:`Laplacian Deform` modifier to actually capture the geometry details of the object, so that altering the anchors vertexes actually alters the shape of the deformed object.|   :width: 369px                                                             +
+                                                                                                                                                                                                                                      |   :figwidth: 369px                                                          +
+                                                                                                                                                                                                                                      |                                                                             +
+                                                                                                                                                                                                                                      |   Bind button is enabled when the user selected a valid Anchors Vertex Group+
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+


+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------+
+:guilabel:`Unbind`                                                                                                                                                    |.. figure:: /images/Apinzonf_Diagram_Deform_Modifier_Panel_02.jpg +
+   When a geometry details has been captured from a mesh, it can later be released by selecting the :guilabel:`Unbind` button which replaced the :guilabel:`Bind` one.|   :width: 369px                                                  +
+                                                                                                                                                                      |   :figwidth: 369px                                               +
+                                                                                                                                                                      |                                                                  +
+                                                                                                                                                                      |   Unbind button is enabled after the user pressed the Bind button+
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------+


Repeat
   Repetitions iteratively improve the solution found. The objective of the system is to find the rotation of the differential coordinates preserving the best possible geometric detail. The system retains details better if more repetitions are used. A small Repeat number is recommended, as the system takes a long time to calculate each repetition.


+------------------------------------------------------+-------------------------------------------------------+-------------------------------------------------------+-------------------------------------------------------+
+.. figure:: /images/Apinzonf_Deform_Cactus_09.jpg     |.. figure:: /images/Apinzonf_Deform_Cactus_repeat_1.jpg|.. figure:: /images/Apinzonf_Deform_Cactus_repeat_2.jpg|.. figure:: /images/Apinzonf_Deform_Cactus_repeat_5.jpg+
+   :width: 150px                                      |   :width: 150px                                       |   :width: 150px                                       |   :width: 150px                                       +
+   :figwidth: 150px                                   |   :figwidth: 150px                                    |   :figwidth: 150px                                    |   :figwidth: 150px                                    +
+                                                      |                                                       |                                                       |                                                       +
+   Original Model                                     |   Repeat: 1                                           |   Repeat: 2                                           |   Repeat: 5                                           +
+------------------------------------------------------+-------------------------------------------------------+-------------------------------------------------------+-------------------------------------------------------+
+.. figure:: /images/Apinzonf_Deform_Horse_repeat_0.jpg|.. figure:: /images/Apinzonf_Deform_Horse_repeat_1.jpg |.. figure:: /images/Apinzonf_Deform_Horse_repeat_2.jpg |.. figure:: /images/Apinzonf_Deform_Horse_repeat_10.jpg+
+   :width: 150px                                      |   :width: 150px                                       |   :width: 150px                                       |   :width: 150px                                       +
+   :figwidth: 150px                                   |   :figwidth: 150px                                    |   :figwidth: 150px                                    |   :figwidth: 150px                                    +
+                                                      |                                                       |                                                       |                                                       +
+   Original Model                                     |   Repeat: 1                                           |   Repeat: 2                                           |   Repeat: 10                                          +
+------------------------------------------------------+-------------------------------------------------------+-------------------------------------------------------+-------------------------------------------------------+


Hints
=====

If the mesh is dense, with a number of vertices greater than 100,000,
then it is possible that the nonlinear optimization system will fail.


+----------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
+:guilabel:`Vertex group My Anchors is not valid`                                                                      |.. figure:: /images/Apinzonf_Diagram_Deform_Modifier_Panel_05.jpg+
+   This message is displayed when a user deletes a Vertex Group or when the user changes the name of the Vertex Group.|   :width: 369px                                                 +
+                                                                                                                      |   :figwidth: 369px                                              +
+                                                                                                                      |                                                                 +
+                                                                                                                      |   My Anchors is the anchors vertex group for this example       +
+----------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+


+-------------------------------------------------------------------------+--------------------------------------------------------------------------------+
+:guilabel:`Verts changed from 954 to 955`                                |.. figure:: /images/Apinzonf_Diagram_Deform_Modifier_Panel_06.jpg               +
+   This message is displayed when a user add or delete verts to the mesh.|   :width: 369px                                                                +
+                                                                         |   :figwidth: 369px                                                             +
+                                                                         |                                                                                +
+                                                                         |   954 to 955 correspond to the number of verts changed by user before and after+
+-------------------------------------------------------------------------+--------------------------------------------------------------------------------+


+-------------------------------------------------------------------------+----------------------------------------------------------------------------------+
+:guilabel:`Edges changed from 2009 to 2010`                              |.. figure:: /images/Apinzonf_Diagram_Deform_Modifier_Panel_07.jpg                 +
+   This message is displayed when a user add or delete edges to the mesh.|   :width: 369px                                                                  +
+                                                                         |   :figwidth: 369px                                                               +
+                                                                         |                                                                                  +
+                                                                         |   2009 to 2010 correspond to the number of edges changed by user before and after+
+-------------------------------------------------------------------------+----------------------------------------------------------------------------------+


+-------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
+:guilabel:`The system did not find a solution`                                                   |.. figure:: /images/Apinzonf_Diagram_Deform_Modifier_Panel_09.jpg+
+   This message is displayed if the solver SuperLU did not find a solution for the linear system.|   :width: 369px                                                 +
+                                                                                                 |   :figwidth: 369px                                              +
+-------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+


Examples
========

+-----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
+.. figure:: /images/Apinzonf_Deform_Cactus_repeat_5.jpg                                                          |.. figure:: /images/Apinzonf_Deform_Horse_repeat_10.jpg                                                        +
+   :width: 150px                                                                                                 |   :width: 150px                                                                                               +
+   :figwidth: 150px                                                                                              |   :figwidth: 150px                                                                                            +
+                                                                                                                 |                                                                                                               +
+   Cactus example with Armature object                                                                           |   Horse example with Hook objects                                                                             +
+   `Download Cactus blend file <http://wiki.blender.org/index.php/Media:Apinzonf_Deform_Cactus_example1.blend>`__|   `Download Horse blend file <http://wiki.blender.org/index.php/Media:Apinzonf_Deform_Horse_example1.blend>`__+
+-----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+


History
=======

`Laplacian Surface Editing <http://igl.ethz.ch/projects/Laplacian-mesh-processing/Laplacian-mesh-editing/laplacian-mesh-editing.pdf>`__ is a method developed by Olga Sorkine and others in 2004. This method preserves geometric details as much as possible while the user makes editing operations. This method uses `differential coordinates <http://igl.ethz.ch/projects/Laplacian-mesh-processing/Laplacian-mesh-editing/diffcoords-editing.pdf>`__ corresponding to the difference between a vector and the weighted average of its neighbors to represent the local geometric detail of the mesh.


.. figure:: /images/Apinzonf_Diagram_differential_coordinate.jpg
   :width: 369px
   :figwidth: 369px

   Differential Coordinate


See Also
========

`Laplacian Surface Editing (Original paper) <http://igl.ethz.ch/projects/Laplacian-mesh-processing/Laplacian-mesh-editing/laplacian-mesh-editing.pdf>`__

`Differential Coordinates for Interactive Mesh Editing <http://igl.ethz.ch/projects/Laplacian-mesh-processing/Laplacian-mesh-editing/diffcoords-editing.pdf>`__