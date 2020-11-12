.. index:: Object Constraints; Armature Constraint
.. _bpy.types.ArmatureConstraint:

*******************
Armature Constraint
*******************

*Armature* is the constraint version of the :ref:`Armature Modifier <bpy.types.ArmatureModifier>`,
exactly reproducing the weight-blended bone transformations and applying it to its owner orientation.
It can be used like a variant of the :ref:`Child Of <bpy.types.ChildOfConstraint>` constraint
that can handle multiple parents at once, but requires all of them to be bones.

.. note::

   Unlike the Armature modifier, the constraint does not take
   the :doc:`Deform </animation/armatures/bones/properties/deform>` checkbox
   of bones into account, and can use any bone as target.


Options
=======

.. figure:: /images/animation_constraints_relationship_armature_panel.png

   Armature constraint.

Preserve Volume
   Like the matching option of the modifier, it enables the use of quaternions
   for preserving the volume of the object during deformation.

Use Envelopes
   To approximate envelope-only behavior of the modifier,
   add all relevant bones with weight 1.0 and enable this option.

   .. note::

      Unlike the modifier, the constraint always requires explicitly listing all
      of its target bones with associated weights. This option merely enables
      envelopes for all bones, as if they had :ref:`Envelope Multiply <armature-bones-envelope>` enabled.

Use Current Location
   Only for constraints on bones: Instead of using the rest location,
   use the current location of the owner bone to compute envelope weights or
   binding to B-Bone segments.

   With envelope weights, this can be used to change the active "parent" bone
   of the owner bone dependent on its location. For non-bones this mode is always active,
   because they don't have a rest location.

Add Target Bone
   This button adds a new empty entry at the end of the target list.

Normalize Weights
   This button normalizes all weight values in the target list so that they add up to 1.0.

Influence
   Controls the percentage of affect the constraint has on the object.
   See :ref:`common constraint properties <bpy.types.constraint.influence>` for more information.


Bones
-----

This specifies the list of bones used by the constraint to deform its owner.
Each target bone has the following input fields and controls:

Target
   Unlike the modifier, the constraint can use bones coming from different armatures at the same time.
   See :ref:`common constraint properties <rigging-constraints-interface-common-target>` for more information.

Sub-target
   Name of the target bone.

Remove Button ``X``
   Removes the entry from the target list.

Weight
   Weight associated with the bone, equivalent to vertex groups in the modifier.
