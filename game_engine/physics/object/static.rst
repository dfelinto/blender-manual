
Static Physics Object Type
**************************

Static objects in the :doc:`Blender Game Engine <game_engine>` do not automatically react to physics, including gravity and collisions. Even if hit by the force of a speeding 18-wheeler truck, it will remain unresponsive in terms of location, rotation, or deformation.

It will, however, give collision reactions. Objects will bounce off of Static Objects,
and rotational inertia will transfer to objects capable of rotating (that is,
Rigid Body Objects will spin in response, though Dynamic Objects will not).

Note that none of this prevents you from transforming the Static Objects with
:doc:`Logic Bricks <game_engine/logic>` or Python code.
The visual objects will correctly move and their physics representation will update in the engine as well.

Another important note is that the default
FIXME(TODO: Internal Link;
[[#Collision_Bounds|Collision Bounds]]
) is a Triangle Mesh, meaning it is higher in computational requirements but also in detail. This in turn means the "Radius" option has no effect by default.

In the example game demo, :doc:`Frijoles <ls/frijoles>`,
the Static type is represented by the "Arena" object that holds all the moving bits.

For more documentation, see the :doc:`Top BGE Physics page <game_engine/physics>`.


Options
=======

FIXME(Template Unsupported: Doc:2.6/Manual/Game_Engine/Physics/PythonAccessToOptions;
{{Doc:2.6/Manual/Game_Engine/Physics/PythonAccessToOptions}}
)


FIXME(Template Unsupported: Doc:2.6/Manual/Game_Engine/Physics/CommonOptions;
{{Doc:2.6/Manual/Game_Engine/Physics/CommonOptions}}
)


FIXME(Template Unsupported: Doc:2.6/Manual/Game_Engine/Physics/RadiusOption;
{{Doc:2.6/Manual/Game_Engine/Physics/RadiusOption}}
)


FIXME(Template Unsupported: Doc:2.6/Manual/Game_Engine/Physics/AnisotropicFrictionOptions;
{{Doc:2.6/Manual/Game_Engine/Physics/AnisotropicFrictionOptions}}
)


Collision Bounds
================

Note: The Static type differs from the others in that it defaults to a Triangle Mesh bounds,
instead of a simple sphere.


FIXME(Template Unsupported: Doc:2.6/Manual/Game_Engine/Physics/Collision_Bounds;
{{Doc:2.6/Manual/Game_Engine/Physics/Collision_Bounds}}
)


Create Obstacle
===============

FIXME(Template Unsupported: Doc:2.6/Manual/Game_Engine/Physics/Create_Obstacle;
{{Doc:2.6/Manual/Game_Engine/Physics/Create_Obstacle}}
)


All Types
=========

FIXME(Template Unsupported: Doc:2.6/Manual/Game_Engine/Physics/AllTypes;
{{Doc:2.6/Manual/Game_Engine/Physics/AllTypes}}
)


