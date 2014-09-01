
Laplacian Smooth and Shape Enhanced Modifier
********************************************

.. admonition:: Reference
   :class: refbox

   | Mode:     Any mode
   | Panel:    :guilabel:`Modifiers`


Description
===========

The :guilabel:`Laplacian Smooth` and :guilabel:`Shape Enhanced` modifier allows you to reduce
noise on a mesh's surface with minimal changes to its shape, and exaggerates a shape using a
Laplacian smoothing modifier in the reverse direction using a single parameter,
The :guilabel:`factor` , that supports negative and positive values:
**negative for enhancement** and **positive for smoothing**.

The :guilabel:`Shape enhanced` method exaggerates a shape using a Laplacian smoothing operator
in the reverse direction.

The :guilabel:`Laplacian Smooth` is useful for objects that have been reconstructed from the
real world containing undesirable noise. A mesh smoothing tool removes noise while still
preserving desirable geometry as well as the shape of the original model.

The :guilabel:`Laplacian Smooth` and :guilabel:`Shape Enhanced` modifier is based on a
curvature flow Laplace Beltrami operator in a diffusion equation.

The Catmull-Clark subdivision surfaces together with :guilabel:`Shape Enhancement` can easily
generate families of shapes by changing a single parameter.


Options
=======

.. figure:: /images/Apinzonf_Diagram_Modifier_Panel.jpg
   :width: 369px
   :figwidth: 369px

   Laplacian Smooth and Shape Enhanced modifier


:guilabel:`Repeat`
   Repetitions allow you to run the Laplacian smoothing and Shape Enhancement multiple times. Each repetition causes the flow curvature of the mesh to be recalculated again, and as a result it removes more noise at every new iteration in Laplacian smoothing cases (positive factor) using a small :guilabel:`Factor` < ``1.0``. In a Shape Enhancement case (negative Factor) multiple iterations can magnify the noise.

- :guilabel:`Repeat`: ``0`` Disables the modifier and no repetition is made.
- :guilabel:`Repeat`: ``1`` to ``200`` Number of repetitions to be done by the modifier. Be careful with large numbers of vertices, because it will take a lot of time to execute all iterations.


+---------------------------------------------------------------+---------------------------------------------------------------+---------------------------------------------------------------+----------------------------------------------------------------+
+.. figure:: /images/Apinzonf_GSOC_2012_Diagram_repeat0.jpg     |.. figure:: /images/Apinzonf_GSOC_2012_Diagram_repeat1.jpg     |.. figure:: /images/Apinzonf_GSOC_2012_Diagram_repeat5.jpg     |.. figure:: /images/Apinzonf_GSOC_2012_Diagram_repeat10.jpg     +
+   :width: 150px                                               |   :width: 150px                                               |   :width: 150px                                               |   :width: 150px                                                +
+   :figwidth: 150px                                            |   :figwidth: 150px                                            |   :figwidth: 150px                                            |   :figwidth: 150px                                             +
+                                                               |                                                               |                                                               |                                                                +
+   Repeat: 0, Lambda_Factor: 0.5                               |   Repeat: 1, Lambda_Factor: 0.5                               |   Repeat: 5, Lambda_Factor: 0.5                               |   Repeat: 10, Lambda_Factor: 0.5                               +
+---------------------------------------------------------------+---------------------------------------------------------------+---------------------------------------------------------------+----------------------------------------------------------------+
+.. figure:: /images/Apinzonf_GSOC_2012_Diagram_cube_repeat0.jpg|.. figure:: /images/Apinzonf_GSOC_2012_Diagram_cube_repeat1.jpg|.. figure:: /images/Apinzonf_GSOC_2012_Diagram_cube_repeat5.jpg|.. figure:: /images/Apinzonf_GSOC_2012_Diagram_cube_repeat10.jpg+
+   :width: 150px                                               |   :width: 150px                                               |   :width: 150px                                               |   :width: 150px                                                +
+   :figwidth: 150px                                            |   :figwidth: 150px                                            |   :figwidth: 150px                                            |   :figwidth: 150px                                             +
+                                                               |                                                               |                                                               |                                                                +
+   Repeat: 0, Lambda_Factor: 2.0                               |   Repeat: 1, Lambda_Factor: 2.0                               |   Repeat: 5, Lambda_Factor: 2.0                               |   Repeat: 10, Lambda_Factor: 2.0                               +
+---------------------------------------------------------------+---------------------------------------------------------------+---------------------------------------------------------------+----------------------------------------------------------------+
+.. figure:: /images/Apinzonf_Diagram_camel_repeat0.jpg         |.. figure:: /images/Apinzonf_Diagram_camel_repeat1.jpg         |.. figure:: /images/Apinzonf_Diagram_camel_repeat5.jpg         |.. figure:: /images/Apinzonf_Diagram_camel_repeat10.jpg         +
+   :width: 150px                                               |   :width: 150px                                               |   :width: 150px                                               |   :width: 150px                                                +
+   :figwidth: 150px                                            |   :figwidth: 150px                                            |   :figwidth: 150px                                            |   :figwidth: 150px                                             +
+                                                               |                                                               |                                                               |                                                                +
+   Repeat: 0, Lambda_Factor: -0.5                              |   Repeat: 1, Lambda_Factor: -0.5                              |   Repeat: 5, Lambda_Factor: -0.5                              |   Repeat: 10, Lambda_Factor: -0.5                              +
+---------------------------------------------------------------+---------------------------------------------------------------+---------------------------------------------------------------+----------------------------------------------------------------+


