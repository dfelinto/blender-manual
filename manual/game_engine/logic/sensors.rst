
Sensors
*******

Sensors are the logic bricks that cause the logic to do anything.
Sensors give an output when something happens, e.g.
a trigger event such as a collision between two objects, a key pressed on the keyboard,
or a timer for a timed event going off. When a sensor is triggered,
a positive pulse is sent to all controllers that are linked to it.


The logic blocks for all types of sensor may be constructed and changed using the `Logic Editor <http://wiki.blender.org/index.php/User:Sculptorjim/Game Engine/Logic/Editor>`__; details of this process are given in the `Sensor Editing <http://wiki.blender.org/index.php/User:Sculptorjim/Game Engine/Logic/Sensors/Editing >`__ page.


The following types of sensor are currently available:


+------------------------------------------------------+----------------------------------------------------------------------------------------------------+
+:doc:`Actuator <game_engine/logic/sensors/actuator>`  |Detects when a particular actuator receives an activation pulse.                                    +
+------------------------------------------------------+----------------------------------------------------------------------------------------------------+
+:doc:`Always <game_engine/logic/sensors/always>`      |Gives a continuous output signal at regular intervals.                                              +
+------------------------------------------------------+----------------------------------------------------------------------------------------------------+
+:doc:`Collision <game_engine/logic/sensors/collision>`|Detects collisions between objects or materials.                                                    +
+------------------------------------------------------+----------------------------------------------------------------------------------------------------+
+:doc:`Delay <game_engine/logic/sensors/delay>`        |Delays output by a specified number of logic ticks.                                                 +
+------------------------------------------------------+----------------------------------------------------------------------------------------------------+
+:doc:`Joystick <game_engine/logic/sensors/joystick>`  |Detects movement of specified joystick controls.                                                    +
+------------------------------------------------------+----------------------------------------------------------------------------------------------------+
+:doc:`Keyboard <game_engine/logic/sensors/keyboard>`  |Detects keyboard input.                                                                             +
+------------------------------------------------------+----------------------------------------------------------------------------------------------------+
+:doc:`Message <game_engine/logic/sensors/message>`    |Detects either text messages or property values                                                     +
+------------------------------------------------------+----------------------------------------------------------------------------------------------------+
+:doc:`Mouse <game_engine/logic/sensors/mouse>`        |Detects mous events.                                                                                +
+------------------------------------------------------+----------------------------------------------------------------------------------------------------+
+:doc:`Near <game_engine/logic/sensors/near>`          |Detects objects that move to within a specific distance of themselves.                              +
+------------------------------------------------------+----------------------------------------------------------------------------------------------------+
+:doc:`Property <game_engine/logic/sensors/property>`  |Detects changes in the properties of its owner object.                                              +
+------------------------------------------------------+----------------------------------------------------------------------------------------------------+
+:doc:`Radar <game_engine/logic/sensors/radar>`        |Detects objects that move to within a specific distance of themselves, within an angle from an axis.+
+------------------------------------------------------+----------------------------------------------------------------------------------------------------+
+:doc:`Random <game_engine/logic/sensors/random>`      |Generates random pulses.                                                                            +
+------------------------------------------------------+----------------------------------------------------------------------------------------------------+
+:doc:`Ray <game_engine/logic/sensors/ray>`            |Shoots a ray in the direction of an axis and detects hits.                                          +
+------------------------------------------------------+----------------------------------------------------------------------------------------------------+
+:doc:`Touch <game_engine/logic/sensors/touch>`        |Detects when the object is in contact with another object.                                          +
+------------------------------------------------------+----------------------------------------------------------------------------------------------------+


