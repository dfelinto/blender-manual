
Action Actuator
***************

.. figure:: /images/BGE_Actuator_Action.jpg
   :width: 292px
   :figwidth: 292px

   Action Actuator


Actuates armature actions, and sets the playback method.
The Action actuator is only visible when an armature is selected,
because actions are stored in the armature.

See :doc:`Actuator Common Options </game_engine/logic/actuators/common_options>` for common options.

Special Options:
**Action Playback Type**

   :guilabel:`Play`
      Play ipo once from start to end when a TRUE pulse is received.
   :guilabel:`Ping Pong`
      Play ipo once from start to end when a TRUE pulse is received. When the end is reached play ipo once from end to start when a TRUE pulse is received.
   :guilabel:`Flipper`
      Play ipo once from start to end when a TRUE pulse is received. (Plays backwards when a FALSE pulse is received).
   :guilabel:`Loop End`
      Play ipo continuously from end to start when a TRUE pulse is received.
   :guilabel:`Loop Start`
      Play ipo continuously from start to end when a TRUE pulse is received.
   :guilabel:`Property`
      Uses a property to define what frame is displayed.

**Action**
   Select the action to use

**Continue**
   Restore last frame when switching on/off, otherwise play from the start each time.

**Start Frame**
   Set the start frame of the action.

**End Frame**
   Set the end frame of the action.

**Child Button**
   Update action on all children objects as well.

**Blendin**
   Number of frames of motion blending.

**Priority**
   Execution priority - lower numbers will override actions with higher numbers. With 2 or more actions at once, the overriding channels must be lower in the stack.

**Frame Property**
   Assign the action's current frame number to this property.

**Property**
   Use this property to define the Action position. Only for Property playback type.

**Layer**
   The animation layer to play the action on.

**Layer Weight**
   How much of the previous layer to blend into this one.