:guilabel:`Lambda factor`
   The Lambda factor ranges from ``-1000.0`` to ``1000.0``; this factor controls the amount of displacement of every vertex along the curvature flow.


- :guilabel:`Lambda factor`: ``-1000.0`` to ``0.0`` Using a Lambda factor you can enhance the shape, preserving desirable geometry.
- :guilabel:`Lambda factor`: ``0.0`` Disables the modifier and no smoothing or enhancing is done.
- :guilabel:`Lambda factor`: ``0.0`` to ``5.0`` Using a small Lambda factor, you can remove noise from the shape without affecting desirable geometry.
- :guilabel:`Lambda factor`: ``5.0`` to ``1000.0`` Using a large Lambda factor you get smoothed versions of the shape at the cost of losing fine geometry details.


+-----------------------------------------------------------------+-----------------------------------------------------------------+------------------------------------------------------------------+------------------------------------------------------------------+
+.. figure:: /images/Apinzonf_GSOC_2012_Diagram_lambda0_0.jpg     |.. figure:: /images/Apinzonf_GSOC_2012_Diagram_lambda0_5.jpg     |.. figure:: /images/Apinzonf_GSOC_2012_Diagram_lambda2_5.jpg      |.. figure:: /images/Apinzonf_GSOC_2012_Diagram_lambda5_0.jpg      +
+   :width: 150px                                                 |   :width: 150px                                                 |   :width: 150px                                                  |   :width: 150px                                                  +
+   :figwidth: 150px                                              |   :figwidth: 150px                                              |   :figwidth: 150px                                               |   :figwidth: 150px                                               +
+                                                                 |                                                                 |                                                                  |                                                                  +
+   Repeat: 1, Lambda_Factor: 0.0                                 |   Repeat: 1, Lambda_Factor: 0.5                                 |   Repeat: 1, Lambda_Factor: 2.5                                  |   Repeat: 1, Lambda_Factor: 5.0                                  +
+-----------------------------------------------------------------+-----------------------------------------------------------------+------------------------------------------------------------------+------------------------------------------------------------------+
+.. figure:: /images/Apinzonf_GSOC_2012_Diagram_cube_lambda0_0.jpg|.. figure:: /images/Apinzonf_GSOC_2012_Diagram_cube_lambda1_0.jpg|.. figure:: /images/Apinzonf_GSOC_2012_Diagram_cube_lambda10_0.jpg|.. figure:: /images/Apinzonf_GSOC_2012_Diagram_cube_lambda50_0.jpg+
+   :width: 150px                                                 |   :width: 150px                                                 |   :width: 150px                                                  |   :width: 150px                                                  +
+   :figwidth: 150px                                              |   :figwidth: 150px                                              |   :figwidth: 150px                                               |   :figwidth: 150px                                               +
+                                                                 |                                                                 |                                                                  |                                                                  +
+   Repeat: 1, Lambda_Factor: 0.0                                 |   Repeat: 1, Lambda_Factor: 1.0                                 |   Repeat: 1, Lambda_Factor: 10.0                                 |   Repeat: 1, Lambda_Factor: 50.0                                 +
+-----------------------------------------------------------------+-----------------------------------------------------------------+------------------------------------------------------------------+------------------------------------------------------------------+
+.. figure:: /images/Apinzonf_Diagram_camel_lambda0_0.jpg         |.. figure:: /images/Apinzonf_Diagram_camel_lambda20_0.jpg        |.. figure:: /images/Apinzonf_Diagram_camel_lambda50_0.jpg         |.. figure:: /images/Apinzonf_Diagram_camel_lambda300_0.jpg        +
+   :width: 150px                                                 |   :width: 150px                                                 |   :width: 150px                                                  |   :width: 150px                                                  +
+   :figwidth: 150px                                              |   :figwidth: 150px                                              |   :figwidth: 150px                                               |   :figwidth: 150px                                               +
+                                                                 |                                                                 |                                                                  |                                                                  +
+   Repeat: 1, Lambda_Factor: 0.0                                 |   Repeat: 1, Lambda_Factor: -20.0                               |   Repeat: 1, Lambda_Factor: -50.0                                |   Repeat: 1, Lambda_Factor: -300.0                               +
+-----------------------------------------------------------------+-----------------------------------------------------------------+------------------------------------------------------------------+------------------------------------------------------------------+


