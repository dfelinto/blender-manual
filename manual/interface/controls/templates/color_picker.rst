.. _ui-color-picker:

************
Color Picker
************

.. figure:: /images/interface_controls_templates_color-picker_circle-hsv.png
   :align: right

   Circle HSV.

The color picker is a pop-up that lets you define a color value.
Holding :kbd:`Ctrl` while dragging snaps the hue to make it quick to select primary colors.

Color Field
   Lets you pick the first and second color component. The shape can be selected by the `Types`_.

Color Slider
   The slider with a gradient in the background lets you define the third color component.
   It can also be controlled with the :kbd:`Wheel`.

Color Model
   Selects the :term:`Color Space` for the number fields below.

   RGB, HSV/HSL, Hex

   .. note::

      In Blender, the RGB and HSV/HSL values are in Scene Linear color space,
      and are therefore not :term:`Gamma` corrected.
      On the contrary, *Hex* are automatically :term:`Gamma`
      corrected for the :term:`sRGB Color Space <Color Space>`.
      For more information, see :doc:`Color Management </render/color_management>`.

Color Values
   Blender uses (0 to 1.0) values to express colors for RGB and HSV colors.

   Hexadecimal (Hex) values are expressed as ``RRGGBB``.
   Shorthand hex colors are also supported as ``RGB``,
   e.g. dark-yellow ``FFCC00``, can be written as ``FC0``.

   For operations that are capable of using the :term:`Alpha Channel`, another slider "A" is added.

.. _bpy.ops.ui.eyedropper_color:

Eyedropper (pipette icon)
   Samples a color from inside the Blender window using the :ref:`ui-eyedropper`
   The :ref:`ui-eyedropper` (pipette icon) can be used
   to sample a color value from inside the Blender window.


Shortcuts
=========

- :kbd:`Ctrl-LMB` (drag) snaps to hue.
- :kbd:`Shift-LMB` (drag) precision motion.
- :kbd:`Wheel` adjust the brightness.
- :kbd:`Backspace` reset the value.


Types
=====

The default color picker type can be selected in the Preferences,
see: :ref:`Interface <prefs-interface-color-picker-type>`.

Circle
   The color values ranging from center to the borders. The center is a mix of the colors.
Square
   The Borders of the square are the axis for the two color components, with the center on the bottom right.

.. list-table:: Color Picker types.

   * - .. figure:: /images/interface_controls_templates_color-picker_circle-hsv.png

          Circle HSV.

     - .. figure:: /images/interface_controls_templates_color-picker_circle-hsl.png

          Circle HSL.

     - ..

   * - .. figure:: /images/interface_controls_templates_color-picker_square-sv-h.png

          Square (SV + H).

     - .. figure:: /images/interface_controls_templates_color-picker_square-hs-v.png

          Square (HS + V).

     - .. figure:: /images/interface_controls_templates_color-picker_square-hv-s.png

          Square (HV + S).
