
Introduction
************

After completing your character, you need to manipulate it for animation or just for posing.
Rigging is the process of attaching a skeleton to your character mesh object so you can deform
and pose it in different ways.

These actions do not fundamentally alter the mesh, and can easily be changed, undone,
or combined with other poses.


.. admonition:: note for editors
   :class: note

   below we need to add more introductory text for all steps in rigging!


The following is a typical workflow for rigging:

- Add an armature, which starts out with a single bone.
- Add more bones as needed and link them together to form "limbs".

(you can either extrude an existing bone, which parents it to the extruded bone automatically; or add new bones first and then link them together.)

- Edit the bones to give proper proportions to the skeleton
- Apply constraints to the joints

(e.g. a human elbow can bend through about 170 degrees in one plane only)

- Give a 'rest' (default) position to the skeleton.
- Apply a mesh (body) to the armature (skinning)
- Define how the movement of the armature affects the skin

(folding, flexing, bulging)

- Give poses to the armature.

(There are multiple methods: By arranging each bone of the armature manually, or by copying a template armature, or by arranging the bones to follow a curve, or by making the armature follow externally collected motion-capture data.)

- Check how the armature movement affects the skin, and adjust the parameters.

 (adjust the topology of the skin to make it look more natural)

All these steps are explained in details below.

-done! Please check+edit
--\ `Raindrops <http://wiki.blender.org/index.php/User:Raindrops>`__ 19:32, 31 May 2013 (CEST)


[[Doc:2.6/Manual/Rigging/Armatures|Armatures]]
==============================================

Armatures are like the real-life skeletons;
and provide the structure for a mesh for the purpose of posing or animation.

:doc:`Armature and Bone Panels </rigging/armatures/panels>`
   shows how to use the different panels in Blender to adjust the armatures and bones.
:doc:`Bones </rigging/armatures/bones>`
   explains properties of Bones, which are the basic elements of armatures.
:doc:`Visualization </rigging/armatures/visualization>`
   how to display bones in four different ways.
:doc:`Structure </rigging/armatures/structure>`
   Explains the structure of bones in an armature.
:doc:`Selecting </rigging/armatures/selecting>`
   Select only the section of your armature that matters to you.

[[Doc:2.6/Manual/Rigging/Armatures/Editing|Editing]]
----------------------------------------------------

:doc:`Bones </rigging/armatures/editing/bones>`
   Learn how to practically edit bones in Blender and see what that causes.
:doc:`Sketching </rigging/armatures/editing/sketching>`
   Use the Skeleton Sketching tool to easily sketch bones and bring them to reality in Blender.
:doc:`Templating </rigging/armatures/editing/templating>`
   Templates offer a great way to quickly reuse already created rigs for your own models.


[[Doc:2.6/Manual/Rigging/Skinning|Skinning]]
============================================

This section shows how to "flesh out" your character from a given armature.

In normal English, "to skin" means 'to peel off skin', but here it is just the reverse
(used in the sense of covering the armature with a skin): You will be putting a body (mesh)
around an armature.

:doc:`Linking Objects to Bones </rigging/skinning/objects>`
   How to parent a bone to an object, so that the bone controls that object. This type of linking is used to simulate mechanical linkage (for example, `Newton's cradle <http://en.wikipedia.org/wiki/Newton_Pendulum|>`__) or where the parts of the mesh are not deformed when the armature moves, as in case of modeling an insect body, crab, etc.

:doc:`Skinning to Objects' Shapes </rigging/skinning/obdata>`
   How to attach the armature so that each of its bones controls a specific part of the "skin" object's geometry. This type of linkage is used when the object surface flexes when the armature moves, such as bulging of biceps when the arm is folded.

:doc:`Retargeting </rigging/skinning/retargeting>`
   How to apply motion-capture data (acquired from real world) to a rig, so that it mimics the original movements realistically. This method also avoids laborious programming of each movement.


[[Doc:2.6/Manual/Rigging/Posing|Posing]]
========================================

Posing means shaping and arranging the objects in your scene in a particular way to create an
interesting composition. For example,
look at the body language of `The Thinker <http://en.wikipedia.org/wiki/The_Thinker>`__,
or think of a scorpion raising its tail to strike.

Poses are also used to create animation. For example,
to create animation of a tennis player serving a ball,
you would have to create poses at different moments of the stroke: (a)
when she holds the ball and racket at waist height (b) when she tosses the ball up, (c)
when she strikes the ball, and (d)
when her racket reaches at the lowest point after the strike (follow through).
Then Blender creates all the intermediate poses to create the animation.

:doc:`Visualization </rigging/posing/visualization>`
   describes the visual aids that help you in posing the armature; especially for animation.
:doc:`Editing Poses </rigging/posing/editing>`
   how to create a pose, and how to edit it to create the snapshots of an animation at different moments.
:doc:`Pose Library </rigging/posing/pose_library>`
   storing frequently used poses or existing poses from another armature, so that they can be quickly accessed and applied.
:doc:`Using Constraints </rigging/posing/constraints>`
   how to apply constraints to bones so that they cannot form an unnatural pose.
:doc:`Inverse Kinematics </rigging/posing/inverse_kinematics>`
   a feature where you move the last bone in a chain, and Blender automatically  moves the whole chain accordingly. This is like lifting someone's finger: His whole hand automatically follows that movement.
:doc:`Spline IK </rigging/posing/inverse_kinematics/spline_ik>`
   a feature where you can align a chain of bones along a curve.


