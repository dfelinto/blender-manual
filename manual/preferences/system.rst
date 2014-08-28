
FIXME(Template Unsupported: Doc:2.5/Manual/Interface/Configuration/index;
{{Doc:2.5/Manual/Interface/Configuration/index}}
)


System preferences
******************

This picture shows the :guilabel:`System` tab in the :guilabel:`User Preferences` editor in
Blender. Options are explained below.


.. figure:: /images/(Doc_26x_Manual_Preferences_System)_(Screenshot_Full)_(GBV266FN).jpg
   :width: 650px
   :figwidth: 650px


General
=======

:guilabel:`DPI`
   Value of the screen resolution which controls the size of Blender's interface fonts and internal icons shown.
   Useful for taking screen shots for book printing and use of high resolution monitors,
   (such as Retina Display and others) matching the screen DPI with Blender DPI.
   During normal usage, most Blender users might prefer to zoom screen elements
   pressing :kbd:`ctrl` and dragging :kbd:`mmb` left and right over a panel to resize its contents,
   or use the :kbd:`Numpad-+` and :kbd:`Numpad--` to zoom in and out the contents.
   Pressing :kbd:`home` (Show All) will reset the zooming at the screen/panel focused by the mouse pointer.
   Minimum: **48** , Maximum: **128** , Default:\ **72**
:guilabel:`Frame Server Port`
   TCP/IP port used in conjunction with the IP Address of the machine for frameserver rendering.
   Used when working with distributed rendering.
   Avoid changing this port value unless it is conflicting with already
   existing service ports used by your Operating System and/or softwares.
   Always consult your operating system documentation and services or
   consult your system administrator before changing this value.
   Minimum: **0** , Maximum: **32727** , Default: **8080**
:guilabel:`Console Scrollback`
   The number of lines, buffered in memory of the console window.
   Useful for debugging purposes and command line rendering.
   Minimum: **32** , Maximum: **32768** , Default: **256**


Sound
=====

:guilabel:`Sound`
   Set the audio output device or no audio support. There are 3 Options:


   :guilabel:`None`
      No Audio support (no audio output, audio strips can be loaded normally)
   :guilabel:`SDL`
      Uses Simple Direct Media Layer API from `libsdl.org <http://www.libsdl.org>`__ to render sounds directly
      to the sound device output. Very useful for sequencer strips editing.
   :guilabel:`OpenAL`
      Uses OpenAL soft API for Linux and OpenAL from creative Labs for Windows.
      This API provides buffered sound rendering with 3D/spatial support. Useful for the BGE Games.

:guilabel:`'Specific sound options'` (With :guilabel:`SDL` or :guilabel:`OpenAL` enabled)



   :guilabel:`Channels`
      Set the audio channel count. Available options are:
      *Stereo* (Default) , :guilabel:`4 Channels` , :guilabel:`5.1 Surround` , :guilabel:`7.1 Surround`
   :guilabel:`Mixing Buffer`
      Set the number of samples used by the audio mixing buffer. Available options are:
       :guilabel:`512` , :guilabel:`1024` , *2048* (Default), :guilabel:`4096` , :guilabel:`8192`, :guilabel:`16384`, and :guilabel:`32768`
   :guilabel:`Sample Rate`
      Set the audio sample rate. Available options are:
      *44.1 Khz* (Default), :guilabel:`48 Khs` , :guilabel:`96 Khz` and :guilabel:`192Khz`
   :guilabel:`Sample Format`
      Set the audio sample format. Available options are:
      *32 bit float* (Default),  :guilabel:`8 bit Unsigned` , :guilabel:`16 Bits Signed` , :guilabel:`24 Bits Signed` , :guilabel:`32 Bits Signed` , :guilabel:`32 Bits Float` and :guilabel:`64 Bits Float`


Screencast
==========

TODO


Compute Device
==============

