
*****
World
*****

The world environment can emit light, ranging from a single solid color
to arbitrary textures.

In Eevee, the world lighting contribution is first rendered and
stored in smaller resolution textures before being applied to the objects.
This makes the lighting less precise than Cycles.

.. seealso::

   :doc:`Indirect Lighting </render/eevee/render_settings/indirect_lighting>`.
