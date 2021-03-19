.. _bpy.ops.curve.draw:

****
Draw
****

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Tool:      :menuselection:`Toolbar --> Draw`

The Curve draw tool allows you to free-hand draw curves.


.. _bpy.types.CurvePaintSettings:

Tool Settings
=============

.. figure:: /images/modeling_curves_tools_draw_curve-stroke-panel.png
   :align: right

   Curve Stroke panel.

Type
   Type of curve to use for drawing.

   Poly
      Bézier Curve with straight line segments (auto handles).
   Bézier
      Tolerance
         Lower values give a result that is closer to the drawing stroke,
         while higher values give more smoothed results.

      Method
         Refit
            Incrementally refits the curve (gives best results).
         Split
            Splits the curve until the tolerance is met (gives a better drawing performance).

      Detect Corners
         Detects corners while drawing based on a specified angle;
         Any angles above the specified value are considered corners.
         If a corner is detected, the curve uses non-aligned handles
         for the corner resulting in a more crisp corner.

Radius
   Min
      Minimum radius when the minimum pressure is applied (also the minimum when tapering).
   Max
      Radius to use when the maximum pressure is applied (or when a tablet is not used).

Use Pressure
   Uses stylus pressure to control the radius of the curve.

Depth
   Controls where and how the curves are drawn.

   Cursor
      Uses the depth under the cursor to draw curves.

   Surface
      Used to draw on top of other objects.

      Offset
         Distance to offset the curve from the surface.
      Absolute Offset
         Applies a fixed offset (does not scale by the curve radius).
      Only First
         Only uses the start of the stroke for the depth.
      Plane
         The orientation plane to draw on, available when *Only First* is enabled.

         Normal/View
            Draws perpendicular to the surface.
         Normal/Surface
            Draws aligned to the surface.
         View
            Draws aligned to the viewport.


Options
=======

After the tool is run, these options are available in the :ref:`ui-undo-redo-adjust-last-operation` panel.

Error
   Error distance in object units. This can be seen similar to a subdivision rate for the curve.
   Lower values give a result that is closer to the drawing stroke while higher values give more smoothed results.

Fit Method
   Refit
      Incrementally refits the curve (gives best results).
   Split
      Splits the curve until the tolerance is met (gives a better drawing performance).

Corner Angle
   Any angles above this are considered corners.

Cyclic
   Toggles whether or not the curve is :term:`Cyclic`.
