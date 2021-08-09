
******
Sculpt
******

Show & Hide
===========

.. reference::

   :Mode:      Sculpt Mode
   :Menu:      :menuselection:`Sculpt`

Portions of the mesh can be hidden in Sculpt Mode to improve the viewport performance and
to access parts of the mesh that would otherwise be difficult to access,
because they are occluded by other parts. The hidden faces cannot be sculpted on.
Hiding is shared between Edit Mode and Sculpt Mode
(i.e. hiding/unhiding in one mode affects the other mode too).

Show All :kbd:`Alt-H`
   Reveal all hidden parts.
Show Bounding Box :kbd:`Shift-H`
   To reveal a hidden part of a mesh inside the selection.
Hide Bounding Box :kbd:`H`
   To hide a part of a mesh inside the selection.
   This works similar to the :ref:`Box Select <tool-select-box>` tool.
Hide Masked
   Hides all masked vertices.


.. _bpy.ops.sculpt.set_pivot_position:

Set Pivot
=========

.. reference::

   :Mode:      Sculpt Mode
   :Menu:      :menuselection:`Sculpt --> Set Pivot`

Like Object and Edit Mode, Sculpt Mode also has a :term:`Pivot Point`.
This is because the basic move, scale, rotate transforms are also possible in Sculpt Mode.

Origin
   Sets the pivot to the origin of the sculpt.
Unmasked
   Sets the pivot position to the average position of the unmasked vertices.
Mask Border
   Sets the pivot position to the center of the mask's border.
Active Vertex
   Sets the pivot position to the active vertex position.
Surface
   Sets the pivot position to the surface under the cursor.

.. seealso::

   :doc:`Object and Edit Mode Pivot </editors/3dview/controls/pivot_point/index>`


.. _bpy.ops.sculpt.optimize:

Rebuild BVH
===========

.. reference::

   :Mode:      Sculpt Mode
   :Menu:      :menuselection:`Sculpt --> Rebuild BVH`

Recalculates the :term:`BVH` used by :doc:`/sculpt_paint/sculpting/tool_settings/dyntopo`
which can improve performance which might degrade over time while using Dyntopo.


.. _bpy.ops.object.transfer_mode:

Transfer Sculpt Mode
====================

.. reference::

   :Mode:      Sculpt Mode
   :Menu:      :menuselection:`Sculpt --> Transfer Sculpt Mode`
   :Shortcut:  :kbd:`Alt-Q`

Adds the object under the mouse to Sculpt Mode and removes the :term:`Active` from Sculpt Mode.
This operator is useful to easily switch between objects when you want to sculpt on multiple objects at once.

When accessed from the menu, an :ref:`ui-eyedropper` is used to select the object to add to Sculpt Mode.
