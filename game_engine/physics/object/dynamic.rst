


Dynamic Physics Object Type
===========================


Dynamic objects in the :doc:`Game Engine <game_engine>` give/receive collisions, but when they do so they themselves do not rotate in response. So, a Dynamic ball will hit a ramp and slide down, while a Rigid Body ball would begin rotating.

If you do not need the rotational response the Dynamic type can save the extra computation.

Note that these objects can still be rotated with :doc:`Logic Bricks <game_engine/logic>` or Python code. Their physics meshes will update when you do these rotations - so collisions will be based on the new orientations.

In the example game demo, :doc:`Frijoles <ls/frijoles>`\ , the Dynamic type is represented by the titular jumping beans. Though we want these characters to recoil back when they hit a Boulder or each other, having them torque in response to these collisions would result in their being impossible to control.

For more documentation, see the :doc:`Top BGE Physics page <game_engine/physics>`\ .


Options
-------


FIXME(Template Unsupported: Doc:2.6/Manual/Game_Engine/Physics/PythonAccessToOptions;
{{Doc:2.6/Manual/Game_Engine/Physics/PythonAccessToOptions}}
)


FIXME(Template Unsupported: Doc:2.6/Manual/Game_Engine/Physics/CommonOptions;
{{Doc:2.6/Manual/Game_Engine/Physics/CommonOptions}}
)


FIXME(Template Unsupported: Doc:2.6/Manual/Game_Engine/Physics/RightColumnOfOptions;
{{Doc:2.6/Manual/Game_Engine/Physics/RightColumnOfOptions}}
)


FIXME(Template Unsupported: Doc:2.6/Manual/Game_Engine/Physics/MassOption;
{{Doc:2.6/Manual/Game_Engine/Physics/MassOption}}
)

FIXME(Template Unsupported: Doc:2.6/Manual/Game_Engine/Physics/RadiusOption;
{{Doc:2.6/Manual/Game_Engine/Physics/RadiusOption}}
)

FIXME(Template Unsupported: Doc:2.6/Manual/Game_Engine/Physics/FormFactorOption;
{{Doc:2.6/Manual/Game_Engine/Physics/FormFactorOption}}
)


FIXME(Template Unsupported: Doc:2.6/Manual/Game_Engine/Physics/AnisotropicFrictionOptions;
{{Doc:2.6/Manual/Game_Engine/Physics/AnisotropicFrictionOptions}}
)


FIXME(Template Unsupported: Doc:2.6/Manual/Game_Engine/Physics/TransformOptions;
{{Doc:2.6/Manual/Game_Engine/Physics/TransformOptions}}
)


Collision Bounds
----------------


FIXME(Template Unsupported: Doc:2.6/Manual/Game_Engine/Physics/Collision_Bounds;
{{Doc:2.6/Manual/Game_Engine/Physics/Collision_Bounds}}
)


Create Obstacle
---------------


FIXME(Template Unsupported: Doc:2.6/Manual/Game_Engine/Physics/Create_Obstacle;
{{Doc:2.6/Manual/Game_Engine/Physics/Create_Obstacle}}
)


All Types
---------


FIXME(Template Unsupported: Doc:2.6/Manual/Game_Engine/Physics/AllTypes;
{{Doc:2.6/Manual/Game_Engine/Physics/AllTypes}}
)


