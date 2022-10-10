.. _bpy.types.View3DOverlay:
.. |overlays-icon| image:: /images/editors_3dview_display_overlays.png

*****************
Viewport Overlays
*****************

.. reference::

   :Mode:      All Modes
   :Header:    |overlays-icon| :menuselection:`Overlays`

Clicking the icon toggles all overlays in the 3D Viewport.
The dropdown button displays a popover with more detailed settings,
which are described below.

The available options depend on the mode that the 3D Viewport is in.


Object Mode
===========

The following options are always present, independent of the current mode.
Some of the overlays can be customized in the
:doc:`Viewport Preferences </editors/preferences/viewport>`.

Guides
------

Grid
   Show grid in orthographic side view.
Floor
   Show the ground plane in perspective view.
Axis
   Show the X, Y and/or Z axis lines.

Scale
   The distance between lines in the grid/floor.
Subdivision
   The number of subdivisions between grid lines.

Text Info
   Show various bits of information in the top left corner of the viewport.
   
   View Perspective
      Name of the :doc:`View Perspective </editors/3dview/navigate/projections>`,
      such as "Top Orthographic" or "User Perspective."
   Playback Frame Rate (FPS)
      Displays the Frames Per Second at which the animation is playing.
      By default, Blender goes through every single frame, which may result in an FPS that's lower than
      intended (and the animation playing slower than realtime); the FPS turns red in this case.
      You can change this behavior in the Playback popover of the :doc:`Timeline </editors/timeline>`.
   Object Info
      Shows the current frame in parentheses, followed by the names of the selected
      :doc:`Collection </scene_layout/collections/index>` and the :ref:`active object <object-active>`.
      When applicable, also shows the selected :doc:`Shape Key </animation/shape_keys/introduction>`
      and (in angle brackets) the :doc:`Marker </animation/markers>` on the current frame.
      If the object has a keyframe on the current frame, the Object Info is displayed in yellow.
   Grid Resolution
      When the view is aligned to a world axis (see :doc:`/editors/3dview/navigate/viewpoint`),
      the Text Info additionally shows the smallest distance between two parallel grid lines.

Statistics
   Show information about the amount of objects and geometry.
   Note that the counters depend on the current selection.
   For example, selecting a mesh gives info on the number of vertices, edges, and faces,
   while selecting a light shows the number of lights in the scene.

   - Objects -- Number of the selected objects and the total count.
   - Geometry -- Displays information about the current scene depending on the mode and object type.
     This can be the number of vertices, faces, triangles, or bones.

HDRI Preview
   Show two spheres, one glossy and one diffuse, to preview the HDRI that's being used for world lighting.
   While HDRIs can be used in both the *Material Preview* and *Rendered*
   :doc:`shading modes </editors/3dview/display/shading>`, the HDRI Preview overlay
   is only available in the former.
3D Cursor
   Show the :doc:`3D Cursor </editors/3dview/3d_cursor>`.
Annotations
   Show :doc:`annotations </interface/annotate_tool>`.


Objects
-------

Extra
   Show objects that don't have geometry (such as empties, cameras and lights).
Relationship Lines
   Show dashed lines indicating parent or constraint relationships.
Outline Selected
   Show an outline around selected objects.
Bones
   Show Bones.
Motion Paths
   Show the :doc:`motion path </animation/motion_paths>` overlay.
Origin
   Show the :doc:`origins </scene_layout/object/origin>` of the selected objects.
Origin (All)
   Show the origins of all objects.


Geometry
--------

.. _bpy.types.View3DOverlay.wireframe_threshold:
.. _bpy.types.View3DOverlay.show_wireframes:

Wireframe
   Display mesh edges. Similar to :ref:`Wireframe Shading <3dview-shading-rendered>`,
   but displays edges on top of existing shading.
   The value slider adjusts which edges to display:
   lower values hide edges on surfaces that are almost flat, while a value of 1 shows all edges.

   .. _bpy.types.View3DOverlay.wireframe_opacity:

   Opacity
      The opacity of the displayed edges, from 0 (invisible) to 1 (fully opaque).

.. _bpy.types.View3DOverlay.fade_inactive_alpha:
.. _bpy.types.View3DOverlay.show_fade_inactive:

Fade Inactive Geometry
   In modes other than Object Mode, fade out objects that you're not working on.
   The slider controls how much they're faded out.

.. _bpy.types.View3DOverlay.show_face_orientation:

Face Orientation
   Show faces whose normal is pointing towards the camera in blue,
   and faces whose normal is pointing away from the camera in red.
   This lets you quickly check for faces that are oriented incorrectly:
   the outside surface of an object should typically be all blue.


.. _bpy.types.SpaceView3D.show_reconstruction:

Motion Tracking
---------------

Show the :doc:`motion tracking </movie_clip/tracking/introduction>` overlay.

Camera Path
   Show the reconstructed camera path.
Marker Names
   Show the names for reconstructed track objects.

Tracks
   Change the display of the reconstructed tracks:
   plain axes, arrows and so on.

Size
   Change the display size of the reconstructed tracks.


.. _3dview-overlay-mesh_edit_mode:

Mesh Edit Mode
==============

The following options are available when in Mesh Edit Mode.

Edges
   Highlight selected and partially selected edges.
   Only affects vertex and face selection modes, as edges are always highlighted in edge selection mode.
Faces
   Highlight selected faces. Affects all selection modes.
