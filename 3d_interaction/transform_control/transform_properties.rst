

..    TODO/Review: {{review|text= delta transforms}} .

Transform Properties
====================

Each object stores its position, orientation, and scale values.
These may need to be manipulated numerically, reset, or applied.


Transform Properties Panel
==========================


 .. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` and :guilabel:`Object` modes
   | Menu:     :menuselection:`Object --> Transform Properties`
   | Hotkey:   :kbd:`N`


The :guilabel:`Transform Properties` section in the :guilabel:`View Properties` panel allows you to view and manually/numerically control the position, rotation, and other properties of an object, in :guilabel:`Object` mode. In :guilabel:`Edit` mode, it mainly allows you to enter precise coordinates for a vertex, or median position for a group of vertices (including an edge/face). As each type of object has a different set of options in its :guilabel:`Transform Properties` panel in :guilabel:`Edit` mode, see their respective descriptions in the :doc:`Modeling chapter <modeling>`\ .


Options in Object mode
----------------------


.. figure:: /images/Transform-properties-panel.jpg

   Transform Properties panel in Object mode.


:guilabel:`Location X`\ , :guilabel:`Location Y`\ , :guilabel:`Location Z`
   The object's center location in global coordinates.

:guilabel:`Rotation X`\ , :guilabel:`Rotation Y`\ , :guilabel:`Rotation Z`
   The object's orientation, relative to the global axes and its own center.

:guilabel:`Scale X`\ , :guilabel:`Scale Y`\ , :guilabel:`Scale Z`
   The object's scale, relative to its center, in local coordinates (i.e. the :guilabel:`Scale X` value represents the scale along the local X-axis). Each object (cube, sphere, etc.), when created, has a scale of one blender unit in each local direction. To make the object bigger or smaller, you scale it in the desired dimension.

:guilabel:`Dimensions X`\ , :guilabel:`Dimensions Y`\ , :guilabel:`Dimensions Z`
   The object's basic dimensions (in blender units) from one outside edge to another, as if measured with a ruler. For multi-faceted surfaces, these fields give the dimensions of the bounding box (aligned with the local axes - think of a cardboard box just big enough to hold the object).

..    Comment: <!-- ;{{Literal|Link Scale}}
   :If this toggle-button is activated the relation (proportion) between the X, Y and Z values in the {{Literal|Scale}} and the {{Literal|Dim}} fields is always preserved. Changing one value will change all the others as well with the same multiplication-factor. --> .

Use this panel to either edit or display the object's transform properties such as position,
rotation and/or scaling. These fields change the object's center and then affects the aspect
of all of its *vertices* and faces.


 .. admonition:: Note
   :class: note

   center


Some fields have extra functionality or features, such as scroll regions. When attempting to edit these types of fields it is easier to use {\ :kbd:`shift-lmb` instead of just :kbd:`lmb`\ . After you have edited a field click outside of the field's edit area or press :kbd:`enter` to confirm the changes. Changes will be reflected in the display window immediately. To cancel, hit :kbd:`Esc`\ . For further descriptions of the other features of an edit field see :doc:`The Interface <interface>` section.


Transform Properties Locking
----------------------------

The locking feature of the Location, Rotation and Scale fields allows you to control a
transform property solely from the properties panel.
Once a lock has been activated any other methods used for transformation are blocked.
For example, if you locked the :guilabel:`Location X` field then you can't use the mouse to
translate the object along the global X axis. However,
you can still translate it using the :guilabel:`Location X` edit field.
Consider the locking feature as a rigid constraint only changeable from the panel.

To lock a field, click the padlock icon next to the field. The field is unlocked if the icon appears as (

.. figure:: /images/Manual-Part-II-ObjectMode-TransformProperties-Panel-Unlocked.jpg


), and it is locked if the icon appears as (

.. figure:: /images/Manual-Part-II-ObjectMode-TransformProperties-Panel-Locked.jpg


).


