.. |kg/m3| replace:: kg/m\ :sup:`3`

*******************
Physical Properties
*******************

.. reference::

   :Panel:     :menuselection:`Physics --> Cloth --> Physical Properties`

Mass
   The mass of the cloth material.
Air Viscosity
   Air has some thickness which slows falling things down.
Bending Model
   Linear
      Cloth model with linear bending springs (old).
   Angular
      Cloth model with angular bending springs.


Stiffness
=========

Tension
   How much the material resists stretching.
Compression
   How much the material resists compression.
Structural
   Overall stiffness of the cloth (only in linear bending model).
Shear
   How much the material resists shearing.
Bending
   Wrinkle coefficient. Higher creates more large folds.


Damping
=======

Tension
   Amount of damping in stretching behavior.
Compression
   Amount of damping in compression behavior.
Structural
   Amount of damping in stretching behavior (only in linear bending model).
Shear
   Amount of damping in shearing behavior.
Bending
   Amount of damping in bending behavior.


.. _bpy.types.ClothSettings.internal_spring:
.. _bpy.types.ClothSettings.internal_tension:
.. _bpy.types.ClothSettings.internal_compression:
.. _bpy.types.ClothSettings.vertex_group_intern:

Internal Springs
================

As stated in the introduction, cloth physics are simulated through :ref:`physics-cloth-introduction-springs`
connecting vertices on the surface of a mesh. But these springs only interact on the surface
and only apply to 2D surfaces. 3D or *Internal Springs* can be used to make a mesh behave similarly to
a :doc:`Soft Body </physics/soft_body/index>`. Internal springs can be enabled by toggling the checkbox in
the *Internal Springs* panel header.

Max Spring Creation Length
   The maximum length an internal spring can have during creation.
   If the distance between internal points is greater than this,
   no internal spring will be created between these points.
   A length of zero means that there is no length limit.
Max Creation Diversion
   The maximum angle that is allowed to use to connect the internal points can diverge from the vertex normal.
Check Surface Normals
   Requires the points the internal springs connect to have opposite normal directions.
Tension
   How much the material resists stretching.
Compression
   How much the material resists compression.
Vertex Group
   The *Tension* and *Compression* of internal springs can be controlled via
   a :doc:`Vertex Group </modeling/meshes/properties/vertex_groups/index>` to
   specify which the portions of the mesh have internal springs or the spring strength.
Max Tension
   Maximum tension stiffness value.
Max Compression
   Maximum Compression stiffness value.


.. _bpy.types.ClothSettings.use_pressure:
.. _bpy.types.ClothSettings.use_pressure_volume:
.. _bpy.types.ClothSettings.target_volume:
.. _bpy.types.ClothSettings.pressure_factor:
.. _bpy.types.ClothSettings.vertex_group_pressure:

Pressure
========

Cloth pressure allows the simulation of soft-shelled objects
such as balloons or balls that are filled with a type of fluid.
This fluid is modeled as a gas; to emulate an incompressible liquid set
*Pressure Scale* as high as possible without breaking the simulation.
Cloth pressure can be enabled by toggling the checkbox in the *Pressure* panel header.

.. note::

   :term:`Non-manifold` meshes will work with cloth pressure however,
   pressure will escape out of the mesh holes and cause drifting or propulsion forces.
   One way to get around this is by using the *Vertex Group* to exclude the non-manifold portions of the mesh.

Pressure
   The uniform pressure that is constantly applied to the mesh.
   This value is specified in units of *Pressure Scale*, and can be
   negative to simulate implosions or any other case where an object
   has outside pressure pushing inwards.

Custom Volume
   Use the *Target Volume* parameter as the initial volume for the cloth,
   instead of computing it from the mesh itself.

   Target Volume
      The mesh volume where the inner/outer pressure will be the same.
      If set to zero, changes in the volume of the object will not affect pressure.

Pressure Scale
   Ambient pressure (in kPa) that exists both inside and outside the object,
   balancing out when the volume matches the target. Increase the value to
   make the object resist changes in volume more strongly.

Fluid Density
   Specifies the density of the fluid contained inside the object
   (in kg/liter = 1000 |kg/m3|, use 1 for water), used to generate
   a hydrostatic pressure gradient that simulates the weight of the fluid.
   If the value is negative, it instead models buoyancy from a surrounding fluid.

   The fluid is not actually simulated, so while the setting helps to achieve
   a more plausible object shapes at rest, it cannot create realistic fluid dynamics effects.
   It can also be used to give more weight to a soft body like object with heavy and
   sufficiently flexible filling, even if it is not a fluid by itself.

   The volume of the object is not preserved. If that is desired it should be used
   together with *Pressure Scale*. *Fluid density* times *object size* times 50
   is a good start value for *Scale* to make sure that no more than 10% volume change
   if the object does not experience higher acceleration than standard gravity.

Vertex Group
   Cloth pressure can be controlled via a :doc:`Vertex Group </modeling/meshes/properties/vertex_groups/index>`
   to specify which the portions of the mesh to apply pressure.
   Zero weight means no pressure while a weight of one means full pressure.

   Note, faces with a vertex that has zero weight will be excluded from the *Target Volume* calculation.
