
********
Snapping
********

.. _bpy.types.ToolSettings.snap_uv_element:

Snap To
=======

.. reference::

   :Header:    :menuselection:`Snapping --> Snap To`
   :Shortcut:  :kbd:`Shift-Ctrl-Tab`

Increment
   Snap elements along points on a fixed scale.
   These pointes are defined by the grid's intersection points
   and the scale of the increments depending on zoom level,
   unless using :ref:`bpy.types.SpaceUVEditor.use_custom_grid`.

   The Custom Grid can also be used to define a set distance of the scale.

   .. note::

      In this context the grid does not mean the visual grid cue displayed.
      Snapping will use the resolution of the displayed grid,
      but all transformations are relative to the initial position (before the snap operation).

      Note, the behavior can be disabled by using *Absolute Grid Snap*.

Vertex
   Snap to UV vertices.


Additional Options
==================

.. _bpy.types.ToolSettings.use_snap_uv_grid_absolute:

Absolute Grid Snap
   Available only for the *Increment* option.
   Snap to the visual grid, instead of snapping in increments relative to the current location.

Target
    See :ref:`3D Viewport Snapping <bpy.types.ToolSettings.snap_target>` for more information.


Affect
======

Limits the effect of the snap to the transformation type.
