

..    TODO/Review: {{review|}} .


Clear Object transformations
============================


.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object` mode
   | Menu:     :menuselection:`Object --> Clear --> Clear Location/Clear Scale/Clear Rotation/Clear Origin`
   | Hotkey:   :kbd:`alt-G`\ , :kbd:`alt-S`\ , :kbd:`alt-R`\ , :kbd:`alt-O`


Description
-----------

Clearing transforms simply resets the transform values.
The objects location and rotation values return to 0, and the scale returns to 1.


Clear Options
-------------


.. figure:: /images/3D-interaction_Transform-Control_Object-Transformations-clear-transformations.jpg

   Clear Transformation menu


**Clear Location** :kbd:`alt-G`
   Clear (reset) the location of the selection. This will move the selection back to the coordinates 0,0,0.

**Clear Scale** :kbd:`alt-S`
   Clear (reset) the scale of the selection. This will resize the selection back to the size it was when created.

**Clear Rotation** :kbd:`alt-R`
   Clear (reset) the rotation of the selection. This will set the rotation of the selection to 0 degrees in each plane.

**Clear Origin** :kbd:`alt-O`
   Clear (reset) the origin of the Child objects. This will cause Child objects to move to the coordinates of the parent.


Apply Object transformations
============================


.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object` mode
   | Menu:     :menuselection:`Object --> Apply -->`
   | Hotkey:   :kbd:`ctrl-a`


Applying transform values essentially resets the values of object's position, rotation,
or scale, but does not actually do anything to the object.
The center point is moved to the origin and the transform values are set to zero.
In terms of scale, the scale values return to 1.

To apply a transform select the :guilabel:`Apply` sub-menu from the :guilabel:`Object menu` or
use the shortcut :kbd:`ctrl-A` and select the appropriate transform to apply

:guilabel:`Make Duplicates Real` unlinks linked duplicates so each duplicate now has its own datablock.


Apply Options
-------------


.. figure:: /images/3D-interaction_Transform-Control_Object-Transformations-apply-transformations.jpg

   Apply Transformation menu


**Apply Location** :kbd:`ctrl-a`
   Apply (set) the location of the selection. This will make Blender consider the current location to be equivalent to 0 in each plane i.e. the selection will not move, the current location will be considered to be the "default location". The Object Center will be set to actual 0,0,0 (where the coloured axis lines intersect in each view).

**Apply Rotation** :kbd:`ctrl-a`
   Apply (set) the rotation of the selection. This will make Blender consider the current rotation to be equivalent to 0 degrees in each plane i.e. the selection will not rotated, the current rotation will be considered to be the "default rotation".

**Apply Scale** :kbd:`ctrl-a`
   Apply (set) the scale of the selection. This will make Blender consider the current scale to be equivalent to 0 in each plane i.e. the selection will not scaled, the current scale will be considered to be the "default scale".

**Apply Rotation and Scale** :kbd:`ctrl-a`
   Apply (set) the rotation and scale of the selection. Do the above two applications simultaneously.

**Apply Visual Transform** :kbd:`ctrl-a`
   Apply (set) the result of a constraint and apply this back to the Object's location, rotation and scale. See the following post for more detailed discussion: `Apply visual transform <http://projects.blender.org/tracker/index.php?func=detail&group_id=9&atid=498&aid=24616>`__\ .

**Make Duplicate Real** :kbd:`shift-ctrl-a`
   Make any duplicates attached to this Object real so that they can be edited.