:guilabel:`Lambda border`
   The Lambda border ranges from ``-1000.0`` to ``1000.0`` . Borders are treated differently. There is no way to calculate the curvature flow on them. For this reason the Lambda factor just smooths or enhances them.

- :guilabel:`Lambda border`: ``-1000.0`` to ``0.0`` Enhance the borders.
- :guilabel:`Lambda border`: ``0.0`` Disables the modifier and no smoothing on the borders is done.
- :guilabel:`Lambda border`: ``0.0`` to ``10.0`` Smooths the borders.
- :guilabel:`Lambda border`: ``10.0`` to ``1000.0`` Collapses the borders in a small circle.


+-----------------------------------------------------------------+-----------------------------------------------------------------+-----------------------------------------------------------------+------------------------------------------------------------------+
+.. figure:: /images/Apinzonf_GSOC_2012_Diagram_border0_0.jpg     |.. figure:: /images/Apinzonf_GSOC_2012_Diagram_border1_0.jpg     |.. figure:: /images/Apinzonf_GSOC_2012_Diagram_border2_5.jpg     |.. figure:: /images/Apinzonf_GSOC_2012_Diagram_border10_0.jpg     +
+   :width: 150px                                                 |   :width: 150px                                                 |   :width: 150px                                                 |   :width: 150px                                                  +
+   :figwidth: 150px                                              |   :figwidth: 150px                                              |   :figwidth: 150px                                              |   :figwidth: 150px                                               +
+                                                                 |                                                                 |                                                                 |                                                                  +
+   Repeat: 1, Lambda_Factor: 2.5, Lambda_Border: 0.0             |   Repeat: 1, Lambda_Factor: 2.5, Lambda_Border: 1.0             |   Repeat: 1, Lambda_Factor: 2.5, Lambda_Border: 2.5             |   Repeat: 1, Lambda_Factor: 2.5, Lambda_Border: 10.0             +
+-----------------------------------------------------------------+-----------------------------------------------------------------+-----------------------------------------------------------------+------------------------------------------------------------------+
+.. figure:: /images/Apinzonf_GSOC_2012_Diagram_cube_border0_0.jpg|.. figure:: /images/Apinzonf_GSOC_2012_Diagram_cube_border1_0.jpg|.. figure:: /images/Apinzonf_GSOC_2012_Diagram_cube_border5_0.jpg|.. figure:: /images/Apinzonf_GSOC_2012_Diagram_cube_border20_0.jpg+
+   :width: 150px                                                 |   :width: 150px                                                 |   :width: 150px                                                 |   :width: 150px                                                  +
+   :figwidth: 150px                                              |   :figwidth: 150px                                              |   :figwidth: 150px                                              |   :figwidth: 150px                                               +
+                                                                 |                                                                 |                                                                 |                                                                  +
+   Repeat: 1, Lambda_Factor: 20.0, Lambda_Border: 0.0            |   Repeat: 1, Lambda_Factor: 20.0, Lambda_Border: 1.0            |   Repeat: 1, Lambda_Factor: 20.0, Lambda_Border: 5.0            |   Repeat: 1, Lambda_Factor: 20.0, Lambda_Border: 20.0            +
+-----------------------------------------------------------------+-----------------------------------------------------------------+-----------------------------------------------------------------+------------------------------------------------------------------+
+.. figure:: /images/Apinzonf_Diagram_cup_border0_0.jpg           |.. figure:: /images/Apinzonf_Diagram_cup_border20_0.jpg          |.. figure:: /images/Apinzonf_Diagram_cup_border50_0.jpg          |.. figure:: /images/Apinzonf_Diagram_cup_border200_0.jpg          +
+   :width: 150px                                                 |   :width: 150px                                                 |   :width: 150px                                                 |   :width: 150px                                                  +
+   :figwidth: 150px                                              |   :figwidth: 150px                                              |   :figwidth: 150px                                              |   :figwidth: 150px                                               +
+                                                                 |                                                                 |                                                                 |                                                                  +
+   Repeat: 1, Lambda_Factor: -30.0, Lambda_Border: 0.0           |   Repeat: 1, Lambda_Factor: -30.0, Lambda_Border: -20.0         |   Repeat: 1, Lambda_Factor: -30.0, Lambda_Border: -50.0         |   Repeat: 1, Lambda_Factor: -30.0, Lambda_Border: -200.0         +
+-----------------------------------------------------------------+-----------------------------------------------------------------+-----------------------------------------------------------------+------------------------------------------------------------------+


