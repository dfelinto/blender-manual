

..    TODO/Review: {{review|split=X}} .

Motion Tracking
===============


Introduction
------------

Motion tracking is a new technique available in Blender. It is still under development,
and currently supports basic operations for 2D motion tracking, 3D motion tracking,
and camera solution. It's already ready to be used in production,
as validated by "Tears of Steel."


Getting started
---------------


Motion tracking is available in current SVN Trunk and is included with Blender 2.61 release.
It's enabled by default for all platforms and can be used "out-of-box".

Here's brief descriptions of motion tracking tools currently available in Blender


Supervised 2D tracking
~~~~~~~~~~~~~~~~~~~~~~


There's no common algorithm which can be used for all kinds of footage,
feature points and their motions. Such algorithms can be constructed,
but they'll be really slow and they can still fail, so the only way to perform 2D tracking is
to manually choose the tracking algorithm  and its settings. Current defaults work nicely for
general footage which isn't very blurry and where feature points aren't getting highly
deformed by perspective.

Improving 2D tracking is already in our TODO list, but it's not high priority at this moment.
If you aren't sure about algorithms and settings and don't want to read this document,
you can just play with settings and find one which works for you.


Manual lens calibration using grease pencil and/or grid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


All cameras record distorted video.
Nothing can be done about this because of the manner in which optical lenses work.
For accurate camera motion,
the exact value of the focal length and the "strength" of distortion are needed.

Currently, focal length can be automatically obtained only from the camera's settings or from
the EXIF information -- there are no tools inside Blender which can estimate it. But there are
some tools which can help to find approximate values to compensate for distortion. There are
also fully manual tools where you can use a grid which is getting affected by distortion model
and deformed cells defines straight lines in the footage. You can also use the grease pencil
for this - just draw line which should be straight on the footage using poly line brush and
adjust distortion values to make the grease pencil match lines on the footage.

To calibrate your camera more accurately, use the grid calibration tool from OpenCV.
OpenCV is using the same distortion model, so it shouldn't be a problem.


Camera motion solving
~~~~~~~~~~~~~~~~~~~~~


Despite the fact that there's no difference in solving camera motion and object motion from a
mathematical point of view, only camera solving is currently supported.
And it still has some limitations,
like unsupported solve of tripod motions or dominant plane motions
(where all trackable features belong to one plane).
These limitations are planned to be solved in the future.


Basic tools for scene orientation and stabilization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


After solve,
you need to orient the real scene in the 3D scene for more convenient compositing.
There are tools to define the floor, the scene origin,
and the X/Y axes to perform scene orientation.

If something is needed to stabilize video from the camera to make the final result looks
nicer, 2D stabilization is available to help. It stabilizes video from the camera,
which can compensate for camera jumps and tilt.


Basic nodes for compositing scene into real footage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Some new nodes were added to the Compositor to composite scene into footage in easier way.
So there are nodes for 2D stabilization, distortion and undistortion which are easy to use.


Not implemented tools
~~~~~~~~~~~~~~~~~~~~~


Some tools aren't available in Blender yet, but they are in our TODO list.
So there's currently no support for such things as rolling shutter filtering,
object motion solving, motion capturing.
But you can try to hack this stuff using currently implemented things.


Manual
------


Movie Clip Editor
~~~~~~~~~~~~~~~~~


Almost all motion tracking tools are concentrated in the Movie Clip Editor.
Currently it doesn't have any tools which aren't related to motion tracking,
but in the future it may be expanded to be used for masking,
so that's why it's given this more abstract name, rather than motion tracking.

This editor can be found in the list of editor types.


.. figure:: /images/Manual_movie_tracking_clip_editor_type_menu.jpg
   :width: 120px
   :figwidth: 120px

   Editor type menu


When you switch to Movie Clip Editor window, the interface changes in the following way.


.. figure:: /images/Manual_movie_tracking_clip_editor_space_ui.jpg
   :width: 300px
   :figwidth: 300px

   Movie Clip Editor interface


The next logical step to open a new video clip to start working with.
There are several ways to to this:


- Use :kbd:`Open` button from movie editor header
- Use :menuselection:`Clip --> Open` menu
- Use :kbd:`Alt-O>` shortcut

Both movie files and image sequences can be used in the clip editor.
If you're using an image sequence there's one limitation on naming of files:
the numbers at the end of the image name should be increasing continuously.

