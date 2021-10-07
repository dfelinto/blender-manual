.. _bpy.ops.armature.symmetrize:

**********
Symmetrize
**********

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Armature --> Symmetrize`

This operator will mirror the selected bones along the X axis based on Blender's
bone :ref:`naming convention <armature-editing-naming-conventions>` for symmetrical 
armatures, either from left to right or right to left, depending on the selection.

   .. note::

      If the side of the bone cannot be determined, it will be ignored by Symmetrize.

Bones with the opposite names that don't yet exist will be created, and already
existing ones will be overwritten.
If matching bones are selected on both sides, mirroring will happen
from right to left.

Symmetrized bone and constraint properties will have the necessary changes to 
mirror their behaviours.

When symmetrizing bones with :doc:`Action Constraints </animation/constraints/relationship/action>`, 
the necessary keyframes will be added to the target Action to result 
in symmetrical movement when the Action is activated.

   .. note::

      Note that bone or constraint drivers will not be created or affected in any way.
