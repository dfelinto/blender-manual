
Ray Sensor
**********

.. figure:: /images/BGE_Sensor_Ray.jpg
   :width: 300px
   :figwidth: 300px

   Ray sensor


The :guilabel:`Ray` sensor shoots a ray in the direction of an axis and sends a positive pulse
once it hits something.
It can be filtered to only detect objects with a given material or property.

See :doc:`Sensor Common Options </game_engine/logic/sensors/common_options>` for common options.

Special Options:
It shares a lot of buttons and fields with :guilabel:`Radar` sensor.

Property
   This field can be used to limit the sensor to look for only those objects with this property.

.. note::

   #. Unless the Property field is set, the Ray sensor can detect objects "through" other objects (walls etc).
   #. Objects must have "Actor" enabled to be detected.

Axis
   This menu determines the direction of the ray.
   The ± signs is whether it is on the axis direction (+), or the opposite (-).

Range
   Determines the length of the ray. (Blender units).

:kbd:`X-Ray Mode` **button**
   Makes it x-ray, so that it sees through objects that don't
   have the property or material specified in the filter field.

