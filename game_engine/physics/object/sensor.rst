

..    TODO/Review: {{review|partial=X|text=sections}} .

Sensor
======


The object detects static and dynamic objects but not other collisions sensors objects.
The Sensor is similar to the physics objects that underlie the Near and Radar sensors.
Like the Near and Radar object it is:

- static and ghost
- invisible by default
- always active to ensure correct collision detection
- capable of detecting both static and dynamic objects
- ignoring collision with their parent
- capable of broadphase filtering based on:
  - Actor option: the collisioning object must have the Actor flag set to be detected
  - property/material: as specified in the collision sensors attached to it.

Broadphase filtering is important for performance reason:
the collision points will be computed only for the objects that pass the broadphase filter.

- automatically removed from the simulation when no collision sensor is active on it

Unlike the Near and Radar object it can:

- take any shape, including triangle mesh
- be made visible for debugging (just use the Visible actuator)
- have multiple collision sensors using it

Other than that, the sensor objects are ordinary objects.
You can move them freely or parent them. When parented to a dynamic object,
they can provide advanced collision control to this object.

The type of collision capability depends on the shape:

- box, sphere, cylinder, cone, convex hull provide volume detection.
- triangle mesh provides surface detection but you can give some volume to the surface by increasing the margin in the Advanced Settings panel. The margin applies on both sides of the surface.

Performance tip:

- Sensor objects perform better than Near and Radar: they do less synchronizations because of the Scenegraph optimizations and they can have multiple collision sensors on them (with different property filtering for example).
- Always prefer simple shape (box, sphere) to complex shape whenever possible.
- Always use broadphase filtering (avoid collision sensor with empty propery/material)
- Use collision sensor only when you need them. When no collision sensor is active on the sensor object, it is removed from the simulation and consume no CPU.

Known limitations:

- When running Blender in debug mode, you will see one warning line of the console:

 "warning btCollisionDispatcher::needsCollision: static-static collision!"
In release mode this message is not printed.

- Collision margin has no effect on sphere, cone and cylinder shape.


Settings
--------

:guilabel:`Invisible`
   See :doc:`Here <game_engine/physics/object_type/static>`


Collision Bounds
----------------

See :doc:`Here <game_engine/physics/object_type>`\ .

