
..    TODO/Review: {{review|copy=X}} .


Depth Of Field (DOF) Explained
==============================

Real world camera lenses and your eyeball transmit light through a lens (cornea)
that bends the light, and an iris that limits the amount of light,
to focus the image onto the film, CCD/Cmos sensor, or retina.
Because of the interaction of the lens and iris,
objects that are a certain distance away are in focus;
objects in the foreground and background are out of focus. We call this distance their depth,
or "Z" distance from the camera or eye.

Light comes to the lens (in the real world) at an angle; from some direction.
What you see depends on your perspective; if you move closer,
different angles of the scene are revealed. To make "flat" pictures,
like an architectural drawing or plot, Blender can also make an orthographic rendering. So,
there are two kinds of renderings, Perspective and Orthographic.
Perspective simulates light coming in at an angle to the lens from the field of view,
and Orthographic (disabled by default)
simulates light coming straight in to an infinitely large backplane or flat retina.


.. figure:: /images/Manual-Camera-DOF.jpg


Depending on the diameter of the iris, there is a range (of distance)
where objects are in focus. In cameras, the diameter of the iris is controlled by an "f-stop".
Said another way, there is *field* of view that you see left to right, up and down;
your "picture", if you will. At a certain range, or *depth* away from your eye,
things are in focus. For example, at night,
you may be able to focus your eye on objects that are 10 to 15 feet (3 to 5 meters) away.
Anything closer than 10 or farther away than 15 is blurry.
Your **depth of field** is thus 5 feet (2 m).

The larger the iris, the smaller the depth of field. This is why, during the day,
you can focus on a range of things stretching out far from you. In film,
there is a person whose job is to measure the distance from the camera to the actor's nose,
to ensure that the focus is set perfectly.

The more that an object is out of its depth
(the perfect value for this depth is called *focal plane*\ ), the blurrier it is. In fact, the
depth of field is the range on both sides of the focal plane in which the blurriness of the
objects is considered to be low enough to be imperceptible. In Blender, this distance is
called the :guilabel:`Dof Dist` or "Depth of Field Distance" and is set in the
:guilabel:`Editing` context (\ :kbd:`f9`\ ) for the camera. Alternatively,
you can have the camera automatically stay focused on an object,
by entering the name of the object in the :guilabel:`Dof Ob` field.


Field of View and Lens Size
---------------------------

The field of view varies by the size of the lens. With cameras, a 35mm lens is kind of a
standard size because the picture it takes mimics the size of the picture seen by the eye and
pictures can be taken rather close. In Blender,
use the :guilabel:`Camera` settings to change the size of the lens (35mm is the default).
A longer lens taking a picture farther away has the same field of view, but has a different
perspective of the view that many directors love because it "condenses" the scene and smooths
a sweep, since it is farther away from the action:


+----------------------------------------------------+-----------------------------------------------------------+------------------------------------------------------------------------------+
+.. figure:: /images/Manual-Compositing-DOF-35x10.jpg|.. figure:: /images/Manual-Compositing-DOF-210x60.jpg      |.. figure:: /images/Manual-Dof_210mm_50.jpg                                   +
+   :width: 200px                                    |   :width: 200px                                           |   :width: 200px                                                              +
+   :figwidth: 200px                                 |   :figwidth: 200px                                        |   :figwidth: 200px                                                           +
+                                                    |                                                           |                                                                              +
+   35mm lens from 10 units away.                    |   210mm lens from 60 units away at same location/rotation.|   210mm at 50 units; repositioned to frame the view similar to the 35mm shot.+
+----------------------------------------------------+-----------------------------------------------------------+------------------------------------------------------------------------------+


Zooming in Blender
------------------

Zoom is the ability to expand a subset of the picture; we humans have no such ability. Well,
I take that back; we do:
we just get up off the couch and walk up closer to what we want to see (however,
this is more like "traveling" than "zooming"). Blender allows you both actions:
you can move the camera closer to or farther away from an object for a track (or "truck")
in/out, and/or change its lens size. You can automate these by assigning an Interpolated (Ipo)
curve to the object or to the camera, respectively.


Depth of Field in Computer Graphics
-----------------------------------

In computer graphics (CG), there is no physical lens or iris, so the depth-of-field (DOF)
is infinite and all objects are always in focus. However, for artistic reasons,
we want our main characters to be in focus, and everything else a little blurry,
so that our audience does not focus on distracting things in the background. Also,
it is easier to discern the main actors when they are in focus, and everything else isn't. So,
we have to create an effect, or **Depth of Field Effect**\ ,
to composite our images and post-process them to achieve realistic-looking results.


