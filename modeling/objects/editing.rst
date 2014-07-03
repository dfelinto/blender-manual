
..    TODO/Review: {{review|partial=X|text=need more info about Editing function, not all are in this page}} .


Introduction
============

In this section will be described tools for editing objects in :guilabel:`Object Mode`\ .

Information about some additional possibilities are described in :doc:`Manipulation in 3D <3d_interaction/transform_control>`\ .


Object Mode
-----------


.. figure:: /images/Icon-library_3D-Window_header-mode-selection.jpg

   Object Mode button


By default new files opens with enabled :guilabel:`Object Mode`\ .
To enable it you may in :guilabel:`3D View window → Header` click :guilabel:`Object Mode
button` (see picture :guilabel:`Object Mode button`\ )

All edition tools works only with selected objects. See :doc:`Selecting Objects <modeling/objects/selecting>` for more information.


All commands described below can be found in *Object* menu and/or in *Object tools* panel
(see pictures).

+----------------------------------------------------+----------------------------------------------+
+.. figure:: /images/Manual-2.6-Panel-ObjectTools.jpg|.. figure:: /images/Manual-2.6-Menu-Object.jpg+
+   :width: 50px                                     |   :width: 75px                               +
+   :figwidth: 50px                                  |   :figwidth: 75px                            +
+                                                    |                                              +
+   Object tools panel                               |   Object menu                                +
+----------------------------------------------------+----------------------------------------------+


Creation and deletion
=====================

The most basic edition includes manipulation with existence of objects.
Below are listed different types of creation and deletion tools.

Add
---


.. admonition:: Reference
   :class: refbox

   | Menu:     :guilabel:`Main` → :guilabel:`Add`
   | Hotkey:   :kbd:`Shift-A`


We may add one of those primitives:

- **Mesh**\ : Plane, Cube, Circle, UV Sphere, Icosphere, Cylinder, Cone, Grid, Monkey, Torus.
- **Curve**\ : Bezier, Circle, NURBS Curve, NURBS Circle, Path.
- **Surface**\ : NURBS Curve, NURBS Circle, NURBS Surface, NURBS Cylinder, NURBS Sphere, NURBS Torus.
- **Metaball**\ : Ball, Capsule, Plane, Ellipsoid, Cube.
- **Text**\ .
- **Armature**\ : Single Bone.
- **Lattice**\ .
- **Empty**\ : Plane Axis, Arrows, Single Arrow, Circle, Cube, Sphere, Cone, Image.
- **Speaker**\ .
- **Camera**\ .
- **Lamp**\ : Point, Sun, Spot, Hemi, Area.
- **Force Field**\ : Force, Wind, Vortex, Magnetic, Harmonic, Charge, Lennard-Jones, Texture, Curve Guide, Boid, Turbulence, Drag, Smoke Flow.
- **Group Instance**\ : (user defined groups of objects).


Duplicate
---------


.. admonition:: Reference
   :class: refbox

   | Menu:     *Object → Duplicate Objects*
   | Hotkey:   :kbd:`Shift-D`


.. admonition:: Reference
   :class: refbox

   | Menu:     *Object → Duplicate Linked*
   | Hotkey:   :kbd:`Alt-D`


Duplication makes exact copy of objects. May be linkage of some attributes depending on specific tool. See :doc:`Duplication <modeling/objects/duplication>` for more information.


Join

----


.. admonition:: Reference
   :class: refbox

   | Menu:     *Object → Join*
   | Hotkey:   :kbd:`Ctrl-J`


Joining makes one single object from all selected objects. Objects must be of the same type.
Origin point is obtained from the previously *active* object.
Performing a join is equivalent to adding new objects while in :guilabel:`Edit mode`\ .
The non-active objects are deleted (their meshes were taken by active object).
Only the active object remains. This only works with editable objects,
containing meshes and curves.


Delete
------


.. admonition:: Reference
   :class: refbox

   | Menu:     *Object → Delete... → Delete*
   | Hotkey:   :kbd:`X`\ , :kbd:`D` or :kbd:`Delete`\ , :kbd:`D`


Deletion erases selected objects.


Transformation tools
====================

Objects can be transformed in a variety of ways.
Below are listed different types of transformation.


Translate
---------


.. admonition:: Reference
   :class: refbox

   | Menu:     *Object → Transform → Grab/Move*
   | Hotkey:   :kbd:`G`


Translation means changing location of objects. This changes X,
Y and/or Z coordinates of object's :guilabel:`Origin point` relative to center of coordinates.


Rotate
------


.. admonition:: Reference
   :class: refbox

   | Menu:     *Object → Transform → Rotate*
   | Hotkey:   :kbd:`R`


Rotation means changing angles of objects. This changes rotation angles around X,
Y and/or Z axes of object's coordinate system relative to current coordinate system.
No parts of each object are changing their position relative to other parts of the same object.


Scale
-----


.. admonition:: Reference
   :class: refbox

   | Menu:     *Object → Transform → Scale*
   | Hotkey:   :kbd:`S`


Scaling means changing proportions of objects. This proportionally stretches object along X,
Y and/or Z axes of object's coordinate system.


