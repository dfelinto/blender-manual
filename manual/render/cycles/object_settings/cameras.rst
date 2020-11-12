
*******
Cameras
*******

.. _cycles-panoramic-camera:

Panoramic Cameras
=================

Cycles supports three types of panoramic cameras; Equirectangular, Fisheye, and Mirror Ball.
Note that these cannot be displayed in non-rendered modes in the viewport,
i.e. *Solid* mode; they will only work for the final render.


Equirectangular
---------------

Render a panoramic view of the scenes from the camera location and use an equirectangular projection,
always rendering the full 360° over the X axis and 180° over the Y axis.

This projection is compatible with the environment texture as used for world shaders,
so it can be used to render an environment map. To match the default mapping,
set the camera object rotation to (90, 0, -90) or pointing along the positive X axis.
This corresponds to looking at the center of the image using the default environment texture mapping.

Minimum/Maximum Latitude/Longitude
   Limits of the vertical and horizontal field of view angles.


Fisheye
-------

Fisheye lenses are typically wide angle lenses with strong distortion,
useful for creating panoramic images for e.g. dome projection, or as an artistic effect.

The *Fisheye Equisolid* lens will best match real cameras.
It provides a lens focal length and field of view angle,
and will also take the sensor dimensions into account.

The *Fisheye Equidistant* lens does not correspond to any real lens model;
it will give a circular fisheye that does not take any sensor information into account
but rather uses the whole sensor. This is a good lens for full-dome projections.

Lens
   Lens focal length in millimeters.
Field of View
   Field of view angle, going to 360 and more to capture the whole environment.


Mirror Ball
^^^^^^^^^^^

Render is if taking a photo of a reflective mirror ball.
This can be useful in rare cases to compare with a similar photo taken to capture an environment.
