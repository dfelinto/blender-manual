
******
Curves
******

.. reference::

   :Panel:     :menuselection:`Render --> Curves`

These are global settings that apply to all instances of particle hair systems.
The resolution of the strands is controlled by the step values in particle settings.
Each hair system uses the material identified in the particle settings.

.. _bpy.types.CyclesCurveRenderSettings.shape:

Shape
   :Rounded Ribbons:
      Render curves as flat ribbon with rounded normals, for fast rendering.
      Curves are subdivided with a fixed number of specified subdivisions.

      .. _bpy.types.CyclesCurveRenderSettings.subdivisions:

      Curve Subdivisions
         Number of subdivisions used in cardinal curve intersection (power of 2).

   :3D Curves:
      Render curves as circular 3D geometry, for accurate results when viewing curves close up.
      Curves are automatically subdivided until the curve is smooth.


Viewport Display
----------------

These settings control the curve rendering settings used when the 3D viewport is set to
:ref:`Material Preview <3dview-material-preview>`

.. include:: /render/eevee/render_settings/hair.rst
   :start-after: .. --- copy below this line ---
