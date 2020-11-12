
*******
Editing
*******

Transform
=========

.. admonition:: Reference
   :class: refbox

   :Mode:      All Modes
   :Menu:      :menuselection:`Node --> Move, Rotate, Resize`
   :Hotkey:    :kbd:`G`, :kbd:`R`, :kbd:`S`

Move a single node by clicking and dragging it around. A node can be clicked almost anywhere to start dragging.
Multiple nodes can be moved after pressing :kbd:`G`.

In general it is recommended to arrange your nodes within the view such that the data flows from
left to right, top to bottom.

A node can be resized by dragging the edges on the left or right side.


Connecting Sockets
==================

Interactively
-------------

:kbd:`LMB`-click on a socket and drag. You will see a line coming out of it: This is called a *link*.

Keep dragging and connect the link to an input socket of another node, then release the :kbd:`LMB`.

While multiple links can route out of an output socket, only a single link can be attached to an input socket.

To reposition the outgoing links of a node, rather than adding a new one,
hold :kbd:`Ctrl` while dragging from an output socket.
This works for single as well as for multiple outgoing links.

Nodes that have no connections can be inserted on a link.
Just move the node over the link and release when the link is highlighted.

Make Links :kbd:`F`
   Select multiple nodes with open sockets, then use the Make Links to create links between them.
   Use Make Links again if there are other nodes which can be connected.

Make and Replace Links :kbd:`Shift-F`
   *Make and Replace Links* works similarly to *Make Links*, but it will replace existing links if any exist.


Disconnecting Sockets
=====================

Interactively
-------------

Drag the link from an input socket and let it go keeping it unconnected.


Cut Links
---------

.. admonition:: Reference
   :class: refbox

   :Mode:      All Modes
   :Menu:      :menuselection:`Node --> Cut Links`
   :Hotkey:    :kbd:`Ctrl-RMB`

To break a link between sockets click in an empty area, near the link you want to disconnect, and
drag: You will see a little cutter icon appearing at your mouse pointer.
Move it over the link itself, and release.

Detach Links :kbd:`Alt-D`, :kbd:`Alt-LMB` drag
   Use Detach Links in order to cut all links attached to selected nodes at once.


Duplicate
=========

.. admonition:: Reference
   :class: refbox

   :Mode:      All Modes
   :Menu:      :menuselection:`Node --> Duplicate`
   :Hotkey:    :kbd:`Shift-D`

Click :kbd:`LMB` or :kbd:`RMB` on the desired node, press :kbd:`Shift-D` and
move the mouse away to see the duplicate of the selected node appearing under the mouse pointer.

.. note::

   When you duplicate a node, the new node will be positioned *exactly* on top of the node that was duplicated.
   If you leave it there (and it is quite easy to do so),
   you can **not** easily tell that there are *two* nodes there!
   When in doubt, select a node and move it slightly to see if something is hidden underneath.


Copy/Paste
==========

.. admonition:: Reference
   :class: refbox

   :Mode:      All Modes
   :Menu:      :menuselection:`Node --> Copy`, :menuselection:`Node --> Paste`
   :Hotkey:    :kbd:`Ctrl-C`, :kbd:`Ctrl-V`

Not only the selected nodes but also the connections between them are copied to the clipboard.

.. note::

   The pasted node will be placed in the *same* position as when it was copied.
   Use the same cautions as when duplicating.


Delete
======

Delete :kbd:`X`, :kbd:`Delete`
   Deletes the selected node(s).
Delete with Reconnect :kbd:`Ctrl-X`
   Delete the node(s) without loosing the connections.


Mute
====

.. admonition:: Reference
   :class: refbox

   :Mode:      All Modes
   :Menu:      :menuselection:`Node --> Toggle Node Mute`
   :Hotkey:    :kbd:`M`

Muting a node removes the contribution of the node to the node tree,
and makes all links pass through that node without change.
Links will appear red as an indicator of passing through the muted node.


Show/Hide
=========

Hide :kbd:`H`
   Collapses the node so only the node header is visible.
   This can also be toggled by clicking the triangle at the top left of the node header.
Toggle Node Preview :kbd:`Shift-H`
   Shows/Hides a preview region on the node that displays the frame
   after that node's operation has been applied. This can also be toggled
   by clicking the material ball icon in the node header.
Toggle Hidden Node Sockets :kbd:`Ctrl-H`
   Collapses/Expands any input or output sockets that have no other nodes connected to them.
Toggle Node Options
   Shows/Hides all node properties.
Collapse and Hide Unused Sockets
   Applies both the *Toggle Hidden Node Sockets* and *Hide* operations.


.. _bpy.ops.node.read_viewlayers:
.. _bpy.ops.node.read_fullsamplelayers:

Layers
======

.. note:: The tools are only used in the :doc:`Compositor </compositing/index>`.

Read Render Layers :kbd:`Ctrl-R`
   Reads all the current scene's render layers from cache, as needed.
   This can be used to save RAM while rendering because the render layers do not have to be saved in RAM.
   This can also be used to recover some information from a failed render.
   For this to work, :ref:`Save Buffers <render_properties_save-buffers>` must be enabled.