So, when a movie clip is loaded into the clip editor,
extra panels are displayed in the interface.


.. figure:: /images/Manual_movie_tracking_clip_editor_clip_opened_ui.jpg
   :width: 300px
   :figwidth: 300px

   Movie Clip Editor with opened clip


There are plenty of new tools on the screen and here's short description of all of them.

First of all,
it should be mentioned that the camera solver consists of three quite separate steps:


- 2D tracking of footage
- Camera intrinsics (focal length, distortion coefficients) specification/estimation/calibration
- Solving camera, scene orientation, scene reconstruction

Tools in the clip editor are split depending on which step they're used in, so the interface
isn't cluttered up with scene orientation tools when only 2D tracking can be done. The
currently displayed tool category can be changed using the Mode menu which is in the editor
header.


.. figure:: /images/Manual_movie_tracking_clip_editor_mode_menu.jpg
   :width: 300px
   :figwidth: 300px

   Movie Clip Editor mode menu


But almost all operators can be called from menus, so it's not necessary to change the mode
every time you want to use a tool which is associated with a different editor mode.

In tracking mode only tools which are related to tracking and camera solving are displayed.
Camera solving tools are included here because it's after solving you'll most probably want to
re-track existing tracks or place new tracks to make solving more accurate.


Tools available in tracking mode
________________________________


Marker panel
++++++++++++


