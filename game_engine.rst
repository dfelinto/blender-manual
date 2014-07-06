
Introduction to Game Engine
***************************

Blender has its own built in Game Engine that allows you to create interactive 3D applications
or simulations. The major difference between Game Engine and the conventional Blender  system
is  in the rendering process. In the normal Blender engine,
images and animations are built off-line - once rendered they cannot be modified.  Conversely,
the Blender Game Engine renders scenes continuously in real-time,
and incorporates facilities for  user interaction during the rendering process.


.. figure:: /images/BGE_Introduction_ScreenShot.jpg
   :width: 512px
   :figwidth: 512px

   Screenshot from "Yo Frankie", produced with Blender Game Engine


The Blender Game Engine oversees a game loop, which processes logic, sound,
physics and rendering simulations in sequential order. The engine is written in C++.

By default, the user has access to a powerful, high level, Event Driven
:doc:`Logic Editor <game_engine/logic/editor>`
which is comprised of a seriers of specialised components called "Logic Bricks".
The :doc:`Logic Editor <game_engine/logic/editor>` provides deep interaction with the simulation,
and its functionality can be extended through Python scripting.
It is designed to abstract the complex engine features into a simple user interface,
which does not require experience with Programming. An overview of the :doc:`Logic Editor <game_engine/logic/editor>`
can be found in the :doc:`Game Logic Screen Layout <game_engine/screen_layout>`


The Game Engine is closely integrated with the existing code base of Blender, which permits
quick transitions between the traditional modelling featureset and game-specific functionality
provided by the program. In this sense,
the Game Engine can be efficiently used in all areas of game design,
from prototyping to final release.

The Game Engine can simulate content within Blender,
however it also includes the ability to export a binary run-time to Windows, Linux and MacOS.
There is also basic support for mobile platforms with the Android Blender Player GSOC 2012
project.

There are a number of powerful libraries included in the 2.5 / 2.6 releases of Blender,
including:

- Recast - a state of the art navigation mesh construction toolset for games.
- Detour - a path-finding and spatial reasoning toolkit.
- Bullet - a physics engine featuring 3D collision detection, soft body dynamics, and rigid body dynamics
- Audaspace - a sound library for control of audio. Uses OpenAL or SDL

When creating a game or simulation in the BGE, there are four essential steps:

- Create visual elements that can be rendered. This could be 3D models or images.
- Enable interaction within the scene using logic bricks to script custom behaviour and determine how it is invoked (using the appropriate "sensors" such as keyboards or joysticks).
- Create one (or more) camera to give a frustrum from which to render the scene, and modify the parameters to support the environment in which the game will be displayed, such as Stereo rendering.
- Launch the game, using the internal player or exporting a runtime to the appropriate platform.

