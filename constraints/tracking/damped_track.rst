
..    TODO/Review: {{review|im=examples}} .


Damped Track Constraint
=======================


The :guilabel:`Damped Track` constraint constrains one local axis of the owner to always point
towards :guilabel:`Target`\ .
In another 3D software you can find it with the name "Look at" constraint.


Options
-------


.. figure:: /images/25-Manual-Constraints-Tracking-DampedTrack.jpg
   :width: 304px
   :figwidth: 304px

   Damped Track panel


:guilabel:`Target` (Mesh Object Type)
    This constraint uses one target, and is not functional (red state) when it has none.

   :guilabel:`Vertex Group`
      If :guilabel:`Target` is a :guilabel:`Mesh`\ , a new field is displayed offering the optional choice to set a :guilabel:`Vertex Group` as target.


.. figure:: /images/Properties_Editor_-_Object_Constraints_-_Damped_Track_-_Armature_Object_Type.jpg
   :width: 304px
   :figwidth: 304px

   Damped Track for Bones


:guilabel:`Target` (Armature Object Type):
   :guilabel:`Bone`
      If :guilabel:`Target` is an :guilabel:`Armature`\ , a new field is displayed offering the optional choice to set an individual bone as :guilabel:`Target`\ .
   :guilabel:`Head/Tail`
      If :guilabel:`Target` is an :guilabel:`Armature`\ , a new field is displayed offering the optional choice to set whether the Head or Tail of a Bone will be pointed at by the :guilabel:`Target`\ .  It is a slider value field which can have a value between 0 and 1.  A value of 0 will point the Target at the Head/Root of a Bone while a value of 1 will point the Target at the Tail/Tip of a Bone.

:guilabel:`To`
   Once the owner object has had a Damped Track constraint applied to it, you must then choose which axis of the object you want to point at the Target object.  You can choose between 6 axis directions (-X, -Y, -Z, X, Y, Z).  The negative axis direction cause the object to point away from the Target object along the selected axis direction.


