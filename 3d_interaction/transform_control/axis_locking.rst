


Axis Locking
============


Description
-----------


.. figure:: /images/3D_interaction-Transform_Control-Axis_locking-axis-locking.jpg
   :width: 150px
   :figwidth: 150px

   Axis locking


:doc:`Transformations (translation/scale/rotation) <3d_interaction/transformations>` in :guilabel:`Object` and :guilabel:`Edit` mode, as well as extrusion in :guilabel:`Edit` mode) can be locked to particular axis relative to the current :doc:`transform orientation <3d_interaction/transform_control/transform_orientations>`\ . By locking a transformation to a particular axis you are restricting transformations to a single dimension.


Usage
~~~~~


A locked axis will display in a brighter color than an unlocked axis.
For example in the image to the right,
the Z axis is drawn in light blue as movement is constrained to this axis.
This example can be achieved in two ways:


- Press :kbd:`G` to enable translation, press :kbd:`Z` to constrain movement to the Z-axis.


- Press :kbd:`G` to enable translation, move the mouse in the Z direction, then press :kbd:`MMB`\ .


Axis locking types
------------------


Axis locking
~~~~~~~~~~~~


.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object` and :guilabel:`Edit` modes (translate, rotate, scale, extrude)
   | Hotkey:   :kbd:`X`\ , :kbd:`Y`\ , :kbd:`Z` or :kbd:`MMB` after moving the mouse in the desired direction.


Axis locking limits the transformation to a single axis
(or forbids transformations along two axes). An object, face,
vertex or other selectable item will only be able to move,
scale or rotate in a single dimension.


Plane locking
~~~~~~~~~~~~~


.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object` and :guilabel:`Edit` modes (translate, scale)
   | Hotkey:   :kbd:`shift-X`\ , :kbd:`shift-Y`\ , :kbd:`shift-Z` or :kbd:`shift-MMB` after moving the mouse in the desired direction.


.. figure:: /images/3D_interaction-Transform_Control-Axis_locking-plane-locking.jpg
   :width: 150px
   :figwidth: 150px

   Plane locking


Plane locking locks the transformation to *two* axes
(or forbids transformations along one axis),
thus creating a plane in which the element can be moved or scaled freely.
Plane locking only affects translation and scaling.

Note that for rotation, both axis and plane locking have the same effect because a rotation is
always constrained around one axis.
:guilabel:`Trackball` type rotations :kbd:`R-R` cannot be locked at all.


Axis locking modes
~~~~~~~~~~~~~~~~~~


.. figure:: /images/3D_interaction-Transform_Control-Axis_locking-locking-modes.jpg
   :width: 340px
   :figwidth: 340px

   Axis locking modes


A single key press constrains movement to the corresponding :guilabel:`Global` axis. A second
key press of the *same* key constrains movement to the current transform orientation
selection (except if it is set to :guilabel:`Global`\ ,
in which case the :guilabel:`Local` orientation is used). Finally,
a third key press of the same key removes constraints.

For example, if the current transform orientation is set to :guilabel:`Normal`\ ,
pressing :kbd:`G` to start translation, followed by :kbd:`Z` will lock translation
in the Z direction relative to the :guilabel:`Global` orientation, pressing :kbd:`Z`
again will lock translation to the Z axis relative to the :guilabel:`Normal` orientation.
Pressing :kbd:`Z` again will remove all constraints.
The current mode will be displayed in the left hand side of the :guilabel:`3D window header`\ .


----

As can be seen in the *Axis locking modes* image,
the direction of the transform also takes into account the selection. Sections A and B show Z
axis locking in :guilabel:`Global` and :guilabel:`Normal` orientations respectively.
C and D show the same situation with face selection,
E and F with edge selection and G and H with vertex selection.

Note that using a locked axis does not prevent you from using the keyboard to enter :doc:`numeric transformation <3d_interaction/transform_control/numeric_input>` values.

