


Render Layers
=============

Render layers are used to separate your composite image into layers.
Use Render Layers for a specific reason - such as creating depth of field,
relighting isolated elements within the image via a normal pass,
adding a colorcast to specific portions of the image, etc. The keyword here is isolation.
Render layers allow you to dissect, effect and/or correct individual elements or groups within
your composition before outputting your final render. This saves you from endlessly
re-rendering your scene just to find out whether a correction is going to work or not.


Render Layers in Compositing
----------------------------

What are Render Layers *really* used for?  Blender's node-based compositing system!

In Nodes, when you add an Input Node of type *RenderLayers,* and select the Scene,
you bring in whatever information you've specified for that RenderLayer.
This node becomes a source for the rendering pipeline products you've specified
*(see below)*\ , as applied to the objects in the qualifying layer(s).  Each of these products
then "flow out of" that node toward their appointed destinations in the node graph you've
constructed.


Layers or Passes?
-----------------

Blender's :doc:`Render Pass <render/post_process/passes>` system is a subset of Render Layers. Passes are specific to elements of shading properties, such as specular and diffuse, which can later be combined in compositing. Render Layers are more geared for separating scene components, but can include isolated passes as well.


Using Render Layers
===================

In Render buttons, open the Layers tab.
This is where you select the layers that you want to render,
and the settings for the upcoming render.


Enabling and Naming
-------------------

The list box contains the Render Layers that you have created, and options for disabling,
removing, adding, and renaming layers.

Note that the settings in the Layers tab are Render Layer specific.
Make sure that you have the appropriate Render Layer selected when changing settings.

The checkbox enables or disables the computation of the whole render layer.
Enable only those layers you are working with to save time.
The selector allows you to scroll through and examine existing render layers,
or to add a new one.


Creating a new Render Layer
---------------------------

By default, there is 1 Render Layer created for you, and it includes all layers,
whether they are used in your scene or not. To add yet another Render Layer,
click the yellow up-down selector and select Add New render layer.
You now have two Render Layers to choose from, and the active one is shown in the window.
Each Render Layer will have its own set of layers that are rendered (sort of makes sense now,
doesn't it?).

For example, you might have a robot in a scene with a ground object, buildings, etc.
If the robot is on visible-layer 5,
you can create one render layer named "Robot" with layer 5 selected in both the Scene:
and Layer: buttons.

You can create another render layer (maybe named "stuff")
that has all other layers EXCEPT layer 5 selected in both the Scene: and Layer: buttons. Then,
back in the Node Editor, you create TWO input nodes of type Render Layer:
one for the Robot Render Layer, and another for the other Stuff.
Run both through a mixer and out to the Composite viewer to get the big picture.


Scene Layers Settings
---------------------

There are three sets of scene layer buttons:
:guilabel:`Scene`
   These mirror the layer buttons in the 3d view header, and tell which scene layers are visible when rendering.
:guilabel:`Layer`
   Control which scene layers are included in the current Render Layer.
:guilabel:`Exclude`
   Exclude render layer so it will not influence to another layers.
:guilabel:`Mask Layers`
   The image rendered is from the objects that are between the selected layer(s) and the Z-mask layers. In the example, the cube is on layers 2 and 3, and the grass in on layer 1. In the render layer which we have arbitrarily chosen to call "zmask", as shown in the picture above, layer 1 is selected and layer 3 is designated as the Z-mask (as indicated by the black dot). Therefore, only that part of Layer 1 which is in front of the object on layer 3 (the cube) is rendered.

You can select that layer by :kbd:`Lmb`\ clicking the button. To select multiple layers,
:kbd:`shift-Lmb` click.  (The dot in the button in this case turns *dark gray.*\ )


 .. admonition:: Layer Sets AND each other
   :class: note

   Only the objects in layers that are selected BOTH in the main Scene Layer group AND the Render Layer Layer group will be rendered. So, if the Scene has only Layer 1 selected, and your Render Layer set specifies to render only Layers 2 and 3, nothing but the Sky (if selected) will be rendered.


Overrides
---------

The Light and Material selector boxes allow you to override materials and lights per layer,
applying them to all objects in the Render Layer.
:guilabel:`Light`
    Enter the name of a light group, and the scene will be lit with only those lights. Usually, you use this to speed up draft renders of a scene that has complicated lighting, by entering the name of a small group of key lights.
:guilabel:`Material`
    Overrides all material settings to use the name of the Material entered. Use this to speed up draft renders. Use the default material to check basic lighting.


Include Options
---------------

Each render layer has its own set of major products to include in the rendering pipeline.
To save time and give you control when working with passes,
this set of buttons allow you to select which major products to render:

:guilabel:`Z-mask`
   Only render what's in front of the solid z values.
   :guilabel:`Negate`
      Only render what's Behind the solid z values.
:guilabel:`AllZ`
   Z-values are computed for everything in view, not just those things that are rendered. When disabled, objects not included in the render have no ("infinite") z value.
:guilabel:`Solid`
   Solid faces are rendered. All normal meshes are solid faced.
:guilabel:`Halo`
   Halo materials are rendered.
:guilabel:`Z-transp`
   Transparency may be Z-based or Ray-traced. If Z-based, enabling *Ztra* renders transparent areas with the z-value of what is behind the transparent area.
:guilabel:`Sky`
   Turning on Sky renders the sky, as defined in your material world settings. Otherwise, a black alpha transparent background is rendered.
:guilabel:`Edge`
   If Edge is enable in the Output panel, objects in this Render Layer are given an outline edge. Turning on Edge pulls in the Edge settings from the Output tab, and adds an outline to the objects. Edges also have to be enabled on the Output tab.
:guilabel:`Strand`
    Strands are strings of static particles that are colored as part of the material settings; they look like strands of hair or grass.


Passes
------

Render Passes (Combined, Z, Vec, etc.) are discussed on :doc:`the next page <render/post_process/passes>`\ .


Examples
========


Rendering only certain objects
------------------------------

For example, suppose you have added a cool halo to your robot and you want to quickly see what
it looks like. Suppose your scene has boxes on layer 1, laser rifles on layer 2,
the robot on layer 5, and lights and camera on layer 20,
and they are all selected and visible in the 3d view. If you want to render just your robot,
and he is on layer 5, you click on the render layer 5 button
(which is below the Render Layer name), de-select sky
(so that the sky/horizon is not rendered) and select Halo. Presto! When you render,
only the robot is rendered (quickly) and not all the other elements of your scene
(like the boxes he is running in front of).


Outlining only selected objects
-------------------------------

To render an image where only one or two of the objects are outlined,
move those objects onto layer(s) separate from everything else.
Create Render Layer 1 for those layer(s)
by selecting only those layers in the Render Layer layer set.
Create Render Layer 2 for the other stuff. Enable the Edge option for Render Layer 1
(remember to also enable Edge on the Output tab) and make sure it is de-selected (off)
for Render Layer 2. In the Node Editor, create two input nodes, one for each Render Layer.
Mix the two images. Done. Simple. Yea.


