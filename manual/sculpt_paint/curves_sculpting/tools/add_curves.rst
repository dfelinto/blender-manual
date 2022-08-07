
**********
Add Curves
**********

Used to distribute new curves on the surface mesh.
This tool requires the curve to have a :doc:`surface </sculpt_paint/curves_sculpting/introduction>` object set.

The curves follow the surface normals. Using the interpolation options allows the brush to take the characteristics
of existing curves.


Brush Settings
==============

.. _bpy.types.BrushCurvesSculptSettings.add_amount:

Count
   Number of curves added.

.. note::

   Interpolation allows to add hair which are already combed. The new curves are created
   following the previously created curves which are in the vicinity.

.. _bpy.types.BrushCurvesSculptSettings.interpolate_length:

Interpolate Length
   Use the average length of the curves in close proximity.

.. _bpy.types.BrushCurvesSculptSettings.interpolate_shape:

Interpolate Shape
   Use the average shape of the curves in close proximity.

.. _bpy.types.BrushCurvesSculptSettings.interpolate_point_count:

Interpolate Point Count
   Use the average amount of control points of the curves in close proximity.

.. _bpy.types.BrushCurvesSculptSettings.curve_length:

Curve Length
   Length of newly added curves when not interpolated.

.. _bpy.types.BrushCurvesSculptSettings.points_per_curve:

Points per Curve
  Number of Control Points for the new created curves when the point count is not interpolated.