:guilabel:`The Options here will set the compute device used by the Cycles Render Engine`


   :guilabel:`None`
      When set to :guilabel:`None` or the only option is :guilabel:`None`:
      your CPU will be used as a computing device for Cycles Render Engine


   When there are other Options for compute device such as:

   :guilabel:`CUDA` / :guilabel:`OpenCL`:sup:`1`.
      If the system has a compatible CUDA enabled graphics card and appropriate device drivers installed.
      When one or both of the options are available,
      the user will be able to choose whether to use CPU or other computing device for Cycles Rendering.


:guilabel:`OpenCL''`:sup:`1`  is unsupported, see: :doc:`Cycles </render/cycles>` Render engine page


Open GL
=======

:guilabel:`Clip Alpha`
   Clip alpha below this threshold in the 3D viewport.
   Minimum: **0.000** (No Clip) , Maximum: **1.000** , Default **0.000** (No Clip)
:guilabel:`Mipmaps`
   Scale textures for 3D view using mipmap filtering. This increases display quality, but uses more memory.


:guilabel:`GPU MipMap Generation`
   Generate MipMaps on the GPU. Offloads the CPU Mimpap generation to the GPU.


:guilabel:`16 Bit Float Textures`
   Enables the use of 16 Bit per component Texture Images (Floating point Images).
:guilabel:`Anisotropic Filtering`
   Set the level of anisotropic filtering. Available Options are:
   :guilabel:`Off'' (No Filtering)` , 2x (Default) , :guilabel:`4x` , :guilabel:`8x` , :guilabel:`16x`
:guilabel:`VBOs`
   Use Vertex Buffer Objects, or vertex arrays if unsupported, for viewport rendering.
   Helps to speed up viewport rendering by allowing vertex array data to be stored in Graphics card memory.


Window Draw Method
==================

:guilabel:`Window Draw Method`
   Specifies the Window Draw Method used to display Blender Window(s).


   *Automatic* (Default)
      Automatically set based on graphics card and driver.


   :guilabel:`Triple Buffer`
      Use a third buffer for minimal redraws at the cost of more memory.
      If you have a capable GPU, this is the best and faster method of redraw.


   :guilabel:`Overlap`
      Redraw all overlapping regions. Minimal memory usage, but more redraws.
      Recommended for some graphics cards and drivers combinations.


   :guilabel:`Overlap Flip`
      Redraw all overlapping regions. Minimal memory usage, but more redraws (for graphics drivers that do flipping).
      Recommended for some graphic cards and drivers combinations.


   :guilabel:`Full`
      Do a full redraw each time. Only use for reference, or when all else fails.
      Useful for certain cards with bad to no OpenGL acceleration at all.

:guilabel:`Region Overlap`
   This checkbox will enable Blender to draw regions overlapping the 3D Window.
   It means that the Object Tools and Transform Properties Tab,
   which are opened by using the shortcuts :kbd:`t` and :kbd:`n` will be drawn overlapping the 3D View Window.


   If you have a capable graphics card and drivers with :guilabel:`Triple Buffer` support,
   clicking the checkbox will enable the overlapping regions to be drawn using the :guilabel:`Triple Buffer` method,
   which will also enable them to be drawn using Alpha, showing the 3D View contents trough the
   Object Tools and Transform Properties Tab.


Text Draw Options
=================

:guilabel:`Text Draw Options`
   Enable interface text anti-aliasing.
   When disabled, texts are drawn using text straight render (Filling only absolute Pixels).
   Default: Enabled.


Textures
========

:guilabel:`Limit Size`
   Limit the maximum resolution for pictures used in textured display to save memory.
   The limit options are specified in a square of pixels,
   (e.g.: the option 256 means a texture of 256x256 pixels)
   This is useful for game engineers, whereas the texture limit matches paging blocks of the textures in the target graphic card memory .
   Available Options are:
   *Off* (No limit - Default) , :guilabel:`128`, :guilabel:`256`, :guilabel:`512`, :guilabel:`1024`, :guilabel:`2048`, :guilabel:`4096`, :guilabel:`8192`.
