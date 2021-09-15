
****
Hair
****

.. reference::

   :Panel:     :menuselection:`Render --> Hair`

These are global settings that apply to all instances of hair systems.
The resolution of the strands is controlled by the step values in particle settings.
Each hair system uses the material identified in the particle settings.

.. _bpy.types.CyclesCurveRenderSettings.shape:

Shape
   :Rounded Ribbons:
      Render hair as flat ribbon with rounded normals, for fast rendering.
      Hair curves are subdivided with a fixed number of specified subdivisions.

      .. _bpy.types.CyclesCurveRenderSettings.subdivisions:

      Curve Subdivisions
         Number of subdivisions used in cardinal curve intersection (power of 2).

   :3D Curves:
      Render hair as 3D curve, for accurate results when viewing hair close up.
      Hair curves are automatically subdivided until the curve is smooth.
