
Controller Editing
******************

.. figure:: /images/BGE_Controller_Column.jpg
   :width: 292px
   :figwidth: 292px

   Controller Column with Typical Sensor


Blender controllers can be set up and edited in the central column of the Logic Panel.
This page describes the general column controls,
those parameters  which are common to all individual controller types,
and how different states for the objects in the logic system can be set up and edited.

The image shows a typical controller column with a single controller.
At the top of this column, and for sensors and actuators,  the column heading includes menus
and buttons to control which of all the controllers in the current Game Logic are displayed.


Column Heading
==============

.. figure:: /images/BGE_Controller_Column1.jpg
   :width: 292px
   :figwidth: 292px

   Controller Column Headings


The column headings contain controls to set which controllers appear,
and the level of detail given, in the controller column. This is very useful for hiding
unecessary controllers so that the necessary ones are visible and easier to reach.
Both these can be controlled individually.
**Controllers**

+----------------------------+----------------------------------------------------+
+:guilabel:`Show Objects`    |Expands all objects.                                +
+----------------------------+----------------------------------------------------+
+:guilabel:`Hide Objects`    |Collapses all objects to just a bar with their name.+
+----------------------------+----------------------------------------------------+
+:guilabel:`Show Controllers`|Expands all Controllers.                            +
+----------------------------+----------------------------------------------------+
+:guilabel:`Hide Controllers`|Collapses all Controllers to bars with their names. +
+----------------------------+----------------------------------------------------+


It is also possible to filter which controllers are viewed using the three heading buttons:

+----------------+---------------------------------------------------------+
+:guilabel:`Sel` |Shows all controllers for selected objects.              +
+----------------+---------------------------------------------------------+
+:guilabel:`Act` |Shows only  controllers belonging to the active object.  +
+----------------+---------------------------------------------------------+
+:guilabel:`Link`|Shows controllers which have a link to actuators/sensors.+
+----------------+---------------------------------------------------------+


Object Heading
==============

.. figure:: /images/BGE_Controller_Column2.jpg
   :width: 292px
   :figwidth: 292px


.. figure:: /images/BGE_Controller_Column4.jpg
   :width: 292px
   :figwidth: 292px


In the column list, controllers are grouped by object. By default,
controllers for every selected object appear in the list,
but this may be modified by the column heading filters.

At the head of each displayed object controller list, three entries appear:
   **(Used States Button)**
   Shows which states are in use for the  object. Detailed description of the marked panel is given in :doc:`States <game_engine/logic/states>`.
**Name**
   The name of the object.
**Add Controller**
   When clicked, a menu appears with the available controller types. Selecting an entry adds a new controller to the object. See :doc:`Controllers <game_engine/logic/controllers>` for a list of available controller types.