- The :strong:`Add Marker and Move` operator places a new marker at the position of the mouse (which is under the button in this case, not ideal but it's just how things work) and then it can be moved to the needed location. When it's moved to the desired position,

FIXME(Template Unsupported: Shortcut/Mouse;
{{Shortcut/Mouse|lmb}}
) can be used to finish placing the new marker. Also, :kbd:`Enter` and :kbd:`Space` can be used to finish placing the marker.
    But it's faster to use :kbd:`Ctrl-lmb` to place markers directly on the footage. This shortcut will place the marker in the place you've clicked. One more feature here: until you've released the mouse button, you can adjust the marker position by moving the mouse and using the track preview widget to control how accurately the marker is placed.

- The :strong:`Detect Features` operator detects all possible features on the current frame and places markers at these features. This operator doesn't take into account other frames, so it can place markers on features which belong to moving objects, and if camera is turning away from this shot, no markers would be placed on frames after the camera moved away.

    There are several properties for this operator:
       :strong:`Placement` is used to control where to place markers. By default, they'll be added through the whole frame, but you can also outline some areas with interesting features with grease pencil and place markers only inside the outlined area. That's how the "Inside Grease Pencil" placement variant works. You can also outline areas of no interest (like trees, humans and so) and place markers outside of these areas. That's how the "Outside Grease Pencil" placement variant works.
       :strong:`Margin` controls the distance from the image boundary for created markers. If markers are placed too close to the image boundary, they'll fail to track really quickly and they should be deleted manually. To reduce the amount of manual clean-up, this parameter can be used.
       :strong:`Trackability` limits minimal trackability for placing markers. This value comes from the feature detection algorithm and basically it means: low values means most probably this feature would fail to track very soon, high value means it's not much such track. Amount of markers to be added can be controlled with this value.
       :strong:`Distance` defines the minimal distance between placed markers. It's needed to prevent markers from being placed too close to each other (such placement can confuse the camera solver).

- :strong:`Delete Track` is a quite self-explaining operator which deletes all selected tracks.


Track panel
+++++++++++


- The first row of buttons is used to perform tracking of selected tracks (i.e. following the selected feature from frame to frame). Tracking can happen (in order of buttons):
  - Backward one frame
  - Backward along the sequence
  - Forward along the whole sequence
  - Forward one frame

    This operator depends on settings from the Tracking Settings panel, which will be described later.
    If during sequence tracking the algorithm fails to track some markers, they'll be disabled and tracking will continue for the rest of the markers. If the algorithm fails when tracking frame-by-frame, the marker is not disabled, and the most likely position of the feature on the next frame is used.

- :strong:`Clear After` deletes all tracked and keyframed markers after the current frame for all selected tracks.
- :strong:`Clear Before` deletes all tracked and keyframed markers before the current frame for all selected tracks.
- :strong:`Clear` clears all markers except the current one from all selected tracks.
- :strong:`Join` operator joins all selected tracks into one. Selected tracks shouldn't have common tracked or keyframed markers at the same frame.


Solve panel
+++++++++++


:strong:`Camera Motion` operator solves the motion of camera using all tracks placed on the footage and two keyframes specified on this panel. There are some requirements:


- There should be at least 8 common tracks on the both of the selected keyframes.
- There should be noticeable parallax effects between these two keyframes.

If everything goes smoothly during the solve, the average reprojection error is reported to
the information space and to the clip editor header. Reprojeciton error means the average
distance between reconstructed 3D position of tracks projected back to footage and original
position of tracks. Basically, reprojection error below 0.3 means accurate reprojection,
0.3-3.0 means quite nice solving which still can be used.
Values above 3 means some tracks should be tracked more accurately,
or that values for focal length or distortion coefficients were set incorrectly.

The :strong:`Refine` option specifies which parameters should be refined during solve.
Such refining is useful when you aren't sure about some camera intrinsics,
and solver should try to find the best parameter for those intrinsics. But you still have to
know approximate initial values - it'll fail to find correct values if they were set
completely incorrectly initially.


Cleanup Panel
+++++++++++++


This panel contains a single operator and its settings. This operator cleans up bad tracks:
tracks which aren't tracked long enough or which failed to reconstruct accurately.
Threshold values can be specified from sliders below the button. Also,
several actions can be performed for bad tracks:


- They can simply be selected
- Bad segments of tracked sequence can be removed
- The whole track can be deleted


Clip Panel
++++++++++


This panel currently contains the single operator :kbd:`Set as background` which sets the
clip currently being edited as the camera background for all visible 3D viewports.
If there's no visible 3D viewports or the clip editor is open in full screen,
nothing will happen.


Properties available in tracking mode
_____________________________________


Grease Pencil Panel
+++++++++++++++++++


It's a standard grease pencil panel where new grease pencil layers and frames can be
controlled. There's one difference in the behavior of the grease pencil from other areas -
when a new layer is created "on-demand"
(when making a stroke without adding a layer before this)
the default color for the layer is set to pink.
This makes the stroke easy to notice on all kinds of movies.


Objects Panel
+++++++++++++


.. figure:: /images/Manual_movie_tracking_clip_editor_objects_panel.jpg
   :width: 130px
   :figwidth: 130px

   Objects Panel in clip editor


This panel contains a list of all objects which can be used for tracking,
camera or object solving.
By default there's only one object in this list which is used for camera solving.
It can't be deleted and other objects can't be used for camera solving;
all added objects are used for object tracking and solving only.
These objects can be referenced from Follow Track and Object Solver constraints.
Follow Track uses the camera object by default.

New objects can be added using :kbd:`+` and the active object can be deleted with the
:kbd:`-` button.
Text entry at the bottom of this panel is used to rename the active object.

If some tracks were added and tracked to the wrong object, they can be copied to another
object using :menuselection:`Track --> Copy Tracks` and :menuselection:`Track --> Paste Tracks`\ .

The usage for all kind of objects (used for camera and object tracking) is the same:
track features, set camera data, solve motion. Camera data is sharing between all objects and
refining of camera intrinsics happens when solving camera motion only.


Track Panel
+++++++++++


.. figure:: /images/Manual_movie_tracking_clip_editor_track_panel.jpg
   :width: 130px
   :figwidth: 130px

   Track Panel in clip editor


First of all, track name can be changed in this panel.
Track names are used for linking tracking data to other areas, like a Follow Track constraint.

The next thing which can be controlled here is the marker's enabled flag
(using the button with the eye icon). If a marker is disabled,
its position isn't used either by solver nor by constraints.

The button with the lock icon to the right of the button with the eye controls whether the
track is locked. Locked tracks can't be edited at all.
This helps to prevent accidental changes to tracks which are "finished"
(tracked accurate along the whole footage).

The next widget in this panel is called "Track Preview" and it displays the content of the
pattern area. This helps to check how accurately the feature is being tracked
(controlling that there's no sliding off original position)
and also helps to move the track back to the correct position.
The track can be moved directly using this widget by mouse dragging.

If an anchor is used (the position in the image which is tracking is different from the
position which is used for parenting),
a preview widget will display the area around the anchor position. This configuration helps in
masking some things when there's no good feature at position where the mask corner should be
placed. Details of this technique will be written later.

There's small area below the preview widget which can be used to enlarge the vertical size of
preview widget (the area is highlighted with two horizontal lines).

The next setting is channels control. Tracking happens in gray-scale space,
so a high contrast between the feature and its background yields more accurate tracking.
In such cases disabling some color channels can help.

The last thing is custom color, and the preset for it.
This setting overrides the default marker color used in the clip editor and 3D viewport,
and it helps to distinguish different type of features (for example,
features in the background vs. foreground and so on). Color also can be used for "grouping"
tracks so a whole group of tracks can be selected by color using the Select Grouped operator.


- :strong:`Marker Tip 1:`  To select good points for tracking, use points in the middle of the footage timeline and track backwards and forwards from there. This will provide a greater chance of the marker and point staying in the camera shot.


Camera Data Panel
+++++++++++++++++


This panel contains all settings of the camera used for filming the movie which is currently
being edited in the clip editor.

First of all, predefined settings can be used here.
New presets can be added or unused presets can be deleted. But such settings as distortion
coefficients and principal point aren't included into presets and should be filled in even if
camera presets are used.


- :strong:`Focal Length` is self-explanatory; it's the focal length with which the movie was shot. It can be set in millimeters or pixels. In most cases focal length is given in millimeters, but sometimes (for example in some tutorials on the Internet) it's given in pixels. In such cases it's possible to set it directly in the known unit.
- :strong:`Sensor Width` is the width of the CCD sensor in the camera. This value can be found in camera specifications.
- :strong:`Pixel Aspect Ratio` is the  pixel aspect of the CCD sensor. This value can be found in camera specifications, but can also be guessed. For example, you know that the footage should be 1920x1080, but the images themselves are 1280x1080. In this case, the pixel aspect is:

:math:`1920 / 1280 = 1.5`


- :strong:`Optical Center` is the optical center of the lens used in the camera. In most cases it's equal to the image center, but it can be different in some special cases. Check camera/lens specifications in such cases. To set the optical center to the center of image, there's a :kbd:`Center` button below the sliders.
- :strong:`Undistortion K1, K2 and K3` are coefficients used to compensate for lens distortion when the  movie was shot. Currently these values can be tweaked by hand only (there are no calibration tools yet) using tools available in Distortion mode. Basically, just tweak K1 until solving is most accurate for the known focal length (but also take grid and grease pencil into account to prevent "impossible" distortion).


Display Panel
+++++++++++++


This panel contains all settings which control things displayed in the clip editor.


- :strong:`R, G, B` and :strong:`B/W` buttons at the top of this panel are used to control color channels used for frame preview and to make the whole frame gray scale. It's needed because the tracking algorithm works with gray-scale images and it's not always obvious to see which channels disabled will increase contrast of feature points and reduce noise.
- :strong:`Pattern` can be used to disable displaying of rectangles which correspond to pattern areas of tracks. In some cases it helps to make the clip view cleaner to check how good tracking is.
- :strong:`Search` can be used to disable displaying of rectangles which correspond to search areas of tracks. In some cases it helps to make the clip view cleaner to check how good tracking is. Only search areas for selected tracks will be displayed.
- :strong:`Pyramid` makes the highest pyramid level be visible. Pyramids are defined later in the Tracking Settings panel section, but basically it helps to determine how much a track is allowed to move from one frame to another.
- :strong:`Track Path` and :strong:`Length` control displaying of the paths of tracks. The ways tracks are moving can be visible looking at only one frame. It helps to determine if a track jumps from its position or not.
- :strong:`Disabled Tracks` makes it possible to hide all tracks which are disabled on the current frame. This helps to make view more clear, to see if tracking is happening accurately enough.
- :strong:`Bundles` makes sense after solving the movie clip, and it works in the following way: the solved position of each track gets projected back to the movie clip and displayed as a small point. The color of the point depends on the distance between the projected coordinate and the original coordinate: if they are close enough, the point is green, otherwise it'll be red. This helps to find tracks which weren't solved nicely and need to be tweaked.
- :strong:`Track Names and Status` displays information such as track name and status of the track (if it's keyframed, disabled, tracked or estimated). Names and status for selected tracks are displayed.
- :strong:`Compact Markers`\ . The way in which markers are displayed (black outline and yellow foreground color) makes tracks visible on all kind of footage (both dark and light). But sometimes it can be annoying and this option will make the marker display more compactly - the outline is replaced by dashed black lines drawn on top of the foreground, so that marker areas are only 1px thick.
- :strong:`Grease pencil` controls if grease pencil strokes are allowed to be displayed and made.
- :strong:`Mute` changes displaying on movie frame itself with black square, It helps to find tracks which are tracked inaccurately or which weren't tracked at all.
- :strong:`Grid` (available in distortion mode only) displays a grid which is originally orthographic, but os affected by the distortion model. This grid can be used for manual calibration - distorted lines of grids are equal to straight lines in the footage.
- :strong:`Manual Calibration` (available in distortion mode only) applies the distortion model for grease pencil strokes. This option also helps to perform manual calibration.  A more detailed description of this process will be added later.
- :strong:`Stable` (available in reconstruction mode only). This option makes the displayed frame be affected by the 2D stabilization settings. It's only a preview option, which doesn't actually change the footage itself.
- :strong:`Lock to Selection` makes the editor display selected tracks at the same screen position along the whole footage during playback or tracking. This option helps to control the tracking process and stop it when the track is starting to slide off or when it jumped.
- :strong:`Display Aspect Ratio` changes the aspect ratio for displaying only. It does not affect the tracking or solving process.


Tracking Settings Panel
+++++++++++++++++++++++


Common options
**************


This panel contains all settings for the 2D tracking algorithms.
Depending on which algorithm is used, different settings are displayed,
but there are a few that are common for all tracker settings:

:strong:`Adjust Frames` controls which patterns get tracked; to be more precise, the pattern from which frame is getting tracked. Here's an example which should make things clearer.

The tracker algorithm receives two images inside the search area and the position of a point
to be tracked in the first image.
The tracker tries to find the position of that point from the first image in the second image.

Now, this is how tracking of the sequence happens.
The second image is always from a frame at which the position of marker isn't known
(next tracking frame). But a different first image
(instead of the one that immediately precedes the second image in the footage)
can be sent to the tracker. Most commonly used combinations:


- An image created from a frame on which the track was keyframed. This configuration prevents sliding from the original position (because the position which best corresponds to the original pattern is returned by the tracker), but it can lead to small jumps and can lead to failures when the feature point is deformed due to camera motion (perspective transformation, for example). Such a configuration is used if :strong:`Adjust Frames` is set to 0.


- An image created from the current frame is sent as first image to the tracker. In this configuration the pattern is tracking between two neighboring frames. It allows dealing with cases of large transformations of the feature point but can lead to sliding from the original position, so it should be controlled. Such a configuration is used if :strong:`Adjust Frames` is set to 1.

If :strong:`Adjust Frames` is greater than 1, the behavior of tracker is:
keyframes for tracks are creating every :strong:`Adjust Frames` frames,
and tracking between keyframed image and next image is used.

:strong:`Speed` can be used to control the speed of sequence tracking. This option doesn't affect the quality of tracking; it just helps to control if tracking happens accurately. In most  cases tracking happens much faster than real time, and it's difficult to notice when a track began to slide out of position. In such cases :strong:`Speed` can be set to Double or Half to add some delay between tracking two frames, so slide-off would be noticed earlier and the tracking process can be cancelled to adjust positions of tracks.

:strong:`Frames Limit` controls how many frames can be tracked when the Track Sequence operator is called. So, each Track Sequence operation would track maximum :strong:`Frames Limit` frames. This also helps to notice slide-off of tracks and correct them.

:strong:`Margin` can be used disable tracks when they become too close to the image boundary. This slider sets "too close" in pixels.


KLT tracker options
*******************


The KLT tracker is the algorithm used by default.
It allows tracking most kinds of feature points and their motion.
It uses pyramid tracking which works in the following way. The algorithm tracks an image
larger than the defined pattern first to find the general direction of motion. Then it tracks
a slightly smaller image to refine the position from the first step and make the final
position more accurate. This iterates several times. The number of steps of such tracking is
equal to the :strong:`Pyramid Level` option and we tell that on first step tracking
happens for highest pyramid level. So Pyramid Level=1 is equal to pattern itself,
and each next level doubles tracking image by 2.

The search area should be larger than the highest pyramid level and the "free space" between
the search area and highest pyramid level defines how much the feature can move from one frame
to another and still be tracked.

Default settings should work in most general cases,
but sometimes the pyramid level should be changed. For example, when footage is blurry,
adding extra pyramid levels helps to track them.

This algorithm can fail in situations where a feature point is moving in one direction and the
texture around that feature point is moving in another direction.


SAD tracker options
*******************


On each step, the SAD tracker reviews the whole search area and finds the pattern on the
second image which is most like the pattern which is getting tracking.
This works pretty quickly, but can fail in several cases. For example, when there's another
feature point which looks like the tracking feature point in the search area. In this case,
SAD will tend to jump off track from one feature to another.

:strong:`Correlation` defines the threshold value for correlation between two patterns which is still considered successful tracking. 0 means there's no correlation at all, 1 means correlation is full.

There's one limitation: currently: it works for features of size 16x16 pixels only.


Marker Panel
++++++++++++


This panel contains numerical settings for marker position,
pattern and search area dimensions, and offset of anchor point from pattern center.
All sliders are self-explanatory.


Proxy / Timecode Panel
++++++++++++++++++++++


.. figure:: /images/Manual_movie_tracking_clip_editor_proxy_timecode_panel.jpg
   :width: 130px
   :figwidth: 130px

   Proxy / Timecode Panel in clip editor


This panel contains options used for image proxies and timecodes for movies.

Proxy allows displaying images with lower resolution in the clip editor. This can be helpful
in cases when tracking of 4K footage is happening on a machine with a small amount of RAM.

The first four options are used to define which resolutions of proxy images should be built.
Currently it's possible to build images 25%, 50%, 75% and 100% of the original image size.
Proxy size of 100% can be used for movies which contain broken frames which can't be decoded.

:strong:`Build Undistorted` means that the proxy builder also creates images from undistorted original images for the sizes set above. This helps provide faster playback of undistorted footage.

Generated proxy images are encoding using JPEG,
and the quality of the JPEG codec is controlled with the :strong:`Quality` slider.

By default, all generated proxy images are storing to the <path of original
footage>/BL_proxy/<clip name> folder,
but this location can be set by hand using the :strong:`Proxy Custom Directory` option.

:kbd:`Rebuild Proxy` will regenerate proxy images for all sizes set above and regenerate all timecodes which can be used later.

:strong:`Use Timecode Index` can (and better be used) for movie files. Basically, timecode makes frame search faster and more accurate. Depending on your camera and codec, different timecodes can give better result.

:strong:`Proxy Render Size` defines which proxy image resolution is used for display. If :strong:`Render Undistorted` is set, then images created from undistorted frames are used. If there's no generated proxies,  render size is set to "No proxy, full render", and render undistorted is enabled, undistortion will happen automatically on frame draw.


Tools available in reconstruction mode
______________________________________


.. figure:: /images/Manual_movie_tracking_clip_editor_2d_stabilization_panel.jpg
   :width: 130px
   :figwidth: 130px

   Proxy / 2D Stabilization Panel in clip editor


There's one extra panel which is available in reconstruction mode - 2D stabilization panel.

This panel is used to define data used for 2D stabilization of the shot.
Several options are available in this panel.

First of all is the list of tracks to be used to compensate for camera jumps, or location.
It works in the following way: it gets tracks from the list of tracks used for location
stabilization and finds the median point of all these tracks on the first frame.
On each frame, the algorithm makes this point have the same position in screen coordinates by
moving the whole frame. In some cases it's not necessary to fully compensate camera jumps and
:strong:`Location Influence` can be used in such cases.

The camera can also have rotated a bit, adding some tilt to the footage.
There's the :strong:`Stabilize Rotation` option to compensate for this tilt.
A single extra track needs to be set for this, and it works in the following way.
On first frame of the movie, this track is connected with the median point of the tracks from
list above and angle between horizon and this segment is ket constant through the whole
footage. The amount of rotation applied to the footage can be controlled by :strong:`Rotation
Influence`\ .

If the camera jumps a lot, there'll be noticeable black areas near image boundaries.
To get rid of these black holes, there's the :strong:`Autoscale` option,
which finds smallest scale factor which, when applied to the footage,
would eliminate all the black holes near the image boundaries.
There's an option to control the maximal scale factor, (\ :strong:`Maximal Scale`\ ),
and the amount of scale applied to the footage (\ :strong:`Scale Influence`\ ).