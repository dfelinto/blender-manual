
***********
Slide Relax
***********

.. admonition:: Reference
   :class: refbox

   :Mode:      Sculpt Mode
   :Tool:      :menuselection:`Toolbar --> Slide Relax`

This brush slides the topology of the mesh to areas that require more detail.
The brush does this while minimizing changes to the geometrical shape of the mesh.
When pressing :kbd:`Shift`, the brush enters *Relax* mode
which tries to create an even distribution of quads without deforming the volume of the mesh.


Brush Settings
==============

.. _bpy.types.Brush.slide_deform_type:

Deformation
   Deformation type that is used by the brush.

   Drag
      Slides or pulls the topology of the mesh in the direction of the stroke.
   Pinch
      Slides the topology of the mesh towards the center of the stroke.
   Expand
      Slides the topology of the mesh away from the center of the stroke.
