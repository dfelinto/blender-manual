
Cycles Render Engine
********************

Cycles is a ray tracing renderer focused on interactivity and ease of use, while still supporting many production features.
FIXME(Link Type Unsupported: dev;
[[Dev:2.6/Source/Render/Cycles|Developer documentation]]
) is also available.


Getting Started
===============

Cycles is bundled as an addon that is enabled by default. To use Cycles,
it must be set as the active render engine in the top header. Once that is done,
interactive rendering can be started by setting a 3D view editor to draw mode Rendered.
The render will keep updating as material and object modifications are done.

.. toctree::

   getting_started.rst
   camera.rst
   materials/index.rst
   texture_editing.rst
   world.rst
   lamps.rst
   nodes/index.rst
   light_paths.rst
   integrator.rst
   reducing_noise.rst
   passes.rst
   experimental_features.rst
   gpu_rendering.rst
