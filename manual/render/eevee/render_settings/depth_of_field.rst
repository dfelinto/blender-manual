.. _bpy.types.SceneEEVEE.bokeh_max_size:

**************
Depth of Field
**************

Depth of field is done as a post-process effect in Eevee.
The depth of field effect can be controlled in the :doc:`camera settings </render/cameras>`.

.. note::

   In the 3D Viewport, depth of field only works while in Camera View.

.. note::

   Because of performance considerations, the viewport can exhibit color artifacts when using large bokeh sizes.
   These artifacts are not present in the final render.

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Render --> Depth of Field`

Max Size
   Max size of the bokeh shape for the depth of field (lower is faster).

.. seealso:: :ref:`Limitations <eevee-limitations-dof>`.
