
Camera
======

The Game Engine camera is in many ways similar to the Camera in the normal Blender Render
system, and is created, parameterized and manipulated in similar ways.
However because of its use as a real-time device, the Game Engine camera has a number of
additional features - it may be used as not only as a static camera,
but also as a moving device with its default characteristics (ie.
with its own programmed moves), or it may track another object in the game.  Furthermore,
any game object may be used as a camera; the view is taken from the object's origin point.
Lastly, it may be given special capabilities such as Stereo vision, Dome visualisation etc.
which have special relevance to game technology.

When you start the Game Engine, the initial camera view is taken from the latest 3D View.
This may be either a selected camera object  or the default camera (see below).
Thus to start the game with a particular camera,
you must select the camera and press :kbd:`pad0` before starting the Game Engine.


 .. admonition:: To avoid camera distortion
   :class: nicetip

   Always zoom the view in until the camera object fills the entire viewport.


Default Camera
--------------

The default camera view is taken from the latest 3D viewport view,
at a distance equivalent to the viewer. This means that if the normal 3D view is active the
scene does not change when the Game Engine is started.


Camera Object
-------------

The Camera object in the Game Engine follows much the same structure as the conventional Blender camera  - see :doc:`Camera <render/camera>` for details of how to set up, manipulate and select a camera. The following sections show some of the special facilities available in BGE cameras.


Parent Camera to Object
-----------------------

The camera will follow the object. First select the camera and then select the object.
Next :kbd:`ctrl-P` → :guilabel:`Make Parent`\ .

Note that if your object has any rotations then the camera will also have those rotations.
To avoid this use "Parent to Vertex" (see below).


Parent to Vertex
----------------

The easiest way to accomplish this is to select your object and :kbd:`Tab` to
:guilabel:`Edit mode`\ .
Now select the vertex and :kbd:`Tab` back to :guilabel:`Object` mode.

Next, without any objects selected, select the camera and, holding the :kbd:`Shift` key,
select the object. :kbd:`Tab` into :guilabel:`Edit mode`\ ,
and :kbd:`ctrl-P` and choose :guilabel:`Make vertex parent`\ .

Now the camera will follow the object and it will maintain its rotation,
while the object rotates.


Object as a Camera
------------------

Any object may also become a camera with whatever properties are set for the object.

To make an object the camera,
in :guilabel:`Object` mode select the object and press :kbd:`ctrl-pad0` on the numpad.

To reverse it, just select the camera and :kbd:`ctrl-pad0` again.


Camera Lens Shift
-----------------


In the Blender interface,
there is an option to shift the camera view on the x/y plane of the view. It is comparable to
lens shift in video projectors that usually shift the image up along the Y axis.
So for example,
when you put the beamer on a table it does not project half of the image on the table.

Unfortunately, this parameter is not taken in account by the Game Engine.

To manipulate the projection we can then directly modify the camera projection matrix in
Python.

::

   import bge
   scene = bge.logic.getCurrentScene()
   cam = scene.active_camera
   # get projection matrix
   camatrix = cam.projection_matrix
   #modifying the camera projection matrix by modifying the x and y terms of the 3rd row to obtain a shift of the rendered area
   camatrix[2][0] = 2*shiftx
   camatrix[2][1] = 2*shitfy
   cam.projection_matrix = camatrix


Here in field of view units are shiftx and shifty. So for example,
for shifting the view up half a screen shifty is set to 0.5.

Note that a camera's projection_matrix attribute may not be set until after initialization
scripts are executed and running this code immediately after the game starts will mess up the
projection matrix.


