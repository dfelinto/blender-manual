
*******
Sidebar
*******

Image Tab
=========

UV Vertex
---------

Transform Properties :doc:`Selecting UVs </modeling/meshes/uv/editing>`.


Image
-----

See :doc:`/editors/image/image_settings`.


UDIM Grid
---------

Allows you to control the grid size of :doc:`UDIM </modeling/meshes/uv/workflows/udims>` tiles.


Tool Tab
========

Shows the settings for the active tool.


View Tab
========

Display
-------

You can set the editors display options in this panel.

.. figure:: /images/editors_uv_sidebar_display-panel.png
   :align: right

   Display panel: With both an image and UVs selected.

Aspect Ratio
   Display Aspect for this image. Does not affect rendering.

Repeat Image
   Duplicate the image until it is repeated to fill the main view.

.. _bpy.types.SpaceUVEditor.show_pixel_coords:

Pixel Coordinates
   Display UV coordinates in pixels rather than from 0.0 to 1.0


2D Cursor
---------

Location X, Y
   Control 2D cursor location.


Annotations
-----------

Options for the :doc:`annotation tool </interface/annotate_tool>`.


.. _bpy.types.SpaceUVEditor.use_custom_grid:

Custom Grid
-----------

Displays a grid that does not depend on the zoom level to determine
the number of subdivisions. The Custom Grid is useful in combination with
:ref:`Absolute Grid Snap <bpy.types.ToolSettings.use_snap_uv_grid_absolute>`
to create precise incremental snapping.

.. _bpy.types.SpaceUVEditor.custom_grid_subdivisions:

Subdivisions
   The number of grid units in UV that make one UV unit.


.. (TODO add) images per type

Scopes
======

See :ref:`editors-image-scopes` in the Image Editor.
