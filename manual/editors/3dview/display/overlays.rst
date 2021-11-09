.. _bpy.types.View3DOverlay:

*****************
Viewport Overlays
*****************

Using the Viewport Overlays pop-over settings for the overlays can be configured.
There is a switch to turn off all overlays for the 3D Viewport.

The options that are visible in the pop-over depend on the mode that the 3D Viewport is in.


Object Mode
===========

The next options are always present, independent the current mode.


Guides
------

Grid
   Show grid in orthographic side view.
Floor
   Show the ground plane.
Axis
   Show the X, Y and/or Z axis line.

Scale
   The distance between lines in the grid/floor.
Subdivision
   The number of subdivisions between grid lines.

Text Info
   Shows information such as the :doc:`View Perspective </editors/3dview/navigate/projections>`,
   playback :abbr:`FPS (Frames Per Second)`, current frame number,
   and the name of the active :doc:`Collection </scene_layout/collections/index>` and Object.

Statistics
   Show information about the amount of objects and geometry.
   Note the counters that are displayed depends on the current selection.
   For example selecting a mesh gives info on the number of vertices, edges, and faces,
   while selecting other object such as lights shows a count of the lights in the scene.

   - Objects -- Number of the selected objects and the total count.
   - Geometry -- Displays information about the current scene depending on the mode and object type.
     This can be the number of vertices, faces, triangles, or bones.

HDRI Preview
   Show two spheres, one glossy and one diffuse,
   to preview HDRIs used in *Material Preview* and *Rendered* shading modes.
3D Cursor
   Show the 3D Cursor overlay.
Annotations
   Show the annotation overlay.


Objects
-------

Extra
   Show details of objects including empty wires, cameras and other visual guides.
Relationship Lines
   Show dashed lines indicating parents or constraint relationships.
Outline Selected
   Show an outline highlight around selected objects.
Bones
   Show Bones. Disable to only show their motion path.
Motion Paths
   Show the motion path overlay.
Origin
   Show the object origin of the active object.
Origin (All)
   Show the object origin of all objects.


Geometry
--------

.. _bpy.types.View3DOverlay.wireframe_threshold:
.. _bpy.types.View3DOverlay.show_wireframes:

Wireframe
   Displays the mesh's face edges, similar to :ref:`Wireframe Shading <3dview-shading-rendered>`
   but displays edges on top of existing shading.
   The value slider adjusts which edges to display by only showing wires on prominent edges.
   Lower values hide edges with angles close to 180 degrees while a value of 1 shows all wires.

   .. _bpy.types.View3DOverlay.wireframe_opacity:

   Opacity
      The transparency of the displayed edges; a value of 1 is fully opaque, a value of 0 is fully transparent.

.. _bpy.types.View3DOverlay.fade_inactive_alpha:
.. _bpy.types.View3DOverlay.show_fade_inactive:

Fade Inactive Geometry
   Fade inactive geometry using the viewport background color.
   The value slider controls the factor of the objects are blended with the background.

.. _bpy.types.View3DOverlay.show_face_orientation:

Face Orientation
   Show the face orientation overlay. In the face orientation overlay
   all faces where the face normal points towards the camera are colored blue.
   All faces where the face normal points away from the camera are colored red.
   With this overlay, it is easy to detect the orientation of the face normals.


.. _bpy.types.SpaceView3D.show_reconstruction:

Motion Tracking
---------------

Show the motion tracking overlay.

Camera Path
   Show the reconstruction camera path.
Marker Names
   Show the names for reconstructed track objects.

Tracks
   Change the display of the reconstructed tracks.

   - Plain Axes
   - Arrows
   - Single Arrow
   - Circle
   - Cube
   - Sphere
   - Cone

Size
   Change the display size of the reconstructed tracks.


.. _3dview-overlay-mesh_edit_mode:

Mesh Edit Mode
==============

The next options are available when in Edit Mesh Mode.

Edges
   Highlighted selected and partially selected edges.

   *Only affects vertex and face select mode (as edges are always highlighted in edge select mode).*
Faces
   Highlight faces using a face overlay that applies to both selected and unselected faces.

   *Affects all selection modes.*
Center
   Show face center points in solid shading modes.

   *Only affects face select mode.*
Creases
   Display edges marked with a crease
   for the :doc:`Subdivision Surface Modifier </modeling/modifiers/generate/subdivision_surface>`.
Sharp
   Display sharp edges, used with the Edge Split modifier.
Bevel
   Display weights created for the :doc:`Bevel Modifier </modeling/modifiers/generate/bevel>`.
Seams
   Display the UV unwrapping seams.
Edge Marks and Face Marks
   Used by Freestyle.


Shading
-------

Hidden Wire
   Show only front-facing wireframes.
   This is useful for a retopology workflow.

   .. tip::

      Optimally this could be combined with the *X-Ray* display setting.

