
************
Introduction
************

*Curves Sculpt Mode* allows working with curves using various brushes.
It is commonly used for hair grooming, but can be used with all kinds of curves.

Some tools, such as the :doc:`Add Curves </sculpt_paint/curves_sculpting/tools/add_curves>`,
require the Surface to be set already.

.. note::

    Curves Sculpt tools only use the original mesh of the surface object and don't take its modifiers into account.


.. _bpy.types.Curves.surface:

Surface
=======

The curve surface is an optional mesh that is used to anchor the curves, and behave as a scalp for hair grooming.
When adding a new Curves object via the `Add Menu` the active object is automatically set as the surface.

To set a new surface press :kbd:`Ctrl-P` and select *Object (Attach Curves to Surface)*
in the *Set Parent To* pop-up menu. This option can be seen as part of the Curves settings in the Properties Editor.

.. figure:: /images/sculpt-paint_sculpting_curves-surface.png

.. _bpy.types.Curves.surface_uv_map:

Surface UV Map
   The name of the attribute on the surface mesh used to define the attachment of each curve.

   .. note::

      If the UV from the surface changed,
      run :ref:`Snap to Nearest Surfaces <Snap to Nearest Surfaces>` to re-attach the curves.


Curves Menu
===========

.. _bpy.ops.curves.snap_curves_to_surface:

Snap to Deformed Surfaces
   Re-attach curves to a deformed surface using the existing attachment information.
   This only works when the topology of the surface mesh has not changed.

.. _Snap to Nearest Surfaces:

Snap to Nearest Surfaces
   Find the closest point on the surface for the root point of every curve and move the root there.
   This needs to be run after the surface mesh topology changed

.. _bpy.ops.curves.convert_to_particle_system:

Convert to Particle System
   Add a new or update an existing hair particle system on the surface object.
   An operator used for backwards compatibility with the old
   :doc:`hair type particle system </physics/particles/hair/introduction>`.


Select Menu
===========

.. _bpy.ops.sculpt_curves.select_all:

All
   Select all control points.

None
   Deselect all control points.

Invert
   Invert the selection.

.. _bpy.ops.sculpt_curves.select_random:

Random
   Randomizes existing selection or create new random selection.

.. _bpy.ops.sculpt_curves.select_end:

Endpoints
   Select end point of curves.
   Only supported in the Control Point selection mode.

.. _bpy.ops.sculpt_curves.select_grow:

Grow
   Select curves which are close to curves that are selected already.
