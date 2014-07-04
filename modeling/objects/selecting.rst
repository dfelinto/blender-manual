
..    TODO/Review: {{review|partial=X|text=Missing Keying set. }} .


Introduction
============

Selection determines which elements will be the target of our actions.
Blender has advanced selection methods.
Both in :guilabel:`Object mode` and in :guilabel:`Edit mode`.


Selections and the Active Object
================================

Blender distinguishes between two different states of selection:


.. figure:: /images/25-Manual-Object-Selection-001.jpg

   Unselected object in black, selected object in orange, and active object in yellow


- In :guilabel:`Object mode` the last (de)selected item is called the "Active Object" and is outlined in yellow (the others are orange). There is exactly one active object at any time (even when nothing is selected).

   Many actions in Blender use the active object as a reference (for example linking operations). If you already have a selection and need to make a different object the active one, simply re-select it with :kbd:`shift-rmb`.

- All other selected objects are just selected. You can select any number of objects.


Point Selection
===============

The simplest form of object *selection* consists of using :kbd:`rmb` on it.

To *add to the selection*, use :kbd:`shift-rmb` on more objects.

If the *objects are overlapping* in the view,
you can use :kbd:`alt-rmb` to cycle through possible choices.

If you want *to add to a selection* this way then the shortcut becomes
:kbd:`shift-alt-rmb`.

To *activate an object* that is already selected, click :kbd:`shift-rmb` on it.

To *deselect* an active object,
click :kbd:`shift-rmb` one time - and hence two clicks if the object isn't active.
Note that this only works if there are no other objects under the mouse.
Otherwise it just adds those to the selection. There appears to be no workaround for this bug.


Rectangular or Border Select
============================

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object mode` and :guilabel:`Edit mode`
   | Menu:     :guilabel:`Select` → :guilabel:`Border Select`
   | Hotkey:   :kbd:`B`


Description
-----------

With :guilabel:`Border Select` you draw a rectangle while holding down :kbd:`lmb`.
Any object that lies even partially within this rectangle becomes selected.

For deselecting objects,
use :kbd:`mmb` or :guilabel:`Border Select` again with holding :kbd:`Shift`.

To cancel the selection use :kbd:`rmb`.


Example
-------

.. figure:: /images/25-Manual-Object-Selection-Border.jpg
   :width: 610px
   :figwidth: 610px

   Border selecting in three steps


:guilabel:`Border Select` has been activated in the first image and is indicated by showing a dotted cross-hair cursor. In the second image, the *selection region* is being chosen by drawing a rectangle with the :kbd:`lmb`. The rectangle is only covering two cubes. Finally, in the third image, the selection is completed by releasing :kbd:`lmb`.

Notice in the third image, the bright color of left-most selected cube.
This means it is the "active object",
the last selected object prior to using the :guilabel:`Border Select` tool.


Hints
-----

:guilabel:`Border Select` adds to the previous selection, so in order to select only the contents of the rectangle, deselect all with :kbd:`A` first.


Lasso Select
============

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object mode` and :guilabel:`Edit mode`
   | Menu:     no entry in the menu
   | Hotkey:   :kbd:`ctrl-lmb`


Description
-----------

Lasso select is used by drawing a dotted line around the pivot point of the objects,
in :guilabel:`Object mode`.


Usage
-----

While holding :kbd:`ctrl` down, you simply have to draw around the pivot point of each
object you want to select with :kbd:`lmb`.

Lasso select adds to the previous selection. For deselection, use :kbd:`ctrl-shift-lmb`.


.. figure:: /images/25-Manual-Object-Selection-Lasso.jpg
   :width: 610px
   :figwidth: 610px

   Lasso selection example


