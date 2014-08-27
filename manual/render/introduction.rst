
..    TODO/Review: {{review|partial=X|text=needs review and at least some img}} .


Render engines
**************

- Blender Internal
- :doc:`Cycles </render/cycles>`


Rendering
*********

Rendering is the final process of CG (short of post processing, of course)
and is the phase in which a 2D image corresponding to your 3D scene is finally created.
Rendering is a CPU-intensive process. You can render an image on your computer, or use a
render farm which is a network of PCs that each work on a different section of the image or on
different frames. This section provides a full explanation of the features in Blender related
to the process of producing your image or animation.

After you have set up the materials, textures, lighting, and the camera,
you can begin rendering. It is unlikely that you will get it right on the first render,
so be prepared to do many test renderings. This section describes the options and settings for
the rendering process that will result in the desired image quality.

Blender has in internal render engine that it uses. This is a fast renderer,
and can produce nice results if fine tuned.
There are several other external renderers that can be loaded,
which offer more advanced rendering tools.

We know that around the world, our users have PCs of widely varying power. Rendering is
*the* process in CG that can chew up CPU and disk space like there's no tomorrow.
Especially in corporate environments, it is easy to fill up terabyte servers by uploading ten
hour-long DV tapes and doing some editing. So there are lots of options to try to shoehorn a
big job into a small PC by providing you with multiple sets of options that chunk up the work
as best we can, while still preserving image integrity.

This page discusses the main options found on the Render panel,
and subsequent pages explain more.


Overview
========

The rendering of the current scene is performed by pressing the big :guilabel:`Image` button in the :guilabel:`Render` panel, or by pressing :kbd:`f12` (you can define how the rendered image is displayed on-screen in the :doc:`Render Output Options </render/output>`). See also the :doc:`Render Window </render/display>`.

A movie is produced by pressing the big :guilabel:`Animation` button. The result of a rendering is kept in a buffer and shown in its own window. It can be saved by pressing :kbd:`f3` or via the :guilabel:`File→Save Image` menu using the output option in the :guilabel:`Output` panel. Animations are saved according to the format specified, usually as a series of frames in the output directory. See :doc:`Output Options </render/output>` and :doc:`Animations </render/animations>`.

The image is rendered according to the dimensions defined in the :guilabel:`Dimensions` Panel.

Workflow
In general, the process for rendering is:

- Create all the objects in the scene
- :doc:`Light the scene </lighting>`
- :doc:`Position the Camera </render/camera>`
- Render a test image at 25% or so without oversampling or ray tracing etc., so that it is very fast and does not slow you down
- Set and adjust the materials/textures and lighting
- Iterate the above steps until satisfied with the quality level
- Render progressively higher-quality full-size images, making small refinements and using more compute time
- Save your images


Distributed Render Farm
=======================

There are several levels of CPU allocation that you can use to decrease overall render time by
applying more brainpower to the task.

First, if you have a multi-core CPU, you can increase the number of threads,
and Blender will use that number of CPUs to compute the render.

Second, if you have a local area network with available PCs,
you can split the work up by frames. For example, if you want to render a 200-frame animation,
and have 5 PCs of roughly equal processing power,
you can allocate PC#1 to produce frames 1-40, PC#2 to frames 41-80, and so on.
If one PC is slower than the others, simply allocate fewer frames to that PC.
To do LAN renders, map the folder containing the .blend file
(in which you should have packed your external data, like the textures, ...)
as a shareable drive. Start Blender on each PC and open the .blend file.
Change the Start and End frame counts on that PC, but do not save the .blend file.
Start Rendering. If you use relative paths for your output pathspec,
the rendered frames will be placed on the host PC.

Third, you can do WAN rendering,
which is where you email or fileshare or Verse-share the .blend file (with packed data!)
across the Internet, and use anyone's PC to perform some of the rendering.
They would in turn email you the finished frames as they are done.
If you have reliable friends, this is a way for you to work together.

Fourth, you can use a render farm service. These services, like BURP,
are run by an organization. You email them your file,
and then they distribute it out across their PCs for rendering.
BURP is mentioned because it is free, and is a service that uses fellow Blender users' PCs
with a BOINC-type of background processing.
Other services are paid subscriptions or pay-as-you-go services.


Render Workbench Integration
============================

.. figure:: /images/Manual-Render-Pipeline.jpg
   :width: 320px
   :figwidth: 320px


Blender has three independent rendering workbenches which flow the image processing in a
pipeline from one to the other in order:

- Rendering Engine
- :doc:`Compositor </composite_nodes>`
- :doc:`Sequencer </sequencer>`

