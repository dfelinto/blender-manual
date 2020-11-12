.. _bpy.types.LineStyle*Modifier_CreaseAngle:
.. Editors Note: This page gets copied into:
   :doc:`</render/freestyle/parameter_editor/line_style/modifiers/alpha/crease_angle>`
   :doc:`</render/freestyle/parameter_editor/line_style/modifiers/thickness/crease_angle>`
.. --- copy below this line ---

************
Crease Angle
************

A modifier based on the Crease Angle (angle between two adjacent faces).
If a stroke segment does not lie on a crease (i.e. the edge does not have the *Crease Angle nature*),
its properties are not touched by the modifier.

Min Angle and Max Angle
   The range of input values to the mapping.
   Out-of-range crease angle values will be clamped by
   the Min and Max angles and their corresponding property values.

.. figure:: /images/render_freestyle_parameter-editor_line-style_modifiers_color_crease-angle_example.png
   :align: center
   :width: 50%

   Crease Angle modifier example by T.K.
   (`blend-file <https://wiki.blender.org/uploads/b/b4/Render_freestyle_modifier_crease_angle.blend>`__).
