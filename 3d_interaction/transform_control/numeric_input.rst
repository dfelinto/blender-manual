


Numeric input
=============


.. figure:: /images/3D_interaction-Transform_Control-Numeric_Input_numeric-input-header.jpg
   :width: 300px
   :figwidth: 300px

   Numeric input in the 3D window header


Using the mouse for transformations is convenient, but if you require more precise control,
you can also enter numeric values. After pressing :kbd:`G`\ ,
:kbd:`R` or :kbd:`S`\ ,
type a number to indicate the magnitude of the transformation.

You can see the numbers you enter in the bottom left hand corner of the 3D window header.
Negative numbers and decimals can be entered by pressing the minus (\ :kbd:`-`\ ) and period
(\ :kbd:`.`\ ) keys respectively.


Translation
-----------


To move Objects, vertices, faces or edges select the element,
press :kbd:`G` and then type a number. By default and with no other key presses,
movement will occur along the X-axis. To confirm the movement,
press :kbd:`Enter` or :kbd:`LMB`\ . To cancel the movement,
press :kbd:`Esc` or :kbd:`RMB`\ . If you mistype the value,
press :kbd:`Backspace` to cancel the current entry and retype a new value.

To enter numeric values for multiple axes,
use the :kbd:`TAB` key after entering a value for the axis. e.g. To move an Object, one
(1) Blender unit on all three axes press: :kbd:`G`\ , :kbd:`1`\ , :kbd:`TAB`\ ,
:kbd:`1`\ , :kbd:`TAB`\ , :kbd:`1`\ .
This will move the element one unit along the X-axis,
followed by the Y-axis and then the Z-axis.

You can also combine numeric input with axis locking to limit movement to a particular axis.
To do so, press :kbd:`G` followed by :kbd:`X`\ ,
:kbd:`Y` or :kbd:`Z` to indicate the axis. Then type in the transform amount using
:kbd:`0`\ -\ :kbd:`9` followed by :kbd:`Enter` to confirm.
Pressing :kbd:`X`\ , :kbd:`Y` or :kbd:`Z` will initially constrain movement to
the :guilabel:`Global` axis. Pressing :kbd:`X`\ , :kbd:`Y` or :kbd:`Z` again
will constrain movement to the orientation set in the :guilabel:`Transform Orientation`
setting of the 3D window header.

:doc:`Read more about Transform Orientations » <3d_interaction/transform_control/transform_orientations>`

:doc:`Read more about Axis Locking » <3d_interaction/transform_control/axis_locking>`


Rotation
--------


To specify a value for clockwise rotation, press :kbd:`R`\ ,
:kbd:`0`\ -\ :kbd:`9`\ , then :kbd:`Enter` to confirm.
To specify counter-clockwise rotation press :kbd:`R`\ , :kbd:`-`\ ,
:kbd:`0`\ -\ :kbd:`9`\ , then :kbd:`Enter` to confirm. Note that 270 degrees of
clockwise rotation is equivalent to -90 degrees of counter-clockwise rotation.


Scaling
-------


Objects, faces and edges can be scaled by pressing :kbd:`S`\ ,
:kbd:`0`\ -\ :kbd:`9`\ , then :kbd:`Enter` to confirm.,
Scaling transformations can also be constrained to an axis by pressing :kbd:`X`\ ,
:kbd:`Y` or :kbd:`Z` after pressing :kbd:`S`\ . Essentially,
scaling with numeric values works in almost identical fashion to translation.
The primary difference is that by default, scaling applies equally to all three axes. e.g.
pressing :kbd:`S`\ , :kbd:`0`\ :kbd:`.`\ :kbd:`5`\ ,
:kbd:`Enter` will scale an Object by 0.5 on all three axes.


Numeric input via the Properties shelf
--------------------------------------


.. figure:: /images/3D_interaction-Transform_Control-Numeric_Input_properties-panel.jpg
   :width: 300px
   :figwidth: 300px

   Transformations can also be entered through the Transform panel on the Properties shelf.


It is also possible to enter numeric values for each transformation using the
:guilabel:`Transform` panel found on the Properties shelf (\ :kbd:`N`\ ). The
:guilabel:`Transform` panel can also be used to prevent transformations along particular axes
by clicking the lock icon.

