.. _bpy.types.ToolSettings.gpencil_selectmode:
.. _bpy.ops.gpencil.select:

*********
Selecting
*********

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`3D Viewport Header --> Select Mode`
   :Shortcut:  :kbd:`1`, :kbd:`2`, :kbd:`3`

.. figure:: /images/grease-pencil_selecting_mode-buttons.png
   :align: right

   Edit Mode selection buttons.

In Edit Mode there are three different selection modes.
You can enter the different modes by selecting one of the three buttons in the header.

Points
   To select individual points.

Strokes
   To select an entire stroke.

Points in Between
   To select all points that are between other strokes.

.. figure:: /images/grease-pencil_selecting_example.png

   Points, stroke and in between stroke selection sample.


Select Menu
===========

Box/Circle/All/None/Invert Select
   All these options have the same meaning and behavior as in
   :doc:`Object Mode </scene_layout/object/selecting>`.


Select Linked
=============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> Linked`
   :Shortcut:  :kbd:`L`, :kbd:`Ctrl-L`

:kbd:`L` (or :kbd:`Ctrl-L` for all) will add to the selection the cursor's nearest control point,
and all the linked ones, i.e. all points belonging to the same stroke.


Select Alternated
=================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> Alternated`
   :Shortcut:  :kbd:`Shift-L`

Selects alternate points in the selected strokes.


Select Grouped
==============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> Grouped`
   :Shortcut:  :kbd:`Shift-G`

Layer
   Selects all the points/strokes on the same layer.
Material
   Selects all the points/strokes that share the same material.


.. _bpy.ops.gpencil.select_vertex_color:

Select Vertex Color
===================

.. reference::

   :Mode:      Vertex Paint Mode
   :Menu:      :menuselection:`Select --> Vertex Color`

Selects all points with a similar vertex color as the current selection.

Tolerance
   How similar colors are allowed to be; higher values select a wider range of colors.


Select First/Last
=================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> First/Last`

These operators will toggle the selection of the first or last point(s) of the stroke(s) in the object.
This is useful to quickly find the start of a stroke.


Select More/Less
================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> More/Less`
   :Shortcut:  :kbd:`Ctrl-NumpadPlus`, :kbd:`Ctrl-NumpadMinus`

The purpose of these tools is to reduce or enlarge the current selection within a stroke
(i.e. they will never "go outside" of a stroke or "jump" to another stroke in the same object).

More
   For each selected point, select *all* its linked points (i.e. one or two...).
Less
   For each selected point, if *all* points linked to this point are selected, keep this one selected.
   Otherwise, deselect it.

.. hint::

   When *all* points of a stroke are selected, nothing will happen
   (as for *Less*, all linked points are always selected, and of course, *More* cannot add any).
   Conversely, the same goes when no points are selected.
