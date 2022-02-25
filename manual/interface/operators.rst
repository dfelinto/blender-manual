
*********
Operators
*********

Operators execute an action as soon as the operator is started
which make them different from tools which require some sort of input.
Operators can be started from a :ref:`ui-operator-buttons`,
:ref:`ui-header-menu`, or :ref:`bpy.ops.wm.search_menu`.
Examples of operators include adding a new object,
deleting it, or setting its shading to smooth.


Operator Properties
===================

Most operators have properties that can be adjusted to refine the result of the operation.
To adjust an operators properties, the operator must first be executed.
This will execute the operation with its default property values.
These properties can then be adjusted using :ref:`bpy.ops.screen.redo_last`.


Modal Operators
===============

Modal operators exist as concept in between :doc:`Tools </interface/tool_system>`
and regular described above operators.
They require some sort of input to interactively control the operator's properties.


Slider Operators
----------------

Slider operators are a type of modal operator used interactively adjust a factor property.
Slider operators will display a percentage graphic in the editor's :ref:`ui-region-header`.
Slider operators can adjust the operator's factor value by moving
the mouse left or right to decrease or increase the factor property.

Values can be snapped to 10% increments by holding :kbd:`Ctrl`
and changed using precision by holding :kbd:`Shift`.
Values can extend beyond the 0-100% range by toggling "overshoot" on with :kbd:`E`.
Note, overshoot is not be available for all slider operators.
