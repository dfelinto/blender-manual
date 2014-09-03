
Dome Camera
***********

This feature allows artists to visualize their interactive projects within an immersive dome
environment. In order to make it an extensible tool, we are supporting Fulldome,
Truncated domes (front and rear), Planetariums and domes with spherical mirrors.


The Dome camera uses a multipass texture algorithm as developed by Paul Bourke and was
implemented by Dalai Felinto with sponsorship  from **SAT -** Society for Arts and
Technology within the **SAT** **Metalab**
`immersion research program <http://paulbourke.net/miscellaneous/domemirror/BlenderiDome/>`_,
that involves rendering the scene 4 times and placing the subsequent images
onto a mesh designed especially such that the result, when viewed with an
orthographic camera, is a fisheye projection.


.. note::

   Remember to use Blender in **fullscreen mode** to get the maximum out of your projector.

   To accomplish that launch Blender with the command-line argument -W.
   Also to get away of the top menu on Blender try to join all windows (buttons, 3dview, text,
   ...) in a single one. Otherwise if you only maximize it (Ctrl+Up)
   you can't get the whole screen free to run your game
   (the top bar menu takes about 20 pixels).


Dome Camera Settings
********************

.. figure:: /images/Manual-GameEngine-Dome-Panel.jpg

Dome Type
   This menu allows you to select which type of dome camera to use.
   They are outlined below, along with their respective settings.


- `Fisheye Mode`_
- `Front-Truncated Dome Mode`_
- `Rear-Truncated Dome Mode`_
- `Cube Map Mode`_
- `Spherical Panoramic Mode`_

Available camera settings change depending on the selected Dome Type:

Resolution
   Sets the resolution of the Buffer. Decreasing this value increases speed, but decreases quality.

Tesselation
   4 is the default. This is the tesselation level of the mesh. (Not available in Cube Map mode).

Angle
   Sets the field of view of the dome in degrees, from 90 to 250. (Available in Fisheye and Truncated modes).

Tilt
   Set the camera rotation in the horizontal axis. Available in Fisheye and Truncated modes).

`Warp Data Mesh`_
   Use a custom warp mesh data file.


Fisheye Mode
============

An Orthogonal Fisheye view from 90º to 250º degrees.

- From 90º to 180º we are using 4 renders.
- From 181º to 250º we are using 5 renders.


.. figure:: /images/Dev-GameEngine-Dome-Fisheye.jpg

   Fisheye Mode


Front-Truncated Dome Mode
=========================

Designed for truncated domes,
this mode aligns the fisheye image with the top of the window while touching the sides.

- The Field of view goes from 90º to 250º degrees.
- From 90º to 180º we are using 4 renders.
- From 181º to 250º we are using 5 renders.


.. figure:: /images/Dev-GameEngine-Dome-Front-Truncated.jpg

   Front Truncated Dome Mode


Rear-Truncated Dome Mode
========================

Designed for truncated domes,
this mode aligns the fisheye image with the bottom of the window while touching the sides.

- The Field of view goes from 90º to 250º degrees.
- From 90º to 180º we are using 4 renders.
- From 181º to 250º we are using 5 renders.


.. figure:: /images/Dev-GameEngine-Dome-Rear-Truncated.jpg

   Rear Truncated Dome Mode


Cube Map Mode
=============

Cube Map mode can be used for pre-generate animated images for CubeMaps.

- We are using 6 renders for that. The order of the images follows Blender internal EnvMap file format:
  - first line: right, back, left
  - second line: bottom, top, front


.. figure:: /images/Dev-GameEngine-Dome-EnvMap.jpg

   Environment Map Mode


Spherical Panoramic Mode
========================

A full spherical panoramic mode.

- We are using 6 cameras here.
- The bottom and top start to get precision with **Definition** set to 5 or more.


.. figure:: /images/Dev-GameEngine-Dome-Panoramic.jpg

   Full Spherical Panoramic Mode


Warp Data Mesh
==============

Many projection environments require images that are not simple perspective projections that
are the norm for flat screen displays. Examples include geometry correction for cylindrical
displays and some new methods of projecting into planetarium domes or upright domes intended
for VR.

For more information on the mesh format see `Paul Bourke's article <http://paulbourke.net/dataformats/meshwarp/>`_.


.. figure:: /images/Dev-GameEngine-Dome-Warped.jpg

In order to produce that images, we are using a specific file format.

File template:
::

   mode
   width height
   n0_x n0_y n0_u n0_v n0_i
   n1_x n1_y n1_u n1_v n1_i
   n2_x n1_y n2_u n2_v n2_i
   n3_x n3_y n3_u n3_v n3_i
   (...)


First line is the image type the mesh is support to be applied to:
**2** = **rectangular**, **1** = **radial** Next line has the mesh dimensions in
pixelsRest of the lines are the nodes of the mesh.

Each line is compund of **x** **y** **u** **v** **i** (x,y)
are the normalised screen coordinates(u,v)
texture coordinatesi a multiplicative intensity factor

x varies from -screen aspect to screen aspecty varies from -1 to 1u and v vary from 0 to 1i
ranges from 0 to 1, if negative don't draw that mesh node


- You need to create the file and add it to the Text Editor in order to select it as your Warp Mesh data file.
- Open the Text Editor (Window Types/Text Editor).
- Open your mesh data file(ie. myDome.data) in the text editor (Text/Open or Alt O on keyboard).
- Go to Game Framing Settings (Window Types/Buttons Window/Scene Page or F10 on keyboard)
- Enable Dome Mode.
- Type filename in Warp Data field(ie. myDome.data).

To create your own Warp Meshes an interactive tool called meshmapper is available as part of
`Paul Bourke's Warpplayer <http://paulbourke.net/miscellaneous/domemirror/warpplayer/>`__
software package(requires full version).


Example files
-------------

`Spherical Mirror Dome 4x3 <http://wiki.blender.org/uploads/8/81/Dev-GameEngine-Dome-Standard_4x3.data>`__,
`Truncated Dome 4x3 <http://wiki.blender.org/uploads/9/9b/Dev-GameEngine-Dome-Truncated_4x3.data>`__,
`Sample Fullscreen File 4x3 <http://wiki.blender.org/uploads/d/d4/Dev-GameEngine-Dome-Sample-FullScreen_4x3.data>`__,
`Sample Fullbuffer File 4x3 <http://wiki.blender.org/uploads/3/3d/Dev-GameEngine-Dome-Sample-FullBuffer_4x3.data>`__.


.. note::

   Important: the viewport is calculated using the ratio of canvas width by canvas height.
   Therefore different screen sizes will require different warp mesh files. Also in order to get
   the correct ratio of your projector you need to use Blender in Fullscreen mode.