:guilabel:`X`, :guilabel:`Y`, :guilabel:`Z`
   Toggle buttons to enable/disable hard constraints in the X, Y and/or Z axis directions.


+------------------------------------------------------------+----------------------------------------------------------------+---------------------------------------------------------------+--------------------------------------------------------------+
+.. figure:: /images/Apinzonf_GSOC_2012_Diagram_cube_axis.jpg|.. figure:: /images/Apinzonf_GSOC_2012_Diagram_cube_axis_xyz.jpg|.. figure:: /images/Apinzonf_GSOC_2012_Diagram_cube_axis_xy.jpg|.. figure:: /images/Apinzonf_GSOC_2012_Diagram_cube_axis_x.jpg+
+   :width: 150px                                            |   :width: 150px                                                |   :width: 150px                                               |   :width: 150px                                              +
+   :figwidth: 150px                                         |   :figwidth: 150px                                             |   :figwidth: 150px                                            |   :figwidth: 150px                                           +
+                                                            |                                                                |                                                               |                                                              +
+   Repeat: 1, Lambda_Factor: 40.0, X, Y, Z: Unselected      |   Repeat: 1, Lambda_Factor: 40.0, X, Y, Z: Selected            |   Repeat: 1, Lambda_Factor: 40.0, X, Y: Selected              |   Repeat: 1, Lambda_Factor: 40.0, X: Selected                +
+------------------------------------------------------------+----------------------------------------------------------------+---------------------------------------------------------------+--------------------------------------------------------------+
+.. figure:: /images/Apinzonf_GSOC_2012_Diagram_t_axis.jpg   |.. figure:: /images/Apinzonf_GSOC_2012_Diagram_t_axis_xyz.jpg   |.. figure:: /images/Apinzonf_GSOC_2012_Diagram_t_axis_xy.jpg   |.. figure:: /images/Apinzonf_GSOC_2012_Diagram_t_axis_x.jpg   +
+   :width: 150px                                            |   :width: 150px                                                |   :width: 150px                                               |   :width: 150px                                              +
+   :figwidth: 150px                                         |   :figwidth: 150px                                             |   :figwidth: 150px                                            |   :figwidth: 150px                                           +
+                                                            |                                                                |                                                               |                                                              +
+   Repeat: 1, Lambda_Factor: 20.0, X, Y, Z: Unselected      |   Repeat: 1, Lambda_Factor: 20.0, X, Y, Z: Selected            |   Repeat: 1, Lambda_Factor: 20.0, X, Y: Selected              |   Repeat: 1, Lambda_Factor: 20.0, X: Selected                +
+------------------------------------------------------------+----------------------------------------------------------------+---------------------------------------------------------------+--------------------------------------------------------------+


