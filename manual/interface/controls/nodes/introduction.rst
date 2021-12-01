.. index:: Nodes

************
Introduction
************

The different node editors are used to work with node-based workflows.
Each node editor type has its own specific purpose.
Therefore, this section only explains how to work with nodes in general.
In the list below it shows a list of different types of node trees and where each is documented.

.. figure:: /images/interface_controls_nodes_introduction_example.jpg

   Example of a node editor.

.. _tab-node-tree-types:

.. list-table::
   :header-rows: 1
   :class: valign
   :widths: 10 30 60

   * - Icon
     - Name
     - Documentation
   * - .. figure:: /images/interface_controls_nodes_introduction_icons-material.png
     - Shader Nodes
     - Documentation is in the :doc:`Render </render/shader_nodes/index>` section.
   * - .. figure:: /images/interface_controls_nodes_introduction_icons-render-layers.png
     - Composite Nodes
     - Documentation can be found in the :doc:`Compositing </compositing/index>` section.
   * - .. figure:: /images/interface_controls_nodes_introduction_icons-texture.png
     - Texture Nodes
     - Texture Nodes are covered
       in the :doc:`UV editor </editors/texture_node/introduction>` docs.


Editor Interface
================

Header
------

The *Header* contains various menus, buttons and options, partially based on the current node tree type.

.. figure:: /images/interface_controls_nodes_introduction_header.png

   Common node editor header options.

View
   This menu changes your view of the editor.
Select
   This menu allows you to select a node or groups of nodes.
Add
   This menu allows you to add nodes.
Node
   This menu allows you to do things with selected nodes.
Use Nodes
   Tells the render engine to use the node tree when computing the material color or rendering the final image,
   or not. If not, the tree is ignored. For materials, this is mostly a legacy option, because in the past
   materials could not be created with node trees.
Use Pinned
   When enabled, the editor will retain the material or texture, even when the user selects a different object.
   A node tree can then be edited independent of the object selection in the 3D Viewport.
Parent Node Tree
   This button allows you go to parent node tree e.g. leaving a group.
Snapping
   Change options for snapping node positions to achieve a cleaner node tree layout.


.. _bpy.types.SpaceNodeOverlay.show_overlays:

Overlays
^^^^^^^^

Overlays are information that is displayed on top of the nodes and node trees.
There is a toggle to show or hide all overlays for the node editor next to the overlay pop over.

.. _bpy.types.SpaceNodeOverlay.show_wire_color:

Wire Colors
   Color node links based on their connected sockets

.. _bpy.types.SpaceNodeEditor.show_annotation:

Annotations
   Displays :doc:`Annotations </interface/annotate_tool>` in the preview region.


Toolbar
-------

The *Toolbar* contains a set of tools that can be used in the node editor.


Sidebar
-------

The :doc:`Sidebar </interface/controls/nodes/sidebar>` region contains properties for
the current selected node as well as node editor specific settings.


Navigating
==========

Navigating the node editors is done with the use of both mouse movement and keyboard shortcuts.

Pan :kbd:`MMB`
   Move the view up, down, left and right.
Zoom :kbd:`Ctrl-MMB`, :kbd:`Wheel`
   Move the camera forwards and backwards.
Frame Selected :kbd:`NumpadPeriod`
   Adjusts the zooms to fit only the selected nodes in the view.
Frame All :kbd:`Home`
   Adjusts the zoom to fit all nodes in the view.


Adding Nodes
============

.. reference::

   :Mode:      All Modes
   :Tool:      :menuselection:`Toolbar`
   :Menu:      :menuselection:`Add`
   :Shortcut:  :kbd:`Shift-A`

Nodes are added via the *Add* menu or using the :kbd:`Shift-A` shortcut.
