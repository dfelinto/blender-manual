.. _bpy.ops.mesh.rip_edge_move:
.. _tool-mesh-rip_edge:

***********************
Rip Vertices and Extend
***********************

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Vertex --> Rip Vertices and Extend`
   :Hotkey:    :kbd:`Alt-D`

This tool takes any number of selected vertices and duplicate-drags them along the closest edge to the mouse.
When extending an edge loop, it extends the vertices at the endpoints of the loop.
The behavior is similar to the *Extrude* tool, but it creates an n-gon.

It helps to easily add details to existing edges.
