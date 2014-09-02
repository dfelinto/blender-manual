
..    TODO/Review: {{review
   |text=This page contains information that lies beyond the scope of the Blender manual but its supposed topic still has its justification.
   |fixes=Link to wikipedia for general information on how to structure movies and pictures and rewriting of the page to fit it's topic.
   }} .

Scene Management Structure
**************************

Scene management and library appending/linking is based on Blender's :doc:`Library and Data System </data_system>`,
so it is a good idea to read that manual page first if you're not familiar with the basics of that system.


Blender can be used to create something as simple as a single scene or image,
or scaled up to an entire movie. A movie is usually comprised of three acts:

   - Introduction-Conflict.
   - Rising Tension.
   - Climax-Resolution.

Each act contains a few scenes, settings where the action happens.
Each scene is shot on a set, stage or location. Each is set with props and backdrops.
The scene is a set of action sequences where the actors act (hopefully convincingly).
Each sequence, or shot, usually lasts a few seconds.


.. note:: Sequence shot

   Sometimes, a single shot lasts several minutes: its a "sequence shot",
   which might even be a complete scene on its own.
   Technique hard to master if you don't want your audience to fall asleep!


A single Blender file is organized and set up to be able to contain an entire movie. Each .
blend file can contain multiple scenes. A scene is a bunch of objects, organized into layers.
As you progress through the creative process, you use a set of window
:doc:`screen layouts </data_system/scene_creation>`
specifically designed to help you work efficiently through the creative process:
model the objects and create the props, clothe the actors and dress the set (assign materials), define the action
(animation), render the video, and produce the movie. You can tailor these screen layouts, and create custom layouts,
to match your working preferences.


Planning Your Timeline
**********************

Shots within a scene are accomplished by moving a camera and/or actors through the scene for a
few seconds. Time in Blender is measured in frames by default
(even though you can change to seconds too if you wish),
and typical video has 25 or 30 frames per second (fps), and film is 24 fps.
For a five-second shot then, you allocate up to 150 frames for that shot (30 fps × 5 seconds).
Giving yourself some wiggle-room, shot 2 would start at frame 250 and go from there.
A one-minute movie set in a single scene for North America video broadcast (NTSC standard)
would have a timeline that goes up to 1800 final frames,
and may be laid out over the course of 2500 frames.
This timeline allows for cutting out 700 frames, picking the best 1800 frames
(30 fps × 60 seconds = 1800 frames) less transition time.


.. note:: Multiple Cameras

   You can have multiple cameras in a scene, used for different shots,
   and select which one is active when rendering the shot. Press :kbd:`ctrl-0`
   to switch to the camera you wish to use at a point in time.
