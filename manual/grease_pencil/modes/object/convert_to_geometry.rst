.. _bpy.ops.gpencil.convert:

*******************
Convert to Geometry
*******************

.. admonition:: Reference
   :class: refbox

   :Mode:      Object Mode
   :Menu:      :menuselection:`Object --> Convert --> Path, Bézier Curve, Polygon Curve`

In the 3D Viewport, sketches on the active layer can be converted to geometry,
based on the current view settings, by transforming the points recorded when drawing
(which make up the strokes) into 3D space. Currently, all points will be used,
so it may be necessary to simplify or subdivide parts of the created geometry for standard use.
Sketches can currently be converted into curves in Object Mode.


Options
=======

Type
   The type of object to convert to.

   Path
      Create NURBS 3D curves of order 2 (i.e. behaving like polylines).
   Bézier Curve
      Create Bézier curves, with free "aligned" handles (i.e. also behaving like polylines).
   Polygon Curve
      Bézier curve with straight line segments (auto handles).

   .. note:: Converting to Mesh

      If you want to convert your sketch to a mesh,
      simply choose *NURBS* first, and then convert the created curve to a mesh.

Bevel Depth
   The :ref:`Bevel Depth <bpy.types.Curve.bevel_depth>` to use for the converted curve object.

Bevel Resolution
   The :ref:`Bevel Resolution <bpy.types.Curve.bevel_resolution>` to use for the converted curve object.

Normalize Weight
   Will scale weights value so that they fit into the (0.0 to 1.0) range.

Radius Factor
   Multiplier for the points' radii (set from the stroke's width).

Link Strokes
   Will create a single spline, i.e. curve element, from all strokes in active Grease Pencil layer.
   This is especially useful if you want to use the curve as a path.
   All the strokes are linked in the curve by "zero weights/radii" sections.


Timing
------

Grease Pencil stores "dynamic" data, i.e. how fast strokes are drawn.
When converting to curve, this data can be used to create an *Evaluate Time* F-curve
(in other words, a path animation), that can be used
e.g. to control another object's position along that curve
(*Follow Path* constraint, or, through a driver, *Curve* modifier).
So this allows you to reproduce your drawing movements.

*Link Strokes* has to be enabled for all timing options.

Timing Mode
   This control lets you choose how timing data is used.

   No Timing
      Just create the curve, without any animation data (hence all following options will be hidden).
   Linear
      The path animation will be a linear one.
   Original
      The path animation will reflect to original timing, including for the "gaps"
      (i.e. time between strokes drawing).
   Custom Gaps
      The path animation will reflect to original timing, but the "gaps" will get custom values.
      This is especially useful if you want to shorten large pauses between some strokes.

Frame Range
   The "length" of the created path animation, in frames. In other words, the highest value of *Evaluation Time*.
Start Frame
   The starting frame of the path animation.
Realtime
   When enabled, the path animation will last exactly the same duration it has taken you to draw the strokes.
End Frame
   When *Realtime* is disabled, this defines the end frame of the path animation.
   This means that the drawing timing will be adjusted to fit into the specified range.
Gap Duration
   *Custom Gaps* only. The average duration (in frames) of each gap between strokes.
   Please note that, the value will only be exact if *Realtime* is enabled,
   otherwise it will be scaled, exactly as the strokes' timing is.


Example
=======

Here is a simple "hand writing" video created with curves converted from sketch data:

.. youtube:: VwWEXrnQAFI

The blend-file from the above example can be found
`here <https://wiki.blender.org/wiki/File:ManGreasePencilConvertToCurveDynamicExample.blend>`__.
