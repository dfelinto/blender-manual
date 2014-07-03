


Animation
=========


Introduction
------------


Animation is making an object move or change shape over time.
Objects can be animated in many ways:

**Moving as a whole object**
   Changing their position, orientation or size in time;
**Deforming them**
   animating their vertices or control points;
**Character Animation via Armature**
   animated to deform by the movement of bones inside the mesh, a very complex and flexible interaction that makes character-shaped objects appear to walk and jump.

In this chapter we will cover the first two,
but the basics given here are actually vital for understanding the following chapters as well.

Three methods are normally used in animation software to make a 3D object move:
**Key frames**
    Complete positions are saved for units of time (frames). An animation is created by interpolating an object fluidly through the frames. The advantage of this method is that it allows you to work with clearly visualized units. The animator can work from one position to the next and can change previously created positions, or move them in time.
**Animation Curves**
    Curves are interpolated from keyframes, and can be drawn for each XYZ component for location, rotation, and size, as well as any other attribute in Blender. These form the graphs for the movement, with time set out horizontally and the value set out vertically. The advantage of this method is that it gives you precise control over the results of the movement.
**Path**
    A curve is drawn in 3D space, and the Object is constrained to follow it according to a given time function of the position along the path.

The first two systems in Blender are completely integrated in a single one, the :doc:`F-Curve system <animation/fcurves>`\ .

In Blender 2.5x, everything can now be animated. Previously,
only certain datablock had the ability to be keyframed. Now users have the ability to animate
nearly any type of data that can be changed to multiple values.


Chapters
--------

General Principles and Tools
   :doc:`Keyframes <animation/keyframes>`
   :doc:`Animation Editors <animation/editors>`
   :doc:`Using The Timeline <animation/timeline>`
   :doc:`Markers <animation/markers>`

The Graph Editor

FIXME(TODO: Internal Link;
[[User:Tnboma/Doc:2.5/Manual/Animation/Graph Editor|Using the Graph Editor]]
)
   :doc:`F-Curves <animation/fcurves>`
   :doc:`Editing Curves <animation/editors/graph/fcurves>`
   :doc:`F-Curve Modifiers <animation/editors/fmodifiers>`

The Action Editor
   :doc:`Actions <animation/actions>`
   :doc:`Creating Actions <animation/creating_actions>`

Animation Techniques
   :doc:`Constraints <animation/techs/object/constraint>`
   :doc:`Moving objects on a Path <animation/techs/object/path>`
   :doc:`Changing Object Layers <animation/layer_animation>`
   :doc:`Game Engine Physics Recording <physics/using_ge>`

Animating Deformation
   :doc:`Methods of deformation <animation/basic/deformation>`
   :doc:`Shape Keys <animation/techs/shape/shape_keys>`
   :doc:`Deforming by a Lattice <animation/basic/deformation/lattice>`
   :doc:`Deforming with Hooks <modifiers/deform/hooks>`
      See also :doc:`Hooks <modifiers/deform/hooks>` - Uses a modifier as a way to change the shape of a mesh. Sorta like sticking a fish hook in a mesh and pulling. Uses the principles discussed in Shape Keys.

Drivers
   :doc:`Drivers <animation/editors/graph/drivers>`
   :doc:`Driven Shape Keys <animation/driven_shape_keys>`

The [http://wiki.blender.org/index.php/Doc:Tutorials/Animation/BSoD/Character_Animation BSoD
Introduction to Character Animation tutorial]
is a good starting point for learning character animation.
Even if you never used Blender before.


Animation Basics
~~~~~~~~~~~~~~~~


:doc:`Actions <animation/basics/actions>`
   Actions are used to record the animation of objects and properties.
:doc:`Drivers <animation/basics/drivers>`
   Drivers are used to control and animate properties.
:doc:`Keying Sets <animation/basics/keying_sets>`
   Keying Sets are used to record a set of properties at the same time.
:doc:`Markers <animation/basics/markers>`
   Markers are used to mark key points/events within an animation.
:doc:`Motion Paths <animation/basics/motion_paths>`
   Motion Paths are used to visualize an animation.
:doc:`Shape Keys <animation/basics/shape_keys>`
   Shape Keys are used to deform objects into new shapes.


Animation Editors
~~~~~~~~~~~~~~~~~


:doc:`Timeline <animation/editors/timeline>`
   The Timeline Editor is a quick editor to set and control the time frame.
   This also has some tools for animation.
:doc:`Graph Editor <animation/editors/graph>`
   The Graph Editor is mostly used to edit the F-Curves and Keyframes for Channels and Drivers.
:doc:`Dope Sheet <animation/editors/dopesheet>`
   The Dopes Sheet contains a collection of animation editors.
:doc:`NLA Editor <animation/editors/nla>`
   The NLA Editor is used to edit and blend Actions together.


Categories
~~~~~~~~~~


:doc:`Modifiers <modifiers_and_deformation>`
   Modifiers are automatic operations that affect an object in a non-destructive way.
   With modifiers, you can perform many effects automatically that would otherwise be tedious to do manually.
:doc:`Rigging <rigging>`
   Rigging.
:doc:`Constraints <constraints>`
   Constraints are a way of connecting transform properties (position, rotation and scale) between objects.
:doc:`Physical Simulation <physical_simulation>`
   This category covers various advanced Blender effects, often used to simulate real physical phenomena.
   There is the Particle System for things like hair, grass, smoke, flocks.
   Soft Bodies are useful for everything that tends to bend, deform, in reaction to forces like gravity or wind.
   Cloth simulation, to simulate clothes or materials.
   Rigid Bodies can simulate dynamic objects that are fairly rigid.
   Fluids, which include liquids and gasses, can be simulated, including Smoke.
   Force Fields can modify the behavior of simulations.
:doc:`Motion Tracking <motion_tracking>`
   Motion tracking is a new technique available in Blender. It is still under development, and currently supports basic operations for 2D motion tracking, 3D motion tracking, and camera solution.
`Animation Scripts <http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts#Animation_Scripts>`__
   Addon scripts for animation.
`Rigging Scipts <http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts#Rigging_Scripts>`__
   Addon scripts for rigging.


See Also
--------


- :doc:`Manual#Animation <animation>`

