
****************
Amaranth Toolset
****************

A collection of tools and settings to improve productivity.


Activation
==========

- Open Blender and go to Edit menu, Preferences, then Add-ons.
- Search for Amaranth, and activate the add-on.


3D View
=======

Set Camera Bounds as Render Border
----------------------------------

When in camera view, we can now set the border-render to be the same size of the camera,
so we don't render outside the view. Makes faster render preview.

Usage: Context menus (:kbd:`RMB`) when in Camera View.


Select Meshlights
-----------------

Select all the meshes that emit light.

Usage: On the header of the 3D View, top of the select menu.


Adjust Passepartout
-------------------

The passepartout value of local Cameras is now available via the context menu,
while in Camera view.

Usage: Context menus (:kbd:`RMB`) when in Camera View.


Scene, Cameras, and Meshlights Count
------------------------------------

Add the number of scenes, cameras, and light emitting meshes to the stats in the Status Bar.

Disabled by default as there has been reports of very minor slowdown on scenes with many hi-poly objects.
Never experienced myself but just in case.

Usage: Once enabled in the add-on preferences, it will appear in the Status Bar.


Wireframe Toggle
----------------

Enable or disable wireframe display on mesh objects. It even works on linked objects/scenes too, where this option is not accessible.

"Display" will enable the wireframe, while "Clear" will disable it.

Both using the following settings:

Draw All Edges
   Display edges even on coplanar faces

Subdvision Optimal Display
   Enable/Disable the "Optimal Display" option on Subdvision modifiers

Only Selected Objects
   Only apply to the selected objects, otherwise apply to all.

All Scenes
   Display wireframe on all the objects in all scenes.
   Handy when working with linked scenes, where it's impossible to access the Wireframe option from the UI.


Render
======

UI: Final Resolution
--------------------

Display a **Final Resolution** label with the size in pixels of your render.
It also displays the final size for border renders.

Usage: Find it in the 'Format' panel, Render properties.


Cycles: Set Samples Per
-----------------------

A quick way to see and set the number of render samples on each Scene or ViewLayer.

Usage: Find it in the Sampling panel, on Render properties.


Object ID for Collection Instances
----------------------------------

Override the Pass Index for all objects in the Collection.

In order for the Pass Index to be loaded on computers without Amaranth installed,
it will automatically create a text file (called AmaranthStartup.py) and save it inside the .blend,
this will auto-run on startup and set the Pass Index. Remember to have auto-run Python scripts on your Preferences.

Usage: Select an Instanced Collection and set a Pass Index (other than zero) and press "Apply Object ID to Duplis"
in the Relations panel in Object Properties.


Nodes Editor
============

Display Image Node in Image Editor
----------------------------------

A quick way to view an image assigned to an Image node.

Usage: Double-click an Image Node in the Nodes Editor (Compositor or Cycles), there must be at least 1 image editor available.


Node Templates: Vignette
------------------------

Add a set of nodes to create a vignette effect attached to the selected node.

Vignette
   Adjust the size and position of the vignette with the Ellipse Mask's X/Y and width, height values.

Usage: Find the templates in the Compositor's header, "Template" pulldown. Or hit :kbd:`W`.


Nodes: XYZ Sliders for Normal Node
----------------------------------

Tweak the Normal node more accurately by using these sliders.

Usage: Find it in the Properties panel, when selecting a Normal node.


Object / Material Indices Panel
-------------------------------

When working with ID Masks in the Nodes Editor, it's hard to follow track of which Objects/Materials have which Pass Index.

This adds a panel on the sidebar when an ID Mask node is selected. The active object is highlighted between [square brackets]

Usage: On the Nodes Editor's sidebar, when an ID Mask node is selected.


Shaders Extra Info
------------------

Display the name and type of the current object. It works on Materials and Lights.

Usage: Find it in the Node Editor's header.


Nodes Stats
-----------

Display the number of selected and total nodes on the compositor.

Usage: Find it in the Compositing Nodes Editor.


Nodes Simplify Panel
--------------------

Disable/Enable certain nodes at a time. Useful to quickly "simplify" compositing.

This feature is a work in progress, the main issue now is when switching many different kinds one after the other.

Experimental feature.

Usage: Find it in the Nodes Editor sidebar (:kbd:`N`).


Animation
=========

Jump N Frames
-------------

Press :kbd:`Shift+Up` or :kbd:`Shift+Down` to jump forward/backwards a custom number of frames.

Useful for example when animating at 12 frames per second, to be able to jump every 1 second with a shortcut.
Make sure to save the preferences so this value is stored and used in the future.

Usage: Find it in Preferences, Animation section, Timeline panel.


Current Frame Slider
--------------------

Currently the only way to change the current frame is to have a Timeline editor open, but sometimes you don't have one,
or you're fullscreen. This feature adds the `Current Frame` slider to the context menu.

Usage: Find it in the :kbd:`RMB` (context or :kbd:`W` in right-click select keymap) menu in Object mode or Pose mode,
click-drag sideways or click in the middle to set the frame manually.


