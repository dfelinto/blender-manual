
************
Introduction
************

There are many ways to select elements, and it depends on what *Mesh Select Mode*
you are in as to what selection tools are available.
First we will go through these modes and after that a look is taken at basic selection tools.


.. _bpy.types.ToolSettings.mesh_select_mode:

Selection Modes
===============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`3D Viewport Header --> Select Mode`
   :Shortcut:  :kbd:`1`, :kbd:`2`, :kbd:`3`
               (:kbd:`Shift` `Multiple Selection Modes`_,
               :kbd:`Ctrl` `Expand/Contract Selection`_).

In *Edit Mode* there are three different selection modes.
You can enter the different modes by selecting one of the three buttons in the header.

.. figure:: /images/modeling_meshes_selecting_introduction_mode-buttons.png
   :align: center

   Edit Mode selection buttons from right to left: Vertex, Edge, Face.

Vertex
   In this mode vertices are shown as points.
   Selected vertices are displayed in orange, unselected vertices in black,
   and the active or last selected vertex in white.
Edge
   In this mode the vertices are not shown.
   Instead the selected edges are displayed in orange,
   unselected edges black, and the active or last selected edge in white.
Face
   In this mode the faces are displayed with a selection point in the middle which is used for selecting a face.
   Selected faces and their selection point are displayed in orange,
   unselected faces are displayed in black, and the active or last selected face is highlighted in white.

When using these buttons, you can make use of modifier keys, see: `Switching Select Mode`_.

Almost all tools are available in all three mesh selection modes.
So you can *Rotate*, *Scale*, *Extrude*, etc. in all modes.
Of course rotating and scaling a *single* vertex will not do anything useful
(*without* setting the pivot point to another location), so some tools
are more or less applicable in some modes.

See Fig. :ref:`fig-mesh-select-intro-selection-modes` for examples of the different modes.


Multiple Selection Modes
------------------------

By holding :kbd:`Shift-LMB` when selecting a selection mode,
you can enable multiple *Selection Modes* at once.
This allows you to quickly select vertices, edges, or faces,
without first having to switch mode.

.. _fig-mesh-select-intro-selection-modes:

.. list-table:: Selection modes.

   * - .. figure:: /images/modeling_meshes_selecting_introduction_vertex-mode-example.png
          :width: 310px

          Vertex mode example.

     - .. figure:: /images/modeling_meshes_selecting_introduction_edge-mode-example.png
          :width: 310px

          Edge mode example.

   * - .. figure:: /images/modeling_meshes_selecting_introduction_face-mode-example.png
          :width: 310px

          Face mode example.

     - .. figure:: /images/modeling_meshes_selecting_introduction_mixed-mode-example.png
          :width: 310px

          Mixed mode example.


Switching Select Mode
---------------------

When switching modes in an "ascendant" way (i.e. from simpler to more complex),
from *Vertices* to *Edges* and from *Edges* to *Faces*,
the selected parts will still be selected if they form a complete element in the new mode.

For example, if all four edges in a face are selected,
switching from *Edges* mode to *Faces* mode will keep the face selected.
All selected parts that do not form a complete set in the new mode will be unselected.

.. list-table::

   * - .. figure:: /images/modeling_meshes_selecting_introduction_edge-mode-example.png
          :width: 310px

          Edge mode, the initial selection.

     - .. figure:: /images/modeling_meshes_selecting_introduction_face-mode-switched-from-edge.png
          :width: 310px

          Switching to Face mode.

Hence, switching in a "descendant" way (i.e. from more complex to simpler),
all elements defining the "high-level" element (like a face) will be selected
(the four vertices or edges of a quadrangle, for example).


Expand/Contract Selection
^^^^^^^^^^^^^^^^^^^^^^^^^

By holding :kbd:`Ctrl` when selecting a higher selection mode,
all elements touching the current selection will be added,
even if the selection does not form a complete higher element.
Or contracting the selection when switching to a lower mode.

.. list-table::

   * - .. figure:: /images/modeling_meshes_selecting_introduction_vertex-mode-example.png
          :width: 310px

          Vertex mode, the initial selection.

     - .. figure:: /images/modeling_meshes_selecting_introduction_edge-mode-expanding-from-vertex.png
          :width: 310px

          Expanding to Edge mode.


