
Properties
==========

Properties are the game logic equivalent to variables. They are stored with the object,
and can be used to represent things about them such as ammo, health, name, and so on.


Property Types
--------------

There are five types of properties:

+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+:guilabel:`Timer`  |Starts at the property value and counts upwards as long as the object exists. It can for example be used if you want to know how long time it takes the player to complete a level.+
+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+:guilabel:`Float`  |Uses decimal numbers as values, can range from -10000.000 to 10000.000. It is useful for precision values.                                                                         +
+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+:guilabel:`Integer`|Uses integers (whole numbers) as values, between -10000 and 10000. Useful for counting things such as ammunition, where decimals are unnecessary.                                  +
+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+:guilabel:`String` |Takes text as value. Can store 128 characters.                                                                                                                                     +
+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+:guilabel:`Boolean`|Boolean variable, has two values: true or false. This is useful for things that have only two modes, like a light switch.                                                          +
+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


Using Properties
----------------

Properties can be set up and initialised in the Properties panel of the Logic Editor - see the :doc:`Property Editing <game_engine/logic/properties/editing>` page for details.  When a game is running, values of properties are set, manipulated, and evaluated using the :doc:`Property Sensor <game_engine/logic/sensors/property>` and the :doc:`Property Actuator <game_engine/logic/actuators/property>`\ .


FIXME(Template Unsupported: Category:Game engine;
{{Category:Game engine}}
)