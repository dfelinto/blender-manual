
********
Overlays
********

The Overlays pop-over configures the overlays that are displayed on top of images.
In the header, there is a button to turn off all overlays for the UV Editor.
This option also toggles the visibility of :doc:`/modeling/meshes/uv/workflows/udims` tile information.
The options that are visible in the pop-over depend on the UV Editor mode.

.. seealso::

   Addition :doc:`View Properties </editors/uv/sidebar>` can be configured in the sidebar.


UV Editing
==========

.. _bpy.types.SpaceUVEditor.display_stretch_type:
.. _bpy.types.SpaceUVEditor.show_stretch:

Display Stretch
   Shows how much of a difference there is between UV coordinates and 3D coordinates.
   Blue means low distortion, while Red means high distortion.
   Choose to display the distortion of *Angles* or the *Area*.


Geometry
========

.. _bpy.types.SpaceUVEditor.uv_opacity:

UV Opacity
   Opacity of the above UV overlays.

.. _bpy.types.SpaceUVEditor.edge_display_type:

Display As
   Controls how edges are shown.

   :Outline: Display white edges with black outline.
   :Dash: Display dashed black-white edges.
   :Black: Display black edges.
   :White: Display white edges.

.. _bpy.types.SpaceUVEditor.show_modified_edges:

Modified Edges
   Show results of modifiers in the UV display.

.. _bpy.types.SpaceUVEditor.show_faces:

Faces
   Display faces over the image.


Image
=====

Show Metadata
   Displays the metadata if they were set in the render tab's :doc:`/render/output/properties/metadata` panel.
