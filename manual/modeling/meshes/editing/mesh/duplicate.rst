.. _bpy.ops.mesh.duplicate_move:

*********
Duplicate
*********

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Duplicate`
   :Hotkey:    :kbd:`Shift-D`

This tool simply duplicates the selected elements,
without creating any connections with the rest of the mesh (unlike extrude, for example),
and places the duplicate at the location of the original. Once the duplication is done,
only the *new* duplicated elements are selected,
and you are automatically placed in move mode, so you can move your copy elsewhere...

In the *Toolbar* are settings for *Vector* offset, *Proportional Editing*,
*Duplication Mode*, and *Axis Constraints*.

.. TODO: Duplication Mode non-functional?

Note that duplicated elements belong to the same
:doc:`vertex groups </modeling/meshes/properties/vertex_groups/index>` as the "original" ones.
The same goes for the :ref:`material indices <bi-multiple-materials>`,
the edge's *Sharp* and *Seam* marks, and probably for the other vertex/edge/face properties...
