
Motion Actuator
***************

The Motion actuator sets an object into motion and/or rotation.
There are two modes of operation, simple or servo in which the object can either teleport,
rotate or dynamically move. Also,
simple mode operation depends on the type of  Physics setting for the  Object.

See :doc:`Actuator Common Options </game_engine/logic/actuators/common_options>` for common options.

Special Options:
**Motion Type**
Determines type of motion

:guilabel:`Simple Motion`
   applies different kinds of motions directly
:guilabel:`Servo Control`
   sets a target speed and also how quickly it reaches that speed.


.. tip:: Object collisions

   Simple motion can cause an object to go through another object since it never passes the any of the coordinates between the start and end. This can be avoided using Servo Control, which is activated when the Physics setting for the object(s) is set to Dynamic/Rigid Body/Soft Body.


Simple Motion
=============

.. figure:: /images/Manual_gameengine_actuator_motion_simple.jpg
   :width: 271px
   :figwidth: 271px

   Motion actuator for Simple Motion


:guilabel:`Loc`
   The object jumps the number of blender units entered, in each of the three axes,each time a pulse is received.

:guilabel:`Rot`
   The object rotates by the specified amount, in each of the three axes, each time a pulse is received. One revolution is represented by the value 7.2 (i.e. 0.02 for one degree).

:guilabel:`L`
   Coordinates specified are Global (gray) or Local (White).


.. tip:: Servo Control

   To make Servo Control work, it is necessary to turn on Dynamic in the Physics window, and to make the object an Actor.


Servo Control
=============

.. figure:: /images/Manual_gameengine_actuator_motion_servo.jpg
   :width: 271px
   :figwidth: 271px

   Motion actuator for Servo Control


Servo control is a powerful way to achieve motion in way which mimics the movement of objects
in the physical world. It consists in a servo controller that adjusts the force on the object
in order to achieve a given speed. Uses the Proportional - Integral - Derivative (PID)
equations of motion :guilabel:`See Ref.`.

:guilabel:`Reference Ob`
   Specifies the object which the actuator owner uses as a reference for movement, for moving platforms for example. If empty it will use world reference.

:guilabel:`Linear V`
   The target linear velocity, in each of the three axes, which the object will try and achieve.

:guilabel:`L`
   Coordinates specified are Global (gray) or Local (White).

:guilabel:`X, Y, Z`
   Sets maximum and minimum limits for the force applied to the object. If disabled (i.e. X,Y or Z buttons are gray) the force applied is unlimited.

:guilabel:`Proportional Coefficient`
   Set the Proportional Coefficient. This controls the reaction  to differences between the actual and target linear velocity.

:guilabel:`Integral Coefficient`
   Set the Integral Coefficient. This controls the reaction  to the sum of errors so far in this move.

:guilabel:`Derivative Coefficient`
   Set the Derivative Coefficient. This controls the reaction


