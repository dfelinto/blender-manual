
*****
Shape
*****

.. figure:: /images/modeling_surfaces_properties_shape_resolution-panel.png
   :align: center

   Shape panel.

.. _bpy.types.Curve.resolution_v:

Resolution Preview U/V
   Resolution to use in the 3D Viewport.
Render U/V
   Just like :ref:`NURBS curves <curve-nurbs>`, *Resolution* controls the detail of the surface.
   The higher the *Resolution* the more detailed and smoother the surface is.
   The lower the *Resolution* the rougher the surface. However, here you have two resolution settings,
   one for each interpolation axis (U and V).

   You can adjust the resolution separately for both preview and render,
   to not slow things down in the viewport, but still get good render results.

   .. list-table::

      * - .. figure:: /images/modeling_surfaces_properties_shape_resolution-1x1-wire.png

             Resolution 1×1.

        - .. figure:: /images/modeling_surfaces_properties_shape_resolution-3x3-wire.png

             Resolution 3×3.

      * - .. figure:: /images/modeling_surfaces_properties_shape_resolution-1x1.png

             Resolution of 1 for both U and V.

        - .. figure:: /images/modeling_surfaces_properties_shape_resolution-3x3.png

             Resolution of 3 for both U and V.

.. seealso::

   The panels of the *Curve and Surface* tab are the same as for
   :doc:`curves </modeling/curves/introduction>`, just with fewer options...