Bone Motion Paths: Match Frame Range + Clear All Paths
------------------------------------------------------

Clear All Paths
   Simple operator to loop through all bones and clear their paths, useful when having hidden bones
   (otherwise you have to go through each one of them and clear manually)

Match Current Frame Range
   Set the current frame range as motion path range.


Scene
=====

Save & Reload File
------------------

When working with linked libraries, very often you need to save and load again to see the changes.

Note: Since this feature is meant to speed-up the save/reload process, there is no prompt on save.

Usage: Press :kbd:`Ctrl+Shift+W` or find it at the bottom of the File menu


Refresh Scene
-------------

Refresh the current scene, useful when working with libraries or drivers.

Usage: Press :kbd:`F5` or find it in the context menu :kbd:`W`


Debug
=====

List Missing Images
-------------------

Display a list of missing images (that is, images that can't be found) Under a collapsable list.

Display the image name and its path, if the image is coming from a linked .blend, display the path to it.

Clicking on the .blend library path (Blender icon) will open the file in a new Blender instance.

Usage: Find it in the Scene Debug panel, under Scene Properties.


List Missing Node Links
-----------------------

Operator to look for empty image nodes, or missing images in nodes.

The "List Missing Node Links" button will print:
* Node Groups that were linked but are now "Missing Datablock"
* Image Nodes pointing to a non-existent image
* Image Nodes that don't have any output connected

Additionally, it will print in the terminal a list of all the Materials that meet any of the missing cases above,
the object they belong to, and their path (if they're coming from a Library).

Usage: Find it in the Scene Debug panel, on Scene Properties.


List Empty Material Slots
-------------------------

Having empty material slots with no material assigned to it is rare, but can happen.
Sometimes because the material was linked and the link got lost.

The "List Empty Material Slots" button will print a list of all the objects that have empty material slots.

If the objects are linked, it will show a list of the libraries paths, click on them to open a new Blender instance with that library.

Usage: Find it in the Scene Debug panel, on Scene Properties.


List Cycles Material using X shader
-----------------------------------

Where X is any shader type you want. It will display (and print on console) a list of all the materials containing
the shader you specified above.

Good for finding out if there's any meshlight (Emission) material hidden somewhere,
or if there are many glossy shaders making things noisy.


Lighter's Corner
----------------

A list of all the lights in the scene, including meshlights (meshes that have a Material with Emission shader).

From this list it is possible to adjust Ray Visibility (Camera, Diffuse, Glossy, Shadow) and renderability.

Usage: Find it in the Lighter's Corner panel, on Scene Properties.


File Browser
============

Go to Current Blend's Folder
----------------------------

A quick way to go to the currently open blend's directory.


Libraries Bookmark
------------------

The "Libraries" panel in the File Browser displays the path to all the libraries linked to that .blend.
That way you can quickly go to the folders related to the file.

Usage: Find it in the **Libraries** panel in File Browser. Click on any path to go to that directory.


Timeline
========

Timeline Extra Info
-------------------

Display amount of frames left until Frame End, very handy especially when rendering an animation or OpenGL preview.

Display current/end time in `SMPTE <http://en.wikipedia.org/wiki/SMPTE_timecode>`_.

Usage: Find it in the Timeline Editor's header.


Modeling
========

Symmetry Tools
--------------

Two operators to help making a mesh symmetric.

Find Asymmetric
   Selects vertices whose position doesn't match the opposite side.

Make Symmetric
   Move selected vertices to match the position of those on the other side.

Usage: Search (:kbd:`Spacebar`) for **Find Asymmetric**, and **Make Symmetric** operators.


Miscellaneous
=============

Color Management Presets
------------------------

Save your Color Management options as presets, for easy re-use.

Store most options in the Color Management panel, such as the look and color settings. Storing curve points is not supported yet.

Usage: Find the presets selector on the top of the **Color Management** panel under Render Properties.


Instancing: Show Path of Libraries
----------------------------------

Display the library path of a linked Collection Instance. Click on the path to open that .blend file in a new Blender instance.

Usage: Find it in the **Instancing** panel, when a Collection Instance (linked) is active.


Sequencer: Display Image File Name
----------------------------------

When seeking through an image sequence, display the active strips' file name for the current frame, and its playhead (in square brackets).

Usage: Find it in the VSE header.


EXR Render: Warn when Z not connected
-------------------------------------

Display a warning label when exporting EXR, with Z Buffer enabled, but the Z input in the **Composite** node is not connected.

Usage: Find it in the Output panel, Render properties.

.. reference::

   :Category:  Interface
   :Description: A collection of tools and settings to improve productivity.
   :Location: Everywhere
   :File: amaranth folder
   :Author: Pablo Vazquez (pablovazquez)
   :Maintainer: Pablo Vazquez (pablovazquez)
   :License: GPL
   :Support Level: Community
   :Note: This add-on is bundled with Blender.
