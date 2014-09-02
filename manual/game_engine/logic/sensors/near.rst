
Near sensor
***********

.. figure:: /images/BGE_Sensor_Near.jpg
   :width: 300px
   :figwidth: 300px

   Near sensor


A :guilabel:`Near` sensor detects objects that move to within a specific distance of
themselves. It can filter objects with properties, like the :guilabel:`Collision` sensor.


See :doc:`Sensor Common Options </game_engine/logic/sensors/common_options>` for common options.

Special Options:

**Property**
   This field can be used to limit the sensor to look for only those objects with this property.

**Distance**
   The number of blender units it will detect objects within.

**Reset**
   The distance the object needs to be to reset the sensor (send a FALSE pulse).

Notes:
1) The Near sensor can detect objects "through" other objects (walls etc).
2) Objects must have "Actor" enabled to be detected.


.. note:: Note about soft bodies

   The :guilabel:`Near` sensor can not detect soft bodies. This is a limitation in Bullet, the physics library used by the Game Engine.


