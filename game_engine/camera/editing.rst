


Camera Editing
==============


.. figure:: /images/BGE_Camera_Properties.jpg
   :width: 300px
   :figwidth: 300px

   Camera Properties


The camera (or cameras) used in a Blender game have a wide-ranging effect on the way in which
the game is rendered and displayed.
Mostly this is controlled using the Properties panel of the camera(s) used in the game.


 .. admonition:: Render Engine
   :class: nicetip

   Make sure that the render engine is set to Blender Game when attempting to set these controls - otherwise this description will not tally with what you see!


In the Camera Properties area, there are six panels available, as shown.
Each can be expanded or contracted using the usual triangle button.
The features in each panel will be described in detail below.


Embedded Player
---------------


.. figure:: /images/BGE_Camera_Properties_Game.jpg
   :width: 300px
   :figwidth: 300px

   Game Panel


**Start** button - Start the Game Engine. Shortcut :kbd:`P`\ .


Standalone Player
-----------------


.. figure:: /images/BGE_Camera_Properties_Standalone.jpg
   :width: 300px
   :figwidth: 300px

   Standalone Panel


This panel provides information for the Standalone Game Player which allows games to be run without Blender. See :doc:`Standalone Player <game_engine/standalone_player>` for further details.

**Fullscreen** -
   Off - opens standalone game as a new window.
   On - opens standalone game in full screen.

**Resolution**
   **X**
       Sets the X size of the viewport for full-screen display.
   **Y**
       Sets the Y size of the viewport for full-screen display.
**Quality**
   **Bit Depth**
       Number of bits used to represent color of each pixel in full-screen display.
    **FPS**
       Number of frames per second of full-screen display.

**Framing**
Shows how the display is to be fitted in to the viewport.
    **Letterbox**
       Show the entire viewport in the display window, and fill the remainder with the "bar" color.
   **Extend**
       Show the whole display in the viewport, and fill the remainder with bars.
   **Scale**
       Scale the display in X and Y to exactly fill the entire viewport.

**Bar Color**
    Select a color to use as the color of bars around the viewport (default black).
   To use this, select a color mode (RGB, HSV or Hex), then use the color slider and color wheel to choose a bar color.


Stereo
------


.. figure:: /images/BGE_Camera_Properties_Stereo.jpg
   :width: 300px
   :figwidth: 300px

   Stereo Panel


Select a stereo mode that  will be used to capture stereo images of the game (and also,
by implication, that stereo displays will use to render images in the standalone player).
**None**
   Render single images with no stereo.
**Stereo**
   Render dual images for stereo viewing using appropriate equipment. See :doc:`Stereo Camera <game_engine/camera/stereo>` for full details of available options.
**Dome**
   Provides facilities for an immersive dome environment in which to view the game. See :doc:`Dome Camera <game_engine/camera/dome>` for full details of available options.


Shading
-------


.. figure:: /images/BGE_Camera_Properties_Shading.jpg
   :width: 300px
   :figwidth: 300px

   Shading Panel


Specifies the shading mode to be used in rendering the game.The shading facilities available in Blender for use in :doc:`Materials <materials>` and :doc:`Textures <textures>` are essentially the same in the Blender Game Engine. However the constraints of real-time display mean that only some of the facilities are available.

**Single Texture**
   Use single texture facilities.
**Multitexture**
    Use Multitexture shading.
**GLSL**
   Use GLSL shading. GLSL should be used whenever possible for real-time image rendering.


Performance
-----------


.. figure:: /images/BGE_Camera_Properties_Performance.jpg
   :width: 300px
   :figwidth: 300px

   Performance Panel


**Use Frame Rate**
   Respect the frame rate rather than rendering as many frames as possible.
**Display Lists**
   Use display lists to speed up rendering by keeping geometry on the GPU.
**Restrict Animation Updates**
   Restrict number of animation updates to the animation FPS (this is better for performance but can cause issues with smooth playback).


Display
-------


.. figure:: /images/BGE_Camera_Properties_Display.jpg
   :width: 300px
   :figwidth: 300px

   Display Panel


Gives various display options when running the Game Engine. under the .
**Debug Properties**
   Show properties marked for debugging while game runs. Note that debug properties to be shown must be requested at source (eg. i-button in state tables). Only available when game is run within Blender - not in standalone player version.
**Framerate and Profile**
   Show framerate and profiling information while game runs. Only available when game is run within Blender - not in standalone player version.
**Physics Visualization**
   Show physics bounds and interactions while game runs (available in both Blender and standalone versions).
**Deprecation Warnings**
   Print warnings when using deprecated features in the python API. Only available when game is run within Blender - not in standalone player version.
**Mouse Cursor**
   Show mouse cursor while game runs (available in both Blender and standalone versions).


