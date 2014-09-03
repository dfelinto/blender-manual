
Property Sensor
***************

.. figure:: /images/BGE_Sensor_Property1.jpg
   :width: 300px
   :figwidth: 300px

   Property sensor


The :guilabel:`Property` sensor detects changes in the properties of its owner object.

See :doc:`Sensor Common Options </game_engine/logic/sensors/common_options>` for common options.

Special Options:


.. figure:: /images/Property_evaluation_types.jpg
   :width: 300px
   :figwidth: 300px

   Property Evaluation


Evaluation Type
   Specifies how the property  will be evaluated against the value(s).

Greater Than
   Sends a TRUE pulse when the property value is greater than the :guilabel:`Value` in the sensor.

Less Than
   Sends a TRUE pulse when the property value is less than the :guilabel:`Value` in the sensor.

Changed
   Sends a TRUE pulse as soon as the property value changes.

Interval
   Sends a TRUE pulse when the :guilabel:`Value` of the property is between the :guilabel:`Min` and :guilabel:`Max` values of the sensor.

Not Equal
   Sends a TRUE pulse when the property value differs from the :guilabel:`Value` in the sensor.

Equal
   Sends a TRUE pulse when the property value matches the :guilabel:`Value` in the sensor.

Note the names of other properties can also be entered to compare properties.