.. _bpy.ops.view3d.toggle_xray:

X-Ray
=====

The :ref:`X-Ray <3dview-shading-xray>` setting is not just for shading, it impacts selection too.
When enabled, selection isn't occluded by the objects geometry (as if the object was solid).

.. list-table::

   * - .. figure:: /images/modeling_meshes_selecting_introduction_limit-selection-to-visible-off.png
          :width: 310px

          X-ray enabled.

     - .. figure:: /images/modeling_meshes_selecting_introduction_limit-selection-to-visible-on.png
          :width: 310px

          X-ray disabled.


Select Menu
===========

All :kbd:`A`
   Select all.
None :kbd:`Alt-A`
   Select none.
Inverse :kbd:`Ctrl-I`
   Selects all the geometry that is not selected, and deselect currently selected components.

----

:ref:`Box Select <tool-select-box>` :kbd:`B`
   Interactive box selection.
:ref:`Circle Select <tool-select-circle>` :kbd:`C`
   Interactive circle selection.
:ref:`Lasso Select <tool-select-lasso>`
   Interactive free-form selection.

----

:ref:`Select Random <bpy.ops.mesh.select_random>`
   Selects a random group of vertices, edges, or faces, based on a percentage value.
:ref:`Checker Deselect <bpy.ops.mesh.select_nth>`
   Deselect alternate elements relative to the active item.

----

Select Sharp Edges
   This tool selects all edges between two faces forming an angle greater than the angle value,
   where an increasing angle selects sharper edges.

----

:ref:`Select Similar <bpy.ops.mesh.select_similar>` :kbd:`Shift-G`
   Select elements similar to the current selection.

----

:doc:`Select All by Trait </modeling/meshes/selecting/all_by_trait>`
   Select geometry by querying its characteristics.

----

Select More/Less
   More :kbd:`Ctrl-NumpadPlus`
      Expands the selection to the adjacent elements of the selection type.
   Less :kbd:`Ctrl-NumpadMinus`
      Contracts the selection from the adjacent elements of the selection type.
   Next Active :kbd:`Shift-Ctrl-NumpadPlus`
      This uses selection history to select the next vertex, edge, or face based on surrounding topology.
   Previous Active :kbd:`Shift-Ctrl-NumpadMinus`
      Select previous just removes the last selected element.

----

Select Loops
   :ref:`Edge Loops <bpy.ops.mesh.loop_multi_select>`
      Select connected edges.
   :ref:`Face Loops <modeling-meshes-selecting-face-loops>`
      Select connected faces.
   :ref:`Edge Rings <modeling-meshes-selecting-edge-rings>`
      Select connected edge ring.

----

Select Linked
   :ref:`Select Linked <bpy.ops.mesh.select_linked>`
      Selects all components that are connected to the current selection.
   :ref:`Shortest Path <bpy.ops.mesh.shortest_path_select>`
      Path between two selected elements.
   Linked Flat Faces
      Select connected faces based on a threshold of the angle between them.
      This is useful for selecting faces that are planar.

----

Select Side of Active
   Selects all vertices on the mesh in a single axis relative to the active vertex.
   In Vertex selection mode only.
Select Mirror :kbd:`Shift-Ctrl-M`
   Select mesh items at the mirrored location across the chosen axis.


Known Issues
============

Dense Meshes
------------

Selecting dense meshes with X-Ray disabled, has a limitation where dense meshes may not have
all the elements selected.
When selecting regions with Box, Circle and Lasso select, vertices may overlap each other causing
some vertices not to be selected.
This is a limitation with the current selection method, you may workaround this by zooming in or enabling X-Ray.


N-Gons in Face Select Mode
--------------------------

.. figure:: /images/modeling_meshes_selecting_introduction_face-mode-ngon-visual-problem.png

   N-gon face having its center dot inside another face.

As already noted, in X-Ray and Wireframe mode faces are marked with a dot in the middle.
With n-gons that can lead in certain cases to a confusing display.
The example shows the center dot of the U-shaped n-gon being inside of the oblong face inside the "U".
It is not easy to identify which dot belongs to which face (the orange dot in the image is the object origin).
