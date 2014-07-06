
Output Options
**************

The first step in the rendering process is to determine and set the output options.
This includes render size, frame rate, pixel aspect ratio, output location, and file type.


Dimensions
**********

:guilabel:`Resolution`
   The Dimensions section has settings for the size of the rendered images.
   By default the dimensions :guilabel:`SizeX` and :guilabel:`SizeY` are 1920×1080 and can be changed by adjusting the X and Y fields. These buttons control the overall size of the image.

   The :guilabel:`Percentage` slider will scale the currently set resolution by that value. This is useful for small test renders that are the same proportions as the final image.

:guilabel:`Aspect Ratio`
   Just below are two more settings, :guilabel:`AspX` and :guilabel:`AspY` which control the shape of the pixels along the respective axis. By default it is 1:1 since computer screen pixels are square. If television shorts are being made, and since TV pixels are not square, you want to change this aspect ratio to match the destination video standard: PAL for Europe, and NTSC for the Americas.

   See :doc:`Video Output <render/output/video>` for details on pixel aspect ratio.

:guilabel:`Border`
   You can render just a portion of the view instead of rendering the entire frame. While in Camera View, enable :guilabel:`Border` and press :kbd:`ctrl-B`, then drag a rectangle to define the area you want to render. :kbd:`ctrl-alt-B` is the shortcut to disable the border.
   Note that this disables the :guilabel:`Save Buffers` option in :guilabel:`Performance` and :guilabel:`Full Sample` option in :guilabel:`Anti-Aliasing`.

   Enabling :guilabel:`Crop` will crop the rendered image to the :guilabel:`Border` size, instead of rendering a black region around it.

:guilabel:`Frame Range`
   Set the :guilabel:`Start` and :guilabel:`End` frames for :doc:`Rendering Animations <render/animations>`. :guilabel:`Step` controls the number of frames to advance by for each frame in the timeline.

:guilabel:`Frame Rate`
   For an :doc:`Animation <render/animations>` the frame rate, or how many frames will be displayed per second, which, by default, is 24 frames per second, the standard for animation. Use 29.97 frames per second for USA television.

:guilabel:`Time Remapping`
   Use to remap the length of an animation.


Presets
=======

To make life easier the topmost menu provides some common presets (par = Pixel Aspect Ratio).
You can add your own or remove one with the + and - buttons:

+---------------------------+-----------------------------+
+:guilabel:`DVCPRO HD 1080p`|1280x1080, 3:2par 24fps      +
+---------------------------+-----------------------------+
+:guilabel:`DVCPRO HD 720p` |960x720 4:3par  24fps        +
+---------------------------+-----------------------------+
+:guilabel:`HDTV 1080p`     |1920×1080 square pixels 24fps+
+---------------------------+-----------------------------+
+:guilabel:`HDTV 720p`      |1280x720 square pixels 24fps +
+---------------------------+-----------------------------+
+:guilabel:`HDV 1080p`      |1440x1080 4:3par 23.98fps    +
+---------------------------+-----------------------------+
+:guilabel:`HDV NTSC 1080p` |1440x1080 4:3par 29.97fps    +
+---------------------------+-----------------------------+
+:guilabel:`HDV PAL 1080p`  |1440x1080 4:3par 25fps       +
+---------------------------+-----------------------------+
+:guilabel:`TV NTSC 16:9`   |720x480 4:3.3par 29.97fps    +
+---------------------------+-----------------------------+
+:guilabel:`NTSC 4:3`       |720×480 10:11par. 29.97fps   +
+---------------------------+-----------------------------+
+:guilabel:`PAL 16:9`       |720x576 16:11par 25fps       +
+---------------------------+-----------------------------+
+:guilabel:`PAL 4:3`        |720x576 12:11par 25fps       +
+---------------------------+-----------------------------+


These are just the presets; you can set any resolution you wish,
subject to your PC's memory restrictions;
see the Render page for ideas and techniques and tools for enabling huge render outputs.


Output Panel
************

This panel provides options for setting the location of rendered frames for animations,
and the quality of the saved images.


File Locations
==============

