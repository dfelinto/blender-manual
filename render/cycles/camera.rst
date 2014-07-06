
Camera
******

Perspective
===========

:guilabel:`Lens Size and Angle`
   Control the field of view angle.


.. figure:: /images/Manual_cycles_camera_persp.jpg
   :width: 300px
   :figwidth: 300px


Orthographic
============

:guilabel:`Scale`
   Controls the size of objects projected on the image.


.. figure:: /images/Manual_cycles_camera_ortho.jpg
   :width: 300px
   :figwidth: 300px


Panoramic
=========

Cycles supports Equirectangular and Fisheye panoramic cameras.
Note that these can't be displayed with OpenGL rendering in the viewport;
they will only work for rendering.


Equirectangular
^^^^^^^^^^^^^^^

Render a panoramic view of the scenes from the camera location and use an equirectangular

projection, always rendering the full 360- over the X-axis and 180- over the Y-axis.

This projection is compatible with the environment texture as used for world shaders,
so it can be used to render an environment map. To match the default mapping,
set the camera object rotation to (90, 0, -90) or pointing along the positive X-axis. This
corresponds to looking at the center of the image using the default environment texture
mapping.


Fisheye
^^^^^^^

Fisheye lenses are typically wide angle lenses with strong distortion,
useful for creating panoramic images for e.g. dome projection, or as an artistic effect.
The :guilabel:`Fisheye Equisolid` lens will best match real cameras.
It provides a lens focal length and field of view angle,
and will also take the sensor dimensions into account.

The :guilabel:`Fisheye Equidistant` lens does not correspond to any real lens model; it will
give a circular fisheye that doesn't take any sensor information into account but rather uses
the whole sensor. This is a good lens for full dome projection.

:guilabel:`Lens`
   Lens focal length in millimeter.
:guilabel:`Field of View`
   Field of view angle, going to 360 and more to capture the whole environment.


Depth of Field
==============

:guilabel:`Aperture Type`
   Method with which to specify the size of the camera opening through which light enters. With Radius the radius of the opening can be specified, while F/Stop specifies the size relative to the camera focal length, a measure more common in photography. Their relation is: *aperture radius = focal length / (2 f-stop)*
:guilabel:`Aperture Size`
   Also called lens radius. If this is zero, all objects will appear in focus, while larger values will make objects farther than the focal distance appear out of focus.
:guilabel:`Aperture F/Stop`
   Also called F-number or relative aperture. Lower numbers give more depth of field; higher numbers give a sharper image.

:guilabel:`Aperture Blades`
   If this setting is 3 or more, a polygonal-shaped aperture will be used instead of a circle, which will affect the shape of out of focus highlights in the rendered image.
:guilabel:`Aperture Rotation`
   Rotation of the :guilabel:`Aperture Blades`.

:guilabel:`Focal Distance`
   Distance at which objects are in perfect focus. Alternatively, an object can be specified whose distance from the camera will be used.


Clipping
========

:guilabel:`Clip Start and End`
   The interval in which objects are directly visible. Any objects outside this range still influence the image indirectly, as further light bounces are not clipped. For OpenGL rendering, setting clipping distances to limited values is important to ensure sufficient rasterization precision. Ray tracing does not suffer from this issue much, and as such more extreme values can safely be set.