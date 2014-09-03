
Message Sensor
**************

.. figure:: /images/BGE_Sensor_Message.jpg
   :width: 300px
   :figwidth: 300px

   Message sensor


The :guilabel:`Message` sensor can be used to detect either text messages or property values.
The  sensor sends a positive pulse once an appropriate message is sent from anywhere in the
engine. It can be set up to only send a pulse upon a message with a specific subject.


See :doc:`Sensor Common Options </game_engine/logic/sensors/common_options>` for common options.

Special Options:

Subject
   Specifies the message that must be received to trigger the sensor (this can be left blank).

Note:  See :doc:`Message Actuator </game_engine/logic/actuators/message>` for how to send messages

