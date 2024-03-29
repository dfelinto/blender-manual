
******
Stroke
******

.. figure:: /images/sculpt-paint_brush_stroke_stroke-panel.png
   :align: right

   Stroke panel.

.. _bpy.types.Brush.stroke_method:

Stroke Method :kbd:`E`
   Defines the way brush strokes are applied to the canvas.

   .. container:: lead

      .. clear

   :Dots:
      Apply paint on each mouse move step.
   :Drag Dot:
      Leaves only one dab on the canvas which can be placed by dragging.
   :Space:
      Creates brush stroke as a series of dots,
      whose distance (spacing) is determined by the *Spacing* setting.

      .. _bpy.types.Brush.spacing:
      .. _bpy.types.Brush.use_pressure_spacing:

      Spacing
         Limits brush application to the distance specified by the percentage of the brush radius.
   :Airbrush:
      Flow of the brush continues as long as the mouse click is held (spray),
      determined by the *Rate* setting.
      With other methods the brush only modifies the color when the brush changes its location.
      This option is not available for the *Grab* sculpting brush.

      .. _bpy.types.Brush.rate:

      Rate
         Interval between paints for airbrush.
   :Anchored:
      Creates a single dab at the brush location.
      Clicking and dragging will resize the dab diameter.

      .. _bpy.types.Brush.use_edge_to_edge:

      Edge to Edge
         The brush location and orientation are determined by a two point circle,
         where the first click is one point, and dragging places the second point, opposite from the first.
   :Line:
      Clicking and dragging lets you define a line in screen space.
      The line dabs are separated by *Spacing*, similar to space strokes.
      With :kbd:`Alt` the line stroke is constrained to 45 degree increments.
   :Curve:
      Defines the stroke curve with a Bézier curve (dabs are separated according to *Spacing*).
      This Bézier curve is stored in Blender as a "Paint Curve" data-block.

      Use :kbd:`Ctrl-RMB` to create the initial control point of the curve.

      Paint Curves
         Paint Curves are reusable and can be stored and selected by using the :ref:`ui-data-block` menu.

         .. _bpy.ops.paintcurve.new:

         - **Add Points:**
           Use :kbd:`Ctrl-RMB` to create the initial control point of the curve.
           You can define additional curve control points by using :kbd:`Ctrl-RMB`.
           The handles can be defined by dragging the mouse.
           The stroke flows in the direction of the first control point to the second control point.
           If another control point is added after the second control point,
           instead of extending it from the first control point in a different direction,
           it will become the initial control point,
           and thus the stroke still flows in the direction of the first to the second.

         - **Transforming Points:**
           The control points and handles can be dragged with :kbd:`LMB`.
           To make sure that the handles of a control point are symmetrical,
           drag them using :kbd:`Shift-RMB`.
           A few transform operators are supported such as moving, scaling and rotating.

         .. _bpy.ops.paintcurve.select:

         - **Selection:**
           The handles can be selected individually by using :kbd:`RMB`,
           extend the selection by :kbd:`Shift-RMB` and deselect/select all by using :kbd:`A`.

         .. _bpy.ops.paintcurve.delete_point:

         - **Delete Points :kbd:`X`:**
           To delete a curve point, use :kbd:`X`.

      .. _bpy.ops.paintcurve.draw:

      Draw Curve :kbd:`Return`
         To confirm and execute the curved stroke,
         press :kbd:`Return` or use the Draw Curve button.

.. _bpy.types.Brush.use_scene_spacing:

Spacing Distance :guilabel:`Sculpt Mode Only`
   Method used to calculate the distance to generate a new brush step.

   :View:
      Calculates the brush spacing relative to the view.
   :Scene:
      Calculates the brush spacing relative to the scene using the stroke location.
      This avoids artifacts when sculpting across curved surfaces.

.. _bpy.types.Brush.use_space_attenuation:

Adjust Strength for Spacing
   Attenuate the brush strength according to spacing.
   Available for the *Space*, *Line*, and *Curve* stroke methods.

.. _bpy.types.Brush.dash_ratio:

Dash Ratio
   Ratio of samples in a cycle that the brush is enabled.
   This is useful to create dashed lines in texture paint or stitches in Sculpt Mode.
   Available for the *Space*, *Line*, and *Curve* stroke methods.

.. _bpy.types.Brush.dash_samples:

Dash Length
   Length of a dash cycle measured in stroke samples.
   This is useful to create dashed lines in texture paint or stitches in Sculpt Mode.
   Available for the *Space*, *Line*, and *Curve* stroke methods.

.. _bpy.types.Brush.html#bpy.types.Brush.jitter:

Jitter
   Jitter the position of the brush while painting.

   .. _bpy.types.Brush.use_pressure_jitter:

   Jitter Pressure
      Brush *Jitter* can be affected by enabling the pressure sensitivity icon,
      if you are using a :ref:`Graphics Tablet <hardware-tablet>`.

.. _bpy.types.Brush.jitter_unit:

Jitter Unit
   Controls how the brush *Jitter* is measured.

   :View:
      The *Jitter* is measured based on how the cursor appears on the monitor i.e. "screen space".
   :Scene:
      The *Jitter* is measured based on real world units.
      The unit type and scaling can be configured in the :ref:`Scene Units <bpy.types.UnitSettings>`.

.. _bpy.types.Paint.input_samples:

Input Samples
   Recent mouse locations (input samples) are averaged together to smooth brush strokes.


.. _bpy.types.Brush.use_smooth_stroke:

Stabilize Stroke
================

*Stabilize Stroke* makes the stroke lag behind the cursor
and applies a smoothed curve to the path of the cursor.
This can be enabled temporary by holding :kbd:`Shift` while painting
or permanently by clicking the checkbox found in the header.

.. _bpy.types.Brush.smooth_stroke_radius:

Radius
   Minimum distance from the last point before the stroke continues.

.. _bpy.types.Brush.smooth_stroke_factor:

Factor
   A smooth factor, where higher values result in smoother strokes but the drawing sensation
   feels like as if you were pulling the stroke.
