Multi-View Render
*****************

Workflow
========
``To be written.``

Individual Parts
================

``The following sections will be moved to the corresponding individual sections later.``

Scene Views
===========

Views
  In the Render Layer panel you can enable support for Views and setup your Stereo 3D or Multi-View scene. The properties defined here will be used across the entire Blender file (compositor, viewport, image editor).

.. figure:: /images/Manual_multiview_scene.png
   :width: 484px
   :figwidth: 300px

   Scene Views Settings


Views Setup
-----------

Stereo 3D
  Single stereo camera system. This option transforms the active camera in a stereo pair to be controlled by the Stereoscopy settings in the camera property panel.

Multi-View
  Multi camera system. This is a more flexible system that allows for stereo 3d as well as other non-standard outputs such as fulldome and autostereo displays. The **left** and **right** views are considered a special case since they allow your scene to be previsualized as a regular Stereo 3D from the respective cameras.

Suffix
  When using 'Stereo 3D' the suffix is used when saving the images (e.g., ``0001_L.jpg``, ``0001_R.jpg``). When using 'Multi-View' the suffix is also used to identify a group of cameras to use for rendering.

.. note:: Multi-View Camera Suffix

  If you want to render a Left, Right and Center views you start by creating a *center* render view (the *left* and *right* are created by default). The new view is created with an empty suffix while the *left* and *right* have ``_L`` and ``_R`` as their default respective suffices.

  In this case create the following cameras: ``Camera.Wide_L``, ``Camera.Wide_R`` and ``Camera.Wide``. Blender will render and preview those cameras regardless of the actual active camera between them. Now create the cameras: ``Camera.Zoom_L``, ``Camera.Zoom_R``, ``Camera.Zoom``. You can alternate between the render cameras (Wide cameras or Zoom cameras) by simply setting one of them as the active camera. In fact if you use the *Bind Camera to Markers* tool in the Timeline you can change your render cameras during the rendering.

Window Stereo 3D Display
========================

An essential component of the Stereoscopy pipeline is the ability to display the stereo image in a proper display. Blender supports from high-end 3D displays to simple red-cyan glasses. On top of that you can set a different display mode for each window. The display mode can be changed via the Window menu or if you create your own shortcuts for the **wm.stereo_3d** operator.

.. figure:: /images/Manual_multiview_window_stereo_3d.png
   :width: 642px
   :figwidth: 642px

   Window Menu, Stereo 3D Operator

Display Mode
------------

Anaglyph
  Render two differently filtered colored images for each eye. Anaglyph glasses are required. We support Red-Cyan, Green-Magenta and Yellow-Blue glasses.


Interlace
  Render two images for each eye into one interlaced image. A 3D-ready monitor is requiered. We support Row, Column and Checkerboard Interleaved. An option to Swap Left/Right helps to adjust the image for the screen. This method works better in fullscreen.

Time Sequential
  Renders alternate eyes. This method is also known as Page Flip. This requires the graphic card to support Quad Buffer and it only works in fullscreen.

Side-by-Side
  Render images for left and right eye side-by-side. There is an option to support Cross-Eye glasses. It works only in fullscreen, and it should be used with the Full Editor operator.

Top-Bottom
  Render images for left and right eye one above another. It works only in fullscreen, and it should be used with the Full Editor operator.

.. note:: Full Screen Stereo 3D Modes

  If you have a 3D display most of the time you will use it to see in stereo 3D you will have to go to the fullscreen mode. In fact some modes will only work in the full window mode that hides most of the user interface from the work area. In this case it is recommended to work with two monitors, using the 3D screen for visualizing the stereo result while the other screen can be used for the regular Blender work.

Stereo 3D Camera
================

When using the Stereo 3D scene view setup a stereo pair is created on-the-fly and used for rendering and previsualization. For all the purposes the this works as two cameras that share most parameters (focal lenght, clipping, ...). The stereo pair, however, is ofsetted, and can have unique rotation and shift between itself.

.. figure:: /images/Manual_multiview_camera.png
   :width: 805px
   :figwidth: 402px

   Stereo 3D Camera Settings

Interocular Distance
  Set the distance between the camera pair. Although the convergence of a stereo pair can be changed in post-production, different interocular distances will produce different results due to the parts of the scene being occluded from each point of view.