Circle Select
=============

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object mode` and :guilabel:`Edit mode`
   | Menu:     :guilabel:`Select` → :guilabel:`Circle Select`
   | Hotkey:   :kbd:`C`


Description
-----------

.. figure:: /images/26-Manual-Object-Selection-Circle0.jpg
   :width: 100px
   :figwidth: 100px

   Main selection menu


:guilabel:`Circle Select` is used by moving with dotted circle through objects with :kbd:`lmb`. You can select any object by touching of circle area.
It is possible to dynamically change the diameter of circle by scrolling :kbd:`mmb` as
seen in pictures below. Deselection is under the same principle - :kbd:`mmb`.
To cancel the selection use :kbd:`rmb` or key :kbd:`Esc`,

+----------------------------------------------------------+----------------------------------------------------------+
+.. figure:: /images/26-Manual-Object-Selection-Circle1.jpg|.. figure:: /images/26-Manual-Object-Selection-Circle2.jpg+
+   :width: 300px                                          |   :width: 320px                                          +
+   :figwidth: 300px                                       |   :figwidth: 320px                                       +
+                                                          |                                                          +
+   Circle selection                                       |   ...with huge circle                                    +
+----------------------------------------------------------+----------------------------------------------------------+


Menu Selection
==============

The selection methods described above are the most common.
There are also many more options accessible through the :guilabel:`Select` menu of the 3D view.

Each is more adapted to certain operations.


Select Grouped
--------------

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object mode`
   | Menu:     :guilabel:`Select` → :guilabel:`Grouped`
   | Hotkey:   :kbd:`shift-G`


Description
~~~~~~~~~~~

.. figure:: /images/25-Manual-Object-Selection-Grouped.jpg

   Select Grouped menu


There are two ways to organize the objects in relation to one another.
The first one is :guilabel:`parenting`, and the second is simple :guilabel:`grouping`.
We can use these relationships to our advantage by selecting members of respective families or
groups.


Options
~~~~~~~

:guilabel:`Select` → :guilabel:`Grouped` in :guilabel:`Object mode` uses the active object as a basis to select all others.

Available options are:

:guilabel:`Children`
   Selects all children of the active object recursively.
:guilabel:`Immediate Children`
   Selects all direct children of the active object.
:guilabel:`Parent`
   Selects the parent of this object if it has one.
:guilabel:`Siblings`
   Select objects that have the same parent as the active object. This can also be used to select all root level objects (objects with no parents).
:guilabel:`Type`
   Select objects that are the same type as the active one.
:guilabel:`Layer`
   Objects that have at least one shared layer.
:guilabel:`Group`
   Objects that are part of a group (rendered green with the default theme) will be selected if they are in one of the groups that the active object is in.
:guilabel:`Object Hooks`
   Every hook that belongs to the active object.
:guilabel:`Pass`
   Select objects assigned to the same render pass. Render passes are set in :guilabel:`Properties` → :guilabel:`Object` → :guilabel:`Relations` and can be used in the :guilabel:`Node Compositor` (:guilabel:`Add` → :guilabel:`Convertor` → :guilabel:`ID Mask`.)
:guilabel:`Color`
   Select objects with same :guilabel:`Object Color`.  Object colors are set in :guilabel:`Properties` → :guilabel:`Object` → :guilabel:`Display` → :guilabel:`Object Color`.)
:guilabel:`Properties`
   Select objects with same :guilabel:`Game Engine` :guilabel:`Properties`.
:guilabel:`Keying Set`
   Select objects included in active Keying Set.
:guilabel:`Lamp Type`
   Select matching lamp types.
:guilabel:`Pass Index`
   Select matching object pass index.


