.. _bpy.ops.transform.mirror:

******
Mirror
******

.. admonition:: Reference
   :class: refbox

   :Mode:      Object and Edit Modes
   :Menu:      :menuselection:`Object/Mesh --> Mirror`
   :Hotkey:    :kbd:`Ctrl-M`

Mirroring an object or mesh selection will create a reversed version of the selection.
The position of the mirrored version of the selection is determined by
the :doc:`Pivot Point </editors/3dview/controls/pivot_point/index>`.
A common use of mirroring is to model half an object, duplicate it and then use
the mirror transform to create a reversed version to complete the model.

.. note::

   Mirrored duplicates can also be created with a :doc:`Mirror Modifier </modeling/modifiers/generate/mirror>`.

.. _fig-mesh-duplicating-mirror-selection:

.. figure:: /images/scene-layout_object_editing_mirror_example.png

   Mirroring a selection.


Usage
=====

To mirror a selection along a particular global axis, press:
:kbd:`Ctrl-M`, followed by :kbd:`X`, :kbd:`Y` or :kbd:`Z`.
The image :ref:`Mirroring a Selection <fig-mesh-duplicating-mirror-selection>`
shows the results of this action after a mesh element has been duplicated.

In mesh mode, you can mirror the selection on the currently selected
:doc:`Transform Orientations </editors/3dview/controls/orientation>`
by pressing the appropriate axis key a second time. For example,
if the Transform Orientation is set to *Normal*, pressing:
:kbd:`Ctrl-M`, followed by :kbd:`X` and then :kbd:`X` again
will mirror the selection along the X axis of the *Normal Orientation*.

.. figure:: /images/scene-layout_object_editing_mirror_panel.png

   Mirror :ref:`ui-undo-redo-adjust-last-operation` panel.

You can alternatively hold the :kbd:`MMB` to interactively mirror the object by moving
the mouse in the direction of the mirror axis.
