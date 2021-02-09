
*********
Selecting
*********

By default Blender uses the :kbd:`LMB` to select items in the Blender window.
Alternatively, the :kbd:`RMB` can be used instead by changing
the :doc:`Preferences </editors/preferences/keymap>`.
Blender has several selecting tools that can be used across the different editors.


Selection Tools
===============

.. _tool-select-tweak:

Tweak
-----

.. admonition:: Reference
   :class: refbox

   :Hotkey:    :kbd:`LMB`

Clicking on an item selects it, using modifier keys you can perform other operations.
Holding the selection and moving the mouse on interactive items such as objects in the 3D Viewport
or keyframes in an animation editor will general move the item with the mouse.


.. _bpy.ops.*.select_box:
.. _tool-select-box:

Box Select
----------

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Select --> Box Select`
   :Hotkey:    :kbd:`B`

To activate the tool, press :kbd:`B` or click and drag :kbd:`LMB`.
With *Select Box* you draw a rectangle while holding down :kbd:`LMB`.
Any item that lies even partially within this rectangle becomes selected.
If any item that was last active appears in the selection it will become active.

For deselecting items, use :kbd:`MMB`, or :kbd:`Shift-LMB`.
To move the selection area hold :kbd:`Ctrl-Spacebar` while moving the cursor.

.. list-table:: Box Select example.

   * - .. _fig-mesh-select-basics-start:

       .. figure:: /images/interface_selecting_border-select1.png
          :width: 200px

          Start.

     - .. _fig-mesh-select-basics-selecting:

       .. figure:: /images/interface_selecting_border-select2.png
          :width: 200px

          Selecting.

     - .. _fig-mesh-select-basics-complete:

       .. figure:: /images/interface_selecting_border-select3.png
          :width: 200px

          Complete.


.. _bpy.ops.*.select_circle:
.. _tool-select-circle:

Circle Select
-------------

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Select --> Circle Select`
   :Hotkey:    :kbd:`C`

*Circle Select* :kbd:`C` allows you to select multiple items within a circular area.
Move your mouse over any items within the circular area (shown with a dotted circle)
while holding :kbd:`LMB` to select those items. Alternatively, use
:kbd:`MMB` to deselect them. When you're done selecting, press :kbd:`RMB` or
:kbd:`Esc`. To change the diameter of the circle, scroll with the :kbd:`Wheel`
or use the :kbd:`NumpadPlus` and :kbd:`NumpadMinus` keys.

.. list-table:: Circle Select example.

   * - .. figure:: /images/interface_selecting_circle-select1.png
          :width: 320px

          Start.

     - .. figure:: /images/interface_selecting_circle-select2.png
          :width: 320px

          Selecting.

     - .. figure:: /images/interface_selecting_circle-select3.png
          :width: 320px

          Dragging.

.. note::

   In *Object Mode* the *Circle Select* operates on objects by their origins.


.. _bpy.ops.*.select_lasso:
.. _tool-select-lasso:

Lasso Select
------------

.. admonition:: Reference
   :class: refbox

   :Hotkey:    :kbd:`Ctrl-RMB`

*Lasso Select* is used to create a free-form selection. Simply hold :kbd:`Ctrl-RMB`
while drawing a dotted line around the items you want to select.
The shape you draw will be automatically closed by connecting a line
from the current position back to the starting point.

*Lasso Select* adds to the previous selection. For deselection, use :kbd:`Shift-Ctrl-RMB`.
To move the selection area hold :kbd:`Ctrl-Spacebar` while moving the cursor.

.. list-table:: An example of using the *Lasso Select tool* in *Vertex Select Mode*.

   * - .. figure:: /images/interface_selecting_lasso-select1.png
          :width: 200px

          Start.

     - .. figure:: /images/interface_selecting_lasso-select2.png
          :width: 200px

          Selecting.

     - .. figure:: /images/interface_selecting_lasso-select3.png
          :width: 200px

          Complete.

.. note::

   In *Object Mode* the *Lasso Select* operates on objects by their origins.


Selecting Modes
===============

.. admonition:: Reference
   :class: refbox

   :Tool:      Select Tools
   :Panel:     :menuselection:`Tool Settings --> Mode`

Each tool has some sort of mode to configure how to tool interacts with existing selections.
Note that not every selection tool supports each of these modes.

Set
   Sets a new selection ignoring any existing selections.
Extend
   Adds newly selected items to the existing selection.
   The selection can also be extended by :kbd:`Shift-LMB`.
Subtract
   Removes newly selected items from the existing selection.
   Items can be removed from the selection by :kbd:`Shift-LMB` already selected items.
Invert
   Selects non-selected items and deselects existing selection.
   The selection can also be inverted by :kbd:`Ctrl-I`.
Intersect
   Selects items that intersect with existing selection.
