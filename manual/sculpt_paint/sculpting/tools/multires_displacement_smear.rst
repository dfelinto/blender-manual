
***************************
Multires Displacement Smear
***************************

.. admonition:: Reference
   :class: refbox

   :Mode:      Sculpt Mode
   :Tool:      :menuselection:`Toolbar --> Multires Displacement Smear`

This tool deforms displacement information of
the :doc:`Multires Modifier </modeling/modifiers/generate/multiresolution>`,
moving the displaced vertices without affecting the base mesh.

As the tool only modifies displacement values instead of base vertex values,
the total displacement of the affected area does not change.
Which means that this smearing effect can be used multiple times
over the same area without generating any artifacts in the topology.

.. tip::

   This brush works best after using :ref:`Apply Base <bpy.ops.object.multires_base_apply>`.


Brush Settings
==============

Deformation
   Deformation type that is used by the brush.

   :Drag: Pulls the displacement values in the direction of the brush.
   :Pinch: Pulls the displacement values towards the center of the brush,
           creating hard surface effects without pinching the topology.
   :Expand: Pushes the displacement values away from the brush center, smoothing the displacement.
