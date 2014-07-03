

..    TODO/Review: {{review|partial=X|text=missing Ambient Color, Exposure and Range }} .


World Background
================


Description
-----------

The world buttons let you set up the shading of your scene in general.
It can provide ambient color, and special effects such as mist,
but a very common use of a :guilabel:`World` is to shade a background color.


.. admonition:: Background Image in Render
   :class: note

   To use an image as your render background, see :doc:`BackBuf images specified in the Output Panel <render>`


.. admonition:: Background Image in 3D
   :class: note

   To use an image as a background image in your 3D view, for example as a reference when doing a model, see :doc:`using a Background Image <3d_interaction/navigating/3d_view_options>`


Options
~~~~~~~


.. figure:: /images/25-Manual-World-WorldSkyColor.jpg
   :width: 297px
   :figwidth: 297px

   World panel


- **Horizon Color**
  The RGB color at the horizon
- **Zenith Color**
  The RGB color at the zenith (overhead)


How these colors are interpreted depends on which kind of :guilabel:`Sky` is chosen.

- **None Enabled**
  If none of these three buttons is checked, your background will just be plain flat color (using the horizon one).
- **Paper Sky**
  If this option is added, the gradient keeps its characteristics, but it is clipped in the image (it stays on a horizontal plane (parallel to x-y plane): what ever the angle of the camera may be, the horizon is always at the middle of the image).
- **Blend Sky**
  The background color is blended from horizon to zenith. If only this button is pressed, the gradient runs from the bottom to the top of the rendered image regardless of the camera orientation.
- **Real Sky**
  If this option is added, the gradient produced has two transitions, from nadir (same color as zenith) to horizon to zenith; the blending is also dependent on the camera orientation, which makes it more realistic. The horizon color is exactly at the horizon (on the x-y plane), and the zenith color is used for points vertically above and below the camera.


Textures
--------

Instead of a color, or blend of two colors, Blender can use an 2D image which it maps to a
very large Box or sphere which encompasses the entire scene,
or which it maps to a virtual space around the scene.


.. figure:: /images/25-Manual-World-TexCoord.jpg
   :width: 207px
   :figwidth: 207px

   Texture Coordinates popup menu


The World textures are accessible in the texture menu (just select :guilabel:`World` first,
then :guilabel:`Texture`\ .  They are used much like the Materials textures,
except for a couple of differences. The textures can be mapped according to:

- **View**
  The default orientation, aligned with the co-ordinates of the final render
- **Global**
  Uses global coordinates
- **AngMap**
  Used to wrap a standard hemisphere angular map around the scene in a dome. This can be used for image based lighting with :guilabel:`Ambient Occlusion` set to sky color. You'll generally need a high dynamic range image (HDRI) angular map. (It will look like a weird spherical image).
- **Sphere**
  Sphere mapping, similar to that of materials
- **Tube**
  Wrap the rectangular texture around in a cylinder, similar to that of materials
- **Object**
  Position the texture relative to a specified object's local texture space


.. figure:: /images/25-Manual-World-TexInfluence.jpg
   :width: 297px
   :figwidth: 297px

   Texture Influence panel


The texture affects color only, but in four different ways:

- **Blend**
  Makes the Horizon color appear where the texture is non-zero
- **Horizon**
  Affect the color of the horizon
- **Zenith Up**
  Affect the zenith color overhead
- **Zenith Down**
  Affect the zenith color underneath

If you are disappointed that your camera appears to carry the texture with it rather than
rotate through the texture,
you should check the Real Sky checkbox in the World tab of the Properties view.

