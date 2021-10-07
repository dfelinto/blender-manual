
*********
Edge Data
*********

Edges can have several different properties that affect how certain other tools affect the mesh.

.. _bpy.ops.transform.edge_crease:

Edge Crease
===========

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Edge --> Edge Crease`
   :Shortcut:  :kbd:`Shift-E`

This operator interactively sets the :ref:`Edge Crease <modeling-edges-crease-subdivision>` amount
by moving the mouse (or typing a value with the keyboard).
Selecting more than one edge will adjust the mean (average) crease value.
A negative value will subtract from the actual crease value, if present.
To clear the crease edge property, enter a value of -1.


.. _bpy.ops.transform.edge_bevelweight:

Edge Bevel Weight
=================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Edge --> Edge Bevel Weight`

This edge property, a value between (0.0 to 1.0),
is used by the :doc:`Bevel Modifier </modeling/modifiers/generate/bevel>`
to control the bevel intensity of the edges.
This operator enters an interactive mode (a bit like transform tools),
where by moving the mouse (or typing a value with the keyboard)
you can set the bevel weight of selected edges. If two or more edges are selected,
this operator alters the average weight of the edges.

.. seealso::

   :ref:`Vertex Bevel Weight <modeling-vertex-bevel-weight>`


.. _bpy.ops.mesh.mark_seam:

Mark Seam & Clear Seam
======================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Edge --> Mark Seam/Clear Seam`

These operators set or unset this mark for selected edges.
Seams are a way to create separations, "islands", in UV maps.
See the :ref:`UV Mapping section <editors-uv-index>` for more details.


.. _bpy.ops.mesh.mark_sharp:

Mark Sharp & Clear Sharp
========================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Edge --> Mark Sharp/Clear Sharp`

The *Sharp* mark is used by the :ref:`split normals <auto-smooth>`
and the :doc:`Edge Split </modeling/modifiers/generate/edge_split>` modifier,
which are part of the smoothing or customized shading techniques.
As seams, it is a property of edges, and these operators set or unset it for selected ones.
