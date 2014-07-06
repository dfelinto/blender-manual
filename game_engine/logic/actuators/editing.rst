
Actuator Editing
****************

.. figure:: /images/BGE_Actuator_Column.jpg
   :width: 292px
   :figwidth: 292px

   Actuator Column with Typical Actuator


Blender actuators can be set up and edited in the right-hand column of the Logic Panel.
This page describes the general column controls,
and also those parameters  which are common to all individual actuator types.

The image shows a typical actuator column with a single example actuator.
At the top of this column, the column heading includes menus and buttons to control which of
all the actuators in the current Game Logic are displayed.


Column Heading
==============

.. figure:: /images/BGE_Actuator_Column1.jpg
   :width: 292px
   :figwidth: 292px

   Actuator Column Heading


The column headings contain controls to set which actuators, and the level of detail given,
in the actuator column. This is very useful for hiding unecessary actuators so that the
necessary ones are visible and easier to reach. Both these can be controlled individually.

**Actuators**

+--------------------------+----------------------------------------------------+
+:guilabel:`Show Objects`  |Expands all objects.                                +
+--------------------------+----------------------------------------------------+
+:guilabel:`Hide Objects`  |Collapses all objects to just a bar with their name.+
+--------------------------+----------------------------------------------------+
+:guilabel:`Show Actuators`|Expands all actuators.                              +
+--------------------------+----------------------------------------------------+
+:guilabel:`Hide Actuators`|Collapses all actuators to bars with their names.   +
+--------------------------+----------------------------------------------------+


It is also possible to filter which actuators are viewed using the four heading buttons:

+-----------------+----------------------------------------------------------------------+
+:guilabel:`Sel`  |Shows all actuators for selected objects.                             +
+-----------------+----------------------------------------------------------------------+
+:guilabel:`Act`  |Shows only  actuators belonging to the active object.                 +
+-----------------+----------------------------------------------------------------------+
+:guilabel:`Link` |Shows actuators which have a link to a controller.                    +
+-----------------+----------------------------------------------------------------------+
+:guilabel:`State`|Only actuators connected to a controller with active states are shown.+
+-----------------+----------------------------------------------------------------------+


Object Heading
==============

.. figure:: /images/BGE_Actuator_Column2.jpg
   :width: 292px
   :figwidth: 292px

   Actuator Object Heading


In the column list, actuators are grouped by object. By default,
actuators for every selected object appear in the list,
but this may be modified by the column heading filters.

At the head of each displayed object sensor list, two entries appear:

**Name**
   The name of the object.
**Add**
   When clicked, a menu appears with the available actuator types. Selecting an entry adds a new actuator to the object. See `Actuators <http://wiki.blender.org/index.php/User:Sculptorjim/Game Engine/Logic/Actuators/Overview>`__ for list of available actuator types.


