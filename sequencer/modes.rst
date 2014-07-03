
..    TODO/Review: {{review|copy=X}} .


Sequence Display Modes
======================

By default, the VSE only displays the sequencer. Several options in the header bar allow you
change the editor to display the sequence in real time, and in various ways.

The second button will change the editor to display only the preview,
and the third button displays both the sequencer and the preview


the VSE workspace can show you different aspects of the composite result,
for the current frame:


- Image/Sequence: Colors (what you see)
- Chroma: Color hue and saturation
- Luma: Brightness/contrast
- Histogram: Levels of red, green, and blue


In the Chroma, Luma, and Image modes, a channel selector appears;
channel 0 is the result of compositing the strips with their special effects strips.
Channel 1 is what the current frame's image from the strip in channel 1 looks like
(channel 1 is at the bottom of the heap). The display of these modes is either the composite
(channel 0) or the frame from the strip (channels 1 through n).

Zoom the view of any of these workspaces by scrolling your middle mouse wheel.


Image Preview
-------------

In the upper window pane of the Sequence screen layout is another VSE window,
this one set to Image Preview mode.
It shows you what the resulting video will look like when saved.
This is the main working mode for adding strips and moving them around, cutting, grouping
(making meta) and splicing them through special effects.


Luma Waveform
-------------

For the selected channel, brightness, or luminosity, is mapped with this display.

A luma waveform allows you to judge the quality of the luminance distribution across your
video signal,
you can view a luma-waveform instead of the usual output display on every control monitor.

The display plots for every scanline the luminance value.
The lines are all drawn on top of each other. The points get brighter if the lines cross
(which is very likely with several hundred scanlines). You will understand the picture most
easily if you plug an oscilloscope to the Luma-video-output of your television set.
It will basically look the same.

In this mode, the vertical axis represents the luminosity: 0 at the bottom, 1 at the top;
the horizontal axis is a mapping from the horizontal axis of the frame.
There are as many curves as scanlines in the frame:
each one of this curves represents the luminosity of the pixels of one line. Moreover, the
color of a pixel in this mode represents the number of pixels from the matching column of the
frame sharing the same luminosity - i.e. the number of curves that cross at this point
(black/transparent, for no pixel, white/opaque for at least 3 pixels).

This mode is good for:


- If the waveform does not fill the whole picture you might want to play with the "setup" and "gain" master-sliders in the "gamma"-plugin until it fills the whole picture (contrast autostretch).
- With the more advanced gamma-plugin you can decide where you have to desaturate (especially in dark regions).
- You can judge if you want to dump the whole thing since it is completely distorted and clips at the top or the bottom.


+------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
+.. figure:: /images/Manual-VSE-Luma_waveform_ex1.jpg                                                                          |.. figure:: /images/Manual-VSE-Luma_waveform_ex2.jpg                             |Examples of :guilabel:`VSE` :guilabel:`Luma` Previews.                                                                                                +
+                                                                                                                              |                                                                                 |Note that the pictures (first green frame, at the top) are only 50px high, to limit the number of curves displayed in the :guilabel:`Luma waveform`\ !+
+   'Simple' picture.                                                                                                          |   A 'real' picture.                                                             |                                                                                                                                                      +
+   The various horizontal lines in the Luma waveform match the uniform-color lines of the picture.                            |   The curves are quite visible.                                                 |                                                                                                                                                      +
+   Note that the 'grey 20%' one-pixel width line (inside the yellow strip) is represented in the Luma waveform by a grey line.|   We found a luma of 80-100% for the sky,                                       |                                                                                                                                                      +
+   The two lines drawing an 'X' are from the two linear tone shades (white→black and black→white).                            |   a luma around 40% for the sea,                                                |                                                                                                                                                      +
+   Finally, the broken line matches the complex tone shade at the bottom of the picture.                                      |   and a luma of 10-20% for the mountains, growing around 40% for the sunny part.|                                                                                                                                                      +
+------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+


Use this display to check for appropriate contrast and luminosity across all frames in the
channel. When spots in the film that should have even illumination don't,
it looks like a flashbulb went off or an extra light was suddently turned on. This can happen
if two strips were rendered or shot under different lighting conditions but are supposed to be
contiguous.


Chroma Vectorscope
------------------


.. figure:: /images/Manual-VSE-ChromaExample.jpg
   :width: 300px
   :figwidth: 300px

   Example VSE Chroma Preview


Use this mode judge the quality of the color-distribution and saturation,
you can also view a U/V scatter-plot.

The picture is converted to YUV-format. The U- and V-values represent the angle of the color.
For pixel of the picture, one point is plotted in the display at the U and V-value-position.
If several pixels happen to have the same U/V-value the pixel in the plot gets brighter.

To help you understand what color is meant, a hexagram marking the extreme positions (red,
magenta, blue, cyan, green, yellow) is drawn and a red cross to mark the origin.

In other words, for the selected channel,
this display shows the color space of the image inside a hexagon.
Each point of the hexagon is a primary color: red, magenta, blue, cyan, green, and yellow.
Black is at the center, and overall saturation is scaled as dots  closer to the outside.
The example to the right shows that the image has a lot of red (50% saturation)
and small amount of blue, with no green.

Always: remember to activate an additional control monitor of the end result.
Color calibration is a matter of taste and depends on what you want.

Use this display to check for too much color saturation.
While over-saturated images look great for op-art and computer displays,
they stink when shown on the big screen TV.
Use the :guilabel:`Alt-A`\ nimation key to scrub the video;
this display will update with a new/revised map for each frame.
Just like watching the Image preview to see what it looks like,
watch the Chroma Vectorscope to watch for color use.


This mode is good for:


- If you picture looks very moody or desaturated you might want to take a look at the U/V-plot. You will most likely see all pixels building a crowd at the origin. If you add saturation using the "gamma"-plugin you can see in the U/V-plot if you distort the color.
- If you do color-matching on a by hand basis you can match the angle you see of different channels monitors.


Histogram
---------

This mode displays a graph showing the distribution of color information in the pixels of the
currently displayed image. The X-axis represents values of pixel, from 0 to 1 (or 0 to 255),
while the Y-axis represents the number of pixels in that tonal range. A predominantly dark
image would have most of its information toward the left side of the graph.

Use this mode to balance out the tonal range in an image.
A well balanced image should a nice smooth distribution of color values.


