
******
Carver
******

Cut and Boolean objects directly in the 3D Viewport.


Activation
==========

- Open Blender and go to Preferences then the Add-ons tab.
- Click Object then Carver to enable the script.


Description
===========

If you have an active bevel on the object to be cut,
it will update automatically as well as objects that will be created.

To begin, select one or more objects, depending on the number of objects, the add-on will adjust to that.
One object, you can cut (basic operation) and use the default patterns.
Multiple objects, you can also cut, use patterns, and the last selected object serves as a "brush".
If you enter in the *Profile Brush* mode.
It works on all selected objects, so you can cut two objects or apply a "brush" to all objects at the same time.

The add-on is more accurate on orthographic view for basic Boolean operations.
For others operations you can use the view if you wish.

- :kbd:`Shift-Ctrl-X` to call the add-on.
- :kbd:`RMB` to exit.
- :kbd:`Ctrl-Z` to Undo (there are no limits, so be careful to doesn't overload).
- :kbd:`H` to have the help when the screen is large enough to display.


Basic Boolean Operations
------------------------

This mode is active when you run the add-on at start.

Rebool :kbd:`Shift`
   Holding :kbd:`Shift` allows to make a rebool.
Move All :kbd:`Alt`
   Allows you to move the cut.
Cursor Depth :kbd:`D`
   To use the position of the cursor as depth.
Move Cursor :kbd:`Ctrl-LMB`
   You can move the cursor with :kbd:`Ctrl-LMB`.

Tool Type :kbd:`Spacebar`
   To change the tool.

   Rectangle
      The *Rectangle* tool. Click, move and then click again to confirm the operation.
   Line
      The *Line* tool to polygonal cuts. It also allows you to bisect one or more objects.
      Click to the start point, move to the desired end point and then press :kbd:`Spacebar` to confirm the cutting.

      Holding :kbd:`Ctrl` allows to move incrementally.
   Circle
      The *Circle* tool, click then move to change the radius (vertical axis) or rotation (horizontal axis).

      Subdivision :kbd:`W`, :kbd:`X`
         Allows to change the circle subdivisions.

Create Geometry :kbd:`C`
   Switch to Create Mode. It reacts in the same way as above for shortcuts.
   Once validated, the add-on stops and selects the object created.


Profile Brush
-------------

When in profile mode, flat objects are present by default.
You can add your own with the ``ProfilCreate.py`` file that will be explain after (ToDo).

:kbd:`B` to enter this mode when you're in basic Boolean operations.
If you move your mouse over the object, you will see an overview of the pattern that
you can use and a preview at the bottom right.

Rebool :kbd:`Shift-Spacebar`
   For the rebool.
Duplicate :kbd:`Alt-Spacebar`
   To create the object.
Scale :kbd:`S`
   Todo.
Rotation :kbd:`LMB`
   :kbd:`LMB` and move the mouse to rotate.
Step Angle :kbd:`Ctrl`
   Hold :kbd:`Ctrl` to rotate with 45° degree steps.

Tool Type :kbd:`W`, :kbd:`X`
   To change the tool type.
Instantiate :kbd:`L`
   For instances when you duplicate the object (with holding :kbd:`Alt`).
Thickness :kbd:`D`
   To change the thickness of the pattern. Then move your mouse on the horizontal axis.
Axis Locking :kbd:`Ctrl`
   Hold :kbd:`Ctrl` to constraint axis.

Brush Type :kbd:`T`
   Difference
      To make a difference.
   Union
      To do a union Boolean (does not work with multiple objects).


.. admonition:: Reference
   :class: refbox

   :Category:  Object
   :Description: Multiple tools to carve or to create objects.
   :Location: 3D Viewport :kbd:`Shift-Ctrl-X`
   :File: object_carver folder
   :Author: Pixivore, Cedric LEPILLER, Ted Milker, Clarkx
   :License: GPL
   :Note: This add-on is bundled with Blender.
