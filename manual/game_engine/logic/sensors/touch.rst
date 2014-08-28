
Touch sensor
************

.. figure:: /images/BGE_Sensor_Touch.jpg
   :width: 300px
   :figwidth: 300px

   Touch sensor


The :guilabel:`Touch` sensor sends a positive pulse when the object is in contact with another
object.

See :doc:`Sensor Common Options </game_engine/logic/sensors/common_options>` for common options.

Special Options:

**Material**
   This field is for filtering materials. Only contact with the material in this field will generate a positive pulse. Leave blank for touch with any object.
A TRUE pulse is sent on collision and the FALSE pulse is sent once the objects are no longer
in contact.


.. admonition:: Touch sensor has been removed in 2.69
   :class: note

   The :guilabel:`Touch` sensor is no longer available in v2.69 or later. The :doc:`Collision Sensor </game_engine/logic/sensors/collision>` now provides the same functionality.


.. admonition:: Note about soft bodies
   :class: note

   The :guilabel:`Touch` sensor can not detect collisions with soft bodies. This is a limitation in Bullet, the physics library used by the Game Engine.


