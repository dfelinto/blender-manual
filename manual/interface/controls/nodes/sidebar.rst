
*******
Sidebar
*******

Node
====

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Sidebar --> Node`

.. figure:: /images/interface_controls_nodes_sidebar_item.png
   :width: 200px
   :align: right

   Node tab with a compositing Render Layers node selected.


Node
----

.. _bpy.types.Node.name:

Name
   A unique node identifier inside this node tree.

.. _bpy.types.Node.label:

Label
   Nodes can be given a title by modifying the text field.


.. _bpy.types.Node.use_custom_color:

Color
^^^^^

By default, the nodes background color is defined by the user theme.
This color can be overiden by selecting a custom color in this panel.
Custom node colors can be used to provide a visual cue to help distinguish some nodes from others.
In the panel header, colors can be saved as a preset for reuse in other nodes or other projects .

.. _bpy.types.Node.color:

Color
   Color of the node background.

   Node Color Specials
      This menu contains operators for working with nodes with custom colors.

      .. _bpy.ops.node.node_copy_color:

      Copy Color
         Copies the color of the :term:`Active` node and applies it to all selected nodes.


Properties
----------

The properties that are shown depend on the type of node selected,
e.g. a Mix node has different properties than a Mask node.


Tool
====

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Sidebar region --> Tool`


Active Tool
-----------

The info in this panel changes with the selected tool.


View
====

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Sidebar region --> View`


Annotations
-----------

You can select the Annotate tool in the Toolbar to make annotations in the node editor.
See :doc:`Annotate Tool </interface/annotate_tool>` for more info.
