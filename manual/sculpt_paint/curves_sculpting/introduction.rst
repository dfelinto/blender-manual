
************
Introduction
************

*Curves Sculpt Mode* allows working with curves using various brushes.
It is commonly used for hair grooming, but can be used with all kinds of curves.

The curves' surface object plays an important role in many curves sculpting brushes.
Most brushes such as :doc:`Add Curves </sculpt_paint/curves_sculpting/tools/add_curves>`
require the surface to be set already.

.. note::

    Curves Sculpt tools only use the original mesh of the surface object and don't take its modifiers into account.


Curves Menu
===========

.. _bpy.ops.curves.snap_curves_to_surface:

Snap to Deformed Surface
   Re-attach curves to a deformed surface using the existing attachment information.
   This only works when the topology of the surface mesh has not changed.

Snap to Nearest Surface
   Find the closest point on the surface for the root point of every curve and move the root there.
   This needs to be run after the surface mesh topology changed

.. _bpy.ops.curves.convert_to_particle_system:

Convert to Particle System
   Add a new hair particle system, or update an system on the surface object.
   The operator is used for backwards compatibility with the old
   :doc:`hair type particle system </physics/particles/hair/introduction>`.


Select Menu
===========

.. _bpy.ops.sculpt_curves.select_all:

All
   Select all control points or curves.

None
   Deselect all control points or curves.

Invert
   Invert the selection.

.. _bpy.ops.sculpt_curves.select_random:

Random
   Randomizes inside the existing selection or create new random selection if nothing is selected already.

.. _bpy.ops.sculpt_curves.select_end:

Endpoints
   Select endpoints of curves.
   Only supported in the Control Point selection mode.

.. _bpy.ops.sculpt_curves.select_grow:

Grow
   Select points or curves which are close to already selected elements.
