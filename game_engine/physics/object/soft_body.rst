
Soft Body Physics Object Type
=============================

The most advanced type of object in the :doc:`Game Engine <game_engine>`\ . Also, it is the most finicky. If you are used to the fun experimentation that comes from playing around with the non-BGE Soft Body sims (such as Cloth), you will probably find a frustrating lack of options and exciting results. Do not despair, we are here to help you get some reasonable settings.

Your setup will involve making sure you have sufficient geometry in the Soft Body's mesh to
support the deformation, as well as tweaking the options.

In the example game demo, :doc:`Frijoles <ls/frijoles>`\ , the Soft Body type is represented by the decorative checkered flag at the top of the level.

For more documentation, see the :doc:`Top BGE Physics page <game_engine/physics>`\ .


Options
-------

FIXME(Template Unsupported: Doc:2.6/Manual/Game_Engine/Physics/CommonOptions;
{{Doc:2.6/Manual/Game_Engine/Physics/CommonOptions}}
)

FIXME(Template Unsupported: Doc:2.6/Manual/Game_Engine/Physics/MassOption;
{{Doc:2.6/Manual/Game_Engine/Physics/MassOption}}
)


- :guilabel:`Shape Match` - Upon starting the Game Engine this will record the starting shape of the mesh as the "lowest energy" state. This means that the edges will have tension whenever they are flexed to some other form. This is set to on by default, and in this configuration turns the object into more of a thin sheet of metal rather than a cloth.
  - Demo: `BGE-Physics-Objects-SoftBodies_ShapeMatchAndLinearStiffness.blend <http://wiki.blender.org/index.php/Media:BGE-Physics-Objects-SoftBodies_ShapeMatchAndLinearStiffness.blend>`__
  - Default: On.
  - Code effect: When on, it will call `btSoftBody::setPose(false,true) <http://www.continuousphysics.com/Bullet/BulletFull/btSoftBody_8cpp_source.html#l00626>`__
  - Python property: ``obj.game.soft_body.use_shape_match``
  - Suboption: :guilabel:`Threshold` - `Linearly scales the pose match <http://www.continuousphysics.com/Bullet/BulletFull/btSoftBody_8cpp_source.html#l01566>`__
    - A threshold of 1.0 makes it behave like :guilabel:`Shape Match` on with a :guilabel:`Linear Stiffness` of 1.0.
    - A threshold of 0.0 makes it behave like :guilabel:`Shape Match` off with a :guilabel:`Linear Stiffness` of 0.0.
    - Range: 0-1.
    - Default: 0.5.
    - Code effect: Sets `btSoftBody::Config::kMT <http://www.continuousphysics.com/Bullet/BulletFull/structbtSoftBody_1_1Config.html#a8e9d39cceaf15fd8697b2f8831b2fee1>`__\ .
    - Python property: ``obj.game.soft_body.shape_threshold``
- :guilabel:`Welding` - <span style="color: #E7007A">[Note: Seems to not be hooked up. Blender will tell Bullet to weld any time you enable Soft Body. Look at `BL_BlenderDataConversion.cpp <https://svn.blender.org/svnroot/bf-blender/trunk/blender/source/gameengine/Converter/BL_BlenderDataConversion.cpp>`__ where ``objprop.m_soft_welding``\ is hard-coded to 0.0f]
- :guilabel:`Position Iteration` - Increase the accuracy at a linearly-increasing expense of time. The effect is visible especially with Soft Bodies that fall on sharp corners, though this can slow down even very simple scenes.
  - Demo: A situation where only the max setting of 10 works correctly: `BGE-Physics-Objects-SoftBodies_PositionIterations.blend <http://wiki.blender.org/index.php/Media:BGE-Physics-Objects-SoftBodies_PositionIterations.blend>`__\ .
  - Range: 0-10.
  - Default: 2.
  - Code effect: Represents the number of times `this loop <http://www.continuousphysics.com/Bullet/BulletFull/btSoftBody_8cpp_source.html#l01627>`__ is run.
  - Python property: ``obj.game.soft_body.location_iterations``
- :guilabel:`Linear Stiffness` - Linear stiffness of the soft body links. This is most evident when you have :guilabel:`Shape Match` off, but it is also evident with it on.
  - Demo: `BGE-Physics-Objects-SoftBodies_ShapeMatchAndLinearStiffness.blend <http://wiki.blender.org/index.php/Media:BGE-Physics-Objects-SoftBodies_ShapeMatchAndLinearStiffness.blend>`__
  - Range: 0-1.
  - Default: 0.5.
  - Python property: ``obj.game.soft_body.linear_stiffness``
