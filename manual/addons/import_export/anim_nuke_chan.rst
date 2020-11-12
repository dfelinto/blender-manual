
*********************
Nuke Animation (chan)
*********************

.. admonition:: Reference
   :class: refbox

   :Category:  Import-Export
   :Menu:      :menuselection:`File --> Import/Export --> Nuke (.chan)`

The chan format is used to store camera animations, including location, rotation and optionally field of view.
This add-on can import and export chan files using the active object's animation.

A chan file is an ASCII file with parameter values saved in columns, one column per parameter, one line per frame.
The properties saved and read by this script are:

.. code-block:: none

   frame location.x location.y location.z rotation_euler.x rotation_euler.y rotation_euler.z angle_y

The file format itself is as simple as can be, but its simplicity is its greatest advantage.
It is being used by applications like Nuke and Houdini, and since it is so simple
to write an import or export script for it is both fast and easy.

``angle_y`` stands for vertical field of view. It is used for calculation of the camera lens,
and only applies to camera animations, while importing/exporting object animation this parameter is skipped.


Usage
=====

The add-on gets the currently active object (works in Object Mode only) and
saves/loads its transformations from or to a simple ASCII file, through the whole animation range
(set either in the Timeline or in the render settings). All you need to do is to select an object
and run the add-on in :menuselection:`File --> Import/Export --> Nuke(*.chan)`.

Note that Chan saves only the raw property values (``rotation_x``, ``rotation_y``, ``rotation_z``, etc.),
so you have to mind the rotation order. In other words --
the rotation orders during export and import must be the same
(both are being set in the File Browser while importing/exporting).

Another thing is the camera sensor size and its influence on camera lens.
You can set the sensor size so you can fit a real life cameras (default in Blender is 32 × 18),
the best practice in this case is using horizontal fit for the camera (Nuke is using this as a default).
While importing the camera from a chan file you have to remember to set the same sensor size as
you had in Nuke (or other software that this camera has been exported).

.. tip:: File names

   It is a good practice to save the chan files with it's rotations order and sensor size stored in a file name
   (i.e. ``camera_for_shot_ZXY_36x24.chan``) so you don't have to look for those values in old files.

.. tip:: Exporting Geometry to Other Software

   If you want to export the objects movement to other software via the OBJ format,
   you have to save it with the Z up, Y forward setting.
   After loading it to the other software it will be rotated 90 degrees,
   but when you apply the chan file it'll jump into its place.
