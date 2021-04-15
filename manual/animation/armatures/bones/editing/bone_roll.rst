.. _armature-bone-roll:

*********
Bone Roll
*********

In *Edit Mode*, you can control the bone roll
(i.e. the rotation around the Y axis of the bone).

However, after editing the armature, or when using :term:`Euler Rotation`,
you may want to set the bone roll.


Recalculate
===========

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Armature --> Bone Roll --> Recalculate`
   :Shortcut:  :kbd:`Ctrl-N`

Axis Orientation
   Local Tangent
      Align roll relative to the axis defined by the bone and its parent.

      X, Z
   Global Axis
      Align roll to global X, Y, Z axis.

      X, Y, Z
   Active Bone
      Follow the rotation of the active bone.
   View Axis
      Set the roll to align with the viewport.
   Cursor
      Set the roll towards the 3D cursor.
Flip Axis
   Reverse the axis direction.
Shortest Rotation
   Avoids rolling the bone over 90 degrees from its current value.


.. _tool-bone-role:

Set
===

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Armature --> Bone Roll --> Set`
   :Shortcut:  :kbd:`Ctrl-R`

This is a transform mode where you can edit the roll of all selected bones.
