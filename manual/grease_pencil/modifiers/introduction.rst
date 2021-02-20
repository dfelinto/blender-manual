.. index:: Grease Pencil Modifiers
.. index:: Modifiers; Grease Pencil Modifiers

************
Introduction
************

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Properties --> Modifiers`

Grease Pencil has their own set of modifiers.
Modifiers are automatic operations that affect an object in a non-destructive way.
With modifiers, you can perform many effects automatically that would otherwise be
too tedious to do manually and without affecting the base geometry of your object.

They work by changing how an object is displayed and rendered, but not the geometry which you can edit directly.
You can add several modifiers to a single object forming the modifier stack
and *Apply* a modifier if you wish to make its changes permanent.

.. figure:: /images/grease-pencil_modifiers_introduction_menu.png

   Grease Pencil Modifiers menu.

There are three types of modifiers for Grease Pencil:

Generate
   The *Generate* group of modifiers includes constructive tools that either change
   the general appearance of or automatically add new geometry to an object.
Deform
   The *Deform* group of modifiers only changes the shape of an object without adding new geometry,
Color
   The *Color* group of modifiers change the object color output.


.. _bpy.ops.object.gpencil_modifier_apply:

Interface
=========

.. figure:: /images/grease-pencil_modifiers_introduction_interface.png

   Panel layout (Thickness modifier as an example).

Each modifier's interface shares the same basic components like modifiers for meshes.

See :ref:`Modifiers Interface <bpy.types.Modifier.show>` for more information.

.. note::

   Grease Pencil strokes, unlike meshes, still can not be edited directly in the place.


.. _grease-pencil-modifier-influence-filters:

Influence Filters
-----------------

Most of the modifiers share some special properties that restrict the effect only to certain items.

Layer
   Restricts the effect only to one layer or to any layers that share the same
   material :ref:`Pass Index <bpy.types.MaterialGPencilStyle.pass_index>`.

Material
   Restricts the effect only to material that share the same material or
   material :ref:`Pass Index <bpy.types.MaterialGPencilStyle.pass_index>`.

Vertex Group
   Restricts the effect only to a vertex group.

Custom Curve
   When enabled, use a custom curve to shape the effect along the strokes
   from start to end points.

The Invert toggle ``<->`` allows you to reverse the filters behavior.
