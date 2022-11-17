.. index:: Geometry Nodes; Inspection

**********
Inspection
**********

Inspecting intermediate values in a geometry node tree is useful while
building/understanding one or when trying to figure out why something is not working.
Blender provides multiple tools to understand how a node tree is working
or why it is not working.

.. note::

   Generally, the inspection tools display data from the last time the node tree has been evaluated.
   If it has not been evaluated, no information is available.


.. _socket-inspection:

Socket Inspection
=================

.. figure:: /images/modeling_geometry-nodes_inspection_socket-inspection.png
   :align: center

   Socket Inspection.

Socket inspection shows information about the value in a socket during the last evaluation.
For primitive data types such as integers, vectors, and strings the actual value is shown.
For geometry sockets only some data about the geometry is stored, including the set of
data types the geometry contains, and a count of their elements.

Socket values are only logged from when the node tree was executed, so a node must be
connected to the *Group Output* to have a value for inspection. Values are not logged during
rendering, to improve performance.


.. _geometry-nodes-attribute-search:

Attribute Search
================

.. figure:: /images/modeling_geometry-nodes_attribute-reference_search.png
   :align: center

   Attribute Search.

The attribute search is shown when clicking on an attribute input in the modifier.
It contains a list of all the attributes that were available at that point in
the modifier or node execution.


Viewer Node
===========

The Viewer node is used to display intermediate geometry in the :doc:`Spreadsheet Editor </editors/spreadsheet>`
and the Viewport. For more information see :doc:`/modeling/geometry_nodes/output/viewer`.


Node Warnings
=============

.. figure:: /images/modeling_geometry-nodes_inspection_node-warning.png
   :align: center

   Node Warning.

When the inputs to a node are invalid, it displays a warning in the title.
Hovering over the warning icon shows the error message. These warnings are only
generated when the node is executed, so a node must be connected to the *Group Output*
to have a warning.


.. _bpy.types.SpaceNodeOverlay.show_timing:

Node Timings Overlay
====================

.. figure:: /images/modeling_geometry-nodes_inspection_node-timings.png
   :align: center

   The node timings overlay.

Node timings show how long a node took to execute the last time the node group was evaluated.
They can be turned on in the overlays popover on the top right of the node editor.
When a node group is used in multiple places, the timings depend on the context of
the node editor, which is displayed in the path on the top left.

Frame nodes display the total time from all of the contained nodes
and the *Group Output* node displays the total time for the entire node group.

The displayed timings should only be considered an approximation, since they can
also take into account actions like copying or deleting a geometry input that aren't
part of the node's operation. Also, when a node uses multiple CPU cores, the evaluation
system might work on other nodes at the same time. It's also important to remember
that :ref:`field nodes <field-node-types>` generally don't do work by themselves,
so their execution time is only added to the data-flow nodes they are connected to.


.. _bpy.types.SpaceNodeOverlay.show_named_attributes:

Named Attributes Overlay
========================

The "Named Attributes" overlay allows displaying when a custom named attribute is used
by a node or a node group. Named attributes can be used by the
:doc:`/modeling/geometry_nodes/attribute/capture_attribute`, the
:doc:`/modeling/geometry_nodes/input/named_attribute`, and the
:doc:`/modeling/geometry_nodes/attribute/remove_named_attribute`,
and can be written to, read, or removed.

Using named attributes (as opposed to :ref:`anonymous-attributes`) can be problematic
when the original geometry already has attributes with the specified names. In that case
a geometry node group might mistakenly overwrite some essential data. The overlay helps
to make detecting that situation easy.

The same data is also available in the :ref:`geometry-nodes-internal-dependencies` panel
in the modifier's UI.
