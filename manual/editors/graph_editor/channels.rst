
********
Channels
********

Channels Region
===============

.. figure:: /images/editors_graph-editor_channels_region.png

   The Channels region.

The channels region is used to select and manage the curves for the Graph editor.
This part shows the objects and their animation data hierarchy each as headers.
Each level can be expanded/collapsed by the small arrow to the left of its header.

- Scenes, Objects (dark blue)
- :doc:`Actions </animation/actions>`, :doc:`Shape keys </animation/shape_keys/index>`, etc. (light blue)
- Groups (green)
- Channels (gray)

.. _bpy.types.DopeSheet.use_filter_invert:
.. _bpy.types.DopeSheet.filter_text:

Name Filter
   Only displays channels that match the search text.
   Pressing the invert button displays all channels except the channels that match the search text.


Controls
--------

On the headers, there are toggles to control channel's setting:

Pin (pin icon)
   Make the channel always visible regardless of the current selection (Graph editor only).
Hide (eye icon)
   Hides the channel(s)/curve (Graph editor only).
Modifiers (wrench icon)
   Deactivates the F-curve modifiers of the selected curve or all curves in the channel.
Mute (speaker icon)
   Deactivates the channel/curve.
Lock (padlock icon) :kbd:`Tab`
   Toggle channel/curve from being editable.
   Selected channels can be locked by pressing :kbd:`Tab`.

   .. note::

      In the Dope Sheet this is also working inside the NLA,
      but that it does not prevent edition of the underlying F-curve.


Selecting
---------

- Select channel (text in white/black): :kbd:`LMB`
- Multi Select/Deselect: :kbd:`Shift-LMB`
- Select All: :kbd:`A`
- Deselect All: :kbd:`Alt-A`
- Box Select: (:kbd:`LMB` drag) or :kbd:`B` (:kbd:`LMB` drag)
- Box Deselect: (:kbd:`Ctrl-LMB` drag) or :kbd:`B` (:kbd:`Shift-LMB` drag)
- Select all keyframes in the channel: double :kbd:`LMB` on a channel header.


Editing
-------

- Rename: :kbd:`Ctrl-LMB`
- Delete selected: :kbd:`X` or :kbd:`Delete`
- Lock selected: :kbd:`Tab`
- Enable Channel Setting: :kbd:`Shift-Ctrl-W`
- Disable Channel Setting: :kbd:`Alt-W`
- Toggle Channel Setting: :kbd:`Shift-W`


Sliders
^^^^^^^

.. figure:: /images/editors_dope-sheet_introduction_action-editor-sliders.png

   The Action editor showing sliders.

On channels headers you can have another column with number fields or sliders,
allowing you to change the value on the current keyframes, or to add new keyframes.
See :ref:`graph-view-menu` for how to show these sliders.


Editing
=======

.. _bpy.ops.anim.channels_delete:

Delete Channels
---------------

.. reference::

   :Menu:      :menuselection:`Channel --> Delete Channels`
   :Shortcut:  :kbd:`X`

Deletes the whole channel from the current action
(i.e. unlink the underlying F-curve data-block from this action data-block).

.. warning::

   The :kbd:`X` shortcut is area-dependent: if you use it in the left list part,
   it will delete the selected channels, whereas if you use it in the main area,
   it will delete the selected keyframes.


.. _bpy.ops.anim.channels_group:
.. _bpy.ops.anim.channels_ungroup:

Un/Group Channels
-----------------

.. reference::

   :Menu:      :menuselection:`Channel --> Un/Group Channels`
   :Shortcut:  :kbd:`Ctrl-Alt-G`, :kbd:`Ctrl-G`

Un/Groups the selected channels into a collection that can be renamed by double clicking on the group name.
For example, this helps to group channels that relate a part of an armature to keep the editor more organized.


.. _bpy.ops.anim.channels_setting_toggle:
.. _bpy.ops.anim.channels_enable_toggle:
.. _bpy.ops.anim.channels_disable_toggle:

Toggle/Enable/Disable Channel Settings
--------------------------------------

.. reference::

   :Menu:      :menuselection:`Channel --> Toggle/Enable/Disable Channel Settings`
   :Shortcut:  :kbd:`Shift-W`, :kbd:`Shift-Ctrl-W`, :kbd:`Alt-W`

Enable/disable a channel's setting (selected in the menu that pops up).

Protect, Mute
   Todo.


.. _bpy.ops.anim.channels_editable_toggle:

Toggle Channel Editability
--------------------------

.. reference::

   :Menu:      :menuselection:`Channel --> Toggle Channel Editability`
   :Shortcut:  :kbd:`Tab`

Locks or unlocks a channel for editing.


.. _editors-graph-fcurves-settings-extrapolation:
.. _bpy.ops.graph.extrapolation_type:

Extrapolation Mode
------------------

.. reference::

   :Menu:      :menuselection:`Channel --> Extrapolation Mode`
   :Shortcut:  :kbd:`Shift-E`

Change the extrapolation between selected keyframes.

Extrapolation defines the behavior of a curve before the first and after the last keyframes.

There are two basic extrapolation modes:

:Constant:
   .. figure:: /images/editors_graph-editor_fcurves_introduction_extrapolate1.png
      :align: right
      :width: 300px

      Constant extrapolation.

   The default one, curves before their first keyframe and after their last one have a constant value
   (the one of these first and last keyframes).

:Linear:
   .. figure:: /images/editors_graph-editor_fcurves_introduction_extrapolate2.png
      :align: right
      :width: 300px

      Linear extrapolation.

   Curves ends are straight lines (linear), as defined by the slope of their first and last keyframes.

Additional extrapolation methods (e.g. the *Cycles* modifier)
are located in the :doc:`F-Curve Modifiers </editors/graph_editor/fcurves/modifiers>`.


.. _bpy.ops.graph.hide:
.. _bpy.ops.graph.reveal:

Show/Hide
---------

Hide Selected Curves :kbd:`H`
   Hides the selected curves.
Hide Unselected :kbd:`Shift-H`
   Show only the selected curve (and hide everything else).
Reveal Curves :kbd:`Alt-H`
   Show all previous hidden curves.


.. _bpy.ops.anim.channels_expand:
.. _bpy.ops.anim.channels_collapse:

Expand/Collapse Channels
------------------------

.. reference::

   :Menu:      :menuselection:`Channel --> Expand/Collapse Channels`
   :Shortcut:  :kbd:`NumpadPlus`, :kbd:`NumpadMinus`

Expands or collapses selected channels.


.. _bpy.ops.anim.channels_move:

Move
----

.. reference::

   :Menu:      :menuselection:`Channel --> Move...`

This allows you to move selected channels up/down :kbd:`PageUp`, :kbd:`PageDown`,
or directly to the top/bottom :kbd:`Shift-PageUp`, :kbd:`Shift-PageDown`.


.. _bpy.ops.anim.channels_fcurves_enable:

Revive Disabled F-Curves
------------------------

.. reference::

   :Menu:      :menuselection:`Channel --> Revive Disabled F-Curves`

Clears "disabled" tag from all F-curves to get broken F-curves working again.
