
****************
Mirror Selection
****************

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> Mirror Selection`
   :Hotkey:    :kbd:`Shift-Ctrl-M`

*Mirror Selection* flips a selection to the opposite side of the mesh.

Axis
   Choose on which axis the *Mirror Selection* will occur. The axis is based on the meshes origin.
   Therefore, if the origin is not centered within the mesh, the selection will have varying results.

Extend
   The new selection will include the mirrored selection as well as the original.

.. figure:: /images/modeling_meshes_selecting_mirror_extend.png

   (From left to right) initial selection, after Mirror Selection on the X axis, with Extend.

.. tip::

   With *Extend* activated, hold :kbd:`Shift` while choosing an axis to include more than one axis in the selection.
   Otherwise, with *Extend* off, the mirror will take into account two to three axes.


Example
=======

.. figure:: /images/modeling_meshes_selecting_mirror_axis-xz-extend.png

   (From left to right) initial selection, mirrored along X and Z axes, with Extend.
