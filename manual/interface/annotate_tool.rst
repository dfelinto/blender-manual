.. _bpy.types.ToolSettings.annotation:
.. _tool-annotate:

*************
Annotate Tool
*************

The annotation tool is available in multiple editors.
It can be used to add notes to e.g. 3D objects or node setups.

The annotation tool can be activated in the Toolbar on the left side.
It has a couple of sub-tools listed below.

Annotate
   Draw free-hand strokes in the main area.

Annotate Line
   Click and drag to create a line.
   Optionally, you can select the arrow style for the start and end of the line.

Annotate Polygon
   Click multiple times to create multiple connected lines.
   The current polygon is finished when :kbd:`Esc` is pressed.

   Style Start, End
      The decoration to use at the beginning or end of the line segment.
      This can be used for example to create arrows to point out specific details in a scene.

Annotate Eraser
   Click and drag to remove lines.
   The eraser has a *Radius* setting found in :menuselection:`Tool Settings --> Eraser`.


Settings
========

Common
------

There is a panel, :menuselection:`Sidebar --> View --> Annotations`,
in it multiple annotation layers can be managed.

Color
   Adjusts the color of existing and new strokes.

Placement
   Determines where the annotations are drawn.

   :3D Cursor:
      Draw annotations on an imaginary plane that goes through the :doc:`/editors/3dview/3d_cursor` and is aligned to your view.
   :View:
      Draw annotations in screen space rather than 3D space;
      meaning the annotations will stay on the same position in the screen,
      even when the view moves or rotates.
   :Surface:
      Draw annotations on the surface of the object under the mouse.
   :Image:
      Draw annotations in same space as the image/preview/nodes meaning as you zoom
      in or out the annotations stay the same size relative to the zoom factor.

Opacity
   Adjusts the opacity of existing and new strokes.

Thickness
   Adjusts the thickness of existing and new strokes.

Onion Skin
   Shows a ghosted image of strokes made in frames before and after the current frame.
   Onion skinning only works in the 3D Viewport and Sequencer.
   See the Grease Pencil documentation for an explanation of
   :doc:`Onion Skinning </grease_pencil/properties/onion_skinning>`.

Stabilize Stroke
   Helps to reduce jitter of the strokes while drawing by delaying and correcting the location of points.

   Radius
      Minimum distance from the last point before the stroke continues.
   Factor
      A smooth factor, where higher values result in smoother strokes
      but the drawing sensation feels like as if you were pulling the stroke.


2D Editors
----------

When the annotation tool is enabled, the settings for managing multiple layers
can be found in the :menuselection:`Tool --> Active Tool` panel in the right Sidebar.

.. figure:: /images/interface_annotate-tool_node-editor.png
   :align: center

   Annotations tool in a node editor.
