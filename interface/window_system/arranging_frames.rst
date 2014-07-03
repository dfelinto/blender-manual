
Arranging frames
================


Blender uses a novel screen-splitting approach to arrange window frames.
The application window is always a rectangle on your desktop.
Blender divides it up into a number of re-sizable window frames.
A window frame contains the workspace for a particular type of window, like a 3D View window,
or an Outliner.
The idea is that you split up that big application window into any number of smaller
(but still rectangular) non-overlapping window frames. That way,
each window is always fully visible,
and it is very easy to work in one window and hop over to work in another.


Maximizing a window
-------------------


You can maximize a window frame to fill the whole application window with the :guilabel:`View`
→ :guilabel:`Toggle Full Screen` menu entry. To return to normal size,
use again :guilabel:`View` → :guilabel:`Toggle Full Screen`\ .
A quicker way to achieve this is to use :kbd:`shift-space`\ ,
:kbd:`ctrl-down` or :kbd:`ctrl-up` to toggle between maximized and framed windows.
NOTE: The window your mouse is currently hovering over is the one that will be maximized using
the keyboard shortcuts.


Splitting a window
------------------


.. figure:: /images/Manual-Interface-Window_System-Arranging_frames-splitwidget.jpg


In the upper right and lower left corners of a window are the window splitter widgets,
and they look like a little ridged thumb grip. It both splits and combines window panes.
When you hover over it, your cursor will change to a cross.
:kbd:`Lmb` and drag it to the left to split the pane vertically,
or downward to split it horizontally.


Joining two frames
------------------


In order to merge two window frames,
they must be the same dimension in the direction you wish to merge. For example,
if you want to combine two window frames that are side-by-side, they must be the same height.
If the one on the left is not the same as the one on the right,
you will not be able to combine them horizontally.
This is so that the combined window space results in a rectangle.
The same rule holds for joining two window frames that are stacked on top of one another;
they must both have the same width. If the one above is split vertically,
you must first merge those two, and then join the bottom one up to the upper one.


.. figure:: /images/Manual-Interface-Window_System-Arranging_frames-joinframes.jpg
   :width: 250px
   :figwidth: 250px


To merge the current window with the one above it
(in the picture the properties window is being merged "over" the Outliner),
hover the mouse pointer over the window splitter. When the pointer changes to a cross,
:kbd:`Lmb` click and drag up to begin the process of combining.
The upper window will get a little darker, overlaid with an arrow pointing up.
This indicates that the lower (current) frame will "take over" that darkened frame space.
Let go of the :kbd:`Lmb` to merge. If you want the reverse to occur,
move your mouse cursor back into the original (lower) frame,
and it will instead get the arrow overlay.


In the same way, windows may be merged left to right or vice versa.

If you press :kbd:`esc` before releasing the mouse, the operation will be aborted.


Changing window size
--------------------


You can resize window frames by dragging their borders with :kbd:`Lmb`\ . Simply move your
mouse cursor over the border between two frames until it changes to a double-headed arrow,
and then click and drag.


Swapping contents
-----------------


You can swap the contents between two frames with :kbd:`ctrl-Lmb` on one of the
splitters of the initial frame, dragging towards the target frame,
and releasing the mouse there. Those two frames don't need to be side by side,
though they must be inside the same window.


Opening new windows
-------------------


You may wish to have a new full window containing Blender frames. This can be useful,
for instance, if you have multiple monitors and want them to show different information on the
same instance of Blender.

All you need to do is :kbd:`shift-Lmb` on a frame splitter, and drag slightly.
A new window pops up, with its maximize, minimize, close and other buttons
(depending on your platform), containing a single frame with a duplicate of the initial window
on which you performed the operation.

Once you have that new window, you can move it to the other monitor
(or leave it in the current one); you can resize it (or keep it unchanged);
you can also arrange its contents in the same way discussed so far (split and resize frames,
and tune them as needed), and so on.

There is, though, another way to get an extra window: *File* → *User Preferences...*
(or :kbd:`ctrl-alt-u`\ ) pops a new window also,
with the *User Preferences* window in its only frame.
You can then proceed the same way with this window.

