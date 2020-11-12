.. |pivot-icon| image:: /images/editors_3dview_controls_pivot-point_menu.png

************
Median Point
************

.. admonition:: Reference
   :class: refbox

   :Mode:      Object Mode and Edit Mode
   :Header:    |pivot-icon| :menuselection:`Pivot Point --> Median Point`
   :Hotkey:    :kbd:`Period`

The Median Point can be considered to be broadly similar to the concept of
Center of Gravity (COG). If we assume that every element (object, face, vertex, etc.)
of the selection has the same mass,
the median point would sit at the point of equilibrium for the selection (the COG).


In Object Mode
==============

In Object Mode, Blender only considers the object origins when determining the median point.
This can lead to some counter-intuitive results.
In the Fig. :ref:`fig-view3d-median-point-object-mode` below,
you can see that the median point is between the object origins and
can be nowhere near the objects' mesh (geometric center).

.. _fig-view3d-median-point-object-mode:

.. figure:: /images/editors_3dview_controls_pivot-point_median-point_object-mode.png
   :align: center

   Median points in Object Mode.


In Edit Mode
============

In Edit Mode,
the median point is determined via the part of the selection that has the most elements.
For example, in the Fig. :ref:`fig-view3d-median-point-edit-mode`,
when there are two cubes with an equal number of vertices,
the median point lies directly between the two cubes.
But if you subdivide one cube multiple times so that it has many more vertices,
you can see that the median point has shifted to the region with the most vertices.

.. _fig-view3d-median-point-edit-mode:

.. figure:: /images/editors_3dview_controls_pivot-point_median-point_edit-mode.png
   :align: center

   Median points in Edit Mode.
