
************
Introduction
************

Eevee is Blender's realtime render engine built using :term:`OpenGL` focused on
speed and interactivity while achieving the goal of rendering :abbr:`PBR (Physically Based Rendering)` materials.
Eevee can be used interactively in the 3D Viewport but also produce high quality final renders.

.. figure:: /images/render_eevee_introduction_viewport.png

   Eevee in the 3D Viewport -- "Tiger" by Daniel Bystedt.

Eevee materials are created using the same shader nodes as Cycles, making it easy to render existing scenes.
For Cycles users, this makes Eevee work great for previewing materials in realtime.

Unlike Cycles, Eevee is not a raytrace render engine.
Instead of computing each ray of light, Eevee uses a process called rasterization.
Rasterization estimates the way light interacts with objects and materials using numerous algorithms.
While Eevee is designed to use :abbr:`PBR (Physically Based Rendering)` principles,
it is not perfect and Cycles will always provide more physically accurate renders.
Because Eevee uses rasterization it has a large set of :doc:`limitations </render/eevee/limitations>`.

.. figure:: /images/render_eevee_introduction_final-render.png

   Eevee final render -- "Temple" by Dominik Graf.
