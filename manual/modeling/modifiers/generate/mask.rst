.. index:: Modeling Modifiers; Mask Modifier
.. _bpy.types.MaskModifier:

*************
Mask Modifier
*************

The *Mask* modifier allows vertices of an object to be hidden dynamically based on vertex groups.


Options
=======

Mode
   The Mask Modifier can hide parts of a mesh based on two different modes, selectable from this select menu.

   Vertex Group
      When the *Vertex Group* option is selected,
      all vertices belonging to the chosen vertex group (with a weight above zero) will be visible,
      and all other vertices will be hidden.

      .. list-table:: The Mask modifier in Vertex Group mode.

         * - .. figure:: /images/modeling_modifiers_generate_mask_vertex-group.png

           - .. figure:: /images/modeling_modifiers_generate_mask_panel-vertex-group.png

   Armature
      When in Pose Mode,
      vertices belonging to the vertex group associated with the active bone (same names) will be visible.
      Vertices not in that group will be hidden.

      .. list-table:: The Mask modifier in Armature mode.

         * - .. figure:: /images/modeling_modifiers_generate_mask_armature.png

           - .. figure:: /images/modeling_modifiers_generate_mask_panel-armature.png

Invert
   Normally, vertices belonging to the selected vertex group (or group associated with the active pose bone)
   will be shown. The *Invert* toggle allows you to reverse this behavior, instead only showing vertices
   which do not belong to the vertex group.

Threshold
   Vertices with weights less or equal to this value will be hidden.
