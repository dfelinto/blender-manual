
..    TODO/Review: {{review
   |text=Section "Editing sequences" entirely rewritten, needs an Admin to check and replace these pages. Here is the summary of the rewritten content :
   |fixes=[[Meta:Sanbox/Doc:2.6/Manual/Sequencer|Summary at Meta:Sanbox/Doc:2.6/Manual/Sequencer]]
   }} .

..    TODO/Review: {{WikiTask/Inprogress|50|--[[User:Polosson|http&#58;//www.polosson.com]] 00:48, 31 May 2013 (CEST)|link=Meta:Sanbox/Doc:2.6/Manual/Sequencer/Usage}} .


Overview of the Sequence Editor
===============================

Blender's Video Sequence Editor is a flexible workbench for editing your video footage.
It is used to review your footage, and glue many sequences of your movie together.
It offers a number of built-in and plug-in effects to transition from sequence to sequence,
providing advanced hollywood-style effects for a professional looking video.


.. figure:: /images/2.5_Manual-VSE-header.jpg
   :width: 400px
   :figwidth: 400px

   Video Sequence Editor in Sequence display mode


The Video Sequence Editor has a header (where the menu and view modes are shown) and a workspace,
and works in one of several view modes. The Marker menu allows you to add markers in the VSE.
Markers are shared across animation editors. See :doc:`Markers <animation/markers>`

The sequencer workspace is horizontally striped into channels and each video strip will go in
a horizontal channel. Each channel is numbered on the left-hand side, starting from 0
(you can't put anything thing in this special one!) and going up.
Stripes toward the bottom are more dominant, which we'll get to in a minute.
In the x direction, seconds of animation or frames of animation
(:kbd:`Ctrl-T` to choose) are used as the measure of time
(seconds 1 through 7 are shown). You can scale the time using the zoom keys or mouse actions
(see the Reference for more info).


.. figure:: /images/2.5_Manual-VSE-DoSequence.jpg

   Sequence Output Enabled


When you click Render or Anim to generate an image or video,
Blender has a choice of what image to compose for the current frame/scrub range:

- Current Scene layer result
- Sequence Editor channel 0 result
- Composition Node Editor renderlayer result

The video sequencer is enabled by default.


When you go to the render panel where ordinary renderings take place and you click animation
or image with the VSE open, it will render the clips for the VSE instead of the scene.


Using the Sequence Editor
=========================

Adding Strips
-------------

.. figure:: /images/VseAddMenu.jpg

   the add menu


The Add menu is the main menu you will be using to add content to the VSE. In general,
you load up your strips, create strips of special transition effects,
and then animate out your sequence by selecting "Do Sequence" and clicking the Anim button.
You can use the Add menu in the header,
or hover your mouse cursor over the Sequence workspace and press :kbd:`shift-A`.


.. admonition:: Clips can be Huge
   :class: note

   A three minute quicktime .mov file can be 140Megs.
   Loading it, even over a high-speed LAN can take some time.
   Don't assume your computer or Blender has locked up if nothing happens for awhile.


First, let's add a clip:

- A movie clip in the Audio-Video Interleaved format (``*.avi`` file)
- A movie clip in the Apple QuickTime format (``*.mov``)
- A single still image to be repeated for a number of frames (``*.jpg``, ``*.png``, etc.)
- A numbered sequence of images (``*-0001.jpg``, ``*-0002.jpg``, ``*-0003.jpg``, etc, of any image format)
- One or more images from a directory
- A Scene in your ``.blend`` file.

Blender does not care which of these you use; you can freely mix and match any of them.
They all become a color-coded strip in the VSE:

- Blue is used for Avi/mov codec strips
- Grey is a single image that is repeated/copied
- Purple is an image sequences or group of images played one after the other
- Green is an Audio track

When you choose to add one of these,
the VSE window will switch to a file browser for you to select what you want to add.
Supported files have a little rectangle next to their name (blue for images, green for clips)
as a visual cue that you can pick them successfully:


Add Movies or Images
~~~~~~~~~~~~~~~~~~~~

When adding a Movie or Movie+Audio\ :kbd:`Lmb` LEFT CLICK to put the name of the file into
the text box at the top; this selects a **single** file (like a movie)

In the case of (numbered) image **sequences**, you have a choice:

- **Directory**:
  :kbd:`Rmb` right-click on a directory name,
  and all files in that directory will be brought in as part of the image,
  in sort order, one image per frame
- **Range**:
  Navigate into the directory and right-click and drag over a range of names to highlight multiple files.
  You can page down and continue right-click-dragging to add more to the selection
- **Batch**:
  Shift-right-click selected non-related stills for batch processing; each image will be one frame, in sort order,
  and can be a mix of file types (jpg, png, exr, etc.)
- **All**:
  Press :guilabel:`A` to select/deselect All files in the directory.

When you click the :guilabel:`Select <whatever>` button,
the window pane will switch back to VSE, and the strip will be rubber-banded to your mouse.
You cannot load multiple movies at the same time by right-clicking them;
no movies load if you right click them. Right-clicking only works for images.

.. admonition:: Error: The selected file is not a movie or FFMPEG support not compiled in!
   :class: note

   means that the file is not a movie that Blender can recognize, or **you selected with the wrong button**.
   You get this error message because you *right* -clicked on a movie file,
   OR you don't have a codec that can decode the avi file. If it's the latter,
   find a codec so you can play the file outside of Blender, and then you will be able to load it.
   If it's the former, you must left-click to select movies.



In order to add items to the VSE, left-click for movies, left-click for single images,
or right-click and drag for image sequences.
Move your mouse to the frame/time and stripe you want,
and click to break the rubberband and drop the strip in place
(in a channel and starting at a frame).

When you add an image, Blender makes it into a 50-frame strip,
which means that image will be in your video for two seconds (at 25 fps - PAL).
Aside from re-positioning it,
you will want to scale it by :kbd:`Rmb` -clicking on either the start or end arrow,
and dragging left or right. As you move, the frame number updates to say where the arrow is.
Click :kbd:`Lmb` to validate, or :kbd:`Rmb` to cancel the modification.

.. admonition:: Dealing with Different Sizes
   :class: nicetip


   Dealing with different sized images and different sized outputs is tricky. Think like a pixel.
   If you have a mis-match between the size of the input image and the render output size,
   the VSE does try to auto-scale the image to fit it entirely in the output.
   This may result in clipping. If you do not want that, use Crop and/or Offset in the Input
   panel to move and select a region of the image within the output. When you use Crop or Offset,
   the auto-scaling will be disabled and you can manually re-scale by adding the Transform
   effect.


.. figure:: /images/Manual-VSE-sample.jpg


If you scroll up the workspace, you will see an information channel
(at vertical location channel 0) that gives you some helpful hints about the active strip.
The example above shows a color strip from frames 1 to 25, then a mov file,
and then an image strip. The info channel shows handy information about the image strip,
whose name has been scrunched in the strip display,
but is clearly spelled out in the information strip.


.. admonition:: 9999 frames go by (IMAGE strips only!)
   :class: note

   Ok, so that was a very obscure reference to a song about 99 balloons,
   but we really have not anticipated how fast Blender has moved into mainstream video editing. Unfortunately,
   we initially reserved 4 digits for the filename of each video image sequence set.
   While that provides for up to 400 seconds of video (about 5 minutes US), with Blender moving into movies,
   you need to break up IMAGE strips into 4 digits only, and others 5 digits (10000-19999), (20000-29999), etc.
   Important: that only affects IMAGE strips at the moment. All the other strip types work fine with up to 300,
   000 frames (approximately 3 hours, read: Ben Hur :) ).


.. admonition:: Codecs
   :class: note

   You must have a codec on your machine that can decode the avi file. Blender does not control these. For example,
   the XviD codec is available from www.xvid.org


.. admonition:: FFMPEG Support
   :class: note

   If you are using a Blender build with FFMPEG support, you will be able to load audio and video strips together;
   select Movie+Audio(HD) and when you drop the strip, the strip will split into an audio and video channel strips.


Add Scene
~~~~~~~~~

You can add the virtual image output of a Scene in your current .blend file as well.
Select the scene from the popup list,
and a strip will be added and rubberbanded to your mouse just like a movie or image.
The strip length will be determined based on the animation settings in that scene
(not the current scene, unless the VSE is operating in the same scene).

When adding a Scene strip, please note that,
in order to show you the strip in the VSE Image preview mode, Blender must render the scene.
This may take awhile if the scene is complex,
so there may be a delay between the time you select the scene and the time the strip appears.
To reduce the delay, simplify the scene rendering by selecting fewer layers to render.

If the extra overhead of rendering the scene becomes burdensome
(for either preview or for multiple test renders) and you have enough disk space consider
rendering the scene to a sequence of PNGs and using an Image Sequence strip instead of a
scene.  This is very popular for static graphic overlays like title cards which are often
little more than a static image with animated opacity.


Add Audio
~~~~~~~~~

The VSE can incorporate an audio channel which you can hear as you scrub.
Add an audio track when you are trying to time your video/animation to an audio track, or vice versa.
Please refer to :doc:`the Audio Sequences section <sequencer/audio>` for more information.


Adding Effects
--------------

.. figure:: /images/Manual-VSE-SFX.jpg

   Available Built-in Effects


Blender offers two categories of effects: Built-in and Plug-in.
The built-in effects are listed to the right.
They are built-in to Blender and everyone has them. The plug-in effects are separate files in
a sequence-plugin directory on your PC that are loaded as they are needed.
While a standard set of plugins are distributed when you installed Blender,
everyone's computer may have a different set.

Every Built-in effect is explained in the next page individually,
but they all are added and controlled in the same way. To add an effect strip,
select one base strip (image, movie, or scene) by :kbd:`Rmb` clicking on it.
For some effects, like the Cross transition effect,
you will need to :kbd:`shift-Rmb` a second overlapping strip
(it depends on the effect you want).
Then select Add → Effect and pick the effect you want from the pop-up menu. When you do,
the Effect strip will be shown above the source strips. If it is an independent effect,
like the color generator (described later), it will be rubberbanded to your mouse;
click to drop the strip.

Since most Effects strips depend on one or two source strips,
their frame location and duration depends on their source strips. Thus,
you may not be able to move it;
you have to move the source strips in order to affect the effect strip.

To use an effect that combines or makes a transition between (or composites) two strips,
you must :guilabel:`B` ox select or shift-right-click two of them.
When you add the effect strip, it will be placed in a channel above the two in Grab mode
(click to drop it on a channel).
Its duration will be the overlap between the two strips as a maximum.

With some effects, like the AlphaOver, the order in which you select the strips is important.
You can also use one effect strip as the input or source strip with another strip,
thus layering effects on top of one another.

Note: The only exception is the Color Generator effect. It does not depend on a base strip;
you can add and position it independent of any other strip.
Change the length as you would any strip.

.. admonition:: Reference
   :class: refbox

   | Mode:     Sequence, Effects Strip Selected
   | Menu:     Strip → Change Effect
   | Hotkey:   :kbd:`C`


If you picked the wrong effect from the menu, you can always change it by selecting the strip
(:kbd:`Rmb`) and using the Strip→Change Effect selection. Or,
you can press :guilabel:`C` hange to switch effects on a selected Effects strip.


Adding Plugin Effects
~~~~~~~~~~~~~~~~~~~~~

FIXME(Template Unsupported: Warning/Not Yet Implemented;
{{Warning/Not Yet Implemented|VSE plugins are not working in Blender 2.6 currently…}})

.. Comment: <!--[[File:Manual-VSE-Plugins.png|right]]
   Sequence Plugins are special little routines written by special programmers in the C language
   as a dynamic load library (.DLL). A DLL can be loaded at any time (dynamically)
   as it is needed, so it "plugs in" to Blender. (In case you wondered:
   the extension is platform dependent. These files are named .so (shared object) on Linux e.g.)

   The image to the right shows the Sequence DLL's that I have available on my system. Each of
   them do some special effect indicated by their name or as explained on the
   [http://www-users.cs.umn.edu/~mein/blender/plugins/ Blender Resource Page for Plugins]
   or programmer website. For example, the Iris plugin transitions between two strips by opening
   an expanding hole in the middle of the first and letting the second one show through,
   like an iris of a camera opening up.
   Some of these plugins can be five or more years old and still work very well;
   Blender tries to ensure backward compatibility,
   and they should work independent of output format or resolution (size).--> .


Strip Properties
----------------

The properties for the strip are examined and set in the properties panel,
shortcut :kbd:`N`.


- Edit Strip - change properties of the strip
- Strip Input - where to pull images from
- Effect - Settings for effects strips
- Filter - Image pre-processing
- Proxy - Use representatives of the real image, for low-powered PCs
- Scene - Settings for when a scene strip is selected
- Sound - Settings for a sound clip

The panels for each of these sets of options and controls are shown to the right


Edit Strip Panel
~~~~~~~~~~~~~~~~

:guilabel:`Name`
   You can name or rename your strips here.
:guilabel:`Type`
   Displays the type of strip selected.
:guilabel:`Blend Mode`
   By default, a strip Replaces the output image of any lower-level strips. However,
   many other blending modes are available based on the strip type. For example,
   Alpha-Over automatically overlays the image on top of a lower level strip.
   Autoblending modes remove the need for separate effect strips.
   Blend percent controls how much of an effect the strip exerts, even over time.

:guilabel:`Opacity`
   Set the opacity of the strip.
:guilabel:`Mute`
   Hides the strip so that it does not participate in the final image computation
:guilabel:`Lock`
   Prevents the strip from being moved.
:guilabel:`Channel`
   Changes the channel number, or row, of the strip.
:guilabel:`Start Frame`
   Changes the starting frame number of the strip, which is the same as grabbing and moving the strip.
   Tip: when you add a strip, I like to just drop it and then use this field to place it at the frame I want,
   rather that trying to drag and drop in exactly the right place.
:guilabel:`Length`
   Specify the number of frames to use for the strip.

Use the :guilabel:`Convert to Premul` button if a strip has an Alpha (transparency) channel.
Use :guilabel:`FilterY` if the strip is from broadcast video and has even or odd interlacing
fields. Enhance the color saturation through the :guilabel:`Mul` tiply field.
Play a strip backwards by enabling :guilabel:`Reverse Frames`.
Tell Blender to display every nth frame by entering a :guilabel:`Strobe` value. Finally,
when using MPEG video (VCD, DVD, XVid, DivX, …),
an image is built up over the course of a few frames; use the :guilabel:`Preseek` field to
tell Blender to look backward and compose the image based on the n previous frames (e.g.
**15** for Mpeg2 DVD).


Effect Strip
~~~~~~~~~~~~

For all effects, use the Strip Properties panel to control the effects strip;
each effect has different controls, but they can all be set in the Properties panel.
Control the length of the strip to vary the speed with which the transform happens.
Regardless of whether they are built-in or plug-in,
all effect strips do some special image manipulation,
usually by operating on another strip or two in a different channel.
The effect strip is shown in some channel, but its resultant effect shows up as Channel 0.


Strip Input
~~~~~~~~~~~

Controls the source of the strip. Fields include file path, file name, image offset,
crop settings.

This is here you can edit/update the path of the file used by a strip. Very useful when you
moved it one way or the other - this avoid you deleting and re-creating the strip!

You have two text fields for path, the first being the path of the parent directory
(:guilabel:`Path`), and the second the file name itself.


Filter
~~~~~~

Enables you to quickly set common image pre-processing options.
:guilabel:`Strobe`

:guilabel:`Flip`
   X flips (reverses) the image left-to-right, Y reverses top-to-bottom.
:guilabel:`Backwards`
   Reverses strip image sequence
:guilabel:`De-Interlace`
   Removes fields in a video file.

:guilabel:`Saturation`
   Increase or decrease the saturation of an image.
:guilabel:`Multiply`
   Multiplies the colors by this value.
:guilabel:`Premultiply`
   Premultiply the Alpha channel.
:guilabel:`Convert Float`
   Converts input to float data.

:guilabel:`Use Color Balance`
   Provides three filters to adjust coloration: Lift, Gamma, and Gain. Each pass can have a positive,
   or inverted effect by clicking the appropriate button.
   Set the amount of the effect by setting the color swatch; white (RGB 1,1,1) has no effect.


Proxy Strip Properties Panel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A proxy is a smaller image (faster to load) that stands in for the main image.
When you :guilabel:`Rebuild proxy` Blender computes small images (like thumbnails)
for the big images and may take some time. After computing them, though, editing functions
like scrubbing and scrolling and compositing functions like cross using these proxies is much
faster but gives a low-res result. Disable proxies before final rendering.

In order to actually *use* the proxies, the proper "Proxy Render Size" dropdown value must
be selected in the Properties panel of the Sequencer View (where the edit plays back).


Sound
~~~~~

This panel appears when a sound file is selected.

Here you can specify the Sound Strip's file path and file name.

:guilabel:`Pack`
   Packs the sound file into the current .blend file.
:guilabel:`Caching`
   The sound file is decoded and loaded into RAM.
:guilabel:`Volume`
   Set the volume of the Sound file.
:guilabel:`Attenuation/dB`
   Attenuation in decibels
:guilabel:`Trim Duration Start/End`
   Offset the start and end of a sound strip.


Scene
~~~~~

Specify the scene to be linked to the current scene strip.

:guilabel:`Sequencer`
   Process the render (and composited) result through the video sequence editor pipeline,
   if sequencer strips exist. This is the same function as in the render settings.
:guilabel:`Camera Override`
   Change the camera that will be used.


Adjusting the View
------------------

Use these shortcuts to adjust the sequence area of the VSE:
Pan :kbd:`mmb`
Zoom :kbd:`wheel`
Vertical Scroll use :kbd:`Shift-wheel`, or drag on the left scroll bar.
Horizontal Scroll use :kbd:`ctrl-wheel`, or drag on the lower scroll ;bar.
Scale View Vertically, drag on the circles on the vertical scroll bar.
Scale View Horizontally, drag on the circles on the horizontal scroll bar.

As usual, the View Menu controls what and how you view in the workspace.

:guilabel:`Properties Panel`
   The Properties Panel contains options for the the way the preview is displayed.
:guilabel:`View all Sequences` :kbd:`home`
   Zooms (out) the display to show all strips.
:guilabel:`Fit preview in Window` :kbd:`home`
   Resizes preview so that it fits in the window.
:guilabel:`Show Preview 1:1` :kbd:`pad1`
   Resizes preview to a 1:1 scale (actual size).
:guilabel:`View Selected` :kbd:`pad.`
   Zooms in the display to fit only the selected strips

Use this when working arranging a lot of strips and you want to use all of your screen to work.

.. admonition:: Reference
   :class: refbox

   | Mode:     Sequence
   | Menu:     View → Show Frames, View → Show Seconds
   | Hotkey:   :kbd:`T`


:guilabel:`Draw Frames`
   Diplays the frame number instead of the time, in the Frame Number Indicator.
:guilabel:`Show Frame Number Indicator`
   Toggles the units of measure across the bottom of the workspace between seconds or frames.
:guilabel:`Safe Margin`
   Displays an overlay on the preview, marking where title safe region is.
:guilabel:`Separate Colors`
   When using Luma Waveform view, this separates R,G, and B into separate graphs.
:guilabel:`Transform Markers`
   Transform Markers as well as Strips.


Scrubbing
~~~~~~~~~

To move back and forth through your movie, use the Timeline window.
:kbd:`Lmb` click and drag left/right in the timeline window,
moving the vertical bar which indicates the current frame. As you do,
the image for that frame is displayed in the VSE window.

Real-time scrubbing and image display is possible on reasonable computers when viewing an
image sequence or movie (avi/mov) file. Scene images have to be rendered individually,
which may take some time.


View Modes
~~~~~~~~~~

The icons in the header allow to change the view of the VSE. By default,
only the sequencer is displayed. The second button displays only the Preview window,
and the third button displays both the Sequencer and the Preview.

When the preview is enabled, you have several options to change what type pf preview to display. They are explained in the :doc:`Display Modes Page <sequencer/modes>`.


Scene Preview
~~~~~~~~~~~~~

When using a Scene Strip in the sequencer,
these settings in the Properties Panel determine how they are shown in the preview window.

:guilabel:`Open GL Preview`
   If you have Open GL, enable this setting to use Open GL for the scene preview renders.
   The drop down menu allows you to change how the Scene is displayed (Bounding Box, Wireframe, Solid, Textured).


View Settings
~~~~~~~~~~~~~

The View Settings section in the properties panel contains addition display options.

:guilabel:`Show Overexposed`
   Increasing this number to 1 or greater displays a striped overlay to the preview image, showing where it is overexposed. A higher number gives a higher threshold for marking overexposure.

:guilabel:`Safe Margin`
   Displays an overlay on the preview, marking where title safe region is.

:guilabel:`Proxy Render Size`
   Draws preview using full resolution or different proxy resolutions. Render resolution is determined in the render settings panel. Using a smaller preview size will increase speed.


Refresh View
~~~~~~~~~~~~

Certain operations, like moving an object in 3D View,
may not force the Sequencer to call for a refresh of the rendered image
(since the movement may not affect the rendered image). If an image or video, used as a strip,
is changed by some application outside of Blender,
Blender has no real way of being notified from your operating system.
To force Blender to re-read in files, and to force a re-render of the 3D View, click the
Refresh button to force Blender to update and synchronize all cached images and compute the
current frame.


Selecting Strips
----------------

The Select Menu helps you select strips in different ways.

:guilabel:`Strips to the Left`
   Select all strips to the left of the currently selected strip.
:guilabel:`Strips to the Right`
   Select all strips to the right of the currently selected strip.
:guilabel:`Select Surrounding Handles` :kbd:`alt-ctrl-Rmb`
   Select both handles of the strip, plus the neighboring handles on the immediately adjoining strips. Select with this method to move a strip that is between to others without affecting the selected strip's length.
:guilabel:`Left Handle` :kbd:`alt-Rmb`
   Select the left handle of the currently selected strip.
:guilabel:`Right Handle` :kbd:`ctrl-Rmb`
   Select the right handle of the currently selected strip.
:guilabel:`Linked`
   Select all strips linked to the currently selected strip
:guilabel:`Select All` :kbd:`A`
   Selects all the strips loaded.
:guilabel:`Select Inverse`
   Inverts the current selection.
:guilabel:`Border Select` :kbd:`B`
   Begins the :guilabel:`Box` mode select process. Click and drag a rectangular lasso around a region of strips in your Sequence workspace. When you release the mouse button, the additional strips will be selected.


Moving and Modifying Strips
---------------------------

:kbd:`G` Moves the selected strip(s) in time or in channels. Move your mouse horizontally (left/right) to change the strip's position in time. Move vertically (up/down) to change channels.


- To snap while dragging hold :kbd:`Ctrl`
- To 'ripple edit' (Make room for strips you drag) hold :kbd:`Alt` when placing a strip.

If you have added a strip by mistake or no longer want it,
delete it by pressing :guilabel:`X` or using this menu option.

:guilabel:`Duplicate` a strip to make an unlinked copy; drag it to a time and channel, and drop it by :kbd:`Lmb` click.

The Strip Menu contains additional tools for working with strips:
:guilabel:`Grab/Move`

:guilabel:`Grab/Extend from Frame`

:guilabel:`Cut (hard) at frame`

:guilabel:`Cut (soft) at frame`

:guilabel:`Separate Images`
:guilabel:`Deinterlace Movies`

:guilabel:`Duplicate Strips`

:guilabel:`Erase Strips`

:guilabel:`Set Render Size`

:guilabel:`Make Meta Strip`

:guilabel:`UnMeta Strip`

:guilabel:`Reload Strips`

:guilabel:`Reassign Inputs`

:guilabel:`Swap Inputs`


:guilabel:`Lock Strips`

:guilabel:`UnLock Strips`

:guilabel:`Mute Strips`

:guilabel:`Un-Mute Strips`

:guilabel:`Mute Deselected Strips`

:guilabel:`Snap Strips`

:guilabel:`Swap Strips`



Snap to Frame
~~~~~~~~~~~~~

:kbd:`shift-S`
Position your cursor (vertical green line) to the time you want.
Snap to current frame to start a strip exactly at the beginning of the frame.
If your Time display is in seconds,
you can get to fractional parts of a second by zooming the display;
you can get all the way down to an individual frame.


Separate Images to Strips
~~~~~~~~~~~~~~~~~~~~~~~~~

:kbd:`Y` Converts the strip into multiple strips, one strip for each frame. Very useful for slide shows and other cases where you want to bring in a set on non-continuous images.


Editing Strips
~~~~~~~~~~~~~~

- :kbd:`Rmb` in the middle of the strip selects the **entire** strip; holding it down (or pressing :kbd:`G` rab) and then moving the mouse drags a strip around.


- :kbd:`Rmb` on the left arrow of the strip selects the **start** frame offset for that strip; holding it down (or pressing :kbd:`G` rab and then moving the mouse left/right changes the start frame within the strip by the number of frames you move it:
  - If you have a 20-image sequence strip, and drag the left arrow to the right by 10 frames, the strip will start at image 11 (images 1 to 10 will be skipped). Use this to clip off a rollup or useless lead-in.
  - Dragging the left arrow left will create a lead-in (copies) of the first frame for as many frames as you drag it. Use this when you want some frames for transitions to the this clip.


- :kbd:`Rmb` on the right arrow of the strip selects the **end** frame of the strip; holding it down (or pressing :kbd:`G` rab) and then moving the mouse changes the ending frame within the strip:
  - Dragging the right arrow to the left shortens the clip; any original images at the tail are ignored. Use this to quickly clip off a rolldown.
  - Dragging the right arrow right extends the clip. For movies and images sequences, more of the animation is used until exhausted. Extending a clip beyond its end results in Blender making a copy of the last image. Use this for transitions out of this clip.

.. admonition:: Multiple selection
   :class: note

   You can select several (handles of) strips by :kbd:`shift-Rmb` -clicking: when you'll hit :kbd:`G`, everything that's selected will move with your mouse - this means that, for example, you can at the same time move a strip, shorten two others, and extend a forth one.


- STRIP EXTEND. With a number of Image strips selected, pressing :kbd:`E` enters EXTEND mode. All selected strip handles to the "mouse side" of the current frame indicator will transform together, allowing you to essentially extend the strips that fall exactly on the current frame marker and having all others adjust to compensate.

While splicing two strips happens just by placing them finish-to-start,
cut a strip by pressing :kbd:`K` to cut. At the selected frame for the selected strips,
K cuts them in two. Use Cut to trim off roll-ups or lead-ins, or roll-downs or extra film shot
("C" was already taken for Change).


.. admonition:: Note on the 'cut'
   :class: note

   When you 'cut' a strip, you don't really make a cut like it was with the 'old editing' on real film. In fact, you make a copy of the strip: the end of the original one is 'winded' to the cut point, as with the beginning of the new copy.

   For example, imagine that you have a strip of **50** frames,
   and that you want to delete the first ten ones.
   You have to go to the **11** :sup:`th` frame, and hit :kbd:`K`;
   the cut 'divides' your strip in two parts. You now can select the first small part
   (frames **1** to **10**), and delete it hitting :kbd:`X`.

   You might think that you have really erased the frames **1** to **10**,
   but there are still there, 'winded', as in a film reel, under your frame **11** :
   you just have deleted one of the two copies of your strip created by the 'cut'.
   And you can at any time get your 'lost' frames back
   (just :kbd:`Rmb` -click on the left arrow of the strip,
   then :kbd:`G` grab it to the left to display the desired number of frames again (or to
   the right to 'hide' more frames - this is another way to remove frames at the beginning/end of
   a strip!).

   This is at the heart of nearly every editor solution, and that's quite handy!


.. admonition:: Action Stops
   :class: note

   When extending the start beyond the beginning or end after the ending, keep in mind that only the last image copies, so when viewed, action will stop on that frame. Start your transition (fade, cross) a little early while action is still happening so that the stop action is not that noticeable (unless, of course, you want it to be, like the 80's drama sitcoms).


Change the length of an effect strip by changing the start/end frame of the origin strips.


Copy and Paste
~~~~~~~~~~~~~~

You can copy a clip and paste it using the two header buttons.


Meta Strips
~~~~~~~~~~~

A Meta-Strip is a group of strips. Select all the strips you want to group,
and Ctrl-g to group them into one meta.
The meta spans from the beginning of the first strip to the end of the last one,
and condenses all channels into a single strip, just like doing a mixdown in audio software.
Separating (ungrouping) them restores them to their relative positions and channels.

The default blend mode for a meta strip is Replace.  There are many cases where this alters
the results of the animation so be sure to check the results and adjust the blend mode if
necessary.

One convenient use for meta strips is when you want to apply the same effect to multiple
strips.  For example: scaling a loop.  Until blender gets a Loop effect,
the only way to loop a clip is to duplicate it several times.
If the clip needs any transforms (like scaling or translating an animated watermark or source
material in a different aspect ratio) it is much more convenient to apply a single set of
transforms to a meta strip built from the repeated duplicates than apply copies of those
transforms to each instance in the loop.

It is possible to edit the contents of a meta strip by selecting it and pressing Tab.
You can press Tab again to finish editing that strip.  Since meta strips can be nested, to pop
out one level of meta strip make sure you do not have a meta strip as the active strip when
you press Tab.


