
Constraints Actuator
********************

Adds a constraint to the location, orientation

See :doc:`Actuator Common Options </game_engine/logic/actuators/common_options>` for common options.

Special Options:
**Constraint Mode**
Menu specifying type of constraint required.

- Force Field Constraint
- Orientation Constraint
- Distance Constraint
- Location Constraint


.. figure:: /images/BGE_Actuator_Constraint_ForceField.jpg
   :width: 271px
   :figwidth: 271px

   Constraint actuator - Force Field


**Force Field Constraint**
   Create a force field buffer zone along one axis of the object.

   :guilabel:`Damping`
        Damping factor of the Fh spring force (Range 0.0 - 1.0)
   :guilabel:`Distance`
        Height of Fh area
   :guilabel:`Rot Fh`
        Make game object axis parallel to the normal of trigger object.
   :guilabel:`Direction`
      Axis in which to create force field (can be + or -, or None)
   :guilabel:`Force`

   :guilabel:`N`
        When on, use a horizontal spring force on slopes
   :guilabel:`M/P`
        Trigger on another Object will be either Material (M) or Property (P)
   :guilabel:`Property`
        Property/Material that triggers the Force Field constraint (blank for ALL Properties/Materials)
   :guilabel:`Per`
      Persistence button
      When on, force field constraint always looks at Property/Material; when off, turns itself off if it can't find the Property/Material.
   :guilabel:`Time`
        Number of frames for which constraint remains active
   :guilabel:`RotDamp`
        Damping factor for rotation


.. figure:: /images/BGE_Actuator_Constraint_Orientation.jpg
   :width: 271px
   :figwidth: 271px

   Constraint Actuator - Orientation


**Orientation Constraint**
Constrain the specified axis in the Game to a specified direction in the World axis.

   :guilabel:`Direction`
      Game axis to be modified (X, Y, Z or none)
   :guilabel:`Damping`
      Delay (frames) of the constraint response (0 - 100)
   :guilabel:`Time`
      Time (frames) for the constraint to remain active (0 - 100)
   :guilabel:`ReferenceDir`
      Reference direction (global coordinates) for the specified game axis.
   :guilabel:`MinAngle`
      Minimum angle for the axis modification;
   :guilabel:`MaxAngle`
      Maximum angle for the axis modification;


.. figure:: /images/BGE_Actuator_Constraint_Distance.jpg
   :width: 271px
   :figwidth: 271px

   Constraint actuator - Distance


**Distance Constraint**
Maintain the distance the Game Object has to be from a surface

   :guilabel:`Direction`
      Axis Direction (X, Y, Z, -X, -Y, -Z, or None)
   :guilabel:`L`
      If on, use local axis (otherwise use World axis)
   :guilabel:`N`
      If on, orient the Game Object axis with the mesh normal.
   :guilabel:`Range`
      Maximum length of ray used to check for Material/Property on another game object (0 - 2000 Blender Units)
   :guilabel:`Force Distance`
      •Distance to be maintained between object and the Material/Property that triggers the  Distance Constraint(-2000 to +2000 Blender Units).
   :guilabel:`Damping`
      Delay (frames) of the constraint response (0 - 100)
   :guilabel:`M/P`
      Trigger on another Object will be either Material (M) or Property (P)
   :guilabel:`Property`
      Property/Material that triggers the Force Field constraint (blank for ALL Properties/Materials)
   :guilabel:`Per`
      Persistence button: When on, force field constraint always looks at Property/Material; when off, turns itself off if it can't find the Property/Material.
   :guilabel:`Time`
      Number of frames for which constraint remains active
   :guilabel:`RotDamp`
      Damping factor for rotation


.. figure:: /images/BGE_Actuator_Constraint_Location.jpg
   :width: 271px
   :figwidth: 271px

   Constraint actuator - Location


**Location Constraint**
Limit the position of the Game Object within one World Axis direction.
To limit movement within an area or volume, use two or three constraints.

   :guilabel:`Limit`
      Axis in which to apply limits (LocX, LocY, LocZ or none)
   :guilabel:`Min`
      Minimum limit in specified axis (Blender Units)
   :guilabel:`Max`
      Maximum limit in specified axis (Blender Units)
   :guilabel:`Damping`
      Delay (frames) of the constraint response (0 - 100)