Convergence Plane Distance
  The converge point for the stereo cameras. This is often the distance between a projector and the projection screen. You can visualize this in the 3D Viewport.

Convergence Mode
----------------

Off-Axis
  The stereo camera pair is separated by the interocular distance, and shifted inwards so it converges in the convergence plane. This is the ideal format since it is the one closest to how the human vision works.

Parallel
  This method produces two parallel cameras that do not converge. For the viewport stereo 3d preview a *Viewport Convergence Distance* is used. For rendering this is not considered though. This method is common when combining real footaged with rendered elements.

Toe-in
  A less common approach is to rotate the cameras instead of shifting their frustum. The Toe-in method is rarely used in modern 3D productions.

Pivot
  The stereo pair can be constructed around the active camera with a new camera built for each eye (Center Pivot) or using the existing camera and creating (Left or Right). The latter is what is used when only one eye needs to be rendered for an existing monoscopic project.

Viewport Stereo 3D
==================

When you enable 'Views' in the Render Layer panel a new are is available in the 3D Viewport properties panel. In this panel you can pick whether to see the stereo 3d in the viewport, or which camera to see. It also allow you to see the Cameras, the Plane and the Volume of the stereo cameras.

.. figure:: /images/Manual_multiview_viewport_settings.png
  :width: 407px
  :figwidth: 250px

  Viewport Stereo 3D Settings


Cameras
  When working with the Stereo 3D views setup you can inspect what each individual generated camera is looking or the combined result of them. In the Multi-View mode you can see the combined result of the left and right cameras (when available) or the current selected camera.

Plane
  The convergence plane represents the screen as it is perceived by the audience. Visualizing it in the 3D Viewport allows you to layout your scene based on your depth script outside the camera view.

Volume
  The intersection of the stereo cameras frustums helps planning the show by avoiding elements being visible by only one camera. The volume is defined by the cameras start and end clipping distances. The areas that are in the frustum of one camera only are known as **retinal rivalry areas**. They are tolerated in the negative space (the region from the convergence plane into the image) but are to be avoided at all costs in the positive space (the area from the convergence plane to the camera).

.. figure:: /images/Manual_multiview_volume.png
   :width: 538px
   :figwidth: 402px

   Viewport 3D: Convergence Plane and Volume Display

Image I/O
=========
``To be written.``
``Talk about equivalency of display modes and stereo 3d modes``
``Talk about destructive formats```
``Talk about OpenEXR```

- Views Format

  - Stereo 3D
  - Individual
  - Multi-View

Image Editor
============

View Menu
  After you render your scene with Stereo 3D you will be able to see the rendered result in the combined stereo 3d or to inspect the individual views. This works for Viewer nodes, render results or opened images.

.. figure:: /images/Manual_multiview_image_editor_header.png
   :width: 1225px
   :figwidth: 700px

   Stereo 3D and View menu

Views Format
  When you drag and drop an image into the Image Editor, Blender will open it as a individual images at first. If your image was saved with one of the Stereo 3D formats you can change how Blender should interpret the image by switch the mode to Stereo 3D and picking the corresponding stereo method.

.. figure:: /images/Manual_multiview_image_editor_stereo_3d.png
   :width: 494px
   :figwidth: 300px

   Views Formats and Stereo 3D

Compositor
==========
The compositor works smoothly with Multi-View. The compositing of a view is completed before the remaining views start to be composited. The pipeline is the same as the single-view workflow, with the difference that you can use Image, Movies or Image Sequences in any of the supported Multi-View formats.

The views to render are defined in the current scene views, in a similar way as you define the composite output resolution in the current scene render panel, regardless of the Image nodes resolutions or RenderLayers from different scenes.

.. note:: Single-View Images

  If the image from an Image Node does not have the view you are trying to render, the image will be treated as a single-view image.

.. figure:: /images/Manual_multiview_compositor.png
   :width: 1717px
   :figwidth: 700px

   Compositor, Backdrop and Split Viewer Node

Performance
  By default when compositing and rendering from the user interface all views are rendered and then composited. During test iterations you can disable all but one view from the Scene Views panel, and re-enable it after you get the final look.

Switch View Node
  If you need to treat the views separately you can use the Switch View node to combine the views before an output node.

.. figure:: /images/Manual_multiview_compositor_switch_view.png
   :width: 338px
   :figwidth: 200px

   Switch View Node