Center
   Show face center points in solid shading modes. (They're always shown in wireframe shading mode.)

   Only affects face selection mode.
Creases
   Display edges marked with a crease
   for the :doc:`Subdivision Surface Modifier </modeling/modifiers/generate/subdivision_surface>`.
Sharp
   Display sharp edges, used with the :doc:`Edge Split modifier </modeling/modifiers/generate/edge_split>`.
Bevel
   Display weights created for the :doc:`Bevel Modifier </modeling/modifiers/generate/bevel>`.
Seams
   Display the :doc:`UV unwrapping seams </modeling/meshes/uv/unwrapping/seams>`.


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
      Display unreferenced and zero-weighted areas in black.
      This helps to identify areas with very low weights that have been painted onto.

      None
         Vertices are displayed in the usual way.
      Active
         Vertices are shown in black if they have no weight in the active vertex group.
      All
         Vertices are shown in black if they have no weight in any vertex group.


Mesh Analysis
-------------

Show the :ref:`modeling-mesh-analysis` overlay.


Measurement
-----------

Show numerical measures of the selected elements.
The :ref:`bpy.types.UnitSettings` can be set in the Scene properties.

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

   These values respect the :ref:`Transform Space <modeling-mesh-transform-panel>`
   in the Sidebar. Use *Global* if you want the object's scale to be applied to the measurements.


.. seealso::
   The :doc:`Measure </editors/3dview/toolbar/measure>` tool for measuring
   arbitrary distances and angles.

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
      Keep the size of normals constant in relation to the zoom level.


Developer
---------

These overlays are only available if *Developer Extras* is enabled
in the :doc:`Interface Preferences </editors/preferences/interface>`.

Indices
   Display the indices of selected vertices, edges, and faces.


Freestyle
---------

These settings apply to the :doc:`Freestyle </render/freestyle/introduction>`
line art renderer.

Edge Marks
   Display Freestyle edge marks.
Face Marks
   Display Freestyle face marks.


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
   Does nothing. (Stencil masks are only available for texture painting.)
Show Wire
   Display mesh edges in white (unlike the *Wireframe* overlay which shows them in black).


Weight Paint
============

Opacity
   The opacity of the overlay.
Zero Weights
   Display unreferenced and zero-weighted areas in black.
   This helps to identify areas with very low weights that have been painted onto.

   None
      Vertices are displayed in the usual way.
   Active
      Vertices are shown in black if they have no weight in the active vertex group.
   All
      Vertices are shown in black if they have no weight in any vertex group.

Show Weight Contours
   Show contour lines formed by points with the same interpolated weight.

   This visualizes weight variations too small to be seen from colors and can be useful for judging
   the smoothness and consistency of gradients, e.g. when using smoothing tools and brushes.

Show Wire
   Display mesh edges in white (unlike the *Wireframe* overlay which shows them in black).


Texture Paint
=============

.. _bpy.types.View3DOverlay.texture_paint_mode_opacity:

Stencil Mask Opacity
   Opacity of the :doc:`stencil mask </sculpt_paint/texture_paint/tool_settings/mask>` overlay.


Bones
=====

Fade Geometry
   Show the bones on top and face other geometry to the back.
   The opacity can be controlled with the slider.
   Only available in Pose Mode.

Bone Wireframe Opacity
   The maximum opacity used for bones drawn in the *Wireframe*
   :doc:`shading mode </editors/3dview/display/shading>`
   (or in *Solid* shading mode with X-Ray active).
   This is helpful when it is necessary to reduce clutter and focus on
   the mesh rather than bones.


.. _3dview-overlay-grease-pencil:

Grease Pencil
=============

Onion Skin
   Show ghosts of the keyframes before and after the current frame.
   If :doc:`Multiframe </grease_pencil/multiframe>` is enabled,
   ghosts of the selected keyframes are shown instead.
   See :doc:`/grease_pencil/properties/onion_skinning`.
Canvas
   Display a grid over the Grease Pencil drawing plane.
   The opacity of the grid can be controlled with the slider.
   When using the *Canvas X-Ray* option, objects are drawn behind the canvas grid.
Fade Inactive Layers
   Decrease the opacity of all the layers in the object other than the active one.
   The opacity factor can be controlled with the slider.
Fade Inactive Objects
   Cover all of the viewport except the active Grease Pencil object with a full color layer to improve visibility
   while drawing over complex scenes.

   Fade Grease Pencil Objects
      Include or exclude Grease Pencil objects.
Edit Lines
   Show edit lines in Edit Mode.
Only in Multiframe
   When Multiframe is enabled and keyframes other than the current frame are selected,
   strokes on those keyframes are displayed as just their edit lines -- the strokes themselves are hidden.
   Note that this does not affect Onion Skinning.
Stroke Direction
   Toggle the display of the selected strokes' start points (green) and end points (red) to visualize their direction.
Material Name
   Show material name next to the selected strokes.
Vertex Opacity
   Opacity for vertices (points) and edit lines in Edit Mode.
Vertex Paint Opacity
   The opacity of the vertex color overlay in Vertex Paint Mode and Draw Mode.
   Note that in Draw Mode, vertex paint is only visible in the *Material Preview*
   and *Rendered* shading modes by default. To see it in *Solid* mode, you either
   need to use Vertex Paint Mode, or set the :doc:`Color </render/workbench/color>`
   shading setting to *Attribute*.

.. _bpy.types.View3DOverlay.display_handle:

Handles
   When :doc:`Curve Editing </grease_pencil/modes/edit/curve_editing>` is active,
   this option controls how curves are displayed in the 3D Viewport.

   :None: No handles are displayed, only the control points.
   :Selected: Only handles for selected control points are displayed.
   :All: All the handles are displayed.
