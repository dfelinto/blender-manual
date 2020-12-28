
*****
Solve
*****

.. _clip-tracking-plane:
.. _bpy.ops.clip.create_plane_track:

Plane Track
===========

The *Create Plane Track* operator creates a new plane track.
Planar tracking takes advantage of the fact that there are often planar surfaces in footage,
by attaching markers to points on these flat planes.
It can be used to replace things like billboards and screens on the footage with another image or video.
It also might be used for masking.

This button will create a plane object
which is deforming in the same way as plane defined by all selected point tracks.
At least four feature points tracked across the footage which belongs to
the plane you want to replace are needed. More tracks will give better estimation of plane motion.

Feature points used to estimate plane motion could be used from any place on the plane,
meaning it's not necessarily need to be corners. Corners are not always easy to be tracked,
they might be occluded. In this case you can position tracked features that lay on the same plane
far away from the actual plane which should be replaced.

This provides more information about the possible deformation of the marker in following frames,
and such markers can be tracked even if partially occluded (appear and disappear during the time).
It is only required that two neighbor frames have at least four common tracks.

An image can be projected onto the plane with
the :doc:`/compositing/types/distort/plane_track_deform` compositing node.


Solve
=====

.. _bpy.types.MovieTrackingSettings.use_tripod_solver:

Tripod
   Tripod Motion can be used for footage where the camera does not move and only rotates.
   Such footage can't be tracked with a generic solver approach, and
   it is impossible to determine the actual feature points in space due to a lack of information.
   So this solver will solve only the relative camera rotation and then reproject the feature points into a sphere,
   with the same distance between feature and camera for all feature points.

   .. note::

      This is special type of camera solver and it behaves different from regular solver.
      It means using more tracks doesn't imply more accurate solution.
      Having 5-10 tracks on frame is likely what shall be commonly used for this kind of solver.

.. _bpy.types.MovieTrackingSettings.use_keyframe_selection:

Keyframe
   Automatically select keyframes for initial reconstruction.
   This option enables complex algorithms which tries to find a keyframe pair
   with minimal reconstruction error and best scene scale guess.

.. _bpy.types.MovieTrackingObject.keyframe_a:
.. _bpy.types.MovieTrackingObject.keyframe_b:

Keyframe A/B
   Start (A) and End (B) frame of the range used for reconstruction.


Refine
   Specifies which parameters should be refined during solve.
   Such refining is useful when you are not sure about some camera intrinsics,
   and solver should try to find the best parameter for those intrinsics.
   But you still have to know approximate initial values --
   it will fail to find correct values if they were set completely incorrectly initially.

   .. _bpy.types.MovieTrackingSettings.refine_intrinsics_focal_length:

   Focal Length
      Refine the camera's :ref:`Focal Length <bpy.types.MovieTrackingCamera.focal_length>`.

   .. _bpy.types.MovieTrackingSettings.refine_intrinsics_principal_point:

   Optical Center
      Refine the camera's :ref:`Optical Center <bpy.types.MovieTrackingCamera.principal>`.

   .. _bpy.types.MovieTrackingSettings.refine_intrinsics_radial_distortion:

   Radial Distortion
      Refine the camera's :ref:`Radial Distortion Parameters <bpy.types.MovieTrackingCamera.k>`.

   .. _bpy.types.MovieTrackingSettings.refine_intrinsics_tangential_distortion:

   Tangential Distortion
      Refine the camera's :ref:`Tangential Distortion Parameters <bpy.types.MovieTrackingCamera.brown_p>`.


.. _editors-movie-clip-tracking-clip-solve-motion:

Solve Camera/Object Motion
   See :ref:`bpy.ops.clip.solve_camera`.


Cleanup
=======

This panel contains operators and their settings which are needed to clean up bad tracks:
tracks which are not tracked long enough or which failed to reconstruct accurately.

Frames
   Tracks or tracked segments shorter than this number of frames will be removed.

Error
   Tracks which has reprojection error higher than this value will be removed.

Type
   Several actions can be performed for bad tracks:

   Select
      They can simply be selected.
   Delete Track
      The whole track can be deleted.
   Delete Segments
      Bad segments of tracked sequence can be removed.

Clean Tracks
   See :ref:`bpy.ops.clip.clean_tracks`.

Filter Tracks
   This operator deletes obviously bad tracks (for example, the ones which are too short).
   Additionally, it identifies tracks which has suspicious spikes in their motion and selects them.


Geometry
========

3D Markers to Mesh
   See :ref:`bpy.ops.clip.bundles_to_mesh`.
Link Empty to Track
   See :ref:`bpy.ops.clip.track_to_empty`.


Orientation
===========

Scene orientation tools can be used for orienting object to bundles.

Floor
   See :ref:`bpy.ops.clip.set_origin`.
Wall
   See :ref:`bpy.ops.clip.set_plane`.
Set Origin
   See :ref:`bpy.ops.clip.set_plane`.
Set X, Y Axis
   See :ref:`bpy.ops.clip.set_axis`.
Set Scale
   See :ref:`bpy.ops.clip.set_scale`.
Apply Scale
   Similar to Set Scale, but actually modifies the tracking data.

Distance
   Distance in active scene units which is used by Set/Apply scale.


Scene Setup
===========

Set as Background
   Sets the clip currently being edited as the camera background for all visible 3D Viewports.
   If there is no visible 3D Viewports or the Clip Editor is open in full screen, nothing will happen.

Setup Tracking Scene
   Performs all usual steps to set up a VFX scene:

   - Create reference objects for floor and test object.
   - Create node set up for combining CG with an actual clip.
