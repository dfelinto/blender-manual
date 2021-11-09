.. _bpy.types.SequencerToolSettings.pivot_point:

***********
Pivot Point
***********

The Pivot Point is primarily used in operations such as Rotate and Scale.
It defines the point around which the strip image will be rotated or scaled.
Using drop-down menu in the header of the Preview, you can change the location of the pivot point.

The *Pivot Point* is also extensively used in the 3D Viewport.

Bounding Box Center
   The bounding box is a rectangular box that is wrapped as tightly as possible around the selection.
Median Point
   The Median Point is the points that is closest to all the origins of the selected strips.
   You can think of it as the midpoint of the area that is covered with the selected strips.
2D Cursor
   Sometimes you want to rotate a strip around a specific point in the Preview.
   Therefore, you can set the 2D Cursor and change the Pivot Point accordingly.
Individual Origins
    If multiple strips are selected, you may want to rotate or scale these strip around
    there own origins instead of for example the Median Point of all selected strips.
    For example, if you have three portrait strip's of faces,
    you probably want each face to be rotated around its individual origin.
