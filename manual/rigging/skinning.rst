
..    TODO/Review: {{review|copy=X}} .


Skinning
********

We have seen in :doc:`previous pages </rigging/armatures>` how to design an armature, create chains of bones, etc. Now, having a good rig is not the final goal - unless you want to produce a "Dance Macabre" animation, you'll likely want to put some flesh on your skeletons! Surprisingly, "linking" an armature to the object(s) it should transform and/or deform is called the "skinning" process...


+----------------------------------------------+
+.. figure:: /images/Manual-Part-I-Quick62.jpg +
+   :width: 600px                              +
+   :figwidth: 600px                           +
+                                              +
+   The ginebread mesh skinned on its armature.+
+----------------------------------------------+


In Blender, you have two main skinning types:

- You can :doc:`Parent/Constrain Objects to Bones </rigging/skinning/objects>` - then, when you transform the bones in :guilabel:`Pose` mode, their "children" objects are also transformed, exactly as with a standard parent/children relationship... *The "children" are* **never** *deformed when using this method*.
- You can :doc:`Using the Armature modifier on entire Mesh </rigging/skinning/obdata>`, and then, some parts of this object to some bones inside this armature. This is the more complex and powerful method, and *the only way to really deform the geometry of the object*, i.e. to modify its vertices/control points relative positions.


