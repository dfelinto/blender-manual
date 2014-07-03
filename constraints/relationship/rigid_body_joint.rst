
..    TODO/Review: {{review
   |text=
   Complete rewrite needed.  Unclear and Child object field not explained what it does.
   }} .


Rigid Body Joint Constraint
===========================

Description
-----------

The :guilabel:`Rigid Body Joint` constraint is very special. Basically, it is used by the
physical part of the Blender Game Engine to simulate a joint between its owner and its target.
It offers four joint types: hinge type, ball-and-socket type, cone-twist, and generic six-DoF
(degrees of freedom) type.

The joint point and axes are defined and fixed relative to the owner.
The target moves as if it were stuck to the center point of a stick,
the other end of the stick rotating around the joint/pivot point…

This constraint is of no use in most "standard" static or animated projects. However, you can use its results outside of the BGE, through the :menuselection:`Game --> Record Animation` menu entry (from the main menu of the :guilabel:`User Preferences` window, see :doc:`Rigid Bodies <physics/using_ge>` for more info on this topic).

For a demo file that shows some of the different types, see: `BGE-Physics-RigidBodyJoints.blend <http://wiki.blender.org/index.php/Media:BGE-Physics-RigidBodyJoints.blend>`__\ .


Options
-------

.. figure:: /images/25-Manual-Constraints-Relationship-RigidBodyJoint.jpg
   :width: 304px
   :figwidth: 304px

   Rigid Body Joint panel


:guilabel:`Target`
   This constraint uses one target, and is not functional (red state) when it has none.

:guilabel:`Joint Type`\ :
   :guilabel:`Ball`
      works like an ideal ball-and-socket joint, i.e. allows rotations around all axes like a shoulder joint.
   :guilabel:`Hinge`
      works in one plane, like an elbow: the owner and target can only rotate around the X axis of the pivot (joint point).
      :guilabel:`Limits`
         Angular limits for the X axis
   :guilabel:`Cone Twist`
      similar to :guilabel:`Ball`\ , this is a point-to-point joint with limits added for the cone and twist axis
      :guilabel:`Limits`
         Angular limits
   :guilabel:`Generic 6DOF`
      works like the *Ball* option, but the target is no longer constrained at a fixed distance from the pivot point, by default (hence the six degrees of freedom: rotation and translation around/along the three axes).
       In fact, there is no longer a joint by default, with this option, but it enables additional settings which allow you to restrict some of these DoF:
      :guilabel:`Limits`
         Linear and angular limits for a given axis (of the pivot) in Blender Units and degrees respectively.

:guilabel:`Child Object`
   normally, leave this blank. You can reset it to blank by right clicking and selecting Reset to Default Value.
   Comment: <!-- Is this right? 2.4 just had a 'to object'. Now we have a 'target' and a 'child object'.
   These are not documented. It seems that we recreate the behaviour of 2.4 by leaving the child object blank.
   The target seems to be the 2.4 'to object'. What is the child object? Please explain: m.e --> .

:guilabel:`Linked Collision`
   When enabled, this will disable the collision detection between the owner and the target (in the physical engine of the BGE).

:guilabel:`Display Pivot`
   When enabled, this will draw the pivot of the joint in the 3D views. Most useful, especially with the :guilabel:`Generic 6DOF` joint type!

:guilabel:`Pivot`
   These three numeric fields allow you to relocate the pivot point, *in the owner's space*\ .

:guilabel:`Axis`
   These three numeric fields allow you to rotate the pivot point, *in the owner's space*\ .


