
Game Actuator
=============

The Game actuator allows the user to perform Game-specific functions, such as Restart Game,
Quit Game and Load Game.

See :doc:`Actuator Common Options <game_engine/logic/actuators/common_options>` for common options.

Special Options:


.. figure:: /images/2.5_Game_Engine_Actuator_Game.jpg
   :width: 271px
   :figwidth: 271px

   Game actuator


.. figure:: /images/2.5_Game_Engine_Actuator_Game_Options.jpg
   :width: 271px
   :figwidth: 271px

   Game


**Game**

:guilabel:`Load bge.logic.globalDict`
   Load :guilabel:`bge.logic.globalDict` from .bgeconf.
:guilabel:`Save bge.logic.globalDict`
   Save :guilabel:`bge.logic.globalDict` to .bgeconf.
:guilabel:`Quit Game`
   Once the actuator is activated, the blenderplayer exits the runtime.
:guilabel:`Restart Game`
   Once the actuator is activated, the blenderplayer restarts the game (reloads from file).
:guilabel:`Start Game From File`
   Once the actuator is activated, the blenderplayer starts the .blend file from the path specified.

   :guilabel:`File`
      Path to the .blend file to load.


**Notes**
If you use the keyboard sensor as a hook for the :kbd:`ESC` key,
in the event that the quit game actuator fails, such as an error in a python file,
the game will be unable to close. Data may be recovered from quit.blend
:menuselection:`File --> Recover Last Session`


