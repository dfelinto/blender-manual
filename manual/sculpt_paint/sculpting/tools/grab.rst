
****
Grab
****

.. admonition:: Reference
   :class: refbox

   :Mode:      Sculpt Mode
   :Tool:      :menuselection:`Toolbar --> Grab`
   :Hotkey:    :kbd:`G`

Used to drag a group of vertices around. *Grab* selects a group of vertices on mouse-down,
and pulls them to follow the mouse. And unlike other brushes,
*Grab* does not move different vertices as the brush is dragged across the model.
The effect is like moving a group of vertices in Edit Mode with Proportional Editing enabled,
except that *Grab* can make use of other Sculpt Mode options (like textures and symmetry).


Brush Settings
==============

.. _bpy.types.Brush.use_grab_active_vertex:

Grab Active Vertex
   Snaps the maximum strength of the brush to the highlighted active vertex,
   making it easier to manipulate low poly models or meshes with subdivision surfaces.

   Enabling *Grab Active Vertex* also enables a dynamic mesh preview which
   generates a preview of vertices connected to the active vertex.
   This helps to visualize the real geometry that is being manipulating while sculpting with active modifiers.
