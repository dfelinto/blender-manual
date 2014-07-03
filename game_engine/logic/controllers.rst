


Controllers
===========

The controllers are the bricks that collect data sent by the sensors,
and also specify the state for which they operate.
After performing the specified logic operations,
they  send out pusle signals to drive the actuators to which they are connected.

When a sensor is activated, it sends out a positive pulse, and when it is deactivated,
it sends out a negative pulse.
The controllers' job is to check and combine these pulses to trigger the proper response.

The logic blocks for all types of controller may be constructed and changed using the :doc:`Logic Editor <game_engine/logic/editor>`\ ; details of this process are given in the :doc:`Controller Editing <game_engine/logic/controllers/editing>` page.


Controller Types
----------------


There are eight types of controller logic brick to carry out the logic process on the input
signal(s): these are described in the separate pages shown below:


- :doc:`AND <game_engine/logic/controllers/and>`
- :doc:`OR <game_engine/logic/controllers/or>`
- :doc:`XOR <game_engine/logic/controllers/xor>`
- :doc:`NAND <game_engine/logic/controllers/nand>`
- :doc:`NOR <game_engine/logic/controllers/nor>`
- :doc:`XNOR <game_engine/logic/controllers/xnor>`
- :doc:`Expression <game_engine/logic/controllers/expression>`
- :doc:`Python <game_engine/logic/controllers/python>`

This table gives a quick overview of the logic operations performed by the logical controller
types. The first column, input,
represents the number of positive pulses sent from the connected sensors.
The following columns represent each controller's response to those pulses.
True means the conditions of the controller are fulfilled,
and the actuators it is connected to will be activated;
false means the controller's conditions are not met and nothing will happen. Please consult
the individual controller pages for a more detailed description of each controller.


 .. admonition:: Note
   :class: note

   It is assumed that more than one sensor is connected to the controller. For only one sensor, consult the "All" line.


+----------------+-----------+----------------------------------------------+--------------------------------------------+----------------------------------------------+------------------------------------------------+----------------------------------------------+------------------------------------------------+----+-----+-----+-----+----+----+----+---+-----+----+----+----+-----+-----+-----------------+-----+----+-----+----+-----+----+---+----+----+-----+-----+-----+----+
+Positive sensors|Controllers|:doc:`AND <game_engine/logic/controllers/and>`|:doc:`OR <game_engine/logic/controllers/or>`|:doc:`XOR <game_engine/logic/controllers/xor>`|:doc:`NAND <game_engine/logic/controllers/nand>`|:doc:`NOR <game_engine/logic/controllers/nor>`|:doc:`XNOR <game_engine/logic/controllers/xnor>`|None|False|False|False|True|True|True|One|False|True|True|True|False|False|Multiple, not all|False|True|False|True|False|True|All|True|True|False|False|False|True+
+----------------+-----------+----------------------------------------------+--------------------------------------------+----------------------------------------------+------------------------------------------------+----------------------------------------------+------------------------------------------------+----+-----+-----+-----+----+----+----+---+-----+----+----+----+-----+-----+-----------------+-----+----+-----+----+-----+----+---+----+----+-----+-----+-----+----+