You can use each one of these independently, or in a linked workflow. For example,
you can use the Sequencer by itself to do post-processing on a video stream.
You can use the Compositor by itself to perform some color adjustment on an image.
You can render the scene via the active Render Layer, and save that image directly,
with the scene image computed in accordance with the active render layer,
without using the Compositor or Sequencer.
These possibilities are shown in the top part of the image to the right.

You can also link scenes and renders in Blender as shown,
either directly or through intermediate file storage.
Each scene can have multiple render layers,
and each Render Layer is mixed inside the Compositor.
The active render layer is the render layer that is displayed and checked active.
If the displayed render layer is not checked active/enabled,
then the next checked render layer in the list is used to compute the image. The image is
displayed as the final render if :guilabel:`Compositing` and :guilabel:`Sequencer` are NOT
enabled.

If :guilabel:`Compositing` is enabled, the render layers are fed into the Compositor.
The nodes manipulate the image and send it to the Composite output, where it can be saved, or,
if *Do Sequence* is on, it is sent to the Sequencer.

If :guilabel:`Sequencer` is enabled, the result from the compositor
(if Do Composite is enabled) or the active Render layer (if Do Composite is not enabled)
is fed into the Scene strip in the Sequencer. There,
it is manipulated according to the VSE settings,
and finally delivered as the image for that scene.

Things get a little more complicated when a .blend file has multiple scenes,
for example Scene A and Scene B. In Scene B, if :guilabel:`Compositing` is enabled,
the Render Layer node in Scene B's compositor can pull in a Render Layer from Scene A.
Note that this image will not be the post-processed one.
If you want to pull in the composited and/or sequenced result from Scene A,
you will have to render Scene A out to a file using Scene A's compositor and/or sequencer,
and then use the Image input node in Scene B's compositor to pull it in.

The bottom part of the possibilities graphic shows the ultimate blender: post-processed images
and a dynamic component render layer from Scene A are mixed with two render layers from Scene
B in the compositor, then sequenced and finally saved for your viewing enjoyment.

These examples are only a small part of the possibilities in using Blender.
Please read on to learn about all the options,
and then exercise your creativity in developing your own unique workflow.


The Render Settings Panel
*************************

The Render tab contains all of the options for the internal render engine, or an external one,
if selected.


Render
======

Here you can activate the rendering process, by rendering a :doc:`Still Image </render/display>` or an :doc:`Animation </render/animations>`.

You can also select where the image is rendered to. This are described on the :doc:`Render Display </render/display>` page.


Layers
======

The Layers menu contains options for rendering in :doc:`Layers </render/post_process/layers>` and :doc:`Passes </render/post_process/passes>`


Dimensions
==========

This menu has settings for the size of the rendered images (see :doc:`Output Options </render/output>`), and options for rendering sequences (see :doc:`Animations </render/animations>`)).


Anti-Aliasing
=============

:doc:`Antialiasing </render/options/antialiasing>` is important for producing high quality renders that do not have "jaggies" or stair-stepped pixel artifacts.


Motion Blur
===========

:doc:`Motion Blur </render/post_process/motion_blur>` is an important effect in rendering moving images. It prevents the animation from appearing unrealistic and stuttery, as in stop-motion, where each frame is a perfect still image.


Shading
=======

These are options for controlling what shading effects are calculated in the render.
Deselecting them disables them.


- :doc:`Textures </textures>`
- :doc:`Shadows </lighting/shadows>`
- :doc:`Subsurface Scattering </materials/properties/subsurface_scattering>`
- :doc:`Environment Maps </textures/types/environment_maps>`
- :doc:`Ray Tracing <introduction_to_shading>`
- :doc:`Color Management </render/color_management>`

      Uses a linear workflow when enabled


- :doc:`Alpha </render/output>`

      Set how transparent pixels are rendered.


Output
======

Set where images are rendered to and what file type. See
:doc:`Output Options </render/output>`.


Performance
===========

Control the way the renderer performs with respect to the computer's memory and processor. See :doc:`Performance </render/performance>`.


Post Processing
===============

Control effects that are applied after the image has been rendered. If you are using the :doc:`Compositor <composite_nodes>` or :doc:`Sequencer <sequencer>`, you can tell Blender to process those effects instead of directly rendering the scene.

Fields are used when :doc:`Rendering for Video </render/output/video>`.

:doc:`Dithering </render/post_process>` is method of blurring pixels.

You can also enable :doc:`Edge Rendering </render/post_process>` to create sketch-like or toon-like effects.


Stamp
=====

:doc:`Stamping </render/post_process>` inserts text over the rendered images, as well as stamps meta-data into image formats that support it (PNG, JPEG and EXR).


Bake

----


:doc:`Render Baking </render/bake>` is a process that creates texture files that hold desired rendered effects, like lighting, shadows, or color information. This is useful for working with real-time graphics that benefit from not having to calculate shading when not necessary.


