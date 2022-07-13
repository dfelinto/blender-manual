
**********
Add Curves
**********

Used to distribute new curves on the surface mesh.
This tool requires the curve to have a :doc:`Surface </sculpt_paint/curves_sculpting/introduction>`,
commonly used for hair scalp.

The curves follow the Surface normals and can be used to expand existent curve interpolating their characteristics.


Brush Settings
==============

.. _bpy.types.BrushCurvesSculptSettings.add_amount:

Count
   Number of curves added.

.. note::

   Interpolation allows to add hair which is already combed. The new hair is then created
   following the previously created hair which are in the vicinity.

.. _bpy.types.BrushCurvesSculptSettings.interpolate_length:

Interpolate Length
   Use length of the curves in close proximity.

.. _bpy.types.BrushCurvesSculptSettings.interpolate_shape:

Interpolate Shape
   Use shape and the amount of control points of the curves in close proximity.

.. _bpy.types.BrushCurvesSculptSettings.interpolate_point_count:

Interpolate Point Count
   Use the amount of control points of the curves in close proximity.

.. _bpy.types.BrushCurvesSculptSettings.curve_length:

Curve Length
   Length of newly added curves when not interpolated.

.. _bpy.types.BrushCurvesSculptSettings.points_per_curve:

Points per Curve
  Number of Control Points for the new created curves when the shape is not interpolated.
