.. _bpy.ops.curve.primitive*add:

**********
Primitives
**********

.. reference::

   :Mode:      Object Mode and Edit Mode
   :Menu:      :menuselection:`Add --> Curve`
   :Shortcut:  :kbd:`Shift-A`

.. seealso::

   When adding curves there are some common options like other :ref:`Objects <object-common-options>`.

.. note::
   Eventually all the primitive curves will be replaced to use the same curve system used for hair curves.
   Until this is done, their features will diverge.

   They can be converted interchangeably to access the full range of edit and sculpting functionalities.

In Object/Edit Mode, the *Add Curve* menu, provides a few different curve primitives:

Bézier Curve
============

Adds an open 2D Bézier curve with two control points.


Bézier Circle
=============

Adds a closed, circle-shaped 2D Bézier curve (made of four control points).


NURBS Curve
===========

Adds an open 2D :term:`NURBS` curve, with four control points, with *Uniform* knots.


NURBS Circle
============

Adds a closed, circle-shaped 2D :term:`NURBS` curve (made of eight control points).


Path
====

Adds a :term:`NURBS` open 3D curve made of five aligned control points,
with *Endpoint* knots and the *Curve Path* setting enabled.


Empty Hair
===========

Adds an empty high-performance curves object and automatically:

* Assigns the active object as the :doc:`Surface </sculpt_paint/curves_sculpting/introduction>`.
* Set the surface object as the parent of the new object.
* Adds a Geometry Nodes modifier to deform the curves on the surface.

The curves can be edited via :doc:`sculpting </sculpt_paint/curves_sculpting/introduction>`.

.. note::

   Hair curves currently have the following limitations:

   * No Edit Mode.
   * Not supported in Wireframe viewport shading.