:guilabel:`Preserve Volume`
   The smoothing process can produce shrinkage. That is significant for large :guilabel:`Lambda factor` or large :guilabel:`Repeat` values; to reduce that effect you can use this option.

+-------------------------------------------------------------------+------------------------------------------------------------------+--------------------------------------------------------------------+-------------------------------------------------------------------+
+.. figure:: /images/Apinzonf_GSOC_2012_Diagram_cube_volumeFalse.jpg|.. figure:: /images/Apinzonf_GSOC_2012_Diagram_cube_volumeTrue.jpg|.. figure:: /images/Apinzonf_GSOC_2012_Diagram_cube_volume2False.jpg|.. figure:: /images/Apinzonf_GSOC_2012_Diagram_cube_volume2True.jpg+
+   :width: 150px                                                   |   :width: 150px                                                  |   :width: 150px                                                    |   :width: 150px                                                   +
+   :figwidth: 150px                                                |   :figwidth: 150px                                               |   :figwidth: 150px                                                 |   :figwidth: 150px                                                +
+                                                                   |                                                                  |                                                                    |                                                                   +
+   Repeat: 1, Lambda_Factor: 40.0, Volume Preservation: Unselected |   Repeat: 1, Lambda_Factor: 40.0, Volume Preservation: Selected  |   Repeat: 1, Lambda_Factor: 20.0, Volume Preservation: Unselected  |   Repeat: 1, Lambda_Factor: 20.0, Volume Preservation: Selected   +
+-------------------------------------------------------------------+------------------------------------------------------------------+--------------------------------------------------------------------+-------------------------------------------------------------------+


:guilabel:`Vertex Group`
   A vertex group name, to constrain the effect to a group of vertices only. Allows for selective, real-time smoothing or enhancing, by painting vertex weights.


