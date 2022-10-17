
**************
Brush Settings
**************

Radius
   This option controls the radius of the brush, measured in pixels.
   :kbd:`F` allows you to change the brush size interactively by
   dragging the mouse and then :kbd:`LMB` (the texture of the brush should be visible inside the circle).
   Typing a number then enter while using :kbd:`F` allows you to enter the size numerically.

   Size Pressure
      Brush size can be affected by enabling the pressure sensitivity icon,
      if you are using a :ref:`Graphics Tablet <hardware-tablet>`.
   Use Unified Radius
      Use the same brush *Radius* across all brushes.

Radius Unit
   Controls how the brush *Radius* is measured.

   View
      The *Radius* is measured based on how the cursor appears on the monitor i.e. "screen space".
   Scene
      The *Radius* is measured based on real world units.
      The unit type and scaling can be configured in the :ref:`Scene Units <bpy.types.UnitSettings>`.

Strength
   Controls how much each application of the brush affects the model.
   For example, higher values cause the *Draw* brush to add depth to the model more quickly,
   and cause the *Smooth* brush to smooth the model more quickly.
   This setting is not available for *Grab*, *Snake Hook*, or *Rotate*.

   You can change the brush strength interactively by pressing :kbd:`Shift-F`
   in the 3D Viewport and then moving the brush and then :kbd:`LMB`.
   You can enter the size numerically also while in :kbd:`Shift-F` sizing.

   Strength Pressure
      Brush strength can be affected by enabling the pressure sensitivity icon,
      if a supported tablet is being used.
   Use Unified Strength
      Use the same brush *Strength* across all brushes.

   .. tip::

      If the range of strengths does not seem to fit the model
      (for example, if even the lowest strength setting still makes too large of a change on the model)
      then you can scale the model (in Edit Mode, not Object Mode).
      Larger sizes will make the brush's effect smaller, and vice versa.

Direction :kbd:`Ctrl`
   Brush direction toggle, *Add* raises geometry towards the brush,
   *Subtract* lowers geometry away from the brush. This setting can be toggled with :kbd:`Ctrl` while sculpting.

.. _bpy.types.Brush.normal_radius_factor:

Normal Radius
   The ratio between the brush radius and the radius that is going to be used to sample
   the normal i.e. take the average of multiple normals. This influences the brush orientation;
   increasing this value causes the brush to follow a smooth version of the mesh,
   while a small value causes the brush to closely follow the contours of the mesh.

.. _bpy.types.Brush.hardness:

Hardness
   How close the brush falloff starts from the edge of the brush.

.. _bpy.types.Brush.auto_smooth_factor:

Autosmooth
   Sets the amount of smoothing to be applied to each stroke.

Topology
   See :ref:`Dyntopo <bpy.types.Brush.topology_rake_factor>`.

Normal Weight :kbd:`Ctrl`
   Constrains brush movement along the surface normal.
   Especially useful with the *Grab* brush, can be temporarily enabled by holding :kbd:`Ctrl`.
   E.g. *Grab* brush can be used to push a depression (hole) into the mesh when *Normal Weight* is set.

   Applies to *Grab* and *Snake Hook* brushes.

Plane Offset
   Offset for planar brushes (Clay, Fill, Flatten, Scrape),
   shifts the plane that is found by averaging the faces above or below.

Plane Trim
   Ability to limit the distance that planar brushes act.
   If trim is enabled vertices that are further away from the offset plane than
   the trim distance are ignored during sculpting.


.. _sculpt-tool-settings-brush-settings-advanced:

Advanced
========

.. _bpy.types.Brush.use_automasking_topology:

Topology
   Setting per each brush, affects only vertices connected to the active vertex under the brush.
   This can be used for isolating disconnected meshes, face sets, masking cavities,
   mesh boundary edges, or creating topological falloffs.

.. _bpy.types.Brush.use_automasking_face_sets:

Face Sets
   Affect only vertices that share face sets with active vertex.

.. _bpy.types.Brush.use_automasking_boundary_edges:

Mesh Boundary
   Does not affect non-manifold boundary edges.

.. _bpy.types.Brush.use_automasking_boundary_face_sets:

Face Sets Boundary
   Does not affect vertices which belong to a face set boundary.

Propagation Steps
   The distance where *Mesh Boundary Auto-Masking* is going to protect vertices from the fully masked edge.

.. _bpy.types.Brush.sculpt_plane:

Sculpt Plane
   Use this menu to set the plane in which the sculpting takes place.
   In other words, the primary direction that the vertices will move.

   :Area Plane:
      The movement takes place in the direction of average normal for all active vertices within the brush area.
      Essentially, this means that the direction is dependent on the surface beneath the brush.
   :View Plane:
      Sculpting in the plane of the current 3D Viewport.
   :X, Y, Z Plane:
      The movement takes place in the positive direction of one of the global axes.

.. _bpy.types.Brush.use_original_normal:
.. _bpy.types.Brush.use_original_plane:

Original
   Normal
      When locked it keeps using the normal of the surface where stroke was initiated,
      instead of the surface normal currently under the cursor.
   Plane
      When locked keep using the plane origin of surface where stroke was initiated,
      instead of the surface plane currently under the cursor.

Accumulate
   Causes stroke dabs to accumulate on top of each other.

Front Faces Only
   When enabled, the brush only affects vertices that are facing the viewer.

.. toctree::
   :hidden:

   Texture </sculpt_paint/brush/texture.rst>
   Stroke </sculpt_paint/brush/stroke.rst>
   Falloff </sculpt_paint/brush/falloff.rst>
   Cursor </sculpt_paint/brush/cursor.rst>


Texture
=======

See the global brush settings for :doc:`Texture </sculpt_paint/brush/texture>` settings.


Stroke
======

See the global brush settings for :doc:`Stroke </sculpt_paint/brush/stroke>` settings.


Falloff
=======

See the global brush settings for :doc:`Falloff </sculpt_paint/brush/falloff>` settings.


Cursor
======

See the global brush settings for :doc:`Cursor </sculpt_paint/brush/cursor>` settings.
