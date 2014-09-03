
Buttons and Controls
********************

Buttons and other controls can be found in almost every :doc:`Window </interface/window_types>` of the Blender
interface. The different types of controls are described below.



Operation Buttons
=================

.. figure:: /images/Manual-Part-I-ConceptButtons2_25.jpg

   Operation button


These are buttons that perform an operation when clicked with :kbd:`lmb`.
They can be identified by their gray color in the default Blender scheme.

Pressing :kbd:`ctrl-C` over these buttons copies their python command into the clipboard
which can be used in the python console or in the text editor when writing scripts.


Toggle Buttons
==============

.. figure:: /images/Manual-Part-I-ConceptButtons1_1_25.jpg

   Toggle buttons


Toggle buttons consist of tick boxes.
Clicking this type of button will toggle a state but will not perform any operation.  In some
cases the button is attached to a number button to control the influence of the property.


Radio Buttons
=============

.. figure:: /images/Manual-Part-I-ConceptButtons1_25.jpg

   Radio buttons


Radio buttons are used to choose from a small selection of "mutually exclusive" options.


Number Buttons
==============

.. figure:: /images/Manual-Part-I-ConceptButtons3_25.jpg

   Number buttons


Number buttons can be identified by their labels,
which in most cases contains the name and a colon followed by a number.
Number buttons are handled in several ways:


- To change the value in steps, click :kbd:`lmb` on the small triangles on the sides of the button.
- To change the value in a wider range, hold down :kbd:`lmb` and drag the mouse to the left or right.
  If you hold :kbd:`ctrl` after holding down :kbd:`lmb`, the value is changed in discrete steps;
  if you hold :kbd:`shift` instead, you'll have finer control over the values.
- :kbd:`enter` or :kbd:`lmb` lets you enter the value by hand.

When entering values by hand, pressing :kbd:`home` or :kbd:`end` will move the
cursor to the beginning or the end of the range.
Pressing :kbd:`esc` will cancel editing.
You can copy the value of a button by hovering over it and pressing :kbd:`ctrl-C`.
Similarly you can paste a copied value with :kbd:`ctrl-V`.


Expressions
-----------

You can also enter expressions such as ``3*2`` instead of ``6``. or ``5/10+3``.
Even constants like ``pi`` (3.142) or functions like ``sqrt(2)`` (square root of 2)
may be used.

*These expressions are evaluated by Python; for all available math expressions
see:* `math module reference <http://docs.python.org/py3k/library/math.html>`__


Units
-----

As well as expressions, you can mix units with numbers; for this to work,
units need to be set in the scene settings (Metric or Imperial).

Examples of valid units include:

- ``1cm``
- ``1m 3mm``
- ``1m, 3mm``
- ``2ft``
- ``3ft/0.5km``
- ``2.2mm + 5' / 3" - 2yards``

*Note that the commas are optional.
Also notice how you can mix between metric and imperial even though the display can only show one at a time.*


Menu Buttons
============

.. figure:: /images/Manual-Part-I-ConceptButtons4_25.jpg

   Datablock link buttons


Use the Menu buttons to work with items on dynamically created lists.
Menu buttons are principally used to link DataBlocks to each other.
DataBlocks are items like Meshes, Objects, Materials, Textures, and so on.
Linking a Material to an Object will assign that material to the selected Objects.


.. figure:: /images/Manual-Part-I-ConceptButtons4_1_25.jpg

   Datablock link menu with search


- The first button (with an icon of the DataBlock type) opens a menu that lets you select the DataBlock to
  link by clicking :kbd:`lmb` on the requested item. This list has a search box at the bottom.
- The second button displays the name of the linked DataBlock and lets you edit it after clicking :kbd:`lmb`.
- The "+" button duplicates the current DataBlock and applies it.
- The "X" button clears the link.

Sometimes there is a list of applied DataBlocks
(such as a list of materials used on the object). See *DataBlock link buttons* above.


- To select a datablock, click :kbd:`lmb` on it.
- To add a new section (e.g. material, or particle system), click :kbd:`lmb` on the "+" button to the right of the list.
- To remove a section, click :kbd:`lmb` on the "-" to the right of the list.


Another type of a Menu button block will show a static list with a range of options.
For example, the Add Modifier button will produce a menu with all of the available modifiers.


.. figure:: /images/Manual-Part-I-ConceptButtons4_menue_25.jpg

   Modifier options


.. note:: Unlinked objects

   Unlinked data is *not* **lost until you quit Blender**. This is a powerful Undo feature.
   If you delete an object the material assigned to it becomes unlinked, but is still there! You
   just have to re-link it to another object or supply it with a "Fake User" (i.e.
   by clicking that option in the corresponding DataBlock in the datablock-view of the Outliner).

   :doc:`Read more about Fake User » </data_system/data_system>`


Color Selector Controls
=======================

In Blender, you can choose from **4** types of color pickers; the options are:
   :guilabel:`Circle` (Default), :guilabel:`Square (HS + V)` , :guilabel:`Square (SV + H)` and :guilabel:`Square (HV + S)`


For more information about how to select the type of color picker,
please go to the :doc:`System </preferences/system>` preferences page.



   All of the Color picker types have the common :guilabel:`RGB`, :guilabel:`HSV` and :guilabel:`Hex` options to show values.
   Optionally, depending on the operation, another slider for Alpha control is added at the bottom of the color picker.


   Blender uses Floating point values to express colors for :guilabel:`RGB` and :guilabel:`HSV` values.
   The :guilabel:`Hex` values are expressed in the same way HTML colors are expressed.


   Note that Blender corrects Gamma by default; for more information about how to disable Gamma correction in Blender,
   please go to the :doc:`Color Management and Exposure </render/post_process/cm_and_exposure>` page.


