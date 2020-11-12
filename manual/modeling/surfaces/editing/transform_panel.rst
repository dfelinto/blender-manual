
***************
Transform Panel
***************

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Panel:     :menuselection:`Sidebar --> Transform`

When nothing is selected, the panel is empty.
When more than one control point is selected, the median values are edited
and "Median" is added in front of the labels.

Control Point, Median
   The first controls (X, Y, Z) show the coordinates of the selected point or handle (vertex).
   The last control (W), defines the :ref:`weight <modeling-surfaces-weight>`
   of the selected control point or the median weight.
Space
   The Space radio buttons let you choose if those coordinates are relative to
   the object origin (local) or the global origin (global).

   Global, Local

.. _surface-goal-weight:

Weight
   Controls the "goal weight" of selected control points,
   which is used when a surface has :doc:`Soft Body </physics/soft_body/index>` physics,
   forcing the surface to "stick" to their original positions, based on the weight.
Radius
   Surface objects do not have a *Radius* property, this value has no effect.
Tilt
   Surface objects do not have a *Radius* property, this value has no effect.
