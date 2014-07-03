
Collision sensor
================

.. figure:: /images/BGE_Sensor_Collision.jpg
   :width: 300px
   :figwidth: 300px

   Collision sensor


A :guilabel:`Collision` sensor works like a :guilabel:`Touch` sensor but can also filter by
property or material. Only objects with the property/material with that name will generate a
positive pulse upon collision. Leave blank for collision with any object.

See :doc:`Sensor Common Options <game_engine/logic/sensors/common_options>` for common options.

Special Options:
:kbd:`Pulse` **button**
    Makes it sensible to other collisions even if it is still in touch with the object that triggered the last positive pulse.

:kbd:`M/P` **button**
    Toggles between material and property filtering.


.. admonition:: Note about soft bodies
   :class: note

    The :guilabel:`Collision` sensor can not detect collisions with soft bodies. This is a limitation in Bullet, the physics library used by the Game Engine.