+-----------------------------------------------------------+------------------------------------------------------------+--------------------------------------------------------------+---------------------------------------------------------------+
+.. figure:: /images/Apinzonf_GSOC_2012_Diagram_repeat0.jpg |.. figure:: /images/Apinzonf_GSOC_2012_Diagram_lambda2_5.jpg|.. figure:: /images/Apinzonf_GSOC_2012_Diagram_femme_paint.jpg|.. figure:: /images/Apinzonf_GSOC_2012_Diagram_femme_wgroup.jpg+
+   :width: 150px                                           |   :width: 150px                                            |   :width: 150px                                              |   :width: 150px                                               +
+   :figwidth: 150px                                        |   :figwidth: 150px                                         |   :figwidth: 150px                                           |   :figwidth: 150px                                            +
+                                                           |                                                            |                                                              |                                                               +
+   Repeat: 1, Lambda_Factor: 0.0                           |   Repeat: 1, Lambda_Factor: 2.5                            |   Weight Paint, Vertex Group: Group                          |   Repeat: 1, Lambda_Factor: 2.5, Vertex Group: Group          +
+-----------------------------------------------------------+------------------------------------------------------------+--------------------------------------------------------------+---------------------------------------------------------------+
+.. figure:: /images/Apinzonf_GSOC_2012_Diagram_t_normal.jpg|.. figure:: /images/Apinzonf_GSOC_2012_Diagram_t_smooth.jpg |.. figure:: /images/Apinzonf_GSOC_2012_Diagram_t_paint.jpg    |.. figure:: /images/Apinzonf_GSOC_2012_Diagram_t_wgroup.jpg    +
+   :width: 150px                                           |   :width: 150px                                            |   :width: 150px                                              |   :width: 150px                                               +
+   :figwidth: 150px                                        |   :figwidth: 150px                                         |   :figwidth: 150px                                           |   :figwidth: 150px                                            +
+                                                           |                                                            |                                                              |                                                               +
+   Repeat: 1, Lambda_Factor: 0.0                           |   Repeat: 1, Lambda_Factor: 20.0                           |   Weight Paint, Vertex Group: Group                          |   Repeat: 1, Lambda_Factor: 20.0, Vertex Group: Group         +
+-----------------------------------------------------------+------------------------------------------------------------+--------------------------------------------------------------+---------------------------------------------------------------+
+.. figure:: /images/Apinzonf_Diagram_camel_vertex0.jpg     |.. figure:: /images/Apinzonf_Diagram_camel_vertex1.jpg      |.. figure:: /images/Apinzonf_Diagram_camel_vertex2.jpg        |.. figure:: /images/Apinzonf_Diagram_camel_vertex3.jpg         +
+   :width: 150px                                           |   :width: 150px                                            |   :width: 150px                                              |   :width: 150px                                               +
+   :figwidth: 150px                                        |   :figwidth: 150px                                         |   :figwidth: 150px                                           |   :figwidth: 150px                                            +
+                                                           |                                                            |                                                              |                                                               +
+   Repeat: 1, Lambda_Factor: 0.0                           |   Repeat: 1, Lambda_Factor: -240.0                         |   Weight Paint, Vertex Group: Group                          |   Repeat: 1, Lambda_Factor: -240.0, Vertex Group: Group       +
+-----------------------------------------------------------+------------------------------------------------------------+--------------------------------------------------------------+---------------------------------------------------------------+


:guilabel:`Normalized Version`
   The modifier has two versions, the normalized version that does not depend on face size, and the other that is dependent on the face size. Be careful with the face-size-dependent version, which can produce peaks.


+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
+.. figure:: /images/Apinzonf_Diagram_monkey_normalized0.jpg|.. figure:: /images/Apinzonf_Diagram_monkey_normalized1.jpg|.. figure:: /images/Apinzonf_Diagram_monkey_normalized2.jpg|.. figure:: /images/Apinzonf_Diagram_monkey_normalized3.jpg+
+   :width: 150px                                           |   :width: 150px                                           |   :width: 150px                                           |   :width: 150px                                           +
+   :figwidth: 150px                                        |   :figwidth: 150px                                        |   :figwidth: 150px                                        |   :figwidth: 150px                                        +
+                                                           |                                                           |                                                           |                                                           +
+   Normalized Version: Selected, Lambda_Factor: 0.0        |   Normalized Version: Selected, Lambda_Factor: -50        |   Normalized Version: Unselected, Lambda_Factor: -50      |   Normalized Version: Unselected, Lambda_Factor: -250     +
+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+


Hints
=====

Meshes with a great number of vertices, more than ten thousand (10,000),
may take several minutes for processing; you can use small portions of the mesh for testing
before executing the modifier on the entire model.


Examples
========

+-------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
+.. figure:: /images/Apinzonf_GSOC_2012_Diagram_repeat0.jpg                                                         |.. figure:: /images/Apinzonf_Shape_Enhanced_Camel.jpg                                                              +
+   :width: 150px                                                                                                   |   :width: 240px                                                                                                   +
+   :figwidth: 150px                                                                                                |   :figwidth: 240px                                                                                                +
+                                                                                                                   |                                                                                                                   +
+   Femme front view                                                                                                |   Camel Enhanced                                                                                                  +
+   `Femme Front blend file <http://wiki.blender.org/index.php/Media:Apinzonf_GSOC_2012_Media_femme_front.blend>`__ |   `Cube Smooth blend file <http://wiki.blender.org/index.php/Media:Apinzonf_GSOC_2012_Media_cube_smooth.blend>`__ +
+-------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+


See Also
========

- :doc:`Smooth Modifier </modifiers/deform/smooth>`


