
Property Actuator
*****************

Using the Property actuator you can change the value of a given property once the actuator
itself is activated.

See :doc:`Actuator Common Options </game_engine/logic/actuators/common_options>` for common options.

Special Options:


.. figure:: /images/2.5_Game_Engine_Actuator_Property.jpg
   :width: 271px
   :figwidth: 271px

   Property actuator


**Mode**

:guilabel:`Assign`
   the :guilabel:`Property` target property will become equal to the set :guilabel:`Value` once the actuator is activated
:guilabel:`Add`
   adds :guilabel:`Value` to the value of the property :guilabel:`Property` once the actuator is activated (enter a negative value to decrease). For :guilabel:`Bool`, a value other than 0 (also negative) is counted as True.
:guilabel:`Copy`
   copies a property from another object to a property of the actuator owner once the actuator is activated.
:guilabel:`Toggle`
   switches 0 to 1 and any other number than 0 to 0 once the actuator is activated. Useful for on/off switches.

**Property**
   The target property that this actuator will change

**Value**
   The value to be used to change the property


Example
=======

You have a character, it has a property called "hp" (hit points)
to determine when he has taken enough damage to die. hp is an int with the start value of 100.

You set up two :guilabel:`Collision` sensors, one for enemy bullets,
and one for picking up more health. The first one is connected
(through an :guilabel:`AND` controller)
to an :guilabel:`Add Property` actuator with the property hp and the value -10.
Every time the player is hit by an enemy bullet he loses 10 hp. The other sensor is connected
(through an :guilabel:`AND` controller) to an other :guilabel:`Add Property` actuator,
this one with the value 50.
So every time the player collides with a health item the hp increases by 50.
Next you set up a :guilabel:`Property` sensor for an interval, greater than 100.
This is connected (through an :guilabel:`AND` controller)
to an :guilabel:`Assign Property` actuator which is set to 100.
So if the players hp increases over 100 it is set to 100.


