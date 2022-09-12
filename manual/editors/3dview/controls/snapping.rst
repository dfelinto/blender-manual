.. _bpy.types.ToolSettings.use_snap:
.. _transform-snap:

********
Snapping
********

.. reference::

   :Mode:      Object, Edit, and Pose Mode
   :Header:    :menuselection:`Snap`
   :Shortcut:  :kbd:`Shift-Tab`

Snapping lets you easily align objects and mesh elements to others.
It can be toggled by clicking the magnet icon in the 3D Viewport's header,
or more temporarily by holding :kbd:`Ctrl`.

.. figure:: /images/editors_3dview_controls_snapping_header-magnet-icon.png

   Magnet icon in the 3D Viewport header (blue when enabled).

.. figure:: /images/editors_3dview_controls_snapping_element-menu.png

   Snap menu.


.. _bpy.types.ToolSettings.snap_elements:

Snap To
=======

.. reference::

   :Mode:      Object, Edit, and Pose Mode
   :Header:    :menuselection:`Snapping --> Snap To`
   :Shortcut:  :kbd:`Shift-Ctrl-Tab`

Determines the target which the selection will be snapped to.

Increment
   Snaps to grid points. When in Orthographic view, the snapping increment changes depending on the zoom level.

   .. note::

      By default, this option won't snap to the grid that's displayed in the viewport,
      but an imaginary grid with the same resolution that starts at the selection's
      original location. In other words, it lets you move the selection in "increments" of the
      grid cell size.

      If you want to snap to the viewport grid instead, you can enable *Absolute Grid Snap*
      (see below).
Vertex
   Snaps to the nearest vertex of a mesh object.
Edge
   Snaps to the nearest point on the nearest edge.
Face Project
   Snaps to the face by projecting the current point on the nearest face.
   This snap mode will snap geometry to both visible and occluded.
   This snap mode is useful for retopologizing.
Face Nearest
   Snaps to the nearest surface in world space.
   This snap mode will only snap geometry to visible (non occluded) geometry.
Volume
   Snaps to regions within the volume of the first object found below the mouse cursor.
   Unlike the other options, this option controls the depth
   (i.e. Z coordinates in current view space) of the transformed element.
   By toggling *Snap Peel Object* (see below),
   target objects will be considered as a whole when determining the volume center.
Edge Center
   Snaps to the centerpoint of the nearest edge.
Edge Perpendicular
   Snaps to a specific point on the nearest edge so that the line from the selection's
   original location (indicated by a white cross) to its new location is perpendicular to that edge.

.. tip::

   Multiple snapping modes can be enabled at once using :kbd:`Shift-LMB`.


.. _bpy.types.ToolSettings.snap_target:

Snap With
=========

.. reference::

   :Mode:      Object, Edit, and Pose Mode
   :Header:    :menuselection:`Snapping --> Snap with`
   :Shortcut:  :kbd:`Shift-Ctrl-Tab`

Determines what part of the selection will coincide with the target.
(The rest of the selection will follow along.)

Active
   Snaps using the origin (in Object Mode) or center (in Edit Mode) of the active element.
Median
   Snaps using the median of the selection.
Center
   Snaps using the current transformation center
   (another word for the :doc:`pivot point </editors/3dview/controls/pivot_point/index>`).
   This option is especially useful in combination with the
   :doc:`3D Cursor </editors/3dview/3d_cursor>` for choosing the snapping
   point completely manually.
Closest
   Snaps using the vertex that's closest to the target.

.. list-table::

   * - .. figure:: /images/editors_3dview_controls_snapping_target-closest.png

          Closest.

     - .. figure:: /images/editors_3dview_controls_snapping_target-active.png

          Active.

     - .. figure:: /images/editors_3dview_controls_snapping_target-median.png

          Median.


Target Selection
================

.. figure:: /images/editors_3dview_controls_snapping_options.png

As seen in the yellow highlighted area in the image above, besides the snap target,
additional controls are available to alter snap behavior. These options vary between mode
(Object and Edit) as well as snap target. The available options are:

.. _bpy.types.ToolSettings.use_snap_self:

Include Active
   Only available in Edit Mode.
   Allows snapping mesh elements to other elements of the same mesh.

   This checkbox is ignored if
   :doc:`Proportional Editing </editors/3dview/controls/proportional_editing>`
   is enabled.

.. _bpy.types.ToolSettings.use_snap_edit:

Include Edited :guilabel:`Edit Mode`
   Snap onto non-active objects in Edit Mode.

.. _bpy.types.ToolSettings.use_snap_nonedit:

Include Non-Edited :guilabel:`Edit Mode`
   Snap onto objects not in Edit Mode.

.. _bpy.types.ToolSettings.use_snap_selectable:

Exclude Non-Selectable
   Snap only onto objects that are selectable.

.. _bpy.types.ToolSettings.use_snap_grid_absolute:

Absolute Grid Snap
   Only available if Snap To Increment is enabled.
   Snaps to the grid, instead of snapping in increments relative to the current location.

.. _bpy.types.ToolSettings.use_snap_backface_culling:

Backface Culling
   Exclude back-facing geometry from snapping.

.. _bpy.types.ToolSettings.use_snap_align_rotation:

Align Rotation to Target
   Rotates the selection so that its Z axis gets aligned to the normal of the target.

.. _bpy.types.ToolSettings.use_snap_project:

Project Individual Elements
   Only available if Snap To Face is enabled.
   Rather than the default behavior where only the "Snap With" point gets snapped
   to the target and the rest of the selection follows along (maintaining the
   original shape), this option makes each object (in Object Mode) or vertex
   (in Edit Mode) snap to a target independently of the others, which
   may cause the selection's shape to change.

   This can be used for bending a flat sheet so it snugly fits against a curved
   surface, for example.

   .. seealso::

      :doc:`/modeling/modifiers/deform/shrinkwrap`

.. _bpy.types.ToolSettings.use_snap_to_same_target:

Snap to Same Target :guilabel:`Face Nearest`
   Snap only to target that source was initially near.

.. _bpy.types.ToolSettings.snap_face_nearest_steps:

Face Nearest Steps :guilabel:`Face Nearest`
   Number of steps to break transformation into for face nearest snapping.
   This option is only available in Edit mode.

.. _bpy.types.ToolSettings.use_snap_peel_object:

Snap Peel Object
   Only available if Snap To Volume is enabled.
   Consider objects as a whole when finding volume center.


.. _bpy.types.ToolSettings.use_snap_translate:
.. _bpy.types.ToolSettings.use_snap_rotate:
.. _bpy.types.ToolSettings.use_snap_scale:

Affect
======

Specifies which transformations are affected by snapping.
By default, snapping only happens while moving something,
but you can also enable it for rotating and scaling.


Multiple Snap Targets
---------------------

While you're transforming a selection with snapping enabled,
you can press :kbd:`A` whenever there's a highlighted snap target to
mark it. With multiple such targets marked, the selection will
then be snapped to their average location.

Marking a target more than once will give it more weight.

.. figure:: /images/editors_3dview_controls_snapping_target-multiple.png

   Multiple snapping targets.
