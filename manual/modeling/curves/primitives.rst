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


.. _bpy.ops.object.curves_empty_hair_add:

Empty Hair
==========

Adds an empty high-performance curves object and automatically:

* Assigns the active object as the :doc:`Surface </sculpt_paint/curves_sculpting/introduction>`.
* Set the surface object as the parent of the new object.
* Adds a Geometry Nodes modifier to deform the curves on the surface.

The curves can be edited via :doc:`sculpting </sculpt_paint/curves_sculpting/introduction>`.

.. note::

   Hair curves currently have the following limitations:

   * No Edit Mode.
   * Not supported in Wireframe viewport shading.


Properties
----------

Hair Curves have different properties than regular Curve objects;
these properties are documented below.


Attributes
^^^^^^^^^^

The *Attributes* panel contains different hair characteristics such as the position and color of hair strands.

Use the :ref:`List View <ui-list-view>` to manage attributes.

.. seealso::

   See the :doc:`Attribute Reference </modeling/geometry_nodes/attributes_reference>` for details on attributes.


Surface
^^^^^^^

.. _bpy.types.Curves.surface:

Surface
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
      run :ref:`Snap to Nearest Surfaces <bpy.ops.curves.snap_curves_to_surface>` to re-attach the curves.
