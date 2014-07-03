
State Actuator
==============

The State actuator allows the user to create complex logic,
whilst retaining a clear user interface. It does this by having different states,
and performing operations upon them

See :doc:`Actuator Common Options <game_engine/logic/actuators/common_options>` for common options.

Special Options:


.. figure:: /images/2.5_Game_Engine_Actuator_State.jpg
   :width: 271px
   :figwidth: 271px

   State actuator


.. figure:: /images/2.5_Game_Engine_Actuator_State_Options.jpg
   :width: 271px
   :figwidth: 271px

   State actuator options


**Operation**
Menu to select the state operation required.
   :guilabel:`Change State`
    Change from the current state to the state specified.
   :guilabel:`Remove State`
    Removes the specified states from the active states (deactivates them).
   :guilabel:`Add State`
    Adds the specified states to the active states (activates them).
   :guilabel:`Set State`
    Moves from the current state to the state specified, deactivating other added states.


Usage Notes
-----------

With the state actuator, you can create tiers of logic,
without the need for hundreds of properties. Use it well, and you benefit greatly,
but often problems may be circumvented by python.


