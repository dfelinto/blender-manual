.. _bpy.ops.uv.select:

*********
Selecting
*********

Selection tools are available in the *Select Menu* in the header,
and the shortcuts listed below.


.. _bpy.types.ToolSettings.use_uv_select_sync:

Sync Selection
==============

Turning on the *Sync Selection* button causes selection of components
in the 3D Viewport to sync with their corresponding elements in the UV editor.
If off only the selected faces are displayed in the UV editor.
These two modes have very different results when transforming components in the UV editor.

.. seealso::

   :doc:`Selecting in the 3D Viewport </editors/3dview/selecting>`.


.. _bpy.ops.uv.select_mode:
.. _bpy.types.ToolSettings.uv_select_mode:

Selection Modes
===============

Select Modes dependent on the Sync Selection.


Sync Selection Off
------------------

:Vertex: Select individual vertices.
:Edge: Select edges.
:Face: Select faces.
:Island: Select contiguous groups of faces.


Sync Selection On
-----------------

When selecting UVs or Edges, it behaves like the *Shared Vertex* option of the *Sticky Selection Mode*.
When selecting Faces, it behaves like the *Disabled* option of the *Sticky Selection Mode*.

:Vertex: Select individual vertices.
:Edge: Select edges.
:Face: Select faces.


.. _bpy.types.ToolSettings.uv_sticky_select_mode:

Sticky Selection Mode
=====================

This selector lets you enable automatic additional selection.

:Shared Vertex:
   Selects UVs that share a mesh vertex, even if they are in different UV locations.
:Shared Location:
   Selects UVs that are in the same UV location and share a mesh vertex.
:Disabled:
   Disables Sticky Selection.
   When you move a UV in this mode, each face owns its own UVs, allowing them to be separated.


Menu
====

Box Select :kbd:`B`
   Click and drag to box select UV coordinates.
   Alternatively, use :kbd:`B` to start :ref:`box selection <tool-select-box>`.
Box Select Pinned :kbd:`Ctrl-B`
   Use the box lasso to select only pinned UV coordinates.
Circle Select
   See :ref:`tool-select-circle`.
Select All :kbd:`A`
   Selects all UV coordinates.
Select None :kbd:`Alt-A`
   Deselects all UV coordinate.
Inverse :kbd:`Ctrl-I`
   Inverts the current selection.
More/Less :kbd:`Ctrl-NumpadPlus`, :kbd:`Ctrl-NumpadMinus`
   Expands/Contracts the selection to/from the adjacent elements of the selection type.
Select Pinned :kbd:`Shift-P`
   Selects all :ref:`pinned <bpy.ops.uv.pin>` UVs.
Select Linked
   Linked :kbd:`Ctrl-L`
      This operator selects all UVs that are connected to currently selected UVs.
      This works similarly to the tools in 3D Viewport.
   Shortest Path
      Path between two selected elements.

.. _bpy.ops.uv.select_similar:

Select Similar :kbd:`Shift-G`
   Selects UV vertices that have certain similar properties to the :term:`Active` vertex.
   The :ref:`bpy.ops.screen.redo_last` panel provides several selection options:

   Type
      The property to compare against the active vertex.
      The properties that are shown depend on the :ref:`Selection Mode <bpy.types.ToolSettings.uv_select_mode>`.

      Vertex Selection Mode:

      :Pinned: Selects vertices with the same :ref:`pinned <bpy.ops.uv.pin>` state as the active vertex.

      Edge Selection Mode:

      :Length: Selects edges with a similar length.
      :Length 3D: Selects edges with a similar length in world space coordinates.
      :Pinned:
         Selects edges whose both vertices have the same
         :ref:`pinned <bpy.ops.uv.pin>` state as the active vertex.

      Face Selection Mode:

      :Area: Selects faces with a similar area.
      :Area 3D: Selects faces with a similar area in world space coordinates.
      :Polygon Sides: Selects faces with the same number of edges per face.
      :Material: Selects faces that have the same :doc:`Material </render/materials/index>`.

      Island Selection Mode:

      :Area: Selects islands with a similar area.
      :Area 3D: Selects islands with a similar area in world space coordinates.
      :Amount of Face in Island: Selects islands with a similar number of faces per each island.

   Compare
      For quantitative properties, this property selects the type of comparison to between the two numerical values.

      :Equal: Select items with the same value as the active item's chosen property.
      :Greater: Select items with a larger value as the active item's chosen property.
      :Less: Select items with a smaller value as the active item's chosen property.
   Threshold
      For quantitative properties, this property controls how
      close the property's values have to be in the comparison.

Select Split :kbd:`Y`
   Cuts apart the selected UVs from the map. Only those UVs which belong to
   fully selected faces remain selected. As the name implies, this is particularly useful to
   unlink faces and move them elsewhere. The hotkey is analogous to the mesh Split tool.
Select Overlap
   Selects any UVs that are extended over other UVs while also selecting any underlying UVs.


.. _bpy.ops.uv.shortest_path_select:
.. _bpy.ops.uv.shortest_path_pick:

Shortest Path
=============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> Select Linked --> Shortest Path`
   :Shortcut:  :kbd:`Ctrl-LMB`

Selects all UV components along the shortest path from
the active component to the one which was selected.

Face Stepping
   Supports diagonal paths for vertices and faces, and
   selects edge rings with edges.
Topological Distance
   Only takes into account the number of edges of the path and
   not the length of the edges to calculate the distances.
Fill Region :kbd:`Shift-Ctrl-LMB`
   Selects all elements in the shortest paths from the active selection to the clicked area.
Checker Deselect Options
   Allows to quickly select alternate elements in a path.

   Deselected
      The number of deselected elements in the repetitive sequence.
   Selected
      The number of selected elements in the repetitive sequence.
   Offset
      Offset from the starting point.

.. seealso::

   Mesh edit :ref:`Select Shortest Path <bpy.ops.mesh.shortest_path_select>`.


.. _bpy.ops.uv.select_edge_ring:

Select Edge Loops
=================

.. reference::

   :Mode:      Edit Mode
   :Shortcut:  :kbd:`Ctrl-Alt-LMB`, or :kbd:`Shift-Ctrl-Alt-LMB` for modifying existing selection.

Holding :kbd:`Ctrl-Alt` while selecting a UV component selects a loop of edges that are connected in
a line end-to-end, passing through the edge under the mouse pointer.
Holding :kbd:`Shift-Ctrl-Alt` while clicking adds to the current selection.

.. seealso::

   Mesh edit :ref:`Select Edge Loops <bpy.ops.mesh.loop_multi_select>`.
