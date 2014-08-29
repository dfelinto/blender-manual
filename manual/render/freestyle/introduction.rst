
Introduction
************

What is FreeStyle?
==================

Freestyle is an edge- and line-based non-photorealistic (NPR) rendering engine.
It relies on mesh data and z-depth information to draw lines on selected edge types.
Various line styles can be added to produce artistic ("hand drawn", "painted", etc.)
or technical (hard line) looks.

The two operating modes - :doc:`Python Scripting </render/freestyle/python>` and
:doc:`Parameter Editor </render/freestyle/parameter_editor>` -
allow a powerful diversity of line styles and results. Line styles such as Japanese big brush, cartoon, blueprint,
thickness-with-depth are already pre-scripted in Python. The Parameter Editor mode allows intuitive editing of
features such as dotted lines and easy setup of multiple line types and edge definitions. On top of all of that,
with the introduction of line style modifiers, the sky is the limit!


.. figure:: /images/Manual-2.6-Render-Freestyle-Demo-OHACartoon.jpg
   :width: 600px
   :figwidth: 600px

   A cartoon scene from `OHA Studio <http://oha-studios.com/>`__
   (`the .blend file <http://download.blender.org/demo/test/freestyle_demo_file.blend.zip>`__).
   © Mechanimotion Entertainment.


.. figure:: /images/Manual-2.6-Render-Freestyle-Demo-BluePrint.jpg
   :width: 600px
   :figwidth: 600px

   Blueprint render of Martin M-130 from 1935 by LightBWK. CC0. WARNING:
   HEAVY FILE! DESIGNED FOR STRESS TEST BLENDER TO THE LIMITS & MAY CRASH BLENDER.
   (`File:M-130Blueprint.zip <http://wiki.blender.org/index.php/File:M-130Blueprint.zip>`__)


.. figure:: /images/Manual-2.6-Render-Freestyle-Demo-HVACPreViz.jpg
   :width: 600px
   :figwidth: 600px

   HVAC Pre-Viz by Lee Posey. CC0 (`File:HVACPreViz.zip <http://wiki.blender.org/index.php/File:HVACPreViz.zip>`__)


.. figure:: /images/Manual-2.6-Render-Freestyle-Demo-KitchenSet.jpg
   :width: 600px
   :figwidth: 600px

   Kitchen by Vicente Carro. © AnigoAnimation


More artwork can be found at
http://wiki.blender.org/index.php/Dev:Ref/Release_Notes/2.67/FreeStyle#Freestyle_Artwork_Showcase


The Big Picture
===============

- Activate FreeStyle by :guilabel:`Properties` window → :guilabel:`Render` tab → :guilabel:`FreeStyle` panel,
  tick check box. Please note that FreeStyle is only available for the Blender Internal renderer.
- Freestyle settings are located in the new :guilabel:`Render Layers` context.
- One render layer can only have one viewmap. A viewmap holds the edge detection settings (Crease Angle,
  Culling toggle, Face Smoothness toggle, Material Boundaries toggle,
  Sphere Radius and Kr Derivative Epsilon advanced options).
- A viewmap can have multiple line sets.
- A line set controls which line types and selections will be rendered, from lines based on your scene.
- Each line set uses one line style (which can be shared between multiple line sets).
- A line style tells Freestyle how to render the linked line sets in terms of color, alpha, thickness and other aspects.


.. figure:: /images/FreeStyle_Block_Diagram.jpg
   :width: 400px
   :figwidth: 400px

   block diagram of Freestyle view map and processes


Known Limitations and issues
============================

- FreeStyle is only available for the Blender Internal renderer.
- Highly memory demanding: All mesh objects in a render layer are loaded at once.
- Only faced mesh objects are supported.  The following kinds of meshes are ignored.
  - Mesh faces with wire materials.
  - Mesh faces with completely transparent materials.
- Transparent faces are treated as opaque faces.
- No edges at face intersections are detected yet.
- Layer masks do not work with Freestyle.
- Freestyle rendering results do not have any Z depth information.
- Does not work with a panoramic camera.
