
********
Overlays
********

The Overlays popover configures the overlays that are displayed on top of images.
In the header, there is a button to turn off all overlays for the UV Editor.
This option also toggles the visibility of :doc:`/modeling/meshes/uv/workflows/udims` tile information.
The options that are visible in the pop-over depend on the UV Editor mode.

.. seealso::

   Additional :doc:`View Properties </editors/uv/sidebar>` can be configured in the Sidebar.


Guides
======

.. _bpy.types.SpaceImageOverlay.show_grid_background:

Grid
   Show the grid background and borders.

.. _bpy.types.SpaceUVEditor.show_grid_over_image:

Over Image
   Allows the grid overlay to be shown on top of the image rather than behind it.

.. _bpy.types.SpaceUVEditor.grid_shape_source:

Grid Shape Source
   How the size/subdivisions of grid cells are determined.

   :Dynamic: The grid subdivisions changes based on the zoom level.
   :Fixed: The grid subdivisions stays consistent based off the *Fixed Subdivisions* property.
   :Pixel: The grid aligns with pixels from image so each grid cell represents one pixel.

.. _bpy.types.SpaceUVEditor.custom_grid_subdivisions:

Fixed Subdivisions X, Y
   Displays a grid that does not depend on the zoom level to determine
   the number of subdivisions. 

   .. _bpy.types.SpaceUVEditor.custom_grid_subdivisions:

   The number of grid units in UV that make one UV unit can be set via the *Dynamic Grid Size*.

.. _bpy.types.SpaceUVEditor.tile_grid_shape:

Tiles X, Y
   The number of :doc:`UDIM </modeling/meshes/uv/workflows/udims>`
   tile grids to display in each cardinal direction.


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
