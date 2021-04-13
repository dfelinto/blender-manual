
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

Delete Channels
---------------

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Channel --> Delete Channels`
   :Hotkey:    :kbd:`X`

Deletes the whole channel from the current action
(i.e. unlink the underlying F-curve data-block from this action data-block).

.. warning::

   The :kbd:`X` shortcut is area-dependent: if you use it in the left list part,
   it will delete the selected channels, whereas if you use it in the main area,
   it will delete the selected keyframes.


Un/Group Channels
-----------------

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Channel --> Un/Group Channels`
   :Hotkey:    :kbd:`Ctrl-Alt-G`, :kbd:`Ctrl-G`

Un/Groups the selected channels into a collection that can be renamed by double clicking on the group name.
For example, this helps to group channels that relate a part of an armature to keep the editor more organized.


Toggle/Enable/Disable Channel Settings
--------------------------------------

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Channel --> Toggle/Enable/Disable Channel Settings`
   :Hotkey:    :kbd:`Shift-W`, :kbd:`Shift-Ctrl-W`, :kbd:`Alt-W`

Enable/disable a channel's setting (selected in the menu that pops up).

Protect, Mute
   Todo.


Toggle Channel Editability
--------------------------

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Channel --> Toggle Channel Editability`
   :Hotkey:    :kbd:`Tab`

Locks or unlocks a channel for editing.


Extrapolation Mode
------------------

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Channel --> Toggle Channel Editability`
   :Hotkey:    :kbd:`Shift-E`

Change the :ref:`extrapolation <editors-graph-fcurves-settings-extrapolation>` between selected keyframes.


Expand/Collapse Channels
------------------------

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Channel --> Toggle Channel Editability`
   :Hotkey:    :kbd:`NumpadPlus`, :kbd:`NumpadMinus`

Expands or collapses selected channels.


Show/Hide
---------

Hide Selected Curves :kbd:`H`
   Hides the selected curves.
Hide Unselected :kbd:`Shift-H`
   Show only the selected curve (and hide everything else).
Reveal Curves :kbd:`Alt-H`
   Show all previous hidden curves.


Move
----

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Channel --> Move...`

This allows you to move selected channels up/down :kbd:`PageUp`, :kbd:`PageDown`,
or directly to the top/bottom :kbd:`Shift-PageUp`, :kbd:`Shift-PageDown`.


Revive Disabled F-Curves
------------------------

.. admonition:: Reference
   :class: refbox

   :Menu:      :menuselection:`Channel --> Toggle Channel Editability`

Clears "disabled" tag from all F-curves to get broken F-curves working again.
