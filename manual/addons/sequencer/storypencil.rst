
***********
Storypencil
***********

Storypencil is an add-on that adds tools to help the storyboarding workflow using the video sequencer.
It adds many features to help adding, editing and rendering linked scenes.


Activation
==========

- Open Blender and go to Edit Menu, Preferences, then Add-ons.
- Search for Storypencil, and activate the add-on.

Description
===========

After activating the add-on, it will place buttons on the video sequencer header to control the linked Scenes Strips:
Edit, New and Render.

In the video Sequencer sidebar you will find a Storypencil tab with all the Settings for the add-on.

Usage
=====

With the 2D Animation Template in Draw Mode, you can use the menu located in the
:menuselection:`3D Viewport --> Draw --> Setup Storyboard Session`
and the add-on will take care to set up all the general settings and create the work-spaces and Scenes needed for the
storyboard session.

Use the main buttons on the video sequencer header to add, edit and render Scene Strips.

New
---

Add a new Scene Strip to the active channel based on the Base Scene selected in the add-on settings.
The name of the new Scene Strip will use the prefix and suffix stablished on the settings.

Edit
----

Opens the linked source scene under the timeline cursor in the video sequencer.
There are two modes for editing source scenes, you can control the behavior by toggling the checkbox
"Open in new window" next to the button.


New Window mode
^^^^^^^^^^^^^^^

Storypencil will open the source scene in a new window keeping their timelines synchronized.
When you finish editing the source scene you can close the opened window or keep it opened and control the timeline in
the video sequencer to change to another scene.

This method is best suited when using multiple monitors.


Switching mode
^^^^^^^^^^^^^^

Storypencil will open the source scene switching to the proper Workspace at the same video sequencer cursor position.
When you finish editing the source scene you can return to the video Sequencer using the Back button on the Dope Sheet
header in the source scene Workspace.

This method is best suited when using only one monitor.

.. important::

   There is still a known issue when the Add-on is used together with a scene pinned to a workspace.
   Synchronization between scenes may fail.


Render
------

Render all or only selected scene strips, depending on the Add-on Render Strips settings.


Settings
========

New Scenes
----------

Name Prefix
   Prefix that will be added to the name of new Scene Strips.

Name Suffix
   Suffix that will be added to the name of new Scene Strips.

Frames
   Duration in frames for the new Scene Strips.

Base Scene
   The Scene used as base for Scene Strips.
   In this Base Scene you can setup cameras, Grease Pencil objects,
   background objects, etc. to avoid start from scratch every time.

Render Strips
-------------

If the render format is Movie the add-on will render one Movie clip per Scene strip using the video sequencer render
settings. All rendered Movies will be imported (if Import Rendered Strips setting is enabled) as Movie clips on the
selected channel.

If the render format is Image the add-on will render one image on each keyframe found in the source scene of the
Scene strip using the video sequencer render settings. All rendered Images will be imported (if Import Rendered
Strips setting is enabled) as Image Strips on the selected channel, the length used for the imported Image Clip will
correspond to the gap between keyframes.

Output Path
   Directory name where rendered video or images will be saved.

Render Only Selected Strips
   When enabled, only the selected Scene Strips will be rendered.

File Format
   Select the File Format to render the Scene Strips.

Container
   Output file container to use.

Audio Codec
   FFmpeg audio codec to use.

Import Rendered Strips
   When enabled, The Movie clips or images generated will be imported after rendered.

Channel
   The Channel to use for Movie clips or images imported after rendered.

Image Steps
   If greater than 0, when rendering images sets the number of images to generate between keyframes.

Image Numbering
   Sets the Numbering format for the generated images to use.

Folder by Strip
   When enabled, saves the images to the Output Path inside different folders with the Scene Strip name.

General
-------

VSE Workspace
   Workspace to use for video editing.

VSE Scene
   Scene to use as the main video editing scene.

Drawing Workspace
   Workspace to use for edit the source scenes.


.. reference::

   :Category: Sequencer
   :Description: Storyboard tools.
   :Location: Video Sequencer
   :File: Storypencil folder
   :Author: Antonio Vazquez, Matias Mendiola, Daniel Martinez Lara, Rodrigo Blaas
   :Note: This add-on is bundled with Blender.
