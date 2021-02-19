.. _bpy.types.GreasePencil.use_curve_edit:

*************
Curve Editing
*************

Curve Editing allows you to edit Grease Pencil strokes using Bézier curves.


Usage
=====

#. Select the desired strokes to edit as curves.
#. Activate curve editing in the 3D Viewport's header with the toggle button (Bézier curve icon).
#. Once activated you can:

   - Edit the curves with the curve handles.
   - Select strokes to automatically convert them to curves.

.. note::

   Selecting :doc:`points in between </grease_pencil/selecting>` is disabled while in curve editing is active.

.. seealso::

   The curve editing handles display can be tweaked in
   the :ref:`Overlays <bpy.types.View3DOverlay.display_handle>` popover.


Curve Editing Popover
=====================

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Panel:     :menuselection:`3D Viewport --> Header --> Curve Editing`

.. figure:: /images/grease-pencil_curve_editing_panel.png

   Curve Editing popover.

.. _bpy.types.GreasePencil.edit_curve_resolution:

Curve Resolution
   Number of points generated along each curve segment (between two handles) if *Adaptive Resolution* is disabled.

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
   When activated, the *Curve Resolution* is no longer constant for all curve segments but calculated dynamically.
   The length of each segment is approximated, then multiplied by the *Curve Resolution* and rounded down.
   This will be the number of points to generate for that segment.
   With Adaptive Resolution the points will be distribute more evenly across all the strokes.
   The *Curve Resolution* option will change the point density.

   .. list-table:: Adaptive Resolution.

      * - .. figure:: /images/grease-pencil_curve_editing_adaptive_resolution_off.png
             :width: 320px

             Off.

        - .. figure:: /images/grease-pencil_curve_editing_adaptive_resolution_on.png
             :width: 320px

             On.


Curve Data
==========

Once a stroke has been converted to a curve, the data will be saved to the file.
When Curve Editing is deactivated and the curve is changed, for example using
:doc:`Sculpt Mode </grease_pencil/modes/sculpting/introduction>`,
then the curve will be refitted once Curve Editing is activated again.


Operators
=========

Curve editing is currently more limited than stroke editing.
Every operation in Edit Mode for strokes and stroke points work for curves as well except for the following:

- Duplicate
- Copy and Paste
- Snap to Cursor and Cursor to selected
- Flip
- Simplify and Simplify Fixed
- Trim
- Separate
- Split
- Interpolate
