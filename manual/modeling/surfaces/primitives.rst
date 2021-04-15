.. _bpy.ops.surface.primitive*add:

**********
Primitives
**********

.. admonition:: Reference
   :class: refbox

   :Mode:      Object Mode and Edit Mode
   :Menu:      :menuselection:`Add --> Curve`
   :Shortcut:  :kbd:`Shift-A`

.. seealso::

   When adding curves there are some common options like other :ref:`Objects <object-common-options>`.

In Object/Edit Mode, the *Add Surface* menu, provides six different surface primitives:

.. list-table::

   * - .. figure:: /images/modeling_surfaces_primitives_surface.png

          NURBS surface primitives.

     - .. figure:: /images/modeling_surfaces_primitives_curve.png

          NURBS curve primitives.


NURBS Curve
===========

Adds a generic curve of four control points forming an arc.


NURBS Circle
============

Adds an a closed loop of control point forming a circle.
Note, a circle :term:`NURBS` surface is never filled, unlike its "real" curve counterpart...


NURBS Surface
=============

Adds a generic surface patch consisting of a 4×4 grid plane with the center grid slightly raised.


NURBS Cylinder
==============

Adds an open end cylinder, consisting of an extruded *NURBS Circle*.


NURBS Sphere
============

Adds a generic sphere constructed by revolving a grid of control points about an axis.


NURBS Torus
===========

Adds a doughnut-shaped primitive created by rotating a circle around an axis.
