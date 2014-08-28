
Logic Editor
************

The Logic Editor provides the main method of setting up and editing the game logic for the
various actors (i.e. objects) that make up the game.  The logic for the objects which are
currently selected in the associated 3D panel are displayed as logic bricks,
which are shown as a table with three columns, showing sensors, controllers, and actuators,
respectively. The links joining the logic bricks conduct the pulses between sensor-controller
and controller-actuator.

To give you a better understanding of the Logic Editor panel, the image below shows a typical
panel content in which the major components have been  labeled.
We will look at each one individually.


+-------------------------------------------------------------+
+.. figure:: /images/Manual-2.5-Logic_Panel_Expanded_menus.jpg+
+   :width: 610px                                             +
+   :figwidth: 610px                                          +
+                                                             +
+   The different parts of the Logic Panel.                   +
+-------------------------------------------------------------+


 **1) Game Property Area**

Game properties are like variables in other programming languages. They are used to save and access data associated with an object. Several types of properties are available. Properties are declared by clicking the Add Game Property button in this area. For a more in-depth look at the content, layout and available operations in this area, see :doc:`Properties </game_engine/logic/properties>`.


 **2) Object Name**

This box shows the name of the object  which owns the logic bricks below.


 **3) Links**

Links (3A) indicate the direction of logical flow between objects.
Link lines are drawn by :kbd:`Lmb` dragging from one Link node (3B) to another.
Links can only be drawn from Sensors to Controllers, or from Controllers to Actuators.
You cannot directly link Sensors to Actuators; likewise,
Actuators cannot be linked back to Sensors
(however special actuator and sensor types are available to provide these connections).

Sending nodes (the black circles found on the right-hand side of Sensors and Controllers)
can send to multiple Reception nodes
(the white circles found on the left-hand side of Controllers and Actuators).
Reception nodes can likewise receive multiple links.

Links can be created between logic bricks belonging to different objects.

To delete a link between two nodes, :kbd:`Lmb` drag between the two nodes.


 **4) Sensor Area**

This column contains a list of all sensors owned by the active object (and any other selected objects). New sensors for the active object are created using the "Add Sensor" button.  For a more in-depth look at the content, layout and available operations in this area, see :doc:`Sensors </game_engine/logic/sensors>`.


 **5) Controller Area**

This column contains a list of all controllers owned by the active object (and any other selected objects). New controllers for the active object are created using the "Add Controller" button, together with the creation of states for the active object. For a more in-depth look at the content, layout, and available operations in this area,  see :doc:`Controllers </game_engine/logic/controllers>`.


 **6) Actuator Area**
This column contains a list of all actuators owned by the active object (and any other selected objects). New actuators for the active object are created using the "Add Actuator" button.  For a more in-depth look at the content, layout, and available operations in this area, see :doc:`Actuators </game_engine/logic/actuators>`.


