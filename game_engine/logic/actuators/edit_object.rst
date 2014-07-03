


Edit Object Actuator
====================

The Edit Object actuator allows the user to edit settings of objects in game

See :doc:`Actuator Common Options <game_engine/logic/actuators/common_options>` for common options.

Special Options:


.. figure:: /images/2.5_Game_Engine_Actuator_Edit_Object.jpg
   :width: 271px
   :figwidth: 271px

   Edit Object actuator


**Edit Object**
Menu of options for Edit Object actuator
   :guilabel:`Dynamics`
   :guilabel:`Track To`
   :guilabel:`Replace Mesh`
   :guilabel:`End Object`
   :guilabel:`Add Object`


.. figure:: /images/BGE_Actuator_Edit_Object_Dynamics.jpg
   :width: 271px
   :figwidth: 271px

   Edit Object actuator - Dynamics


**Dynamics**
Provides a menu of :guilabel:`Dynamic Operations` to set up dynamics options for object.
   :guilabel:`Set Mass`
      Enables the user to set the mass of the current object for Physics (Range 0 - 10,000).
   :guilabel:`Disable Rigid Body`
      Disables the Rigid Body state of the object - disables collision.
   :guilabel:`Enable Rigid Body`
      Disables the Rigid Body state of the object - enables collision.
   :guilabel:`Suspend Dynamics`
      Suspends the object dynamics (object velocity).
   :guilabel:`Restore Dynamics`
      Resumes the object dynamics (object velocity).


.. figure:: /images/BGE_Actuator_Edit_Object_Track_to.jpg
   :width: 271px
   :figwidth: 271px

   Edit Object actuator - Track to


**Track To**
Makes the object "look at" another object, in 2D or 3D.
The Y-axis is considered the front of the object.
   :guilabel:`Object`
      Object to follow.
   :guilabel:`Time`
      No. of frames it will take to turn towards the target object (Range 0-2000).
   :guilabel:`3D Button`\ (toggle).
      Enable 2D (X,Y) or 3D (X,Y,Z) tracking.


.. figure:: /images/BGE_Actuator_Edit_Object_Replace_Mesh.jpg
   :width: 271px
   :figwidth: 271px

   Edit Object actuator - Replace Mesh


**Replace Mesh**
Replace mesh with another. Both the mesh and/or its physics can be replaced,
together or independently.
   :guilabel:`Mesh`
      name of mesh to replace the current mesh.
   :guilabel:`Gfx Button`
      replace visible mesh.
   :guilabel:`Phys  Button`
      replace physics mesh (not compound shapes)


.. figure:: /images/BGE_Actuator_Edit_Object_End_Object.jpg
   :width: 271px
   :figwidth: 271px

   Edit Object actuator - End Object


**End Object**
Destroy the current object (Note, debug properties will display error Zombie Object in console)


.. figure:: /images/BGE_Actuator_Edit_Object_Add_Object.jpg
   :width: 271px
   :figwidth: 271px

   Edit Object actuator - Add Object


**Add Object**
Adds an object at the centre of the current object.
The object that is added needs to be on another, hidden, layer.
   :guilabel:`Object`
      The name of the object that is going to be added.:;\ :guilabel:`Time`\ : the time (in frames) the object stays alive before it disappears. Zero makes it stay forever.
   :guilabel:`Linear Velocity`
      Linear Velocity, works like in the motion actuator but on the created object instead of the object itself. Useful for shooting objects, create them with an initial speed.
   :guilabel:`Angular Velocity`
      Angular velocity, works like in the motion actuator but on the created object instead of the object itself.


