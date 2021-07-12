.. _bpy.ops.mesh.select_nth:

****************
Checker Deselect
****************

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> Checker Deselect`

This tool applies an alternating selected/deselected checker pattern.
This only works if you already have more than one mesh element selected.

Changes the current selection so that only every Nth elements (vertices, edges or faces,
depending on the active selection mode) will remain selected, starting from the active one.

In case of islands of selected elements, this tool will affect
only the island of the active element (if there is one), or the island of the first element
in the order of internal storage (if there is no active element).

Deselected
   The number of deselected elements in each pattern repetition.
Selected
   The number of selected elements in each pattern repetition.
Offset
   Offset from the starting point.
