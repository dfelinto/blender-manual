
Delay sensor
============

.. figure:: /images/BGE_Sensor_Delay.jpg
   :width: 300px
   :figwidth: 300px

   Delay sensor


The :guilabel:`Delay` sensor is designed for delaying reactions a number of logic ticks.
This is useful if an other action has to be done first or to time events.

See :doc:`Sensor Common Options <game_engine/logic/sensors/common_options>` for common options.
Special Options:
**Delay**
    The number of logic ticks the sensor waits before sending a positive pulse.
**Duration**
    The number of logic ticks the sensor waits before sending the negative pulse.
**Repeat Button**
    Makes the sensor restart after the delay and duration time is up.

