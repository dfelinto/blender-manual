
********************
Geometry Node Editor
********************

The Geometry Node editor is used to edit a :doc:`Node Group </interface/controls/nodes/groups>`
which is used by the :doc:`Geometry Node Modifier </modeling/modifiers/generate/geometry_nodes>`.
This node group can define many operations to modify an object's geometry.

.. .. figure:: /images/editors_shader-editor_main.png
..
..    Geometry Node Editor with an example node setup.

A list of all :doc:`Geometry Nodes </modeling/geometry_nodes/index>` is available in the modeling section.


Interface
=========

Header
------

View
   Standard view menu.
Select
   Menu for :doc:`Selecting Nodes </interface/controls/nodes/selecting>`.
Add
   Menu for adding new :doc:`Geometry Nodes </modeling/geometry_nodes/index>`.
Node
   Menu for :doc:`Editing Nodes </interface/controls/nodes/editing>`.

-----

Geometry Node Group
   The :ref:`data-block selector <ui-data-block>` can change the active node group being edited.
Pin (pin icon)
   The pin button will keep the current geometry node group selection fixed,
   instead of using the :ref:`Active Modifier <modifier-stack-active>`.
   When a geometry node group is pinned, it will remain visible in the Geometry Node editor
   even when another object or modifier is selected elsewhere.

-----

Parent Node Tree
   Jumps up a node group level, see :ref:`bpy.ops.node.tree_path_parent` for more information.
Snapping
   Controls to control snapping when transforming nodes.


Toolbar
-------

The Geometry Node editor has several tools to work with tools that can be accessed from the Toolbar.


Sidebar
-------

Node
^^^^

This tab allows you to edit the geometry node group's inputs and outputs.

.. tip::

   The inputs of the node group can be edited as properties of
   the :doc:`Geometry Node Modifier </modeling/modifiers/generate/geometry_nodes>`.


Item
^^^^

This tab gives access to the active node's properties.


Tool
^^^^

This tab gives access to the active tool's settings.


View
^^^^

This tab gives access properties that affect editor data such as annotations.
