
Displaying and Saving Images
****************************

After you have adjusted your render settings,
in regards to :doc:`Quality </render/options>` and :doc:`Format </render/output>`,
you will need to actually render the image. Rendering still images is fairly simple.
:doc:`Rendering Animations </render/workflows/animations>` is a bit more complex and is covered in the next sections.

To render an image from the active camera, in the Render Panel, hit the big Image button.
By default the 3D view is replaced with the UV/Image Editor and the render appears.


Displaying Renders
==================

Renders are displayed in the Image Editor. You can set the way this is displayed to several
different options in the Display drop-down menu:

:guilabel:`Keep UI`
   The image is rendered to the Image Editor, but the UI remains the same.
   You will need to open the Image Editor manually to see the render result.
:guilabel:`New Window`
   A new floating window opens up, displaying the render.
:guilabel:`Image Editor`
   The 3D view is replaced with the Image Editor, showing the render.
:guilabel:`Full Screen`
   The Image editor replaces the UI, showing the render.

For each of these options,
pressing :kbd:`esc` will close the render view and return to the previous view.


Saving
======

Rendered images can be saved by clicking on the Image menu and using the save options.


Animation Playback
==================

The 'Play' button in the render panel will play back your rendered animation in a new window.

You can also drop images or movie files in a running animation player.
It will then restart the player with the new data.

Key Short-Cuts

- :kbd:`A` toggle frame skipping.
- :kbd:`P` toggle ping-pong.
- :kbd:`Enter` start playback (when paused).
- :kbd:`pad0` toggle looping.
- :kbd:`padperiod` manual frame stepping.
- :kbd:`left` step back one frame.
- :kbd:`right` step forward one frame.
- :kbd:`down` step back 10 frames.
- :kbd:`up` step forward 10 frames.
- :kbd:`shift-down` use backward playback.
- :kbd:`shift-up` use forward playback.
- :kbd:`shift` hold to show frame numbers.
- :kbd:`lmb` scrub in time.
- :kbd:`ctrl-plus` zoom in
- :kbd:`ctrl-minus` zoom out
- :kbd:`esc` quit
- :kbd:`pad1` 60 fps
- :kbd:`pad2` 50 fps
- :kbd:`pad3` 30 fps
- :kbd:`pad4` 25 fps
- :kbd:`shift-pad4` 24 fps
- :kbd:`pad5` 20 fps
- :kbd:`pad6` 15 fps
- :kbd:`pad7` 12 fps
- :kbd:`pad8` 10 fps
- :kbd:`pad9` 6 fps
- :kbd:`pad/` 5 fps
- :kbd:`minus` slow down playback.
- :kbd:`plus` speed up playback.


Display Options
===============

When a rendered image is displayed in the Image Editor,
several new menu items become available.

:guilabel:`Slot Menu`
   You can save successive renders into the render buffer by selecting a new slot before rendering. If an image has been rendered to a slot, it can be viewed by selecting that slot. Empty slots appear as blank grids in the image editor. Use the shortcut :kbd:`J` to cycle through saved renders and :kbd:`alt-J` to cycle backwards through the saved renders.

:guilabel:`Render Layer`
   If you are using :doc:`Render Layers </render/post_process/layers>`, use this menu to select which layer is displayed.

:guilabel:`Render Pass`
   If you are using :doc:`Render Passes </render/post_process/passes>`, use this menu to select which pass is displayed.

:guilabel:`Image Painting`
   This icon enables or disables Image Painting.

Display Mode
   The last four buttons set how the image is displayed.

   :guilabel:`RGB`
         Draw image as rendered, without alpha channel.
   :guilabel:`RGBA`
         Replaces transparent pixels with background checkerboard, denoting the alpha channel.
   :guilabel:`Alpha Channel`
         Displays a gray-scale image. White areas are opaque, black areas have a an alpha of 0.
   :guilabel:`Z Depth`
         Display the depth from the camera, from Clip Start to Clip End, as specified in the :doc:`Camera settings </render/camera/introduction>`.

:guilabel:`Curves Panel`
   The :guilabel:`Curves` Panel is available in the :guilabel:`Properties` Panel. You can use this to adjust the colors of the image.

