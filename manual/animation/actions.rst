.. _bpy.types.Action:
.. _bpy.ops.action:

*******
Actions
*******

When animating objects and properties in Blender, Actions record and contain the data.
As everything else in Blender, Actions are data-blocks.

.. figure:: /images/animation_actions_data3.png

   Actions.

So when you animate an object by changing its location with keyframes,
the animation is saved to the Action.

Each property has a channel which it is recorded to, for example,
``Cube.location.x`` is recorded to Channel X Location.
The *X location* and *Y location* properties can be shared across multiple objects,
if all objects have *X location* and *Y location* properties beneath them.

.. figure:: /images/animation_actions_keyframes.png

   Graph Editor. Each channel has an F-Curve represented by the lines between the keyframes.

Actions
   Record and contain animation data.
Groups
   Are groups of channels.
Channels
   Record properties.
F-Curves
   :doc:`F-Curves </editors/graph_editor/fcurves/introduction>` are used to
   interpolate the difference between the keyframes.
Keyframes
   :doc:`Keyframes </animation/keyframes/introduction>` are used to
   set the values of properties bound to a point in time.

.. The hierarchy is created with the RNA data paths,


.. _actions-workflow:

Working with Actions
====================

.. figure:: /images/animation_actions_create.png
   :align: right

   The Action data-block menu.

When you first animate an object by adding keyframes,
Blender creates an *Action* to record the data.

*Actions* can be managed with the *Action data-block menu*
in the Dope Sheet :doc:`Action Editor </editors/dope_sheet/action>` header,
or the Sidebar region of the :doc:`NLA Editor </editors/nla/sidebar>`.

If you are making multiple actions for the same object,
press the shield button for each action.
This will give the actions a *Fake User* and will make Blender save the unlinked actions.

Objects can only use one *Action* at a time for editing.
The :doc:`NLA Editor </editors/nla/index>` is used to blend multiple actions together.


Properties
==========

.. figure:: /images/animation_actions_range.png
   :align: center

   Actions with and without a Manual Frame Range in Dope Sheet.

It is possible to manually specify the intended useful frame range of an action via a panel
available in the :doc:`Dope Sheet </editors/dope_sheet/introduction>` or the :doc:`NLA Editor </editors/nla/sidebar>`
when a channel or NLA track is selected.

.. _bpy.types.Action.use_frame_range:

Manual Frame Range
   Manually specify the intended playback frame range for the action
   (this range is used by some tools, but does not affect animation evaluation).
   The manual frame range feature can be toggled with the checkbox.

   When the range is set, it is used instead of the actual range occupied by key frames
   when adding a new track based on the action to NLA. It can also be used by exporters
   to determine the range of frames to export.

   The range is displayed in the background of the editor as diagonal hash fill, to
   distinguish it from the solid fill of the current playback range.

   The frame values are most commonly expected to be integers, but can be fractional.

.. _bpy.types.Action.use_cyclic:

Cyclic Animation
   Specifies that the action is intended to be cyclic over the specified range. The first and last
   frames of the range should represent the same pose of the cycle one loop apart, i.e. the range
   should include the duplicated initial key of the loop.

   .. note::

      This option signifies intent and does **not** make the action cycle on its own. However,
      if :ref:`Cycle-Aware Keying <bpy.types.ToolSettings.use_keyframe_cycle_aware>` is enabled,
      it will automatically enable cyclic extrapolation and set up the loop period for curves
      newly added to the action.


Custom Properties
-----------------

Create and manage your own properties to store data in the action's data block.
See the :ref:`Custom Properties <files-data_blocks-custom-properties>` page for more information.
