
Keyboard Sensor
===============

.. figure:: /images/BGE_Sensor_Keyboard.jpg
   :width: 300px
   :figwidth: 300px

   Keyboard sensor


The :guilabel:`Keyboard` sensor is for detecting keyboard input.
It can also save keyboard input to a :doc:`String property <game_engine/logic/properties#property_types>`.

See :doc:`Sensor Common Options <game_engine/logic/sensors/common_options>` for common options.

Special Options:

**Key**
   This field detects presses on a named key. Press the button with no label and a key to assign that key to the sensor.
   This is the active key, which will trigger the TRUE pulse.
   Click the button and then click outside of the button to deassign the key.

A FALSE pulse is given when the key is released.

:kbd:`All keys` **button**
   Sends a TRUE pulse when any key is pressed.  This is useful for custom key maps with a :doc:`Python controller <_engine/logic/controllers#python_controller>`.

**First Modifier**, **Second Modifier**
   Specifies additional key(s), all of which must be held down while the active key  is pressed in order for the sensor to give a TRUE pulse. These are selected in the same way as Key.  This is useful if you wish to use key combinations,  for  example :kbd:`ctrl-R` or :kbd:`shift-alt-Esc` to do a specific action.

**LogToggle**
   Assigns a :guilabel:`Bool` property which determines if the keystroke will or will not be logged in the target :guilabel:`String`. This property needs to be TRUE if you wish to log your keystrokes.

**Target**
   The name of property to which the keystrokes are saved. This property must be of type :guilabel:`String`.  Together with a :guilabel:`Property` sensor this can be used for example to enter passwords.

