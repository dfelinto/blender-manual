
Sensor Editing
==============

.. figure:: /images/BGE_Sensor_Column.jpg
   :width: 292px
   :figwidth: 292px

   Sensor Column with Typical Sensor


Blender sensors can be set up and edited in the left-hand column of the Logic Panel.
This page describes the general column controls,
and also those parameters  which are common to all individual sensor types.

The image shows a typical sensor column with a single example sensor.
At the top of this column, the column heading includes menus and buttons to control which of
all the sensors in the current Game Logic are displayed.


Column Heading
--------------

.. figure:: /images/BGE_Sensor_Column1.jpg
   :width: 292px
   :figwidth: 292px

   Sensor Column Heading


The column headings contain controls to set which sensors, and the level of detail given,
in the sensor column. This is very useful for hiding unecessary sensors so that the necessary
ones are visible and easier to reach. Both these can be controlled individually.

**Sensors**

+------------------------+----------------------------------------------------+
+:guilabel:`Show Objects`|Expands all objects.                                +
+------------------------+----------------------------------------------------+
+:guilabel:`Hide Objects`|Collapses all objects to just a bar with their name.+
+------------------------+----------------------------------------------------+
+:guilabel:`Show Sensors`|Expands all sensors.                                +
+------------------------+----------------------------------------------------+
+:guilabel:`Hide Sensors`|Collapses all sensors to bars with their names.     +
+------------------------+----------------------------------------------------+


It is also possible to filter which sensors are viewed using the four heading buttons:

+-----------------+--------------------------------------------------------------------+
+:guilabel:`Sel`  |Shows all sensors for selected objects.                             +
+-----------------+--------------------------------------------------------------------+
+:guilabel:`Act`  |Shows only  sensors belonging to the active object.                 +
+-----------------+--------------------------------------------------------------------+
+:guilabel:`Link` |Shows sensors which have a link to a controller.                    +
+-----------------+--------------------------------------------------------------------+
+:guilabel:`State`|Only sensors connected to a controller with active states are shown.+
+-----------------+--------------------------------------------------------------------+


Object Heading
--------------

.. figure:: /images/BGE_Sensor_Column2.jpg
   :width: 292px
   :figwidth: 292px

   Sensor Object Heading


In the column list, sensors are grouped by object. By default,
sensors for every selected object appear in the list,
but this may be modified by the column heading filters.

At the head of each displayed object sensor list, two entries appear:

**Name**
   The name of the object.
**Add Sensor**
   When clicked, a menu appears with the available sensor types. Selecting an entry adds a new sensor to the object. See :doc:`Sensors <game_engine/logic/sensors>` for a list of available sensor types.
