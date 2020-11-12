
********
Settings
********

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Material --> Settings`


Renderer Settings
=================

While shading nodes control the appearance, these settings control the quality and algorithms
that each renderer uses to render the material.

- :doc:`Eevee specific settings </render/eevee/materials/settings>`
- :doc:`Cycles specific settings </render/cycles/material_settings>`


Pass Index
==========

Pass Index
   Index number for the *Material Index* :doc:`render pass </render/layers/passes>`.
   This can be used to give a mask to a material and then be read with
   the :doc:`ID Mask Node </compositing/types/converter/id_mask>` in the Compositor.


.. _render-materials-settings-viewport-display:

Viewport Display
================

These settings control the 3D Viewport display in solid shading.
They provide a faster alternative to full shader nodes,
which may be too heavy or distracting for tasks like modeling, layout or sculpting.

Color
   Diffuse or metal surface color.
Metallic
   Blends between a non-metallic and metallic material model.
   A value of 1.0 gives a fully specular reflection tinted with the base color,
   without diffuse reflection or transmission.
   At 0.0 the material consists of a diffuse or transmissive base layer, with a specular reflection layer on top.
Roughness
   Specifies microfacet roughness of the surface for metal and specular reflection.
