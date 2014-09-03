
Message Actuator
****************

The Message actuator allows the user to send data across a scene,
and between scenes themselves.


.. figure:: /images/2.5_Game_Engine_Actuator_Message.jpg
   :width: 271px
   :figwidth: 271px

   Message actuator


.. figure:: /images/2.5_Game_Engine_Actuator_Message_Options.jpg
   :width: 271px
   :figwidth: 271px

   Message actuator Options


See :doc:`Actuator Common Options </game_engine/logic/actuators/common_options>` for common options.

Special Options:

To
   Object to broadcast to. Leave blank if broadcast to all (or sending to another scene).
Subject
   Subject of message. Useful if sending certain types of message, such as "end-game",
   to a message sensor listening for "end game"→AND→Quit Game actuator
Body
   Body of message sent (only read by Python*).
Text
   User specified text in body.
Property
   User specified property.


**Usage Notes**
You can use the Message Actuator to send data, such as scores to other objects,
or even across scenes! (alternatively use ``bge.logic.globalDict``).

