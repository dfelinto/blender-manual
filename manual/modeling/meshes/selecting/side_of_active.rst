
**************
Side of Active
**************

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> Side of Active`

With an active vertex, this tool will select all vertices in a specified direction.
It is similarly to the *Loop Inner-Region* tool in that it will fill select faces within its perimeters,
however, it is determined by direction and not by a closed loop.

Axis Mode
   Determines the behavior of the selection.
   More information on this can be found in :doc:`Transform Orientations </editors/3dview/controls/orientation>`.

Axis Sign
   Positive/Negative Axis
      Depending on which *Axis* is chosen, the selection will encompass the positive or negative axis
      starting from the active vertex outward.

   Aligned Axis
      Where *Positive and Negative Axis* select all vertices in a given direction,
      *Aligned Axis* will only select the vertices that are in-line with the active vertex.

.. figure:: /images/modeling_meshes_selecting_side-of-active_sign.png

   While following along the X axis: (from left to right) active vertex, Aligned, Positive, and Negative.

Axis
   Chooses the direction of the selection.

Threshold
   The amount of influence the selection has outside the original perimeters.
   The higher the *Threshold* the more vertices will be selected.
