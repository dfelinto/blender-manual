
Rotate
======


.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object` and :guilabel:`Edit` modes
   | Menu:     :menuselection:`Object/Mesh/Curve/Surface --> Transform --> Rotate`
   | Hotkey:   :kbd:`r`


Description
-----------

Rotation is also known as a spin, twist, orbit, pivot, revolve,
or roll and involves changing the orientation of elements (vertices, edge, face, Object etc)
around one or more axes or the element's Pivot Point.
There are multiple ways to rotate an element which include:


- The keyboard shortcut (\ :kbd:`R`\ )
- The 3D manipulator widget
- The Properties menu (\ :kbd:`N`\ )

Basic rotation usage and common options are described below. For additional information, you
may wish to read the Transform Control and Orientation pages which provide more information
about options such as Precision, Axis Locking, Numeric Input,
Snapping and the different types of Pivot Point.

:doc:`Read more about Transform Control » <3d_interaction/transform_control>`
:doc:`Read more about Transform Orientations » <3d_interaction/transform_control/transform_orientations>`


----


Usage
-----


Rotation using the keyboard shortcut
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


- Use :kbd:`RMB` to select the elements you want to rotate.
- Tap :kbd:`r` once to enter rotation mode.
- Rotate the elements by moving the mouse. The closer the mouse is to the elements's center, the higher the rotation influence.
- :kbd:`LMB` click to accept changes.

The amount of rotation will be displayed in the bottom left hand corner of the 3D window.


.. figure:: /images/3D_interaction-Transformations-Basic-Rotate-rotate_value_header.jpg

   Rotation values


Constraining the rotation axis (axis locking)
_____________________________________________

Rotation can be constrained to a particular axis or axes through the use of :doc:`Axis Locking <3d_interaction/transform_control/axis_locking>`\ . To constrain rotation, the following shortcuts can be used:


- :kbd:`r`\ , :kbd:`X`\ : Rotate only along the **X Axis**
- :kbd:`r`\ , :kbd:`Y`\ : Rotate only along the **Y Axis**
- :kbd:`r`\ , :kbd:`Z`\ : Rotate only along the **Z Axis**

Axis locking can also be enabled by pressing the :kbd:`MMB` after enabling rotation and
moving the mouse in the desired direction e.g.


- :kbd:`r`\ , move the mouse along the X axis, :kbd:`MMB`\ : Rotate only along the **X Axis**

:doc:`Read more about Axis Locking » <3d_interaction/transform_control/axis_locking>`


Fine Tuning The Rotation
________________________


:doc:`Precise control <3d_interaction/transform_control/precision>` can be had over rotation through the use of the :kbd:`shift` and :kbd:`ctrl` keys to limit rotation to discrete amounts. You can also enter a :doc:`numerical value <3d_interaction/transform_control/numeric_input>` in degrees to specify the amount of rotation after after initiating a rotation transformation.


- Hold :kbd:`ctrl` down while performing a rotation to rotate the selected element in 5 degree increments.
- Hold :kbd:`shift` down while performing a rotation to rotate the selected element in 0.01 degree increments.
- Hold :kbd:`shift-ctrl` down while performing a rotation to rotate the selected element in 1 degree increments.
- Press :kbd:`r`\ , type in a number and press :kbd:`enter` to confirm.
- Press :kbd:`r`\ ,\ :kbd:`r` to enable Trackball rotation.


.. admonition:: Orientation dependant rotations
   :class: nicetip

   By default, all rotations happen around a Global Orientation. You can change the rotation orientation by pressing the axis key twice. For example, pressing :kbd:`r`\ , :kbd:`x`\ , :kbd:`x` will by default set rotation to occur around the local orientation.


:doc:`Read more about Precision Control » <3d_interaction/transform_control/precision>`
:doc:`Read more about Numerical Transformations » <3d_interaction/transform_control/numeric_input>`
:doc:`Read more about Transform Orientations » <3d_interaction/transform_control/transform_orientations>`


Rotation with the 3D Transform Manipulator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. figure:: /images/Icon-library_3D-Window_3D-transform-rotate-manipulator.jpg
   :width: 100px
   :figwidth: 100px

   Rotation Transform Manipulator


In the 3D View header, ensure that the Transform Manipulator is enabled (the red, green,
and blue triad is selected). Set the manipulator type to rotation
(the highlighted arc icon shown below).


.. figure:: /images/3D_interaction-Transformations-Basic-Rotate-rotate_manipulator_header.jpg


- Select your element with :kbd:`RMB`\ .
- Use :kbd:`LMB` and drag any of the three colored axes on the rotation manipulator to rotate your object along that axis. You can also use :kbd:`shift`\ , :kbd:`ctrl` or numeric input with the 3D manipulator widget for further control.
- Your changes will be applied when you release :kbd:`LMB` or press :kbd:`SPACE` or :kbd:`ENTER`\ . Your changes will be cancelled if you press :kbd:`RMB` or :kbd:`ESC`\ .

:doc:`Read more about the 3D Transform Manipulator » <3d_interaction/transform_control/manipulators>`


Rotation with the Properties Panel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. figure:: /images/3D_interaction-Transformations-Basic-Rotate-rotate_properties_panel.jpg
   :width: 180px
   :figwidth: 180px

   Rotation transform properties panel.


Rotation values can also be specified in the Properties panel (\ :kbd:`n`\ )
by altering the degree value in the rotation slider of the Transform panel.
Rotation along particular axes can be enabled or disabled by toggling the padlock icon.
The rotation mode (Euler, Axis Angle, Quaternion)
can also be set in this panel from the drop down box.

:doc:`Read more about Panels » <interface/panels>`

:doc:`Read more about rotation modes » <3d_interaction/transform_control/transform_orientations>`

`Additional detail about rotation modes » <http://wiki.blender.org/index.php/User:Pepribal/Ref/Appendices/Rotation>`__

