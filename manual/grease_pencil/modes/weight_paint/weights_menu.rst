
************
Weights Menu
************

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Weights`

This page covers many of the tools in the *Weights* menu.


Normalize All
=============

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Weights --> Normalize All`

For each point, this tool makes sure that the sum of the weights across all vertex groups is equal to 1.
It normalizes all of the vertex groups, except for locked groups, which keep their weight values untouched.

Lock Active
   Keep the values of the active group while normalizing all the others.


Normalize
=========

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Weights --> Normalize`

This tool only works on the active vertex group.
All points keep their relative weights, but the entire set of weights is scaled up
such that the highest weight value is 1.0.


Invert
======

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Weights --> Invert`

Replaces each weight of the selected vertex group by × -1.0 weight.

Examples:

- Original 1.0 converts to 0.0
- Original 0.5 remains 0.5
- Original 0.0 converts to 1.0

Subset
   Restrict the tool to a subset.
   See :ref:`The Subset Option <bpy.ops.object.vertex_group_levels>` about how subsets are defined.
Add Weights
   Add vertices that have no weight before inverting (these weights will all be set to 1.0).
Remove Weights
   Remove vertices from the vertex group if they are 0.0 after inverting.


Smooth
======

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Weights --> Smooth`

Smooths the weights of the active vertex group.


Generate Weights
================

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Weights --> Generate Weights`

Generate automatic weight for armatures (requires an Armature modifier).

With Empty Group
   When parenting it will create an empty vertex groups on the child objects (if they do not exist already)
   for and named after each deforming bone in the armature.

With Automatic Weights
   Works similar to *With Empty Groups*, but it will not leave the vertex groups empty.
   It calculates how much influence a particular bone would have on points based on the distance
   from those points to a particular bone ("bone heat" algorithm).
   This influence will be assigned as weights in the vertex groups.
