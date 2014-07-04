
Proportional Edit
=================

Proportional Edit is a way of transforming selected elements (such as vertices)
while having that transformation affect other nearby elements. For example, having the
movement of a single vertex cause the movement of unselected vertices within a given range.
Unselected vertices that are closer to the selected vertex will move more than those farther
from it (i.e. they will move proportionally relative to the location of the selected element).
Since proportional editing affects the nearby geometry,
it is very useful when you need to smoothly deform the surface of a dense mesh.


.. admonition:: Sculpting
   :class: note

   Blender also has :doc:`Sculpt Mode <modeling/meshes/editing/sculpt_mode>` that contains brushes and tools for proportionally editing a mesh without seeing the individual vertices.


Object mode
-----------

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object mode`
   | Menu:     Via the icon in the header indicated by the yellow square in the below image.

   .. figure:: /images/3D-interaction_Transform-Control_Proportional-Edit-proportional-edit-header-icon.jpg
   | Hotkey:   :kbd:`o`


Proportional editing is typically used in :guilabel:`Edit mode`, however,
it can also be used in :guilabel:`Object mode`. In :guilabel:`Object mode` the tool works on
entire objects rather than individual mesh components. In the image below,
the green cube is the active Object, while the red and blue cubes are located within the
proportional edit tool's radius of influence. When the green cube is moved to the right,
the other two cubes follow the movement.


.. figure:: /images/3D-interaction_Transform-Control_Proportional-Edit-object-mode.jpg

   Proportional editing in Object mode.


Edit mode
---------

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit mode`
   | Menu:     :menuselection:`Mesh --> Proportional Editing` and via the highlighted icon in the below image


   .. figure:: /images/3D-interaction_Transform-Control_Proportional-Edit-proportional-edit-header-icon-edit-mode.jpg
   | Hotkey:   :kbd:`o` / :kbd:`alt-o` / :kbd:`shift-o`


When working with dense geometry, it can become difficult to make subtle adjustments to the
vertices without causing visible lumps and creases in the model's surface. When you face
situations like this the proportional editing tool can be used to smoothly deform the surface
of the model.
This is done by the tool's automatic modification of unselected vertices within a given range.


.. figure:: /images/3D-interaction_Transform-Control_Proportional-Edit-edit-mode.jpg

   Proportional editing in Edit mode.


Influence
~~~~~~~~~

You can increase or decrease the radius of the proportional editing influence with the mouse
wheel :kbd:`wheelup` / :kbd:`wheeldown` or :kbd:`pgup` / :kbd:`pgdown`
respectively. As you change the radius,
the points surrounding your selection will adjust their positions accordingly.


.. figure:: /images/3D-interaction_Transform-Control_Proportional-Edit-influence.jpg

   Influence circle.


Options
~~~~~~~

.. figure:: /images/3D-interaction_Transform-Control_Proportional-Edit-proportional-edit-tool.jpg
   :width: 200px
   :figwidth: 200px

   Proportional Editing tool.


.. figure:: /images/3D-interaction_Transform-Control_Proportional-Edit-proportional-edit-falloff-options.jpg
   :width: 200px
   :figwidth: 200px

   Falloff menu.


The :guilabel:`Proportional Editing` mode menu is on the :guilabel:`3D View` header.

:guilabel:`Disable` (:kbd:`o` or :kbd:`Alt-o`)
   Proportional Editing is Off, only selected vertices will be affected.

:guilabel:`Enable` (:kbd:`o` or :kbd:`Alt-o`)
   Vertices other than the selected vertex are affected, within a defined radius.

:guilabel:`Projected (2D)`
   Depth along the view is ignored when applying the radius.


.. figure:: /images/3D-interaction_Transform-Control_Proportional-Edit-2D_Compare.jpg
   :width: 300px
   :figwidth: 300px

   The difference between regular and Projected (2D) proportional option (right).


:guilabel:`Connected` (:kbd:`alt-o`)
   Rather than using a radius only, the proportional falloff spreads via connected geometry. This means that you can
   proportionally edit the vertices in a finger of a hand without affecting the other fingers.
   While the other vertices are physically close (in 3D space),
   they are far away following the topological edge connections of the mesh.
   The icon will have a grey center when :guilabel:`Connected` is active.
   This mode is only available in :guilabel:`Edit mode`.


:guilabel:`Falloff`
   While you are editing, you can change the curve profile used by either using the :menuselection:`Mesh --> Proportional Falloff` submenu, using the toolbar icon (*Falloff menu*), or by pressing :kbd:`shift-o` to toggle between the various options.


+-------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
+.. figure:: /images/3D-interaction_Transform-Control_Proportional-Edit-falloff-constant.jpg|.. figure:: /images/3D-interaction_Transform-Control_Proportional-Edit-falloff-random.jpg+
+   :width: 300px                                                                           |   :width: 300px                                                                         +
+   :figwidth: 300px                                                                        |   :figwidth: 300px                                                                      +
+                                                                                           |                                                                                         +
+   Constant, No Falloff.                                                                   |   Random Falloff.                                                                       +
+-------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
+.. figure:: /images/3D-interaction_Transform-Control_Proportional-Edit-falloff-linear.jpg  |.. figure:: /images/3D-interaction_Transform-Control_Proportional-Edit-falloff-sharp.jpg +
+   :width: 300px                                                                           |   :width: 300px                                                                         +
+   :figwidth: 300px                                                                        |   :figwidth: 300px                                                                      +
+                                                                                           |                                                                                         +
+   Linear Falloff.                                                                         |   Sharp Falloff.                                                                        +
+-------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
+.. figure:: /images/3D-interaction_Transform-Control_Proportional-Edit-falloff-root.jpg    |.. figure:: /images/3D-interaction_Transform-Control_Proportional-Edit-falloff-sphere.jpg+
+   :width: 300px                                                                           |   :width: 300px                                                                         +
+   :figwidth: 300px                                                                        |   :figwidth: 300px                                                                      +
+                                                                                           |                                                                                         +
+   Root Falloff.                                                                           |   Sphere Falloff.                                                                       +
+-------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
+.. figure:: /images/3D-interaction_Transform-Control_Proportional-Edit-falloff-smooth.jpg                                                                                            +
+   :width: 300px                                                                                                                                                                     +
+   :figwidth: 300px                                                                                                                                                                  +
+                                                                                                                                                                                     +
+   Smooth Falloff.                                                                                                                                                                   +
+-------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+


Examples
~~~~~~~~

Switch to a front view (:kbd:`pad1`) and activate the grab tool with :kbd:`g`.
As you drag the point upwards, notice how nearby vertices are dragged along with it.
When you are satisfied with the placement, click :kbd:`lmb` to fix the position.
If you are not satisfied,
cancel the operation and revert your mesh to the way it looked before with :kbd:`rmb`
(or :kbd:`esc`).

You can use the proportional editing tool to produce great effects with the scaling
(:kbd:`s`) and rotation (:kbd:`r`) tools,
as *A landscape obtained via proportional editing* shows.


.. figure:: /images/3D-interaction_Transform-Control_Proportional-Edit-landscape.jpg
   :width: 640px
   :figwidth: 640px

   A landscape obtained via proportional editing.


Combine these techniques with vertex painting to create fantastic landscapes. The *final
rendered landscape* image below shows the results of proportional editing after the
application of textures and lighting.


.. figure:: /images/3D-interaction_Transform-Control_Proportional-Edit-landscape-textured.jpg
   :width: 620px
   :figwidth: 620px

   Final rendered landscape.


