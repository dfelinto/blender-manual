.. _bpy.types.SceneEEVEE.motion_blur:

***********
Motion Blur
***********

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Render --> Motion Blur`

Blender's animations are by default rendered as a sequence of *perfectly still* images.
While great for stop-motion and time-lapses, this is unrealistic, since fast-moving
objects do appear to be blurred in the direction of motion,
both in a movie frame and in a photograph from a real-world camera.

.. note::

   Motion blur is only available in final renders and is not shown in the 3D Viewport
   and thus :ref:`Viewport Renders <bpy.ops.render.opengl>`.

Position
   Controls at what point the shutter opens in relation to the current frame.

   Start on Frame
      Shutter is starting to open at the current frame.
   Center on Frame
      Shutter is fully opened at the current frame.
   End on Frame
      Shutter is fully closed at the current frame.

Shutter
   Time (in frames) taken between shutter open and close.

Background Separation
   Used by the post-process blur to avoid blurring the background over the foreground.
   Lower values will reduce background bleeding onto foreground elements.

Max Blur
   Maximum blur distance a pixel can spread over.
   A value of 0 will disable the post-process blur and only use the accumulation blur.

   .. note::

      High maximum blur values may also reduce the quality.

   It uses a fast post-process vector blur using a vector motion pass.
   This blurs the image between three time steps using pixel velocity.
   This technique is fast and produce clean gradients but issues can occur at object borders
   or if the motion is locally too complex (many vector variations in a small area).

   This technique uses random sampling and the noise amount is proportional to the sample count found in
   :menuselection:`Properties --> Render --> Sampling --> Render Samples`.

   .. note::

      Memory usage (VRAM) will be three times higher for objects using deformation motion blur
      if using post-process blur.

   .. note::

      Alpha blended surface or volumetric effects will not have the correct velocity and will not
      be correctly blurred by this technique. Use the accumulation blur for that.

Steps
   This controls the number of steps used by the accumulation blur and thus its accuracy.
   More steps means longer render time.

   .. note::

      When using multiple time steps, the render sample count is rounded up to the next multiple
      of steps to ensure even distribution of samples across steps.

   Eevee splits the render into multiple time steps and accumulates the result
   which is known as Accumulation Motion Blur.
   This technique is precise but requires many steps for clean gradients.
   This is used in combination with the post-process blur to handle the inter-step gaps.
   Each step corresponds to a full scene re-evaluation and can add a lot of overhead to the render time.
   By adding more steps you can also reduce the *Max Blur* options because the post-process blur
   has to cover a smaller distance.


Example
=======

.. _fig-render-motion-blur-properties-example:

.. list-table::

   * - .. figure:: /images/render_eevee_render-settings_motion-blur_1step-nofx.png
          :width: 310px

          No motion blur.

     - .. figure:: /images/render_eevee_render-settings_motion-blur_1step-fx.png
          :width: 310px

          Only post-process blur.

   * - .. figure:: /images/render_eevee_render-settings_motion-blur_4step-nofx.png
          :width: 310px

          4 time steps without post-process blur.

     - .. figure:: /images/render_eevee_render-settings_motion-blur_4step-fx.png
          :width: 310px

          4 time steps with post-process blur.

   * - .. figure:: /images/render_eevee_render-settings_motion-blur_32step-nofx.png
          :width: 310px

          32 time steps without post-process blur.

     - .. figure:: /images/render_eevee_render-settings_motion-blur_32step-fx.png
          :width: 310px

          32 time steps with post-process blur.
