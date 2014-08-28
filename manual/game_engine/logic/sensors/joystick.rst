
Joystick sensor
***************

.. figure:: /images/BGE_Sensor_Joystick1.jpg
   :width: 300px
   :figwidth: 300px

   Joystick sensor


The :guilabel:`Joystick` sensor triggers whenever the joystick moves.
It also detects events on a range of ancilliary controls on the joystick device (hat, buttons,
etc.). More than one joystick may be used (see "Index").
The exact layout of the joystick controls will depend on the make and model of joystick used.

See :doc:`Sensor Common Options </game_engine/logic/sensors/common_options>` for common options.

Special Options:

**Index**
   Specifies which joystick to use.
**All Events**
   Sensor triggers for all events on this joystick's current type


.. figure:: /images/BGE_Sensor_Joystick_Event.jpg
   :width: 200px
   :figwidth: 200px

   Joystick Events


**Event Type**
   A menu to select which joystick event to use


.. figure:: /images/BGE_Sensor_Joystick_SingAxis.jpg
   :width: 200px
   :figwidth: 200px

   Joystick Single Axis


   :guilabel:`Single Axis`
      Detect movement in a single joystick Axis.

      :guilabel:`Axis Number`
         1 = Horizontal axis (left/right)
         2 = Vertical axis (forward/back)
         3 = Paddle axis up/down
         4 = Joystick axis twist left/right
      :guilabel:`Axis Threshold`
         Threshold at which joystick fires (Range 0 - 32768)


.. figure:: /images/BGE_Sensor_Joystick_Hat.jpg
   :width: 200px
   :figwidth: 200px

   Joystick Hat


   :guilabel:`Hat`
      Detect movement of a specific hat control on the joystick.

      :guilabel:`Hat number`
          Specifies which hat to use (max. 2)
      :guilabel:`Hat Direction`
         Specifies the direction to use: up, down, left, right, up/right, up/left, down/right, down/left.


.. figure:: /images/BGE_Sensor_Joystick_Axis.jpg
   :width: 200px
   :figwidth: 200px

   Joystick Axis


   :guilabel:`Axis`
      :guilabel:`Axis Number`
         Specifies the axis (1 or 2)
      :guilabel:`Axis Threshold`
         Threshold at which joystick fires (Range 0 - 32768)
      :guilabel:`Axis Direction` specifies the direction to use:
          (Axis Number = 1) Joystick Left, Right, Up, Down
          (Axis Number = 2) Paddle upper (Left); paddle Lower (Right); Joystick twist left (Up) Joystick twist right (Down)


.. figure:: /images/BGE_Sensor_Joystick1.jpg
   :width: 200px
   :figwidth: 200px

   Joystick Button


   :guilabel:`Button`
      Specify the :guilabel:`button number` to use.

