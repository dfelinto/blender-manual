

..    TODO/Review: {{review|}} .

Bevel Modifier
==============


.. admonition:: Reference
   :class: refbox

   | Mode:     Object mode
   | Panel:    Properties Window → Context Button :guilabel:`Modifiers`

   .. figure:: /images/CZ_Modifier_ContextButton.jpg


.. figure:: /images/Manual_-_Bevel_Modifier_Default_Cube.jpg
   :width: 250px
   :figwidth: 250px

   Default bevel.


The :guilabel:`Bevel` modifier adds the ability to bevel the edges of the mesh it is applied
to, allowing control of how and where the bevel is applied to the mesh.

The :guilabel:`Bevel` modifier is a non-destructive alternative to the :doc:`Bevel Operation <modeling/meshes/editing/subdividing/bevel>` in mesh editing mode.


+--------------------------------------------------+------------------------------------------------+
+.. figure:: /images/Manual_-_Unbevelled_Square.jpg|.. figure:: /images/Manual_-_Bevelled_Square.jpg+
+   :width: 150px                                  |   :width: 150px                                +
+   :figwidth: 150px                               |   :figwidth: 150px                             +
+                                                  |                                                +
+   Unbeveled square.                              |   Beveled square.                              +
+--------------------------------------------------+------------------------------------------------+


The picture *Unbeveled square* shows a square which has unbeveled edges as the angles

between the corners of the square are 90- (perpendicular).

The picture *Beveled square* shows a square which has beveled corners.

Although the two pictures show 2D squares,
the Blender :guilabel:`Bevel` modifier can work on both 2D and 3D meshes of almost any shape,
not just squares and cubes…

The picture *Default bevel* shows a Blender 3D cube with a bevel applied using just the
default :guilabel:`Bevel` modifier settings.


Options
-------


.. figure:: /images/Manual_CZ_BevelModifier_None_IF.jpg

   Bevel modifier panel.


Width
~~~~~


The :guilabel:`Width` numeric field controls the width/amount of the bevel applied to the base
mesh. It can range from **0.0** (no bevel applied) to **1.0** (Blender Units).
This value is in fact the "backing up" of the two new edges relatively to the original
(beveled) one, along the two concerned faces.


.. admonition:: Note
   :class: note

   When using Metric or Imperial units the :guilabel:`Width` value has a unit. E.g. when 1 Blenderunit is 1m a useful value is between 0cm and 100cm. When it seems that decreasing the :guilabel:`Width` has no effect anymore check if the unit changed to m instead of cm.


+-----------------------------------------------------------------+
+.. figure:: /images/Manual_-_Bevel_Modifier_-_3_Beveled_Cubes.jpg+
+   :width: 610px                                                 +
+   :figwidth: 610px                                              +
+                                                                 +
+   Three Cubes with 0.1, 0.3 and 0.5 bevel Widths.               +
+-----------------------------------------------------------------+


Segments
~~~~~~~~

Set the number of bevel segments for round edges/verts.


Only Vertices
~~~~~~~~~~~~~


The :guilabel:`Only Vertices` button alters the way in which a bevel is applied to the mesh.
When it is active, only the areas near vertices are beveled; the edges are left unbeveled.


+--------------------------------------------------------------------------------------+
+.. figure:: /images/Manual_-_3_Beveled_Cubes_Vertices_Only.jpg                        +
+   :width: 610px                                                                      +
+   :figwidth: 610px                                                                   +
+                                                                                      +
+   Three cubes with 0.1, 0.3 and 0.5' bevel Widths, with Only Vertices option enabled.+
+--------------------------------------------------------------------------------------+


Limit Method
~~~~~~~~~~~~


This section of the :guilabel:`Bevel` modifier is used to control where and when a bevel is
applied to the underlying mesh. The first row of three buttons (mutually exclusive)
controls the algorithm used, and might add some extra options.
:guilabel:`None`
   This button will apply the :guilabel:`Bevel` modifier to the whole underlying mesh, without any way to prevent the bevel on some edges/vertices.


.. figure:: /images/Manual_CZ_BevelModifier_Angle_IF.jpg

   Bevel modifier with the Angle limit enabled.


:guilabel:`Angle`

   This button will only bevel edges where faces make sharp angles. When selected, it displays the :guilabel:`Angle` numeric field, used to set the angle above which an edge will be beveled (it is in fact the complementary angle, i.e. ``180- -(angle between faces)``\ ). When the angle between meeting faces is less than the angle in the slider box, a bevel on those specific edges will not be applied. Similarly, when the angle between two edges is less than this limit, the vertex is not beveled.


.. figure:: /images/Manual_CZ_BevelModifier_Weight_IF.jpg

   Bevel modifier with Weight button active.


:guilabel:`Weight`
   Use bevel weights to determine how much bevel is applied; apply them separately in vert/edge select mode. See :doc:`Here <modeling/meshes/editing/edges>` about adjusting bevel weights. The three options specify what edge weight to use for weighting a vertex.
   :guilabel:`Average`
      Uses the average bevel weight at the vertex
   :guilabel:`Sharpest`
      Uses the smallest bevel weight at the vertex
   :guilabel:`Largest`
      Uses the largest bevel weight at the vertex
:guilabel:`Vertex Group`
      Use a vertex group to determine which parts of the mesh get beveled.


