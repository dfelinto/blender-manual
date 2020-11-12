
*********
Edge Data
*********

Edges can have several different attributes that affect how certain other tools affect the mesh.


.. _modeling-edges-crease-subdivision:
.. _bpy.ops.transform.edge_crease:

Edge Crease
===========

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Edge --> Edge Crease`
               :menuselection:`Sidebar region --> Transform --> Edge Crease`
   :Hotkey:    :kbd:`Shift-E`

This edge property, a value between (0.0 to 1.0), is used by
the :doc:`Subdivision Surface Modifier </modeling/modifiers/generate/subdivision_surface>`
to control the sharpness of the edges in the subdivided mesh.
This operator enters an interactive mode (a bit like transform tools),
where by moving the mouse (or typing a value with the keyboard) you can set the (average)
crease value of selected edges.
A negative value will subtract from the actual crease value, if present.
To clear the crease edge property, enter a value of -1.


.. _modeling-edges-bevel-weight:
.. _bpy.ops.transform.edge_bevelweight:

Edge Bevel Weight
=================

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Edge --> Edge Bevel Weight`
               :menuselection:`Sidebar region --> Transform --> Edge Bevel Weight`

This edge property, a value between (0.0 to 1.0),
is used by the :doc:`Bevel Modifier </modeling/modifiers/generate/bevel>`
to control the bevel intensity of the edges.
This operator enters an interactive mode (a bit like transform tools),
where by moving the mouse (or typing a value with the keyboard)
you can set the bevel weight of selected edges. If two or more edges are selected,
this operator alters the average weight of the edges.

.. seealso::

   Vertices also have a bevel weight which can be edited.

   .. TODO2.8 there are no docs for this yet.


.. _bpy.ops.mesh.mark_seam:

Mark Seam & Clear Seam
======================

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Edge --> Mark Seam/Clear Seam`

Seams are a way to create separations, "islands", in UV maps.
See the :ref:`UV Mapping section <editors-uv-index>` for more details.
These operators set or unset this mark for selected edges.


.. _bpy.ops.mesh.mark_sharp:

Mark Sharp & Clear Sharp
========================

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Edge --> Mark Sharp/Clear Sharp`

The *Sharp* mark is used by the :ref:`split normals <auto-smooth>`
and the :doc:`Edge Split </modeling/modifiers/generate/edge_split>` modifier,
which are part of the smoothing or customized shading techniques.
As seams, it is a property of edges, and these operators set or unset it for selected ones.