By default, each frame of an animation is saved in the /tmp directory. Change this or any
field by :kbd:`shift-Lmb` clicking in the name field and entering a new name.
If you use the // and do not save a new .blend file somewhere,
Blender assumes the // to refer to the Blender install folder.

Clicking the folder icon to the right of the field turns a Blender window pane into a File
Browser window. This window is very handy for scrolling through your hard disk and selecting a
file or directory.


.. admonition:: PathSpecs
   :class: note

   The path specification for the location can be absolute *On Microsoft-Windows include a normal or mapped drive letter (e.g. "F:")*, a breadcrumb notation (e.g. "./" and "../" and "//" (the blend file location). Forward slashes (Unix-style) or backslashes (Windows-style) are acceptable on either platform. If omitted, the file is saved in the current working directory blender was started from.


File Type
=========

Blender supports a wide mix of image formats. These formats are listed in alphabetical order.


The output format for Animations **Animation** :kbd:`ctrl-f12` is selected using the
:guilabel:`File Format` Menu. From here you can select many image or animation formats.
When rendering static images,
you can select the file type after you render when you save the image.

There are many image formats out there for many different uses.
A format stores an image in a *loss-less* or lossy format; with lossy formats you suffer
some image degradation but save disk space because the image is saved using fewer bytes.
A loss-less format preserves the image exactly, pixel for pixel.
You can break formats down into *static* images and movie *clips*.

Within either category there are standards (static formats and clip codecs)
which may be proprietary standards (developed and controlled by one company),
or open standards (which are community or consortium-controlled). Open standards generally
outlive any one particular company and will always be royalty-free and freely obtained by the
viewer. Proprietary formats may only work with a specific video card,
or while the codec may be free, the viewer may cost.


Compression
-----------

Some formats can compress the image to use less disk space.
This compression might be loss-less (PNG, ...) or lossy (Jpeg, ...).
Lossy formats don't store individual pixel information, thus reducing image quality.
All the other formats are more or less equivalent, each having advantages and disadvantages.
Make your compression selection using the button or field located beneath the format selector.
For example, if Jpeg is selected, you can specify a compression level (Quality:90 by default).
Higher quality takes more disk space,
but results in a better looking picture with less compression encoding artifacts.

The default image type is :guilabel:`Targa`, but,
since the image is stored in a buffer and then saved, it is possible to change the image file
type after the rendering and before saving using this menu. (**Attention** :
this is only valid for static images, not when rendering animations!).


Channels
--------

Blender renders color (:guilabel:`RGB`) images by default, but Black and White
(:guilabel:`BW`) and color with Alpha Channel (:guilabel:`RGBA`) are also possible.  Beware:
unless the Extensions button of the Output panel is set,
Blender does *not* automatically add extensions to filenames, hence any :guilabel:`.tga` or
:guilabel:`.png` extension must be explicitly written in the File Save window.

**OpenEXR** and **OpenEXR Multilayer** formats are the only formats that store Z-depth buffer information. **OpenEXR Multilayer** is the only format that stores Render Layer and Render Passes as layers that can then be composited in post-production.


Image Formats
-------------

+-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+:guilabel:`BMP`                |Bit-Mapped Paint loss-less format used by early paint programs.                                                                                                                                                                                                                                         +
+-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+:guilabel:`Iris`               |The standard Silicon Graphics Inc (SGI) format used on those spanking Unix OS machines.                                                                                                                                                                                                                 +
+-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+:guilabel:`PNG`                |Portable Network Graphics, a standard meant to replace old GIF inasmuch as it is loss-less, but supports full true color images. Supports Alpha channel.                                                                                                                                                +
+                               |    Enable the RGBA button to save the Alpha channel.                                                                                                                                                                                                                                                   +
+-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+:guilabel:`Jpeg`               |Joint Picture Expert Group (name of the consortium which defined it), an open format that supports very good compression with little loss of quality. Only saves RGB values. Re-saving images results in more and more compression and loss of quality.                                                 +
+-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+:guilabel:`Jpeg 2000`          |Uses the Jpeg 2000 codec.                                                                                                                                                                                                                                                                               +
+-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+:guilabel:`TARGA and Targa raw`|Truevision Advanced Raster Graphics Adapter is a simple raster graphics format established in 1984 and used by the original IBM PCs. Supports Alpha Channel.                                                                                                                                            +
+                               |    Enable the RGBA button to save the Alpha channel.                                                                                                                                                                                                                                                   +
+-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+:guilabel:`Cineon`             |format produced by a Kodak Cineon camera and used in high-end graphics software and more directed toward digital film.                                                                                                                                                                                  +
+-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+:guilabel:`DPX`                |Digital Moving-Picture eXchange format; an open professional format (close to Cineon) that also contains metainformation about the picture; 16-bit uncompressed bitmap (huge file size). Used in preservation.                                                                                          +
+-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+:guilabel:`MultiLayer`         |an OpenEXR format that supports storing multiple layers of images together in one file. Each layer stores a render pass, such as shadow, specularity, color, etc. You can specify the encoding used to save the MultiLayer file using the codec selector (ZIP (loss-less) is shown and used by default).+
+-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+:guilabel:`OpenEXR`            |an open and non-proprietary extended and highly dynamic range (HDR) image format, saving both Alpha and Z-depth buffer information.                                                                                                                                                                     +
+                               |                                                                                                                                                                                                                                                                                                        +
+                               |   - Enable the *Half* button to use the 16-bit format; otherwise 32-bit floating point precision color depth will be used.                                                                                                                                                                             +
+                               |   - Enable the *Zbuf* button to save the Z-buffer (distance from camera) info.                                                                                                                                                                                                                         +
+                               |   - Choose a compression/decompression *CODEC* (ZIP by default) to save disk space.                                                                                                                                                                                                                    +
+                               |   - Enable the *RGBA* button to save the Alpha channel.                                                                                                                                                                                                                                                +
+                               |   - Because OpenEXR is so new and previews are generally not supported by Operating Systems, enable *Preview* to save a JPG image along with the EXR image so you can quickly and easily see what the basic image looks like.                                                                          +
+-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+:guilabel:`Radiance HDR`       |a High Dynamic Range image format that can store images in floating point (with light brighter than 1.0) - 32bits per channel.                                                                                                                                                                          +
+-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+:guilabel:`TIFF`               |Often used for teletype and facsimile (FAX) images.                                                                                                                                                                                                                                                     +
+-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+:guilabel:`Frame Server`       |This is an alternative output method that allows Blender to serve frames over a network, useful for using external video encoders where the frames would not fit uncompressed on disk. :doc:`documentation <render/output/frameserver>`                                                                 +
+-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


VSE Rendering
*************

Rendering to an Image Sequence
==============================

In many cases, cutting and re-arranging (editing)
a codec-encoded video strip will give you fits, because the encoding algorithm that is used
internally to reconstruct each image gets 'off' by a frame or two or three.
To work directly on the 'raw' frame set, a very common technique is to import your video as a
strip and render it out to series of individual frames,
where each frame is stored in its own image file (JPG most commonly).

To do so, Add→Movie and load your original video. Set your Format SizeX and SizeY
(either to match the original,
or different if you want to distort or upscale/downscale the video), set image type to JPEG,
adjust your Quality settings, and in the Anim panel set your End:
to the number of actual frames in the video strip. Click ANIMATION and a series of numbered
files will be output to the top filespec in the Output panel.

You can now delete the video strip, and Add→Image instead;
right click on the directory name to pull in all of the images, in sequence,
that are within that directory. Now, when you cut at frame 4321, for example,
the next frame of the second strip will *really* start with frame 4322.


Rendering to Video
==================

Ridiculously easy (when you learn where the buttons are):

- Add the sequence of images as described above.
- Set your Output file path and name to wherever you want to save the movie file (e.g. C:\My Documents\MyMovie) in the upper output box of the render buttons.
- Change your Format to a movie file format (AVI, MOV, FFMPEG) and CODEC.
- Set your framerate to match whatever framerate the sequence is to be played back in. Under the Anim/Playback buttons.
- Set your ANIM End: to the number of images in the sequence, and
- ANIM

The single movie file is created and saved;
the name is what you specified but with the starting frame and ending frame numbers appended
(e.g. MyMovie0000-0250.avi)


