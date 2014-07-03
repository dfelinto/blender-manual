


Precision
=========


 .. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object` and :guilabel:`Edit` modes
   | Hotkey:   :kbd:`ctrl` and/or :kbd:`shift`


Description
-----------

Holding :kbd:`ctrl` or :kbd:`shift` during a transformation operation
(such as grab/move, rotate or scale)
will allow you to perform the transformation in either fixed amounts,
very small amounts or both. The magnitude of the transformation can be viewed in the 3D window
header in the bottom left hand corner. Releasing :kbd:`ctrl` or :kbd:`shift`
during the transformation will cause the movement to revert back to its normal mode of
operation.

:doc:`Read more about Window Headers » <interface/window_system/headers>`


Usage
-----


With hotkeys
~~~~~~~~~~~~


Press :kbd:`g`\ , :kbd:`r` or :kbd:`s` and then hold either :kbd:`ctrl`\ ,
:kbd:`shift` or :kbd:`ctrl-shift`\ .


With the Transform Manipulator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Hold :kbd:`ctrl`\ ,
:kbd:`shift` or :kbd:`ctrl-shift` and click on the appropriate manipulator handle.
Then move the mouse in the desired direction. The reverse action will also work i.e.
clicking the manipulator handle and then holding the shortcut key for precision control.

:doc:`Read more about the Transform Manipulator » <3d_interaction/transform_control/manipulators>`


 .. admonition:: Combining with other controls
   :class: nicetip

   All of the precision controls detailed on the page can be combined with the :doc:`Axis Locking <3d_interaction/transform_control/axis_locking>` controls and used with the different :doc:`Pivot Points <3d_interaction/transform_control/pivot_point>`\ .


Holding CTRL
------------


Grab/move transformations
~~~~~~~~~~~~~~~~~~~~~~~~~


.. figure:: /images/3D_interaction-Transform_Control_Precision_blender-units.jpg

   1 Blender Unit - shown at the default zoom level.


For grab/move operations at the default zoom level,
holding :kbd:`ctrl` will cause your selection to move by increments of 1 Blender Unit
(1 BU) (i.e. between the two light grey lines). Zooming in enough to see the next set of grey
lines will now cause :kbd:`ctrl` movements to occur by 1/10 of a BU. Zooming in further
until the next set of grey lines becomes visible will cause movement to happen by 1/100 of a
BU and so on until the zoom limit is reached.
Zooming out will have the opposite effect and cause movement to happen by increments of 10,
100 etc BU.

:doc:`Read more about Zooming » <3d_interaction/navigating/3d_view#zooming_the_view>`


Rotation transformations
~~~~~~~~~~~~~~~~~~~~~~~~


Holding :kbd:`ctrl` will cause rotations of 5 degrees.


Scale transformations
~~~~~~~~~~~~~~~~~~~~~


Holding :kbd:`ctrl` will cause size changes in increments of 0.1 BU.


 .. admonition:: Snapping modes
   :class: note

   Note that if you have a :doc:`Snap Element <3d_interaction/transform_control/snap#snap_element>` option enabled, holding :kbd:`ctrl` will cause the selection to snap to the nearest element.
   :doc:`Read more about Snapping » <3d_interaction/transform_control/snap>`


Holding SHIFT
-------------


Holding :kbd:`shift` during transformations allows for very fine control that does not
rely on fixed increments. Rather, large movements of the mouse across the screen only result
in small transformations of the selection.


Holding CTRL and SHIFT
----------------------


Grab/move transformations
~~~~~~~~~~~~~~~~~~~~~~~~~

For grab/move operations at the default zoom level, holding :kbd:`ctrl-shift` will cause
your selection to move by increments of 1/10 Blender Units. Holding :kbd:`ctrl-shift` at
any zoom level will cause the transformation increments to always be 1/10 of the increment if
you were only holding :kbd:`ctrl`\ .


Rotation transformations
~~~~~~~~~~~~~~~~~~~~~~~~


Holding :kbd:`ctrl-shift` will cause rotations of 1 degree.


Scale transformations
~~~~~~~~~~~~~~~~~~~~~


Holding :kbd:`ctrl-shift` will cause size changes in 0.01 BU increments.

