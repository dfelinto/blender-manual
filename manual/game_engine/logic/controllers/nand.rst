
NAND Controller
***************

This controller **activates** all connected actuators if

- the game object is in the designated state
- at least one connected sensor triggers the controller
- at least one connected sensor evaluated False

This controller **deactivates** all connected actuators if

- the game object is in the designated state
- at least one connected sensor triggers the controller
- ALL connected sensor evaluated True


Options:


.. figure:: /images/BGE_Controller_Nan.jpg
   :width: 292px
   :figwidth: 292px

   NAND Controller


Controller Type menu
   Specifies the type of the controller.

Controller Name
   The name of the controller. This can be selected by the user. It is used to access controllers with python; it needs to be unique among the selected objects.

State Index
   Sets the designated state for which this controller will operate.

Preference Button
   If enabled, this controller will operate before all other non-preference controllers (useful for start-up scripts).

:kbd:`X` **Button**
   Deletes the sensor.


