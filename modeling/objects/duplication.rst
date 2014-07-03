


Duplication
===========


.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` and :guilabel:`Object` modes
   | Menu:     :guilabel:`Object` → :guilabel:`Duplicate`
   | Hotkey:   :kbd:`shift-D`


Description
-----------

This will create a visually-identical copy of the selected object(s). The copy is created at
the same position as the original object and you are automatically placed in :guilabel:`Grab`
mode. Reference (\ *Duplicate Example*\ ) for the discussions below.

This copy is a new object, which "\ **shares**\ " some datablocks with the original object
(by default, all the Materials, Textures, and Ipos), but which has copied others,
like the mesh, for example.
This is why this form of duplication is sometimes called "shallow link",
because not all datablocks are shared; some of them are "hard copied"!

Note that you can choose which types of datablock will be linked or copied when duplicating:
in the :guilabel:`User Preferences`\ ' (available in the :guilabel:`File` menu)
:guilabel:`Editing` "tab", activate those types of datablocks you want to really copy in the
:guilabel:`Duplicate Data` list — the others will just be linked.


Examples
--------


.. figure:: /images/Manual-2.5-Modeling-Duplicate-Example.jpg
   :width: 620px
   :figwidth: 620px

   The mesh Cone.006 of object Cone.002 is being edited.  The mesh's Unique datablock ID name is highlighted in the Outliner.


The cone in the middle has been (1) link duplicated to the left and (2)
duplicated to the right.

- The duplicated right cone is being edited, the original cone in the middle remains unchanged.  The mesh data has been copied, not linked.
- Likewise, if the right cone is edited in object mode, the original cone remains unchanged.  The new object's transform properties or datablock is a copy, not linked.
- When the right cone was duplicated, it inherited the material of the middle cone.  The material properties were linked, not copied.

See above if you want separate copies of the datablocks normally linked.


Linked Duplicates
=================


.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object` mode
   | Menu:     :guilabel:`Object` → :guilabel:`Duplicate Linked`
   | Hotkey:   :kbd:`alt-D`


Description
-----------

You also have the choice of creating a *Linked Duplicate* rather than a *Duplicate*\ ;
this is called a deep link.
This will create a new object with **all** of its data linked to the original object.
If you modify one of the linked objects in :guilabel:`Edit mode`\ ,
all linked copies are modified. Transform properties (object datablocks) still remain copies,
not links, so you still can rotate, scale, and move freely without affecting the other copy.
Reference (\ *Duplicate Example*\ ) for the discussions below.


Examples
--------


.. figure:: /images/Manual-2.5-Modelling-Duplicate-Linked-Example.jpg
   :width: 620px
   :figwidth: 620px

   The object Cone.001 was linked duplicated.  Though both these cones are separate objects with unique names, the single mesh named Cone, highlighted in the Outliner, is shared by both.


The left cone is a :guilabel:`Linked Duplicate` of the middle cone (using :kbd:`alt-D`\ ).

- As a vertex is is moved in :guilabel:`Edit mode` in one object, the same vertex is moved in the original cone as well.  The mesh data are links, not copies.
- In contrast, if one of these two cones is rotated or rescaled in object mode, the other remains unchanged.  The transform properties are copied, not linked.
- As in the previous example, the newly created cone has inherited the material of the original cone.  The material properties are linked, not copied.

A common table has a top and four legs. Model one leg,
and then make linked duplicates three times for each of the remaining legs.
If you later make a change to the mesh, all the legs will still match.
Linked duplicates also apply to a set of drinking glasses,
wheels on a car… anywhere there is repetition or symmetry.


Procedural Duplication
======================


.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object mode` and :guilabel:`Edit mode`
   | Panel:    :guilabel:`Object settings`


There are currently four ways in Blender to procedurally duplicate objects.
These options are located in the :guilabel:`Object` menu.

..    Comment: <!--
   [[Image:Manual-Part-II-ObjectMode-Duplicate-Anim-Settings-Panel.png|frame|right|{{Literal|Anim settings}} panel.]]
   --> .
:doc:`Verts <modeling/objects/duplication/dupliverts>` :This creates an instance of all children of this object on each vertex (for mesh objects only).

:doc:`Faces <modeling/objects/duplication/duplifaces>` :This creates an instance of all children of this object on each face (for mesh objects only).

:doc:`Group <modeling/objects/duplication/dupligroup>` :This creates an instance of the group with the transformation of the object. Group duplicators can be animated using actions, or can get a :doc:`Proxy <data_system/linked_libraries#proxy_objects>`\ .

:doc:`Frames <modeling/objects/duplication/dupliframes>` :For animated objects, this creates an instance on every frame. As you'll see on this topic's subpage, this is also a *very* powerful technique for arranging objects and for modeling them.


Linked Library Duplication
==========================


.. admonition:: Reference
   :class: refbox

   | Menu:     :guilabel:`File` → :guilabel:`Link Append`
   | Hotkey:   :kbd:`Shift-F1`


:doc:`Linked Libraries <data_system/linked_libraries>` :Linked Libraries are also a form of duplication.  Any object or datablock in other :guilabel:`.blend` files can be reused in the current file.


Hints
=====


- If you want transform properties (i.e. object datablocks) to be "linked", see the page on :doc:`parenting <modeling/objects/groups_and_parenting>`\ .
- Material Transparency will not display when instancing dupli-groups; this is a known limitation of Blender's view-port.


