
************
Introduction
************

Freestyle is an edge/line-based non-photorealistic (NPR) rendering engine.
It relies on mesh data and Z-depth information to draw lines on selected edge types.
Various line styles can be added to produce artistic ("hand drawn", "painted", etc.)
or technical (hard line) looks.

The two operating modes: :doc:`Python Scripting </render/freestyle/python>` and
:doc:`Parameter Editor </render/freestyle/parameter_editor/index>` --
allow a powerful diversity of line styles and results. Line styles such as Japanese big brush, cartoon, blueprint,
thickness-with-depth are already pre-scripted in Python. The Parameter Editor mode allows intuitive editing of
features such as dotted lines and easy setup of multiple line types and edge definitions.
On top of all of that, with line style modifiers, the sky is the limit!

.. list-table::

   * - .. figure:: /images/render_freestyle_introduction_example-1.png

          ATV buggy by Rylan Wright (RONIN). CC BY.
          (`File:AtvBuggy.zip <https://wiki.blender.org/wiki/File:AtvBuggy.zip>`__)

     - .. figure:: /images/render_freestyle_introduction_example-2.png

          By mato.sus304. CC BY-SA.
          (`File:Mato_sus304_cut02.zip <https://wiki.blender.org/wiki/File:Mato_sus304_cut02.zip>`__)

   * - .. figure:: /images/render_freestyle_introduction_example-3.png

          A cartoon scene from `OHA Studio <http://oha-studios.com/>`__
          © Mechanimotion Entertainment.
          (`blend-file <https://download.blender.org/demo/test/FreeStyle_demo_file.blend.zip>`__)

     - .. figure:: /images/render_freestyle_introduction_example-4.png

          Blueprint render of Martin M-130 from 1935 by LightBWK. CC0. Warning:
          heavy file! designed for stress test Blender to the limits and may crash Blender.
          (`File:M-130Blueprint.zip <https://wiki.blender.org/wiki/File:M-130Blueprint.zip>`__)


The Big Picture
===============

- Activate Freestyle by the :menuselection:`Properties --> Render --> Freestyle` checkbox.
- Freestyle settings are located in the :doc:`View Layer </scene_layout/view_layers/index>` properties.
- One view layer can only have one view map. A view map holds the edge detection settings
  (Crease Angle, Culling toggle, Face Smoothness toggle, Material Boundaries toggle,
  Sphere Radius, and Kr Derivative Epsilon advanced options).
- A view map can have multiple Line Sets.
- A line set controls which line types and selections will be rendered, from lines based on your scene.
- Each line set uses one line style (which can be shared between multiple Line Sets).
- A line style tells Freestyle how to render the linked Line Sets in terms of color, alpha,
  thickness and other aspects.

.. figure:: /images/render_freestyle_introduction_view-map-processes.png

   Block diagram of Freestyle view map and processes.


Known Limitations
=================

- Highly memory demanding: All mesh objects in a view layer are loaded at once.
- Only faced mesh objects are supported.
- No edges at face intersections are detected yet.
- Freestyle rendering results do not have any Z depth information.
- Panoramic cameras are not supported.
