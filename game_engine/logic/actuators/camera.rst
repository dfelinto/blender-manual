
Camera Actuator
===============

Makes the camera follow or track an  object.

See :doc:`Actuator Common Options <game_engine/logic/actuators/common_options>` for common options.

Special Options:


.. figure:: /images/BGE_Actuator_Camera.jpg
   :width: 271px
   :figwidth: 271px

   Camera Actuator


**Camera Object**
      Name of the Game Object that the camera follows/tracks.

**Height**
      Height the camera tries to stay above the Game Object's object center

**Axis**
      Axis in which the Camera follows (X or Y)

**Min**
      Minimum distance for the camera to follow the Game Object

**Max**
      Maximum distance for the camera to follow the Game Object

**Damping**
      Strength of the constraint that drives the camera behind the target. Range: 0 to 10. The higher the parameter, the quicker the camera will adjust to be inside the constrained range (of min, max and height).


