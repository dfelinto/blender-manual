
****************
Select More/Less
****************

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> Select More/Less --> More`
   :Shortcut:  :kbd:`Ctrl-NumpadPlus`
   :Menu:      :menuselection:`Select --> Select More/Less --> Less`
   :Shortcut:  :kbd:`Ctrl-NumpadMinus`

With at least one vertex, edge, or face selected, *Select More/Less* expands or shrinks the selection.
However, if there is only one selection in any selection mode, *Less* will deselect it.

Face Step
   With *Face Step* on, each use of the tool
   will affect the size of the selection on a face by face basis.
   When deactivated, it will be based on either vertices or edges depending on which
   :doc:`Selection Mode </modeling/meshes/selecting/introduction>` is active.

.. figure:: /images/modeling_meshes_selecting_more-less_example.png

   (From left to right) initial selection, without Face Step,
   with Face Step, and in edge selection mode.


Select Next/Previous Active
===========================

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> Select More/Less --> Next Active`
   :Shortcut:  :kbd:`Shift-Ctrl-NumpadPlus`
   :Menu:      :menuselection:`Select --> Select More/Less --> Previous Active`
   :Shortcut:  :kbd:`Shift-Ctrl-NumpadMinus`

Next Active
   This uses selection history to select the next vertex, edge, or face based on the surrounding topology.
   Which means that, it will derive the next selection from the previous two selections.

.. list-table::

   * - .. figure:: /images/modeling_meshes_selecting_more-less_select-active-1.png
          :width: 200px

          Initial selection.

     - .. figure:: /images/modeling_meshes_selecting_more-less_select-active-2.png
          :width: 200px

          Using Next Active once.

     - .. figure:: /images/modeling_meshes_selecting_more-less_select-active-3.png
          :width: 200px

          Using Next Active twice.

Previous Active
   Only the last selected element will be removed.
