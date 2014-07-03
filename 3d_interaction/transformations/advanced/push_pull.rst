


Push/Pull
=========


.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object` and :guilabel:`Edit` modes
   | Menu:     :menuselection:`Object/Mesh --> Transform --> Push Pull`


Description
-----------


.. figure:: /images/3D_interaction-Transformations-Advanced-Push_Pull_toolshelf-f6.jpg
   :width: 150px
   :figwidth: 150px

   Push/Pull distance.


:guilabel:`Push/Pull` will move the selected elements (Objects, vertices, edges or faces) closer together (Push) or further apart (Pull). Specifically, each element is moved towards or away from the center by the same distance. This distance is controlled by moving the mouse up (Push) or down (Pull), numeric input or through slider control.


Usage
~~~~~


Select the elements you want to operate on and activate the Push/Pull transform function. The
Push/Pull option can be invoked from the :menuselection:`Object/Mesh --> Transform --> Push/Pull` menu option
or by pressing :kbd:`space` and using the search menu to search for :guilabel:`Push` or
:guilabel:`Pull`\ . The amount of movement given to the selection can be determined
interactively by moving the mouse or by typing a number.
Pressing :kbd:`Enter` will confirm the transformation. The confirmed transformation can
be further edited by pressing F6 or by going into the Toolshelf (\ :kbd:`T`\ ) and altering
the Distance slider provided that no other actions take place between the
:guilabel:`Push/Pull` transform confirmation and accessing the slider.


----

Note that the result of the :guilabel:`Push/Pull` transform is also dependant on the number
and type of selected elements (Objects, vertices, faces etc).
See below for the result of using :guilabel:`Push/Pull` on a number of different elements.


.. figure:: /images/3D_interaction-Transformations-Advanced-Push_Pull_equidistant_objects.jpg
   :width: 640px
   :figwidth: 640px

   Equidistant Objects being pushed together.


.. figure:: /images/3D_interaction-Transformations-Advanced-Push_Pull_random_objects.jpg
   :width: 640px
   :figwidth: 640px

   Random Objects being pushed together.


.. figure:: /images/3D_interaction-Transformations-Advanced-Push_Pull_vertices-push-pull.jpg
   :width: 640px
   :figwidth: 640px

   Vertices being pushed together, then pulled apart.


.. figure:: /images/3D_interaction-Transformations-Advanced-Push_Pull_edges-push-pull.jpg
   :width: 640px
   :figwidth: 640px

   Edges on separate meshes being pushed together, then pulled apart.


