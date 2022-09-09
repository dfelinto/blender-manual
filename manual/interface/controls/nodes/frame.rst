.. _bpy.types.NodeFrame:

**********
Frame Node
**********

The Frame node is useful for organizing nodes by collecting related nodes together in a common area.
Frames are useful when a node setup becomes large and confusing yet the re-usability of a Node Group is not required.

.. figure:: /images/interface_controls_nodes_frame_example.png


Properties
==========

.. figure:: /images/interface_controls_nodes_frame_properties.png
   :align: right

Label Size
   Font size of the label. For example, for subordinate frames to have smaller titles.
Shrink
   Once a node is placed in the Frame, the Frame shrinks around it so as to remove wasted space.
   At this point it is no longer possible to select the edge of the Frame to resize it, instead resizing occurs
   automatically when nodes within the Frame are rearranged.
   This behavior can be changed by disabling this option.
Text
   When you need to display more comprehensive text, frame nodes can display the contents of a text data-block.
   This is read-only, so you will need to use the *Text Editor* to modify the contents.


Editing
=======

.. _bpy.ops.node.join:

Join in New Frame
-----------------

.. reference::

   :Menu:      :menuselection:`Node --> Join in new Frame`
   :Shortcut:  :kbd:`Ctrl-J`

Make a new frame including the selected nodes.


.. _bpy.ops.node.parent_set:

Add to Frame
------------

.. reference::

   :Shortcut:  :kbd:`Ctrl-P`

Once a frame node is placed, nodes can be added by dropping them onto the frame or
by selecting the node(s) then the frame and using :kbd:`Ctrl-P`.
This can be thought of as Parenting the selection to the frame.


.. _bpy.ops.node.detach:

Remove from Frame
-----------------

.. reference::

   :Menu:      :menuselection:`Node --> Remove from Frame`
   :Shortcut:  :kbd:`Alt-P`

To remove nodes from a frame, select and use :kbd:`Alt-P`.
This can be thought of as unparenting the selection from the frame.
