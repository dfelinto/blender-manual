
Copy Scale Constraint
*********************

Description
===========

The :guilabel:`Copy Scale` constraint forces its owner to have the same scale as its target.


 .. warning::

   FIXME - warning body below

 Here we talk of **scale**, not of **size** ! Indeed, you can have two objects, one much bigger than the other, and yet both of them have the same scale. This is also true with bones: in :guilabel:`Pose` mode, they all have a unitary scale when they are in rest position, represented by their visible length.


Options
=======

.. figure:: /images/25-Manual-Constraints-Transform-CopyScale.jpg
   :width: 307px
   :figwidth: 307px

   Copy Scale panel


:guilabel:`Target`
   This constraint uses one target, and is not functional (red state) when it has none.

   :guilabel:`Bone`
      If :guilabel:`Target` is an :guilabel:`Armature`, a new field is displayed offering the optional choice to set an individual bone as :guilabel:`Target`.

      :guilabel:`Head/Tail`
         If a :guilabel:`Bone` is set as :guilabel:`Target`, a new field is displayed offering the optional choice of where along this bone the target point lies.
   :guilabel:`Vertex Group`
      If :guilabel:`Target` is a :guilabel:`Mesh`, a new field is displayed offering the optional choice to set a :guilabel:`Vertex Group` as target.

:guilabel:`X`, :guilabel:`Y`, :guilabel:`Z`
   These buttons control along which axes the scale is constrained - by default, it is enabled along all three.

:guilabel:`Offset`
   When enabled, this control allows the owner to be scaled (using its current transform properties), relatively to its target's scale.

:guilabel:`Space`
   This constraint allows you to choose in which space to evaluate its owner's and target's transform properties.


