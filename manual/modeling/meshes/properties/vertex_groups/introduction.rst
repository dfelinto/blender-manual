
************
Introduction
************

.. figure:: /images/modeling_meshes_properties_vertex-groups_introduction_panel.png
   :align: right

   The Vertex Groups panel.

Vertex groups are mainly used to tag the vertices belonging
to parts of a mesh object or :term:`Lattice`. Think of the legs of a chair or
the hinges of a door, or hands, arms, limbs, head, feet, etc. of a character.
In addition you can assign different weight values
(in the range 0 to 1) to the vertices within a vertex group.
Hence vertex groups are sometimes also named 'weight groups'.


Usage
=====

Vertex groups are most commonly used for armatures.
But they are also used in many other areas of Blender, like for example:

- Armature deformation *(also called skinning)*
- Shape keys
- Modifiers
- Particle generators
- Physics simulations

.. seealso::

   :doc:`Skinning Mesh Objects </animation/armatures/skinning/introduction>`.

Many more usage scenarios are possible.
Actually you can use vertex groups for whatever makes sense to you.
In some contexts vertex groups can also be automatically generated
(e.g. for rigged objects). However, in this section we will focus
on manually created (user-defined) vertex groups.

.. note::

   Vertex groups only apply to mesh and lattice objects.