- :guilabel:`Friction` - Dynamic friction coefficient.

FIXME(Tag Unsupported:span;
<span style="color: #E7007A">TODO: Learn/demo/explain.</span>
)

  - Code effect: Sets `btSoftBody::Config::kMT <http://www.continuousphysics.com/Bullet/BulletFull/btSoftBodyInternals_8h.html>`__\ , which, for Soft Bodies, defines the minimum friction versus the Material Friction (which in turn defaults to 0.5).
  - Range: 0-1.
  - Default: 0.2.
  - Python property: ``obj.game.soft_body.dynamic_friction``
- :guilabel:`Margin` - Small value makes the algorithm unstable.

FIXME(Tag Unsupported:span;
<span style="color: #E7007A">TODO: Learn/demo/explain.</span>
)

  - Range: 0.01-1.
  - Default: 0.01.
  - Python property: ``obj.game.soft_body.collision_margin``
- :guilabel:`Bending Constraint` - Enable Bending Constraints

FIXME(Tag Unsupported:span;
<span style="color: #E7007A">TODO: Learn/demo/explain.</span>
)

  - Default: On.
  - Python property: ``obj.game.soft_body.use_bending_constraints``
- :guilabel:`Cluster Collision` - Affects Collision sensors as well as physics.
  - Demo: `BGE-Physics-Objects-SoftBodies_ClusterRigidToSoftBody.blend <http://wiki.blender.org/index.php/Media:BGE-Physics-Objects-SoftBodies_ClusterRigidToSoftBody.blend>`__ for a demonstration of the effect on the :doc:`Collision Sensor <game_engine/logic/sensors/collision>`\ . There you will observe the "Rigid to Soft Body" off, then on with Iterations of 1, 64, and 128. The Off and Iterations: 1 cases do not register collisions, and the other two do (though they send their poor Cubes flying into space).
  - Demo of badness: `Manual-BGE-Physics-SoftBody_BadClusterCollisions.blend <http://wiki.blender.org/index.php/Media:Manual-BGE-Physics-SoftBody_BadClusterCollisions.blend>`__ - four different ways of making misconfigured Soft Body objects.
  - Suboption: :guilabel:`Rigid to Soft Body` - Enable cluster collisions between Rigid and Soft Bodies.
    - Default: Off.
    - Python property: ``obj.game.soft_body.use_cluster_rigid_to_softbody``
  - Suboption: :guilabel:`Soft to Soft Body` - Enable cluster collisions among Soft Bodies.
    - Default: Off.
    - Python property: ``obj.game.soft_body.use_cluster_soft_to_softbody``
  - Suboption: :guilabel:`Iterations` - Number of cluster iterations.
    - Range: 1-128.
    - Default: 64.
    - Python property: ``obj.game.soft_body.cluster_iterations``


Hints
-----

- A very important configurable in the case of Soft Body interactions is :doc:`World properties <game_engine/physics/world>` :menuselection:`--> Physics --> Physics Steps --> Substeps`\ . In the test .blend here: `Manual-BGE-Physics-SoftBody_PhysicsSteps.blend <http://wiki.blender.org/index.php/Media:Manual-BGE-Physics-SoftBody_PhysicsSteps.blend>`__\ , you can see the behavior at various Substep levels:
  - The default level. The Grid object goes straight through the cube, hardly slowing down at all.
  - The Grid slows upon hitting the Cube's top face, and stops fully on the bottom face.
  - The Grid stops at the top face, but two opposite Cube corners are visible.
  - ...no perceptible difference.
  - Finally a working sim. This is good, because it is the maximum step level.
- Surprisingly, the more vertices you have in your hit object, the less likely the Soft Body is to react with it. If you try letting it hit a Plane, it might stop, but a subdivided Grid might fail.


Sensors
-------

Soft bodies do not work with the Collision, Touch, Near, and Radar logic brick sensors.


Goal Weights
------------

TODO:
http://www.blender.org/documentation/blender_python_api_2_62_release/bpy.ops.curve.html#bpy.ops.curve.spline_weight_set


Force Fields
------------

A common practice within the non-BGE Cloth simulator is to employ :doc:`Force Fields <physics/force_fields>` to animate the cloth.

These do not work in the BGE, so you will have to figure out a way to use Python
(or perhaps plain Logic Bricks) to apply forces to the Soft Body objects.


All Types
---------

FIXME(Template Unsupported: Doc:2.6/Manual/Game_Engine/Physics/AllTypes;
{{Doc:2.6/Manual/Game_Engine/Physics/AllTypes}}
)


