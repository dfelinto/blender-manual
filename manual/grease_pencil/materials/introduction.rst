
************
Introduction
************

Materials control the appearance of the Grease Pencil object.
They define the base color and texture of the strokes and filled areas.

There is always only one active material in the list (the selected one).
When you draw, the new strokes use the active material.

You can override the base material color using the tools in
:doc:`Vertex Mode </grease_pencil/modes/vertex_paint/introduction>`
or the Draw and Tint tool in Draw Mode.

The material always remains linked to the strokes, this means that any change in a material will change
the look of already drawn strokes.

.. figure:: /images/grease-pencil_materials_introduction_sample.png

   Same stroke linked to different materials.


Grease Pencil Shader
====================

The Grease Pencil shader creates a material that can work
with strokes and/or filled areas of a Grease Pencil object.

Stroke and fill components has it own section panel and
they can be enabled with a checkbox on the panel header.

*Stroke* only has effect on the lines and *Fill* only on the areas
determined by closed lines (by connecting the lines start and end points).

.. note::

   The shader is not yet a BSDF capable shader and can only be setting up
   on the Material Properties panel (it is not a shader node).


Setting Up Materials
====================

.. reference::

   :Mode:      Drawing Mode
   :Panel:     :menuselection:`Material --> Material Slots`
   :Shortcut:  :kbd:`U`

Grease Pencil materials can be created in the :doc:`Material properties </editors/properties_editor>`
as any other materials in Blender.
See :doc:`Material assignment </render/materials/assignment>` for more information.

The 3D Viewport can be set to Material Preview or Rendered shading,
to interactively preview how the material looks in the scene.

Grease Pencil materials are data-blocks that can be :doc:`assigned </render/materials/assignment>`
to one or more objects, and different materials can be assigned to different strokes.

In Grease Pencil the :doc:`brush </grease_pencil/modes/draw/tools/index>`
settings together with the material used will define the look and feel of the final strokes.

Materials slots in the :ref:`List view <ui-list-view>` also have some extra controls
that help to work with materials while drawing or editing lines.


Common Settings
---------------

.. figure:: /images/grease-pencil_materials_introduction_slots-panel.png
   :align: right

   Grease Pencil material slots panel.

Next to the material name there are three icons buttons that control common properties of the material:

Lock (padlock icon)
   Toggle material from being editable.

Viewport/Render Visibility (eye icon)
   Toggle material visibility in the viewport and in render.

Onion Skinning (onion skin icon)
   Toggle the use of the material for :doc:`Onion Skinning </grease_pencil/properties/onion_skinning>`.


Specials
--------

Show All
   Turns on the visibility of every material in the list.

Hide Others
   Turns off the visibility of every material in the list except the active one.

Lock All
   Locks edition of all the materials in the list.

Unlock All
   Unlocks edition of all the materials in the list.

Lock Unselected
   Locks all materials not used in the selected strokes.

Lock Unused
   Locks and hides all unused materials.

Convert Materials to Vertex Color
   Only keeps necessary materials and convert all materials base color to vertex color.

Extract Palette from Vertex Color
   Add all used vertex color to a new Color Palette. See :ref:`ui-color-palette`.

Copy Material to Selected
   Copy the active material to the selected Grease Pencil object.

Copy All Materials to Selected
   Copy all materials to the selected Grease Pencil object.

Merge Similar
   Combines similar materials in the list and replace the strokes that use the one of
   the merged materials with the new one.

Remove Unused Slots
   Remove all unused materials.


Lock & Visibility General Controls
----------------------------------

Lock (padlock icon)
   Toggle whether the active material is the only one that can be edited.

Visibility (screen icon)
   Toggle whether the active material is the only one that can be edited and is visible.


Grease Pencil Shader
====================

Grease Pencil materials use a special :doc:`shader </grease_pencil/materials/properties>`
that define the appearance of the surface of the stroke and fill.
