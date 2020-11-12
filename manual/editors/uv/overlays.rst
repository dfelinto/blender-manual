
********
Overlays
********

The Overlays pop-over configures the overlays that are displayed on top of images.
In the header, there is a button to turn off all overlays for the UV Editor.
This option also toggles the visibility of :doc:`/modeling/meshes/uv/workflows/udims` tile information.
The options that are visible in the pop-over depend on the UV Editor mode.


UV Editing
==========

Display Stretch
   Shows how much of a difference there is between UV coordinates and 3D coordinates.
   Blue means low distortion, while Red means high distortion.
   Choose to display the distortion of *Angles* or the *Area*.


Geometry
========

.. _bpy.types.SpaceUVEditor.uv_opacity:

UV Opacity
   Opacity of the above UV overlays.

Display As
   Controls how edges are shown.

   Outline
      Display white edges with black outline.
   Dash
      Display dashed black-white edges.
   Black
      Display black edges.
   White
      Display white edges.

Modified Edges
   Show results of modifiers in the UV display.

Faces
   Display faces over the image.


Image
=====

Show Metadata
   Displays the metadata if they were set in the render tab's :doc:`/render/output/metadata` panel.
