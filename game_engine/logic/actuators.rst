
Actuators
=========

Actuators perform actions, such as move, create objects, play a sound.
The actuators initiate their functions when they get a positive pulse from one (or more)
of their controllers.

The logic blocks for all types of actuator may be constructed and changed using the :doc:`Logic Editor <game_engine/logic/editor>`\ ; details of this process are given in the :doc:`Actuator Editing <game_engine/logic/actuators/editing>` page.


The following types of actuator are currently available:
{{Table| width="100%" cellspacing="0" cellpadding="4" border="2" style="border: 1px solid rgb(170, 170, 170); margin: 1em 1em 1em 0pt; border-collapse: collapse;"
|-
|\ :doc:`Action <game_engine/logic/actuators/action>`
|Handles armature actions. This is only visible if an armature is selected.
|-
|\ :doc:`Camera <game_engine/logic/actuators/camera>`
|Has options to follow objects smoothly, primarily for camera objects, but any object can use this.
|-
|\ :doc:`Constraint <game_engine/logic/actuators/constraint>`
|Constraints are used to limit object's locations, distance, or rotation. These are useful for controlling the physics of the object in game.
|-
|\ :doc:`Edit Object <game_engine/logic/actuators/edit_object>`
|Edits the object's mesh, adds objects, or destroys them. It can also change the mesh of an object (and soon also recreate the collision mesh).
|-
|\ :doc:`Filter 2D <game_engine/logic/actuators/2d_filters>`
|Filters for special effects like sepia colours or blur.
|-
|\ :doc:`Game <game_engine/logic/actuators/game>`
|Handles the entire game and can do things as restart, quit, load, and save.
|-
|\ :doc:`Message <game_engine/logic/actuators/message>`
|Sends messages, which can be received by other objects to activate them.
|-
|\ :doc:`Motion <game_engine/logic/actuators/motion>`
|Sets object into motion and/or rotation. There are different options, from "teleporting" to physically push rotate objects.
|-
|\ :doc:`Parent <game_engine/logic/actuators/parent>`
|Can set a parent to the object, or unparent it.
|-
|\ :doc:`Property <game_engine/logic/actuators/property>`
|Manipulates the object's properties, like assigning, adding, or copying.
|-
|\ :doc:`Random <game_engine/logic/actuators/random>`
|Creates random values which can be stored in properties.
|-
|\ :doc:`Scene <game_engine/logic/actuators/scene>`
|Manage the scenes in your .blend file. These can be used as levels or for UI and background.
|-
|\ :doc:`Sound <game_engine/logic/actuators/sound>`
|Used to play sounds in the game.
|-
|\ :doc:`State <game_engine/logic/actuators/state>`
|Changes states of the object.
|-
|\ :doc:`Steering <game_engine/logic/actuators/steering>`
|Provides pathfinding options for the object.
|-
|\ :doc:`Visibility <game_engine/logic/actuators/visibility>`
|Changes visibility of the object.
|-


