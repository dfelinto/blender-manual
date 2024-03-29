.. _bpy.ops.scene.view_layer:
.. _bpy.types.ViewLayer:
.. _render-layers:

************
Introduction
************

Renders can be separated into layers, to composite them back together afterwards.

Some example usages are applying compositing effects to characters separately,
blurring the background and foreground layers separately for depth of field,
or rendering different lighting variations of the same scene.

Using View Layers can also save you from having to re-render your entire image after each change,
allowing you to instead re-render only the layer(s) that you have altered.


View Layers
===========

.. figure:: /images/render_layers_introduction_list.png

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


Usage
=====

Each :doc:`Scene </scene_layout/scene/introduction>` has an associated set of
:doc:`Collections </scene_layout/collections/collections>`.
The visibility settings of each collection can be changed per View Layer to separate the
rendering of different objects and lights into layers.


Collections
===========

Per collection you can adjust the way how the render engine needs to render the objects inside.
Based on the render engine different options can be set.

.. figure:: /images/render_layers_introduction_viewlayer-collection.png

   Collection/View layer settings.

Disable from View Layer
   Remove this collection from the active view layer. Objects that are only in
   this collection will not be rendered for the active view layer.
   This is useful to sometimes leave out some object influence for a particular view layer.

Enable in View Layer
   Add this collection to the active view layer. Objects inside the collection
   will be rendered with the active view layer.

.. _bpy.ops.outliner.collection_holdout_set:

Set Holdout
   Objects inside this collection will generate a holdout/mask in the active view layer.

.. _bpy.ops.outliner.collection_holdout_clear:

Clear Holdout
   Clear the Set Holdout flag.

.. _bpy.ops.outliner.collection_indirect_only_set:

Set Indirect Only :guilabel:`Cycles Only`
   Objects inside this collection will only contribute to the final image
   indirectly through shadows and reflections.

.. _bpy.ops.outliner.collection_indirect_only_clear:

Clear Indirect Only :guilabel:`Cycles Only`
   Clear the *Indirect Only* flag. Objects inside this collection will contribute normally to the final image.


Cycles
======

.. reference::

   :Panel:     :menuselection:`View Layers --> Layer`

This section covers only the Render Layer settings appropriate for the Cycles renderer.
For the engine-independent settings, see :ref:`this section <render-layers>`.


Filter
------

.. _bpy.types.ViewLayer.use_sky:

Include
   Environment
      Disables rendering the *Environment* render pass in the final render.

   .. _bpy.types.ViewLayer.use_solid:

   Surfaces
      Disables rendering object materials in the final render.

   .. _bpy.types.ViewLayer.use_strand:

   Curves
      Disables rendering curve strands in the final render.

   .. _bpy.types.ViewLayer.use_volumes:

   Volume
      Disables rendering :doc:`Volumes </modeling/volumes/index>` in the final render.

.. _bpy.types.ViewLayer.use_motion_blur:

Use
   Motion Blur
      Render motion blur for this Layer,
      if enabled in the :ref:`Render Settings <bpy.types.RenderSettings.use_motion_blur>`.


Override
--------

.. _bpy.types.ViewLayer.material_override:

Material Override
   Overrides all materials in the render layer.

.. _bpy.types.ViewLayer.samples:

Samples
   View layer samples to override the scene samples.
   Controlled by the :ref:`layer samples <bpy.types.CyclesRenderSettings.use_layer_samples>` in the Sampling panel.
