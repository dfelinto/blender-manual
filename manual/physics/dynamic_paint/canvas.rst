
Dynamic Paint Canvas
********************

Main Panel
==========

.. figure:: /images/GSoC-DynamicPaint-Guide-CanvasMain.jpg

   Canvas main panel


The first panel of canvas contains the list of Dynamic Paint surfaces.
These surfaces are basically layers of paint, that work independently from each other.
You can define individual settings for them and bake them separately.

If surface type/format allows previewing results in 3D-viewport,
an eye icon is visible to toggle preview.

The checkbox toggles whether surface is active at all. If not selected,
no calculations or previews are done.

You can also give each surface an unique name to easily identify them.


Below you can set surface type and adjust quality and timing settings.

Each surface has a certain format and type.
Format determines how data is stored and outputted. Currently there are two formats available:


- Image Sequences. Dynamic Paint generates UV wrapped image files of defined resolution as output.
- Vertex. Dynamic Paint operates directly on mesh vertex data.
  Results are stored by point cache and can be displayed in viewports.
  However, using vertex level also requires a highly subdivided mesh to work.

From quality settings you can adjust image resolution (for image sequences) and anti-aliasing.

Then you can define surface processing start and end frame, and number of used sub-steps.
Sub-steps are extra samples between frames, usually required when there is a very fast brush.


Advanced Panel
==============

.. figure:: /images/GSoC-DynamicPaint-Guide-CanvasAdvanced.jpg

   Canvas advanced panel


From "Advanced" panel you can adjust surface type and related settings.

Each surface has a "type" that defines what surface is used for. Available types are:

- Paint
- Displace
- Waves
- Weight


Common options
--------------

For each surface type there are special settings to adjust.
Most types have the settings *Dissolve* and *Brush* :

Dissolve
   used to make the surface smoothly return to its original state during a defined time period

Brush Group
   used to define a specific object group to pick brush objects from


Paint
-----

.. figure:: /images/DynamicPaint-Guide-PaintSurface.jpg
   :width: 360px
   :figwidth: 360px

   Paint Surface


"Paint" is the basic surface type that outputs color and wetness values.
In case of vertex surfaces results are outputted as vertex colors.

Wetmap is a black-and-white output that visualizes paint wetness. White being maximum wetness,
black being completely dry. It is usually used as mask for rendering.
Some "paint effects" affect wet paint only.


Displace
--------

.. figure:: /images/DynamicPaint-Guide-DisplaceSurface.jpg
   :width: 360px
   :figwidth: 360px

   Displace Surface


This type of surface outputs intersection depth from brush objects.


.. tip::

   If the displace output seems too rough it usually helps to add a "Smooth"
   modifier after Dynamic Paint in the modifier stack.


Waves
-----

.. figure:: /images/DynamicPaint-Guide-WavesSurface.jpg
   :width: 360px
   :figwidth: 360px

   Waves Surface


This surface type produces simulated wave motion. Like displace,
wave surface also uses brush intersection depth to define brush strength.

You can use following settings to adjust the motion:

Open Borders
   Allows waves to pass through mesh "edges" instead of reflecting from them.

Timescale
   Directly adjusts simulation speed without affecting simulation outcome.
   Lower values make simulation go slower and otherwise.

Speed
   Affects how fast waves travel on the surface.
   This setting is also corresponds to the size of the simulation.
   Half the speed equals surface double as large.

Damping
   Reduces the wave strength over time. Basically adjusts how fast wave disappears.

Spring
   Adjusts the force that pulls water back to "zero level".


.. tip::

   In some cases the wave motion gets very unstable around brush.
   It usually helps to reduce wave speed, brush "wave factor" or even the resolution of mesh/surface.


Weight
------

.. figure:: /images/DynamicPaint-Guide-WeightSurface.jpg
   :width: 360px
   :figwidth: 360px

   Weight Surface


This is a special surface type only available for vertex format.
It outputs vertex weight groups that can be used by other Blender modifiers and tools.


.. tip::

   It's usually preferred to use "proximity" based brushes for
   weight surfaces to allow smooth falloff between weight values.


Output Panel
============

.. figure:: /images/GSoC-DynamicPaint-Guide-CanvasOutput.jpg

   Canvas output panel


From "Output" panel you can adjust how surface outputs its results.

For "Vertex" format surfaces, you can select a mesh data layer
(color / weight depending on surface type) to generate results to.
You can use the "+"/"-" icons to add/remove a data layers of given name.
If layer with given name isn't found, it's shown as red.

For "Image Sequence" surfaces,
you can define used "UV Layer" and output file saving directory, filenames and image format.


Effects Panel
=============

.. figure:: /images/GSoC-DynamicPaint-Guide-CanvasEffects.jpg

   Canvas effects panel


This is a special feature for "Paint" type surface.
It generates animated movement on canvas surface.

Currently there are 3 effects available:

Spread
   Paint slowly spreads to surrounding points eventually filling all connected areas.
Drip
   Paint moves in specific direction specified by Blender force fields,
   gravity and velocity with user defined influences.
Shrink
   Painted area slowly shrinks until disappears completely.

For spread and drip effects, only "wet paint" is affected, so as the paint dries,
movement becomes slower until it stops.


Cache Panel
===========

.. figure:: /images/GSoC-DynamicPaint-Guide-CanvasCache.jpg

   Canvas cache panel


This panel is currently only visible for "vertex" format surfaces.
You can use it to adjust and bake point cache.

