.. index:: Grease Pencil Modifiers; Offset Modifier
.. _bpy.types.OffsetGpencilModifier:

***************
Offset Modifier
***************

The *Offset* Modifier changes the strokes location, rotation or scale
starting from the object origin.


Options
=======

.. figure:: /images/grease-pencil_modifiers_deform_offset_panel.png
   :align: right

   Offset Modifier.

Location X, Y, Z
   Sets strokes location offset from its object origin.

Rotation X, Y, Z
   Sets strokes rotation.

Scale X, Y, Z
   Sets strokes scale.

Randomize
---------

Offset X, Y, Z
   Add random offset values to the strokes.

Rotation X, Y, Z
   Add random rotation values to the strokes.

Scale X, Y, Z
   Add random scale values to the strokes.

Uniform Scale
   Use the same random *Seed* for each scale axis in the strokes for a uniform scale.

Seed
   :term:`Seed` used by the pseudo-random number generator.


Influence
---------

See :ref:`grease-pencil-modifier-influence-filters`.
