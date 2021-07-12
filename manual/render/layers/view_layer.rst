
**********
View Layer
**********

.. reference::

   :Panel:     :menuselection:`Properties --> Scene --> View Layer`

.. figure:: /images/render_layers_view-layer_panel.png

   View Layer panel (shown here for the Eevee render engine).

The Layer Panel shows the settings of the active View Layer.

.. _bpy.types.ViewLayer.use:

Use for Rendering
   The active view layer will be used during rendering.

.. _bpy.types.RenderSettings.use_single_layer:

Render Single Layer
   Only render the active view layer.

   .. note::

      This option is ignored when rendering from the command line.

.. seealso::

   Additional options shown in this panel are different for each render engine.
   See :doc:`Render Passes </render/layers/passes>` for the options per render engine.
