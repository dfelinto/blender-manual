
*******
Falloff
*******

The Falloff allows you to control the *Strength* falloff of the brush.
The falloff is mapped from the center of the brush (left part of the curve)
towards its borders (right part of the curve).
Changing the shape of the curve will make the brush softer or harder.
Read more about using the :ref:`ui-curve-widget`.

.. figure:: /images/sculpt-paint_brush_falloff_brush-curve.png

   Brush curve example.

Curve Preset
   Custom
      You can choose how the strength of the falloff is determined from the center of the brush
      to the borders by manually manipulating the control points within the curve widget.
      There are also a couple of preset custom curves displayed at the bottom of the curve widget
      that can be used on their own or as a starting point for tweaking.

      .. list-table:: Custom Preset types.

         * - .. figure:: /images/sculpt-paint_brush_falloff_custom-smooth.png

                Smooth.

           - .. figure:: /images/sculpt-paint_brush_falloff_custom-sphere.png

                Sphere.

           - .. figure:: /images/sculpt-paint_brush_falloff_custom-root.png

                Root.

         * - .. figure:: /images/sculpt-paint_brush_falloff_custom-sharp.png

                Sharp.

           - .. figure:: /images/sculpt-paint_brush_falloff_custom-linear.png

                Linear.

           - .. figure:: /images/sculpt-paint_brush_falloff_custom-constant.png

                Constant.

   Smooth
      The center strength, the border strength, and the falloff transition between them are evenly distributed.
   Smoother
      Similar to *Smooth* but produces a wider center point of the brush before tapering off.
   Sphere
      The strength of the brush is predominately at its strongest point
      with a steep falloff near the border of the brush.
   Root
      Similar to a Sphere but the center is a more concentrated point.
   Sharp
      The center of the brush is the strongest point
      then exponentially tapers off to a lower strength, creating a fine point.
   Linear
      With the center being the strongest,
      the strength will consistently weaken as it reaches the border of the brush.
   Sharper
      Similar to *Sharp* but the center point is more condensed.
   Inverse Square
      A hybrid between *Smooth* and *Sphere*.
   Constant
      The strength of the brush remains unified across the entire brush.
      This will create a sharp edge at the border of the brush.

   .. figure:: /images/sculpt-paint_brush_falloff_demo.png

      (From Left to Right) Smooth, Smoother, Sphere, Root,
      Sharp, Linear, Sharper, Inverse square, Constant.

Falloff Shape
   Use projected or spherical falloff.
   Note, this is not supported in Texture Paint Mode.

   :Sphere:
      Applies brushes influence in a sphere, outwards from the center.
   :Projected:
      This turns the brush influence into a cylinder (the depth along the view is ignored) instead of a sphere.
      It can be used along the outline of a mesh to adjust its silhouette.


Normal Falloff
==============

As faces point away from the view the brush strokes fade away to prevent harsh edges.

Angle
   The angle at which the falloff begins.
