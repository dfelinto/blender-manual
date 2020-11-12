
***************
Viewport Render
***************

Viewport rendering uses the 3D Viewport rendering for quick *preview* renders.

This allows you to inspect your animatic
(for object movements, alternate angles, etc.).

This can also be used to preview your animations --
in the event your scene is too complex for your system to play back in real-time in the 3D Viewport.

You can use *Viewport Render* to render both images and animations.

Below is a comparison between the Viewport render and a final render using
the Cycles Renderer.

.. list-table:: Model by © 2016 pokedstudio.com

   * - .. figure:: /images/editors_3dview_viewport-render_example-workbench-render.jpg
          :width: 320px

          Viewport render using Solid Mode.

     - .. figure:: /images/editors_3dview_viewport-render_example-eevee-render.jpg
          :width: 320px

          Viewport render using Material Preview Mode.

     - .. figure:: /images/editors_3dview_viewport-render_example-cycles-render.jpg
          :width: 320px

          Full render.

.. tip::

   Disable overlays to render the viewport without any additional overlays.

   While this option is not specific to Viewport rendering, it's often useful to
   enable, since it removes data such as rigs and empties that can be a distraction.


Settings
========

For the most part, *Viewport Render* uses the current viewport settings.
Some settings are located in the render panel of the render engine
that is used to render the view.

Solid mode uses the render settings of Workbench;
Material Preview mode uses the render settings of Eevee.

Sampling and Alpha Transparency Mode options can be set in :menuselection:`Properties --> Render --> Sampling`.
Make sure the Workbench or Eevee render engine is selected to see the appropriate values.

Additionally, some render settings are used too:

- Render Dimensions
- Render Aspect
- File Format & Output (file path, format, compression settings, etc.)


Rendering
=========

Activating *Viewport Render* will render from the current active view.
This means that if you are not in an active camera view then
a virtual camera is used to match the current perspective.
To get an image from the camera point of view,
enter the active camera view with :kbd:`Numpad0`.

As with a normal render, you can abort it with :kbd:`Esc`.

.. _bpy.ops.render.opengl:

Render a Still Image
   To render a still image, use :menuselection:`3D Viewport --> View --> Viewport Render Image`.
Render an Animation
   to render an animation, use :menuselection:`3D Viewport --> View --> Viewport Render Animation`.
Render Keyframes
   To render an animation, but only those frames that have a keyframe,
   use :menuselection:`3D Viewport --> View --> Viewport Render Keyframes`.
   This only renders those frames for which the selected objects have an animation key.
   The other frames are still written to the output, but will simply repeat the last-rendered frame.

   For example, when a six-frame animation is rendered, and the selected objects
   have a key on frames 3 and 5, the following frames will be output:

   1. The 1st frame is always rendered.
   2. The 1st frame is repeated because there is no key on this frame.
   3. The 3rd frame is rendered.
   4. The 3rd frame is repeated because there is no key on this frame.
   5. The 5th frame is rendered.
   6. The 5th frame is repeated because there is no key on this frame.

.. tip::

   You can limit the viewport render to a particular region with
   :ref:`Render Regions <editors-3dview-navigate-render-region>`.
