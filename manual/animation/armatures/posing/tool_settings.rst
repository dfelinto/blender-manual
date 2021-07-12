
*************
Tool Settings
*************

Pose Options
============

.. _bpy.types.Pose.use_auto_ik:

Auto IK
-------

.. reference::

   :Mode:      Pose Mode
   :Panel:     :menuselection:`Sidebar --> Tool --> Pose Options --> Auto IK`

The auto IK option in the Sidebar enables a temporary IK constraint when posing bones.
The chain acts from the tip of the selected bone to root of the upper-most parent bone.
Note that this mode lacks options,
and only works by applying the resulting transform to the bones in the chain.


.. _bpy.types.Pose.use_mirror_x:

X-Axis Mirror
-------------

.. reference::

   :Mode:      Edit and Pose Mode
   :Panel:     :menuselection:`Sidebar --> Tool --> Options --> X-Axis Mirror`

This option enables automatic mirroring of editing actions along the X axis.
You can enable this option in the :menuselection:`Tool tab --> Options panel`,
while the armature is selected in *Edit Mode*.
When you have pairs of bones of the same name with just a different "side suffix"
(e.g. ".R"/".L", or "_right"/"_left" ...), once this option is enabled,
each time you transform (move, rotate, scale...) a bone,
its "other side" counterpart will be transformed accordingly,
through a symmetry along the armature local X axis.
As most rigs have at least one axis of symmetry (animals, humans, ...),
it is an easy way to keep the model symmetrical.


Relative Mirror
---------------

.. reference::

   :Mode:      Edit and Pose Mode
   :Panel:     :menuselection:`Sidebar --> Tool --> Options --> Relative Mirror`

Accounts for any relative transformations when using *X-Axis Mirror*.

.. seealso::

   :ref:`Naming bones <armature-editing-naming-bones>`.


Known Limitations
=================

Relative Mirror is not supported with `Auto IK`_ enabled.