Vertex Groups Weights
   Display weights in Edit Mode.

   Zero Weights
      To display unreferenced and zero weighted areas in black.
      This helps to identify areas with very low weights that have been painted onto.

      None
         Vertices are displayed in the usual way.
      Active
         Show in black vertices with no weights in the active group.
      All
         The vertex is shown in black if it has zero weight in all groups.


Mesh Analysis
-------------

Show the mesh analysis overlay.

See: :ref:`modeling-mesh-analysis`.


Measurement
-----------

Numerical measures of the selected elements on screen as part of the text info overlay.
The :ref:`data-scenes-props-units` can be set in the Scene properties.

Edge Length
   Show the length of selected edges.
Edge Angle
   Show the angle of selected edges between two faces.
Face Area
   Show the area of selected faces.
Face Angle
   Show the angle of selected face corners.

.. tip::

   Geometry connected to the selection is shown while transforming,
   allowing you to move a vertex and see the connected edge lengths for example.

.. note::

   These values respect :ref:`Global/Local <modeling-mesh-transform-panel>`.

   Use *Global* if you want the Object's scale to be applied to the measurements.


.. _mesh-display-normals:

Normals
-------

- Display vertex normals
- Display face normals at vertices (split normals)
- Display face normals

Size
   The size to show the selected normals.

   .. _bpy.types.View3DOverlay.use_normals_constant_screen_size:

   Constant Screen Size Normals
      Keep size of normals constant in relation to the zoom level.


Developer
---------

Indices
   Display the indices of selected vertices, edges and faces.


Freestyle
---------

Edge Marks
   Display Freestyle edge marks, used with the Freestyle renderer.
Face Marks
   Display Freestyle face marks, used with the Freestyle renderer.


Sculpt Mode
===========

Mask
   Show :ref:`Masks <sculpt-mask-menu>` as overlays on an object. The opacity of the overlay can be adjusted.
Face Sets
   Show :ref:`Face Sets <sculpting-editing-facesets>` as overlays on an object.
   The opacity of the overlay can be adjusted.


Vertex Paint
============

.. _bpy.types.View3DOverlay.vertex_paint_mode_opacity:

Stencil Mask Opacity
   Opacity of the stencil mask overlay in Vertex Paint Mode.
Show Wire
   Use wireframe display in paint modes.


Weight Paint
============

Opacity
   The opacity of the overlay.
Zero Weights
   To display unreferenced and zero weighted areas in black.
   This helps to identify areas with very low weights that have been painted onto.

   None
      Vertices are displayed in the usual way.
   Active
      Show in black vertices with no weights in the active group.
   All
      The vertex is shown in black if it has zero weight in all groups.

Show Weight Contours
   Show contour lines formed by points with the same interpolated weight.

   This visualizes weight variations too small to be seen from colors and can be useful for judging
   the smoothness and consistency of gradients, e.g. when using smoothing tools and brushes.

Show Wire
   Use wireframe display in paint modes.


Texture Paint
=============

.. _bpy.types.View3DOverlay.texture_paint_mode_opacity:

Stencil Mask Opacity
   The opacity of the stencil mask overlay in Texture Paint Mode.


Pose Mode
=========

Fade Geometry
   Show the bones on top and face other geometry to the back.
   The opacity can be controlled with the slider.


.. _3dview-overlay-grease-pencil:

Grease Pencil
=============

Onion Skin
   Show ghosts of the keyframes before and after the current frame.
   If Multiframe is enabled Keyframes before and after of the active frame are displayed using onion colors.
Canvas
   Display a grid over Grease Pencil drawing plane.
   The opacity of the grid can be controlled with the slider.
   When using the *Canvas X-Ray* option objects are drawn behind the canvas grid.
Fade Layers
   Decrease the opacity of all the layers in the object other than the active one.
   The opacity factor can be controlled with the slider.
Fade Objects
   Cover all viewport except the active Grease Pencil object with a full color layer to improve visibility
   while drawing over complex scenes.

   Fade Grease Pencil Objects
      Include or exclude Grease Pencil objects.
Edit Lines
   Show edit lines when editing strokes.
Only in Multiframe
   Show edit lines only when using multiframe edition.
Stroke Direction
   Toggles the display of the strokes start point (green) and end point (red) to visualize the line direction.
Material Name
   Show material name next to the linked stroke.
Vertex Opacity
   Opacity for edit vertices (points).
Vertex Paint Opacity
   The opacity of the overlay.

.. _bpy.types.View3DOverlay.display_handle:

Handles
   When :doc:`Curve Editing </grease_pencil/modes/edit/curve_editing>` is active,
   this option controls how curves are displayed in the 3D Viewport.

   :None: No handles are displayed only the control points.
   :Selected: Only handles for selected control points are displayed.
   :All: All the handles are displayed.
