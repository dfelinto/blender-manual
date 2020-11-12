.. _bpy.ops.scene.view_layer:
.. _bpy.types.ViewLayer:
.. _render-layers:

***********
View Layers
***********

Renders can be separated into layers, to composite them back together afterwards.

Some example usages are applying compositing effects to characters separately,
blurring the background and foreground layers separately for depth of field,
or rendering different lighting variations of the same scene.

Using View Layers can also save you from having to re-render your entire image each time you change something,
allowing you to instead re-render only the layer(s) that you need.


View Layers
===========

.. figure:: /images/render_layers_layers_list.png

   View Layers.

In the top of the screen there is a list of all the View Layers in the active scene.

.. _bpy.types.ViewLayer.name:

Name
   The name of the active view layer, click to edit the name.

.. _bpy.ops.scene.view_layer_add:

Add View Layer
   Will add a new view layer to the active scene.

   New
      Adds a new view layer.
   Copy Settings
      Adds a new view layer with all the settings of current view layer.
   Blank
      Adds a new view layer with all collections disabled.

.. _bpy.ops.scene.view_layer_remove:

Remove View Layer
   Will remove the selected view layer from the active scene.

   .. note::

      A scene must have at least one view layer.


View Layer Panel
================

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Properties --> Scene --> View Layer`

.. figure:: /images/render_layers_layers_panel.png

   View Layer panel (shown here for the Eevee render engine)

The Layer Panel shows the settings of the active View Layer.

Use for Rendering
   The active view layer will be used during rendering.

Render Single Layer
   Only render the active view layer.

   .. note::

      This option is ignored when rendering from the command line.

.. seealso::

   Additional options shown in this panel are different for each render engine.
   See :doc:`Render Passes </render/layers/passes>` for the options per render engine.


Usage
=====

Each Render Layer has an associated set of :doc:`Collections </scene_layout/collections/collections>`.
Objects which are on one of the associated collections are shown in that Render Layer,
as long as that collection is also visible.

.. warning::

   Only the objects in visible Scene Layers will be rendered.
   So, if only Collection 1 is visible and your Render Layer set specifies to render only Collections 2 and 3,
   nothing will be rendered.


Collections
===========

Per collection you can adjust the way how the render engine needs to render the objects inside.
Based on the render engine different options can be set.

.. figure:: /images/render_layers_layers_viewlayer-collection.png

   Collection/View layer settings

.. _bpy.ops.outliner.collection_exclude_set:

Disable from View Layer
   Remove this collection from the active view layer. Objects that are only in
   this collection will not be rendered for the active view layer.

.. _bpy.ops.outliner.collection_exclude_clear:

Enable in View Layer
   Add this collection to the active view layer. Objects inside the collection
   will be rendered with the active view layer.

.. _bpy.ops.outliner.collection_indirect_only_set:

Set Indirect Only
   Objects inside this collection will only contribute to the final image
   indirectly through shadows and reflections.

.. _bpy.ops.outliner.collection_indirect_only_clear:

Clear Indirect Only
   Clear the *Indirect Only* flag. Objects inside this collection will contribute normally to the final image.

.. _bpy.ops.outliner.collection_holdout_set:

Set Holdout
   Objects inside this collection will generate a holdout/mask in the active view layer.

.. _bpy.ops.outliner.collection_holdout_clear:

Clear Holdout
   Clear the Set Holdout flag.


Cycles
======

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`View Layers --> Layer`

This section covers only the Render Layer settings appropriate for the Cycles renderer.
For the engine-independent settings, see :ref:`this section <render-layers>`.


View Layer
----------

Exclude
   Scene layers are shared between all render layers;
   however, sometimes it is useful to leave out some object influence for a particular render layer.


.. _bpy.types.ViewLayer.use_sky:
.. _bpy.types.ViewLayer.use_ao:
.. _bpy.types.ViewLayer.use_solid:
.. _bpy.types.ViewLayer.use_strand:

Filter
------

Include
   Environment
      Disables rendering the *Environment* render pass in the final render.
   Ambient Occlusion
      Disables rendering the *Ambient Occlusion* render pass in the final render.
   Surfaces
      Disables rendering object materials in the final render.
   Hair
      Disables rendering hair strands in the final render.
   Volume
      Disables rendering :doc:`Volumes </modeling/volumes/index>` in the final render.


.. _bpy.types.ViewLayer.material_override:
.. _bpy.types.ViewLayer.samples:

Override
--------

Material Override
   Overrides all materials in the render layer.
Samples
   View layer samples to override the scene samples.
   Controlled by the :ref:`layer samples <render-cycles-integrator-layer-samples>` in the sampling panel.
