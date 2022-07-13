
*********
Operators
*********

Operators execute an action the moment they're activated,
which makes them different from tools (which require some sort of input).
Operators can be started from :ref:`ui-operator-buttons`,
:ref:`ui-header-menu`, or :ref:`bpy.ops.wm.search_menu`.
Examples of operators include adding a new object,
deleting it, or setting its shading to smooth.


Operator Properties
===================

Most operators have properties that can be adjusted to refine their result.
First run the operator (which will use its default settings),
then adjust the properties in the :ref:`bpy.ops.screen.redo_last` region.


Modal Operators
===============

Modal operators exist as a concept in between :doc:`Tools </interface/tool_system>`
and regular operators.
They require some sort of interactive input.

The action of a modal operator can be confirmed using :kbd:`LMB` or :kbd:`Return`.
To cancel a modal operator use :kbd:`RMB` or :kbd:`Esc`.


Slider Operators
----------------

Slider operators are used to interactively adjust a percentage value
in the editor's :ref:`ui-region-header`.

You can adjust the percentage by dragging the slider left or right.
This can be made coarser (snapping in 10% increments) by holding :kbd:`Ctrl`
and more precise by holding :kbd:`Shift`.
For some sliders, you can toggle "overshoot" with :kbd:`E`, which lets
you go beyond the 0-100% range.
