
*********
Line Mask
*********

.. reference::

   :Mode:      Sculpt Mode
   :Tool:      :menuselection:`Toolbar --> Line Mask`

This tool creates a :doc:`Mask </sculpt_paint/sculpting/editing/mask>`
based on plan determined by the camera view and a drawn line.
The masked region of the mesh is visualized by the shaded side of the line.


Tool Settings
=============

Front Faces Only
   Only creates a mask on the front side of faces.

Limit to Segment
   Apply the gesture action only to the area that is contained within
   the segment without extending its effect to the entire line.


Usage
=====

#. Orient the 3D Viewport to define the local view plane to use for the mask.
#. :kbd:`LMB` and hold while moving the cursor to define the line to pick a region of the view plane to mask.
#. Release :kbd:`LMB` to confirm.


Controls
========

Flip :kbd:`F`
   Changes the side of the line that the tool creates a mask.
Snap :kbd:`Ctrl`
   Constrains the line to 15 degree intervals.
Move :kbd:`Ctrl-Spacebar`
   Changes the location of the line.
