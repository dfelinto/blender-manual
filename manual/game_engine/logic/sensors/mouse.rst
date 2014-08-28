
Mouse sensor
************

.. figure:: /images/BGE_Sensor_Mouse1.jpg
   :width: 300px
   :figwidth: 300px

   Mouse sensor


The :guilabel:`Mouse` sensor is for detecting mouse events.

See :doc:`Sensor Common Options </game_engine/logic/sensors/common_options>` for common options.


.. figure:: /images/BGE_Sensor_Mouse_Events.jpg
   :width: 300px
   :figwidth: 300px

   Mouse Events


Special Options:
The controller consist only of a list of types of mouse events. These are:


- :guilabel:`Mouse over any`, gives a TRUE pulse if the mouse moves over any game object.
- :guilabel:`Mouse over`, gives a TRUE pulse if the mouse moves over the owner object.
- :guilabel:`Movement`, any movement with the mouse causes a stream of TRUE pulses.
- :guilabel:`Wheel Down`, causes a stream of TRUE pulses as the scroll wheel of the mouse moves down.
- :guilabel:`Wheel Up`, causes a stream of TRUE pulses as the scroll wheel of the mouse moves up.
- :guilabel:`Right button` gives a TRUE pulse.
- :guilabel:`Middle button` gives a TRUE pulse.
- :guilabel:`Left button` gives a TRUE pulse.

A FALSE pulse is given when any of the above conditions ends.

There is no logic brick for specific mouse movement and reactions
(such as first person camera), these have to be coded in python.

