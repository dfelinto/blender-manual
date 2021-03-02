.. _bpy.types.SceneEEVEE.bokeh_max_size:

**************
Depth of Field
**************

To render a scene, EEVEE uses a pinhole camera model which produces a perfectly focused image of the scene.
To improve realism, EEVEE can simulate the optical :term:`Depth of Field` using a post-process filter, and a sample based method.
The optical settings can be controlled in the :doc:`camera settings </render/cameras>`.
The quality of the effect can be controlled using the settings found in the present section.

.. note::

   In the 3D Viewport, depth of field only works while in Camera View.

The post-process method is computed in two passes.
The first pass is using a blur that fails to produce quality bokeh for highlights but works for the general case.
The second pass is sprite based and is reserved for very bright highlights to improve their quality.
However is too slow to use for every part of the image.
So it is only applied to very bright parts of the image that are different from their surroundings.
The *Sprite Threshold* and *Neighbor Rejection* parameters control which pixels are being processed by second pass.

The sample based method works by randomizing the camera position for every sample.
It is more accurate but needs many samples to achieve smooth results.
The post-process blurring radius is scaled down accordingly to remove under-sampling.
However, some scenes might still need more post-process blur in order to remove the noticeable sample pattern.
This is exactly what the *Overblur* option does, but it will also reduce the bokeh shape sharpness.

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Render --> Depth of Field`

Max Size
   Maximum size in pixels of the depth of field post-process effect (lower is faster).
   A value of 0 will disable the post-process effect but not the sample based method.

Sprite threshold
   Minimum brightness a pixel needs to have to be considered by the sprite based depth of field.
   Higher values will improve performance but will reduce highlight quality.
   Brightness is in scene referred color-space.

Neighbor Rejection
   Maximum intensity to consider when doing sprite neighborhood rejection.
   This should be set to a brightness value above which there is little visual differences to be noticeable after color management.
   Lower values will improve performance but will reduce highlight quality.
   Brightness is in scene referred color-space.

Denoise Amount
   This will reduce the flickering by clamping the color of each pixels to their neighborhood's average instead of their maximum.
   Higher values gives more stable results but may darken the scene.

High Quality Slight Defocus
   Increase the quality of almost in-focus regions.

Jitter Camera
   Randomize the camera position for every scene render sample to increase precision.
   Enabling this option can change the scene's actual sample count.

   .. note::

      Be aware that the actual sample count can grow quite rapidly.

   .. hint::

      The actual number of samples is computed by the following formula:

      .. math::

         sample\_count = (ring\_count^{2} + ring\_count) * 3 + 1

      where :math:`ring\_count` is the number of ring in the hexaweb pattern.
      The :math:`ring\_count` is chosen so that the entire pattern contains at least the number of samples set in :doc:`render settings </render/sampling>`.

Overblur
   Scales the post process depth of field radius to reduce artifacts. Higher values will soften the bokeh shape.

.. seealso:: :ref:`Limitations <eevee-limitations-dof>`.
