
**************
Elastic Deform
**************

.. admonition:: Reference
   :class: refbox

   :Mode:      Sculpt Mode
   :Tool:      :menuselection:`Toolbar --> Elastic Deform`

Used to simulate realistic deformations such as grabbing or twisting of :term:`Elastic` objects.
For example, this tool works great for modeling the shape of flesh like objects such as humans or animals.
When pressing :kbd:`Ctrl`, the brush deforms vertices along the normal of the active vertex.


Brush Settings
==============

.. _bpy.types.Brush.elastic_deform_type:

Deformation
   The surface alteration that is used in the brush.

   Grab
      Used to drag a group of vertices around.
   Bi-scale Grab
      Like *Grab* but the falloff is more localized to the center of the brush.
   Tri-scale Grab
      Like *Bi-scale Grab* but the falloff is more localized to the center of the brush.
   Scale
      Displaces vertices away from the active vertex.
   Twist
      Vertices are rotated around the active vertex.

.. _bpy.types.Brush.elastic_deform_volume_preservation:

Volume Preservation
   Poisson ratio for elastic deformation.
   Higher values preserve volume more, but also lead to more bulging.