Select linked
-------------

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object` mode
   | Menu:     :guilabel:`Select` → :guilabel:`Linked`
   | Hotkey:   :kbd:`shift-L`


Description
~~~~~~~~~~~

.. figure:: /images/25-Manual-Object-Selection-Linked.jpg

   Linked selection menu


Selects all objects which share a common datablock with the active object.


Options
~~~~~~~

:guilabel:`Select` → :guilabel:`Linked` in :guilabel:`Object mode` uses the active object as a basis to select all others.

Available options are:

:guilabel:`Object Data`
   Selects every object that is linked to the same Object Data, i.e. the datablock that specifies the type (mesh, curve, etc.) and the build (constitutive elements like vertices, control vertices, and where they are in space) of the object.
:guilabel:`Material`
   Selects every object that is linked to the same material datablock.
:guilabel:`Texture`
   Selects every object that is linked to the same texture datablock.
:guilabel:`Dupligroup`
   Selects all objects that use the same :guilabel:`Group` for duplication.
:guilabel:`Particle System`
   Selects all objects that use the same :guilabel:`Particle System`
:guilabel:`Library`
   Selects all objects that are in the same
:guilabel:`FIXME(Link Type Unsupported: dev; [[Dev:2.5/Source/Data_system/LibraryBrowser|Library]])`
:guilabel:`Library (Object Data)`


Select All by Type
------------------

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object` mode
   | Menu:     :guilabel:`Select` → :guilabel:`Select All by Type`
   | Hotkey:   None


Description
~~~~~~~~~~~

.. figure:: /images/25-Manual-Object-Selection-Bytype.jpg

   By Type selection menu


The types are :guilabel:`Mesh`, :guilabel:`Curve`, :guilabel:`Surface`, :guilabel:`Meta`,
:guilabel:`Font`, :guilabel:`Armature`, :guilabel:`Lattice`, :guilabel:`Empty`,
:guilabel:`Camera`, :guilabel:`Lamp`, :guilabel:`Speaker`.

With this tool it becomes possible to select every **visible** object of a certain type in
one go.


Options
~~~~~~~

:guilabel:`Select All by Type` in :guilabel:`Object` mode offers an option for every type of object that can be described by the :guilabel:`ObData` datablock.

Just take your pick.


Select All by Layer
-------------------

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object` mode
   | Menu:     :guilabel:`Select` → :guilabel:`Select All by Layer`
   | Hotkey:   None


Description
~~~~~~~~~~~

.. figure:: /images/25-Manual-Object-Selection-AllByLayer.jpg

   All by Layer selection menu


Layers are another means to regroup your objects to suit your purpose.

This option allows the selection of every single object that belongs to a given layer,
visible or not, in one single command.
..    Comment: <!--Not implemented yet?: This selection is added to anything that was already selected at that moment. --> .


Options
~~~~~~~

In the :guilabel:`Tool Shelf` → :guilabel:`Select by Layer` the following options are available:

:guilabel:`Match`
   The match type for selection.
:guilabel:`Extend`
   Enable to add objects to current selection rather than replacing the current selection.
:guilabel:`Layer`
   The layer on which the objects are.


.. admonition:: Selection of Objects
   :class: nicetip

   Rather than using the :guilabel:`Select All by Layer` option, it might be more efficient to make the needed layers visible and use :kbd:`A` on them. This method also allows objects to be deselected.


Other Menu Options
------------------

Available options on the first level of the menu are:

:guilabel:`Select Pattern...`
   Selects all objects whose name matches a given pattern. Supported wildcards: * matches everything, ? matches any single character, [abc] matches characters in "abc", and [!abc] match any character not in "abc". The matching can be chosen to be case sensitive or not.
   As an example *house* matches any name that contains "house", while floor* matches any name starting with "floor".

:guilabel:`Select Camera`
   Select the active camera.

:guilabel:`Mirror` (:kbd:`Shift-Ctrl-M`)
   Select the Mirror objects of the selected object eg. L.sword → R.sword.

:guilabel:`Random`
   Randomly selects unselected objects based on percentage probability on currently active layers. On selecting the command a numerical selection box becomes available in the :guilabel:`Tool Shelf`.
   It's important to note that the percentage represents the likelihood of an unselected object being selected and not the percentage amount of objects that will be selected.

:guilabel:`Inverse` (:kbd:`ctrl-I`)
   Selects all objects that were not selected while deselecting all those which were.

:guilabel:`(De)select All` (:kbd:`A`)
   If anything was selected it is first deselected. Otherwise it toggles between selecting and deselecting every visible object.