.. figure:: /images/(Doc_26x_Manual_Preferences_System)_(Color_Picker_Circle)_(GBAFN).jpg

   Fig. 2 - Color Picker - Circle


   Circle (Default)
      A full gamut of colors ranging from center to the borders is always shown; center is a mix of the colors.
      Brightness is adjusted with the right bar, from top to bottom.
      For operations that are capable of using Alpha, another slider is added at the bottom of the color picker.
      See Fig. 2 - Color Picker - Circle


.. figure:: /images/(Doc_26x_Manual_Preferences_System)_(Color_Picker_HS_PLUS_V)_(GBAFN).jpg

   Fig. 3 - Color Picker
   Square (HS + V)


   Square (HS + V)
      Hue, Saturation plus Value  **→** A full gamut of colors is always shown.
      Brightness is subtracted from the base color chosen on the square of the color picker moving the slider to the left.
      For operations that are capable of using Alpha, another slider is added at the bottom of the color picker.
      See Fig. 3 - Color Picker - Square (HS + V)


.. figure:: /images/(Doc_26x_Manual_Preferences_System)_(Color_Picker_SV_PLUS_H)_(GBAFN).jpg

   Fig. 4 - Color Picker
   Square (SV + H)


   Square (SV + H)
      Saturation, Value plus Hue  **→** A full Gamut of colors is always shown at the bar in the middle of the color picker.
      Colors are adjusted using the a range of brightness of the base color chosen at the color bar in the middle of the picker.
      For operations that are capable of using Alpha, another slider is added at the bottom of the color picker.
      See Fig. 4 - Color Picker - Square (SV + H)


.. figure:: /images/(Doc_26x_Manual_Preferences_System)_(Color_Picker_HV_PLUS_S)_(GBAFN).jpg

   Fig. 5 - Color Picker
   Square (HV + S)


   Square (HV + S)
      Hue, Value and Saturation  **→** A full gamut of colors is always shown at the square of the color picker.
      Brightness is added to the base color chosen on the square of the color picker moving the slider to the left.
      For operations that are capable of using Alpha, another slider is added at the bottom of the color picker.
      See Fig. 5 - Color Picker - Square (HV + S)


- Use :kbd:`mouse wheel` to change overall brightness.
- Color sliders don't have a default value; the last value before any changes is used instead.


Eye Dropper
-----------

The eye dropper allows you to sample a color from anywhere in the Blender window. The Eye
Dropper can be accessed from any color picker or by pressing :kbd:`E` with the mouse
hovering over the color property.

:kbd:`lmb` and dragging the eyedropper will mix the colors you drag over which can help when sampling noisy imagery.
:kbd:`spacebar` resets and starts mixing the colors again.


Cascade Buttons
===============

Occasionally, some buttons actually reveal additional buttons. For example, the
:guilabel:`Ramps` panel has a :guilabel:`Cascade` button called :guilabel:`Ramp` that reveals
additional buttons dealing with colorbanding.
See *Colorband before* and *Colorband after*.


+-------------------------------------------------------------------+------------------------------------------------------------------+
+.. figure:: /images/Manual-Part-I-Interface-ColorBand-Before_25.jpg|.. figure:: /images/Manual-Part-I-Interface-ColorBand-After_25.jpg+
+   :width: 310px                                                   |   :width: 310px                                                  +
+   :figwidth: 310px                                                |   :figwidth: 310px                                               +
+                                                                   |                                                                  +
+   Colorband before                                                |   Colorband after                                                +
+-------------------------------------------------------------------+------------------------------------------------------------------+


Color Ramps
   :guilabel:`Color Ramps` enables the user to specify a range of colors based on color stops.
   Color stops are similar to a mark indicating where the exact chosen color should be.
   The interval from each of the color stops added to the ramp is a result of the color interpolation and
   chosen interpolation method. The available options for Color Ramps are:


   Add (Button)
      Clicking on this button will add a stop to your custom weight paint map.
      The stops are added from the last selected stop to the next one, from left to right and
      they will be placed in the middle of both stops.


   Delete (Button)
      Deletes the selected color stop from the list.


   'F' (Button)
      Flips the color band, inverting the values of the custom weight paint range.


   Numeric Field
      Whenever the user adds a color stop to the custom weight paint range, the color stop will receive an index.
      This field shows the indexes added (clicking in the arrows until the counter stops), and allows
      the user to select the color stop from the list. The selected color stop will be shown with a dashed line.


   Interpolation Options
      Enables the user to choose from **4** types of calculations for the color interpolation for each color stop.
      Available options are:


      B-Spline
         Uses a :guilabel:`B-Spline` Interpolation for the color stops.
      Cardinal
         Uses a :guilabel:`Cardinal` Interpolation for the color stops.
      Linear
         Uses a :guilabel:`Linear` Interpolation for the color stops.
      Ease
         Uses a :guilabel:`Ease` Interpolation for the color stops.
      Constant
         Uses a :guilabel:`Constant` Interpolation for the color stops.


   Position
      This slider controls the positioning of the selected color stop in the range.


   Color Bar
      Opens a color Picker for the user to specify color and Alpha for the selected color stop.
      When a color is using Alpha, the Color Bar is then divided in two, with the left side
      showing the base color and the right side showing the color with the alpha value.