:guilabel:`Time Out`
   Time since last access of a GL texture in seconds, after which it is freed. Set to 0 to keep textures allocated.
   Minimum: **0** , Maximum: **3600** , Default: **120**


:guilabel:`Collection Rate`
   Number of seconds between each run of the GL texture garbage collector.
   Minimum: **0** , Maximum: **3600** , Default: **120**


Sequencer/Clip Editor
=====================

:guilabel:`Prefetch Frames`
   Number of frames to render ahead during playback.
   Useful when the chosen video codec cannot sustain screen frame rates correctly using direct rendering from the disk to video.
   duting video playbacks or editing operations.
   Minimum: **0** , Maximum: **500** , Default: **0** (No prefecth)


:guilabel:`Memory Cache Limit`
   Upper limit of the sequencer's memory cache (megabytes).
   For optimum clip editor and sequencer performance, high values are recommended.
   Minimum: **0** (No cache) , Maximum: **1024** (1 Gigabyte) , Default: **128**


Solid OpenGL lights
===================

:guilabel:`Solid OpenGL Lights`
   :guilabel:`Solid OpenGL Lights`  are used to light the 3D Window,
   mostly during :guilabel:`Solid view`. Lighting is constant and position "world" based.
   There are three virtual light sources, also called OpenGL auxiliary lamps,
   used to illuminate 3D View scenes, which will not display in renders.


   The Lamp Icons allows the user to enable or disable OpenGL Lamps.
   At least one of the three auxiliary OpenGL Lamps must remain enabled for the 3D View.
   The lamps are equal, their difference is their positioning and colors.
   You can control the direction of the lamps, as well as their diffuse and specular colors. Available Options are:


   :guilabel:`Direction:`
      Clicking with :kbd:`lmb` in the sphere and dragging the mouse cursor
      let's the user change the direction of the lamp by rotating the sphere.
      The direction of the lamp will be the same as shown at the sphere surface.


   :guilabel:`Diffuse:`
      This is the constant color of the lamp.
      Clicking on the color widget, opens the color picker mini window and
      allows the user to change colors using the color picker.


   :guilabel:`Specular:`
      This is the highlight color of the lamp
      Clicking on the color widget, opens the color picker mini window and
      allows the user to change colors using the color picker.


Color Picker Type
=================

:guilabel:`Color Picker Type`
   Choose which type of color dialog you prefer - it will show when clicking :kbd:`lmb` on any color field.


   There are **4** types of color pickers available for Blender:
      :guilabel:`Circle` (Default), :guilabel:`Square (HS + V)` , :guilabel:`Square (SV + H)` and :guilabel:`Square (HV + S)`


      The color pickers are detailed at the :doc:`Buttons and Controls </interface/buttons_and_controls>` page.


Custom Weight Paint Range
=========================

:guilabel:`Custom Weight Paint Range`
   :guilabel:`Mesh skin weighting` is used to control how much a bone deforms the mesh of a character.
   To visualize and paint these weights, Blender uses a color ramp (from blue to green, and from yellow to red).
   Enabling the checkbox will enable an alternate map using a ramp starting with an empty range.
   Now you can create your custom map using the common color ramp options.
   For detailed information about how to use color ramps,
   see: to the :doc:`Buttons and Controls </interface/buttons_and_controls>` page.


International Fonts
===================

:guilabel:`International Fonts`
   Blender supports a wide range of languages,
   enabling this check box will enable Blender to support International Fonts.
   International fonts can be loaded for the User Interface and used instead of Blender default bundled font.


   This will also enable options for translating the User Interface
   through a list of languages and Tips for Blender tools which appears
   whenever the user hovers a mouse over Blender tools.


   Blender supports I18N for internationalization, for more information,
   see: :doc:`Internationalization </interface/internationalization>` page.
   For more Information on how to load International fonts,
   see: :doc:`Editing Texts </modeling/texts/editing>` page.

