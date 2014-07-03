
Manipulators
============


.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object` and :guilabel:`Edit` modes
   | Hotkey:   :kbd:`ctrl-Space`


In combination with :doc:`axis locking <3d_interaction/transform_control/axis_locking>`\ , the normal Transform commands (\ :kbd:`G` for Grab, :kbd:`R` for Rotation, :kbd:`S` for Scale), can be used to manipulate objects along any axis. However, there may be times when these options are not adequate. For example, when you want to translate a single face on a randomly rotated object in a direction perpendicular to the face's normal. In instances like this, :guilabel:`Transform Manipulators` may be useful.


.. figure:: /images/Icon-library_3D-Window_3D-transform-manipulator-options.jpg

   Manipulator options in the Window Header.


Transform manipulators provide a visual representation of the transform options and allow
movement, rotation and scaling along any axis, mode and orientation of the 3D view. The
manipulator can be enabled by clicking on the axis icon from the manipulator options portion
of the window header or via the shortcut key :kbd:`ctrl-space`\ .

There is a separate manipulator for each Transform Command.
Each manipulator can be used separately or in combination with the others.
Clicking with :kbd:`shift-lmb` on multiple manipulator icons (arrow, arc, box)
will combine manipulator options.

Manipulators can be accessed in the header of the :guilabel:`3D View` window:

- Axis: Enable/disable the manipulators.
- Arrow: Translation.
- Arc: Rotation.
- Box: Scale.
- Transform Orientation menu: choice of the transformation orientation.


.. figure:: /images/3D_interaction-Transform_Control-Manipulators-manipulator_options.jpg
   :width: 650px
   :figwidth: 650px

   Manipulator Options


Manipulator controls
====================


- Holding down :kbd:`ctrl` constrains the action to set increments. Holding down :kbd:`shift` **after** you :kbd:`lmb` the manipulator handle will constrain the action to smaller increments.
- Holding down :kbd:`shift` **before** you :kbd:`lmb` click on one of the handles will cause the manipulator action to be performed relative to the other two axes (you can let go of :kbd:`shift` once you have clicked). For example, if you :kbd:`shift` then :kbd:`lmb` the Z axis handle of the translate manipulator, movement will occur in the X and Y planes.
- When in rotate mode,  :kbd:`lmb` on the white circle (largest circle around the rotation manipulator) will be equivalent to pressing :kbd:`R`\ .
- When in rotate mode,  :kbd:`lmb` on the grey circle (small inner circle at the center of the rotation manipulator) will be equivalent to pressing :kbd:`R` twice. This will start :guilabel:`trackball` rotation.

:doc:`Read more about constraining transformations » <3d_interaction/transform_control/precision>`
:doc:`Read more about axis locking » <3d_interaction/transform_control/axis_locking>`
:doc:`Read more about trackball rotation » <3d_interaction/transformations/basics/rotate>`


Manipulator Preferences
=======================


.. figure:: /images/3D_interaction-Transform_Control-Manipulators-manipulator_preferences.jpg

   Manipulator preferences.


The settings of the manipulator (e.g. its size)
can be found in the :guilabel:`Interface` section of the :guilabel:`User Preferences` window.

- :guilabel:`Size`\ : Diameter of the manipulator.
- :guilabel:`Handle Size`\ : Size of manipulator handles, as a percentage of the manipulator radius (\ :guilabel:`Size`\ /2).
- :guilabel:`Hotspot`\ : Hotspot size (in pixels) for clicking the manipulator handles.


Choosing the Transform Orientation
==================================


.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object` and :guilabel:`Edit` modes
   | Hotkey:   :kbd:`alt-space`


.. figure:: /images/Orientations-Menu-2.5%2B.jpg

   Transform Orientation options.


You can also change the :doc:`orientation of the Transform Manipulator <3d_interaction/transform_control/transform_orientations>` to global, local, gimbal, normal or view from the Transform options menu. The image below shows a cube with the rotation manipulator active in multiple transform orientations. Notice how the manipulator changes depending on the orientation selected (compare A with F).

Similarly, notice how when normal orientation (F and G)
is selected the manipulator changes between :guilabel:`Object mode` and :guilabel:`Edit mode`\ .
The normal orientation manipulator will also change depending on what is selected in
:guilabel:`Edit mode` i.e. the orientation is based on the normal of the selection which will
change depending on how many and which faces, edges or vertices are selected.


.. figure:: /images/3D_interaction-Transform_Control-Manipulators-manipulator_orientation_options.jpg
   :width: 640px
   :figwidth: 640px

   Transform manipulator orientation options.


- :guilabel:`A`\ : Standard cube in default top view with *global* orientation selected
- :guilabel:`B`\ : Standard cube with view rotated and *global* orientation selected
- :guilabel:`C`\ : Randomly rotated cube with view rotated and *global* orientation selected
- :guilabel:`D`\ : Randomly rotated cube with *local* orientation selected
- :guilabel:`E`\ : Randomly rotated cube with *gimbal* orientation selected
- :guilabel:`F`\ : Randomly rotated cube with *normal* orientation selected
- :guilabel:`G`\ : Randomly rotated cube, vertices selected with *normal* orientation selected
- :guilabel:`H`\ : Randomly rotated cube with *view* orientation selected