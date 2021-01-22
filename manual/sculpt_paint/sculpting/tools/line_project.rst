
************
Line Project
************

.. admonition:: Reference
   :class: refbox

   :Mode:      Sculpt Mode
   :Tool:      :menuselection:`Toolbar --> Line Project`

This tool flattens geometry along a plane determined by the camera view and a drawn line.
The region of the mesh being flattened is visualized by the side of the line that is shaded.


Tool Settings
=============

Limit to Segment
   Apply the gesture action only to the area that is contained within
   the segment without extending its effect to the entire line.


Usage
=====

#. Orient the 3D Viewport to define the local view plane to use for the Boolean.
#. :kbd:`LMB` and hold while moving the cursor to define the line to pick a region of the view plane to remove.
#. Release :kbd:`LMB` to confirm.


Controls
========

Flip :kbd:`F`
   Changes the side of the line that the tool removes geometry.
Snap :kbd:`Ctrl`
   Constrains the line to 15 degree intervals.
Move :kbd:`Ctrl-Spacebar`
   Changes the location of the line.


Example
=======

.. list-table::

   * - .. figure:: /images/sculpt_paint_sculpting_tool_line_project_before.png

          Before Line Poject

     - .. figure:: /images/sculpt_paint_sculpting_tool_line_project_after.png

          After Line Project.
