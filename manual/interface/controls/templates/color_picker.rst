.. _ui-color-picker:

************
Color Picker
************

.. figure:: /images/interface_controls_templates_color-picker_circle-hsv.png
   :align: right

   Circle HSV.

The color picker is a pop-up that lets you define a color value.
Holding :kbd:`Ctrl` while dragging snaps the hue to make it quick to select primary colors.

Color field
   Lets you pick the first and second color component. The shape can be selected by the `Types`_.
Color slider
   The slider with a gradient in the background lets you define the third color component.
   It can also be controlled with the :kbd:`Wheel`.

Color space
   Selects the :term:`Color Space` for the number fields below.

   RGB, HSV/HSL, Hex
Color values
   Blender uses (0 to 1.0) values to express colors for RGB and HSV colors.

   Hexadecimal (Hex) values are expressed as ``RRGGBB``.
   Shorthand hex colors are also supported as ``RGB``,
   e.g. dark-yellow ``FFCC00``, can be written as ``FC0``.

   For operations that are capable of using Alpha, another slider "A" is added.
Eyedropper
   The :ref:`ui-eyedropper` (pipette icon) can be used
   to sample a color value from inside the Blender window.

.. note::

   In Blender, the *Hex* and HSV/HSL values are automatically :term:`Gamma` corrected; however,
   for the RGB values, they are in Scene Linear color space, and are therefore not gamma corrected.
   For more information, see the :doc:`Color Management and Exposure </render/color_management>` page.


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


Shortcuts
---------

- :kbd:`Ctrl-LMB` (drag) snaps to hue.
- :kbd:`Shift-LMB` (drag) precision motion.
- :kbd:`Wheel` adjust the brightness.
- :kbd:`Backspace` reset the value.
