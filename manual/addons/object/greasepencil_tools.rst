
*******************
Grease Pencil Tools
*******************

A set of tools for Grease Pencil drawing.


Activation
==========

- Open Blender and go to Preferences then the Add-ons tab.
- Click Object then Grease pencil tools to enable the script.


Tools
=====

Box Deform
----------

Create a deformation box around Grease Pencil strokes.
Press :kbd:`Ctrl-T` to launch the deformation mode.

The operational scope depends on the mode:

- Object Mode: the whole Grease Pencil object is deformed.
- Edit Mode: deform the selected points.
- Draw Mode: deform the last strokes only.

Shortcuts available during deformation:

- :kbd:`Spacebar`/ :kbd:`Return` to confirm.
- :kbd:`Delete`/ :kbd:`Backspace`/ :kbd:`Ctrl-T`/ :kbd:`Tab` (twice) to cancel.
- :kbd:`M` to toggle between Linear and Spline mode.
- :kbd:`1-9` to set the subdivision level of the box.
- :kbd:`Ctrl-Left`/ :kbd:`Ctrl-Right` to subdivide the box incrementally on the X axis and
  :kbd:`Ctrl-Up`/ :kbd:`Ctrl-Down` on the Y axis.


Rotate Canvas
-------------

Perform a rotation of the view in free navigation or active camera in camera view.

- Maintain :kbd:`Ctrl-Alt-MMB` to rotate view (customizable in add-on preferences).
- Click and release immediately to reset view (free navigation only).


Straighten Stroke
-----------------

Straighten the stroke between first and last point.
The influence can be tweaked in the redo panel.

The scopes for this tool are:

- Last stroke in Grease Pencil Paint Mode.
- Selected stroke in Grease Pencil Edit Mode.

.. tip:: Straight Influence Reset

   The influence percentage is stored for next use.
   Use :kbd:`Shift-LMB` on the button to reset influence to full.


Brush Pack Installer
--------------------

Install included Grease Pencil `textured brush pack
<https://cloud.blender.org/p/gallery/5f235cc297f8815e74ffb90b>`__ (made by Daniel Martinez Lara).
This is available in Draw Mode in the :ref:`Brushes panel <grease-pencil-draw-common-options>`.

.. note::

   This feature will be removed once the Blender official asset manager is released.

.. reference::

   :Category:  Object
   :Description: Set of tools for Grease Pencil drawing.
   :Location: :menuselection:`3D Viewport --> Sidebar --> Grease Pencil`
   :File: greasepencil_addon folder
   :Author: Samuel Bernou, Antonio Vazquez, Daniel Martinez Lara, Matias Mendiola
   :License: GPL
   :Note: This add-on is bundled with Blender.
