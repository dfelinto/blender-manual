
..    TODO/Review: {{review|split=X|text=need to separate generic information from moving, erase join. like 2.4. Need also to explain objects classes (curves, mesh, etc) and possible conversions from and to (greylica)}} .


Object Mode
===========

.. figure:: /images/Manual-2.5-Part-II-ObjectMode-Selected-Ex.jpg
   :width: 300px
   :figwidth: 300px

   Selected object in 3D View:
   1 - Solid shading, 2 - Wireframe shading.


The geometry of a scene is constructed from one or more Objects: For example Lamps, Curves, Surfaces, Cameras, Meshes, and the basic objects ("primitives") described in "\ :doc:`Mesh Primitives <modeling/meshes/primitives>` ".


Types of Objects
================

+------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+:doc:`Meshes <modeling/meshes>`           |Meshes are objects composed of Polygonal Faces, Edges and/or Vertices, and can be edited extensively with Blender's mesh editing tools.                                                                                  +
+------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+:doc:`Curves <modeling/curves>`           |Curves are mathematically defined objects, which can be manipulated with control handles or control points, rather than vertices.                                                                                        +
+------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+:doc:`Surfaces <modeling/surfaces>`       |Surfaces are four-sided patches that are also manipulated with control points. These are useful for very organic, and rounded, but simple forms.                                                                         +
+------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+:doc:`Meta Objects <modeling/metas>`      |Meta Objects (or Metaballs) are objects formed by a function defining the 3d volume in which the object exists. Metaballs can create "Blobby" forms that have a liquid-like quality, when two or more Metaballs are used.+
+------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+:doc:`Text <modeling/texts>`              |Text objects create a 2d representation of a string of characters.                                                                                                                                                       +
+------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+:doc:`Armatures <rigging/armatures>`      |Armatures are used for rigging 3d models in order to make them poseable and animateable.                                                                                                                                 +
+------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+:doc:`Lattice <modifiers/deform/lattice>` |Nonrenderable wireframe. Commonly used for taking additional control over other objects with help of modifiers.                                                                                                          +
+------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+:doc:`Empty <modeling/empties>`           |Empties are null objects that are simple visual transform nodes that do not render. They are useful for controlling the position or movement of other objects.                                                           +
+------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+:doc:`Speaker <sequencer/audio>`          |Brings to scene source of sound.                                                                                                                                                                                         +
+------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+:doc:`Cameras <render/camera>`            |This is the virtual camera that is used to determine what appears in the render.                                                                                                                                         +
+------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+:doc:`Lamps <lighting>`                   |These are used to place light sources in the scene.                                                                                                                                                                      +
+------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+:doc:`Force Fields <physics/force_fields>`|Force fields are used in physical simulations. They give simulations external forces, creating movement, and are represented in 3d editor by small control objects.                                                      +
+------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. figure:: /images/ObjectMode.jpg

   Object Mode button.


Each object can be moved, rotated and scaled in :guilabel:`Object Mode` (see picture).
However, not all of these transformations have an effect on all objects. For example,
scaling a force field will not increase its effect.


.. figure:: /images/Manual-2.5-Part-II-EditMode.jpg

   Edit Mode button.


For making other changes to the geometry of editable objects,
you should use :guilabel:`Edit mode` (see picture).


Once you've added a basic object, you remain in :guilabel:`Object Mode`.
In earlier versions of Blender,
you were automatically switched into :guilabel:`Edit mode` if the Object was a Mesh,
a Curve or a Surface.

You can switch between :guilabel:`Object Mode` and :guilabel:`Edit Mode` by pressing
:kbd:`TAB`.

The object's wireframe should now appear orange.
This means that the object is now selected and active (see picture *Selected object*).

The (*Selected object*)
image shows both the solid view and wireframe view of the default cube.
To switch between wireframe and solid view, press :kbd:`Z`.


Object Centers
==============

Each object has an origin point. The location of this point determines where the object is located in 3D space. When an object is selected, a small circle appears, denoting the origin point. The location of the origin point is important when translating, rotating or scaling an object. See :doc:`Pivot Points <3d_interaction/transform_control/pivot_point>` for more.


Moving Object Centers
---------------------

Object Centers can be moved to different positions through :guilabel:`3D View window →
Transform → Origin`  (press :kbd:`T` to open panel):

- Geometry to Origin

      Move model to origin and this way origin of the object will also be at the center of the object.

- Origin to Geometry

      Move origin to the center of the object and this way origin of the object will also be at the center of the object.

- Origin to 3D Cursor

      Move origin of the model to the place of the 3D cursor.

- Origin to Center of Mass

      Move origin to calculated center of mass of model.


Erase Objects
=============

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` or :guilabel:`Object` mode
   | Menu:     :guilabel:`Object` → :guilabel:`Delete`
   | Hotkey:   :kbd:`X` or :kbd:`DEL`


Erases or deletes selected objects.


Join Objects
============

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object` mode
   | Menu:     :guilabel:`Object` → :guilabel:`Join Objects`
   | Hotkey:   :kbd:`ctrl-J`


Joins all selected objects to one single object. Must be of the same type.
Origin point is obtained from the previously *active* object.
Performing a join is equivalent to adding new objects while in :guilabel:`Edit mode`.
The non-active objects are deleted. Only the active object remains.
This only works with editable objects, like meshes and curves.


