
********
Segments
********

Subdivide
=========

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Surface --> Segments --> Subdivide`

The *Subdivision* operator simply subdivides all selected segments
by adding one or more control points between the selected segments.
Selected grids will be split into four smaller ones.

If used on a 1D surface (a "surface curve"),
this tool works exactly as with :ref:`curves <modeling-curves-subdivision>`.

Number of Cuts
   The number of subdivisions to perform.


.. _modeling_surfaces_editing_segments_switch-direction:

Switch Direction
================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Surface --> Segments --> Switch Direction`

This tool will "reverse" the direction of any curve with at least one selected element
(i.e. the start point will become the end one, and *vice versa*).
Mainly useful when using a curve as path, or the bevel and taper options...
