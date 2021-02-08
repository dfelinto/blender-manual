.. _bpy.types.GreasePencil.use_curve_edit:


*************
Curve Editing
*************

Curve Editing allows you to edit grease pencil strokes using bézier curves.


Usage
=====

#. Select the desired strokes to edit as curves.
#. Activate curve editing in the 3D Viewport's header with the toggle button (bézier curve icon).
#. Once activated you can:

   - Edit the curves with the curve handles.
   - Select strokes to automatically convert them to curves.

.. note::
   Selecting :doc:`points in between </grease_pencil/selecting>` is disabled while in curve edit mode.

Curve Editing Popover
=====================

.. figure:: /images/grease-pencil_curve_editing_panel.png

   Curve Editing popover.


.. _bpy.types.GreasePencil.edit_curve_resolution:

Curve Resolution
   Number of points generated along each curve segment (between two handles) if Apdaptive Resolution is turned off. 

.. _bpy.types.GreasePencil.curve_edit_threshold:

Threshold
   Threshold used for curve fitting. Maximum distance the fitted curve can deviate from the target stroke.
   A threshold of 0.0 will generate a curve point for every stroke point. Higher thresholds will result in higher
   approximations of the target stroke but also smoother curve.

.. _bpy.types.GreasePencil.curve_edit_corner_angle:

Corner Angle
   Any detected corner with an angle above the specified amount will create a sharp (non-aligned) handle.

.. _bpy.types.GreasePencil.use_adaptive_curve_resolution:

Adaptive Resolution
   When activated, the Curve Resolution is no longer constant for all curve segments but calculated dynamically.
   The length of each segment is approximated, then multiplied by the Curve Resolution and rounded down. 
   This will be the number of points to generate for that segment.
   Adaptive resolution will distribute the points more evenly accross all the strokes. 
   The Curve Resolution parameter will change the point density.

.. list-table:: Adaptive Resolution.

   * - .. figure:: /images/grease-pencil_curve_editing_adaptive_resolution_off.png
          :width: 320px

          Off.

     - .. figure:: /images/grease-pencil_curve_editing_adaptive_resolution_on.png
          :width: 320px

          On.

Handle Display
==============

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Panel:     :menuselection:`3D Viewport --> Viewport Overlays --> Edit Grease Pencil`

When Curve Editing is active, curves have special :doc:`overlays </editors/3dview/display/overlays>`
to control how curves are displayed in the 3D Viewport.

Handles
   - None
      No handles are displayed. Just the control points.
   - Selected
      Only handles for selected control points are displayed.
   - All
      All the handles are displayed.

Curve Data
==========

Once a stroke has been converted to a curve, the data will be saved to the file.
When Curve Editing is turned off and the curve is changed, for example using :doc:`Sculpt Mode </grease_pencil/modes/sculpting/introduction>`,
then the curve will be refitted once Curve Editing is activated again.


Operators
=========

Curve editing is currently more limited than stroke editing.
Every edit mode operation for strokes and stroke points work for curves as well except for the following:

 - Duplicate
 - Copy & Paste
 - Snap to Cursor & Cursor to selected
 - Flip
 - Simplify & Simplify Fixed
 - Trim
 - Separate
 - Split
 - Interpolate
