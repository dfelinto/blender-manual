..    TODO/Review: {{review}} .


The Window System
*****************

When you start Blender you should see a screen similar to this
(the splash screen in the center will change with new versions):


.. figure:: /images/Blender-262-main.jpg
   :width: 640px
   :figwidth: 640px

   Initial Blender screen


In the center of the window is the splash screen.
This gives quick and easy access to recently opened Blender files.
If you want to start work on a new file just click outside of the splash screen.
The splash screen will disappear revealing the default layout and cube.

Every window you see can be further broken down into separate areas (as described in the section on :doc:`arranging frames </interface/window_system/arranging_frames>`). The default scene is described below.


The default scene
=================

The default scene is separated into five windows and is loaded each time you start Blender or
a new file. The five windows are:

- The Info window (shaded red) at the top. The Info window is comprised solely of a header.
- A large 3D window (3D View) (shaded green).
- A Timeline window at the bottom (shaded purple).
- An Outliner window at the top right (shaded yellow).
- A Properties window (Buttons window) at the bottom right (shaded blue).

As an introduction we will cover a few of the basic elements.


.. figure:: /images/Interface_Window-System_Default-scene.jpg
   :width: 650px
   :figwidth: 650px

   Default Blender scene and Window arrangement


----


The Info Window (main menu)
---------------------------

.. figure:: /images/Interface_Window-System_Info-window-shaded.jpg
   :width: 640px
   :figwidth: 640px

   Info Window


The Info Window is found at the top of the Default Scene and has the following components:


- **Window/Editor Type Selector** : The red shaded area allows you to change the :doc:`Window/Editor Type </interface/window_types>`. This region is found on every Window.


- **Menu options** :  The dark blue shaded area provides access to the main menu options.


- **Current Screen (default is Default)** : The green shaded area allows you to select different :doc:`Screens </interface/screens>`. By default, Blender comes with several pre-configured :guilabel:`Screen` s for you to choose from.  If you need custom screen layouts, you can create and name them.


- **Current Scene** : The yellow shaded area allows you to select different :doc:`Scenes </interface/scenes>`. Having multiple Scenes allows you to work with separate virtual environments, with completely separate data, or with objects and/or mesh data linked between them. (In some 3D packages, each file contains one scene, while in Blender, one .blend file may contain several scenes.)


- **Current Engine** : The purple shaded area gives a list of available rendering and game engines.


- **Resource Information** : The aqua shaded area gives you information about Blender and system resources in use.  This region will tell you how much memory is being consumed based on the number of vertices, faces and objects in the selected scene, as well as totals of what resources are currently selected. This can help identify when you are reaching the limits of your hardware.


3D Window View
--------------

.. figure:: /images/Icon-library_3D-Window_3D-cursor.jpg

- **3D Cursor** : Can have multiple functions.  For example, it represents where new objects appear when they are first created,  or it can represent where the center of a rotation will be.


.. figure:: /images/Icon-library_3D-Window_3D-transform-manipulator.jpg
   :width: 50px
   :figwidth: 50px


- **3D Transform Manipulator** : Is a visual aid in transforming objects (grab/move, rotate and scale).  Objects can also be transformed using the keyboard shortcuts: (:kbd:`G` / :kbd:`R` / :kbd:`S`); :kbd:`ctrl-Space` will toggle the manipulator visibility.


- **Cube Mesh** : By default, a new installation of Blender will always start with a Cube :guilabel:`Mesh` sitting in the center of Global 3D space (in the picture above, it has been moved).  After a while, you will most likely want to change the "Default" settings; this is done by :doc:`configuring Blender </preferences>` as you would want it on startup and then saving it as the "Default" using :kbd:`ctrl-U` (:guilabel:`Save Default Settings`).


.. figure:: /images/Icon-library_3D-Window_light-lamp.jpg

- **Light (of type Lamp)** : By default, a new installation of Blender will always start with a :guilabel:`Light` source positioned somewhere close to the center of Global 3D space.


.. figure:: /images/Icon-library_3D-Window_camera.jpg
   :width: 50px
   :figwidth: 50px


- **Camera** : By default, a new installation of Blender will always start with a :guilabel:`Camera` positioned somewhere close to the center of Global 3D space and facing it.


3D Window Header
----------------

.. figure:: /images/Icon-library_3D-Window_header.jpg
   :width: 640px
   :figwidth: 640px

   3D Window Header


This is the header for the 3D window.  All windows in Blender have a header,
although in some cases they may be located at bottom of the window.

Read more about :doc:`Blender headers » </interface/window_system/headers>`


.. figure:: /images/Icon-library_3D-Window_Editor-type.jpg

- **Window/Editor Type Selector** : Allows you to change the :doc:`type of Window </interface/window_types>`. This option can be found in every window header.  For example, if you want to see the :guilabel:`Outliner` window you would click and select it.


.. figure:: /images/Icon-library_3D-Window_3D-transform-manipulator-options.jpg

- **3D Transform manipulator options** : Access to the :doc:`manipulator </3d_interaction/transform_control/manipulators>` widget is also possible by clicking the coordinate system icon on the toolbar.  The translation/rotation/scale manipulators can be displayed by clicking each of the three icons to the right of the coordinate system icon.  :kbd:`shift-lmb` -clicking an icon will add/remove each manipulator's visibility.


.. figure:: /images/Icon-library_3D-Window_header-viewport-shading.jpg

- **Viewport shading** : Blender renders the 3D window using `OpenGL <http://en.wikipedia.org/wiki/OpenGL>`__.  You can select the type of :doc:`Viewport shading </3d_interaction/navigating/3d_view_options#view_shading>` that takes place by clicking this button and selecting from a variety of shading styles including simple bounding boxes and complex textures.  It is recommended that you have a powerful graphics card if you are going to use the Textured style.


.. figure:: /images/Icon-library_3D-Window_header-layers.jpg

- **Layers** : Blender :doc:`Layers </3d_interaction/navigating/layers>` are provided to help distribute your objects into functional groups.  For example, one layer may contain a water object and another layer may contain trees, or one layer may contain cameras and lights. To de-clutter the view you can turn layers on and off.


Buttons (Properties) Window Header
----------------------------------

.. figure:: /images/Icon-library_Properties_header.jpg

   Properties Window Header


The  Properties window displays panels of functions.
Panels that contain similar functions are grouped, e.g.
all of the rendering options are grouped.
In the header of the Properties Windows is a row of buttons (called Context Buttons)
that allow you to select which group of panels are shown.
Some panels are only visible when particular Objects are selected.
Panels can be collapsed by use of the small arrow left of the panel title (e.g.
besides *Render*) and may be rearranged by dragging the top right corner.


Outliner Window
---------------

.. figure:: /images/Icon-library_Outliner-Window_header.jpg

   Outliner Window Header


This window lists all the objects in a scene and can be very useful when working with larger
scenes with lots of items.
You can choose what types of elements and how they are displayed in the header.


Timeline Window
---------------

.. figure:: /images/Icon-library_Timeline-Window_header.jpg
   :width: 640px
   :figwidth: 640px

   Timeline Window Header


This window gives a timeline, through which you can scrub with the :kbd:`lmb`.

