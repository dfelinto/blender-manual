
..    TODO/Review: {{review
   |text=This page is not in good shape. Redundant to the introduction page and the how to's should be in the tutorial section.
   }} .


Armatures
*********

An "armature" is a type of object used for :doc:`rigging <rigging>`.
Armature object borrows many ideas from real life skeletons.


Your first armature
===================

In order to see what we're talking about, let's try to add the default armature in Blender.

(Note that armature editing details are explained in the :doc:`armatures editing section <rigging/armatures/editing>`).

Open a default scene, then:

- delete all objects in the scene
- make sure the cursor is in the world origin with :kbd:`shift-C`
- press :kbd:`pad1` to see the world in Front view
- then, either:
  - in the Main Menu, Go to Add > Armature > Single Bone
  - -or- in the 3D view, add an armature with :kbd:`shift-A` :menuselection:`popup --> Armature --> Single Bone`
- press :kbd:`Del NumPad` to see the armature at maximum zoom


+----------------------------------------------------------------------+-----------------------------------------------------+
+`Toolbox: Add » Armature » Single Bone                                |                                                     +
+ <http://wiki.blender.org/index.php/File:ManRiggingAddArmature2.5>`__ |                                                     +
+                                                                      |                                                     +
+                                                                      |                                                     +
+                                                                      |.. figure:: /images/ManRiggingDefaultArmature2.5.jpg +
+                                                                      |   :width: 500px                                     +
+                                                                      |   :figwidth: 500px                                  +
+                                                                      |                                                     +
+                                                                      |   The default armature                              +
+                                                                      |                                                     +
+----------------------------------------------------------------------------------------------------------------------------+


The armature object
===================

As you can see, an armature is like any other object type in Blender:

- It has a center, a position, a rotation and a scale factor.
- It has an ObData datablock, that can be edited in :guilabel:`Edit mode`.
- It can be linked to other scenes, and the same armature data can be reused on multiple objects.
- All animation you do in :guilabel:`Object mode` is only working on the whole object, not the armature's bones (use the :guilabel:`Pose mode` to do this).

As armatures are designed to be posed, either for a static or animated scene,
they have a specific state, called "rest position". This is the armature's default "shape",
the default position/rotation/scale of its bones, as set in :guilabel:`Edit mode`.

In :guilabel:`Edit mode`, you will always see your armature in rest position,
whereas in :guilabel:`Object` and :guilabel:`Pose mode`,
you usually get the current "pose" of the armature
(unless you enable the :guilabel:`Rest Position` button of the :guilabel:`Armature` panel).


Armature chapter overview
=========================

In the "Armatures" section, we will only talk about armatures themselves,
and specifically we will talk about:

- the armature object :doc:`panels <rigging/armatures/panels>`
- the basics of :doc:`bones <rigging/armatures/bones>`
- the different :doc:`armature visualizations <rigging/armatures/visualization>`
- the armature :doc:`structure types <rigging/armatures/structure>`
- how to :doc:`select <rigging/armatures/selecting>` its parts,
- how to :doc:`edit an armature <rigging/armatures/editing>`
- how to :doc:`Edit Bones <rigging/armatures/editing/bones>`
- how to :doc:`edit bones properties <rigging/armatures/editing/properties>`
- how to sketch armatures with the :doc:`Etch-a-Ton tool <rigging/armatures/editing/sketching>`
- how to use :doc:`templates <rigging/armatures/editing/templating>`


