
Lattice Modifier
****************

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object` mode
   | Panel:    Properties Window → Context Button :guilabel:`Modifiers`

   .. figure:: /images/CZ_Modifier_ContextButton.jpg

The :guilabel:`Lattice` modifier deforms the base object according to the shape of a
:guilabel:`Lattice` object.


Options
=======

.. figure:: /images/Reference-Panels-Modifier-Lattice.2.5.jpg

   Lattice modifier.


:guilabel:`Object`
   The :guilabel:`Lattice` object with which to deform the base object.

:guilabel:`Vertex Group`
   An optional vertex group name which lets you limit the modifier effect to a part of the base mesh.


Method
======

You can control the :guilabel:`Lattice` object attributes in the :guilabel:`Object Data` context for the :guilabel:`Lattice` in the :guilabel:`Properties Window`

.. figure:: /images/Lattice-Modifier-Context-Button.jpg

A lattice consists of a non-renderable three-dimensional grid of vertices.
Its main use is to give extra deformation capabilities to the underlying object it controls
(either *via* a modifier, or as its parent). Objects to be deformed can be meshes, curves,
surfaces, text, lattices and even particles.

The lattice should be scaled and moved to fit around your object in object mode.
Any scaling applied to the object in edit mode will result in the object deforming. This
includes applying scale with :kbd:`ctrl-A` as this will achieve the same result as
scaling the lattice in edit mode, and therefore the object.


Hints
=====

Why would you use a lattice to deform a mesh instead of deforming the mesh itself in
:guilabel:`Edit mode` ? There are a couple of reasons for that:

- First of all: it's easier. Since your mesh could have a zillion vertices, scaling, grabbing and moving them could be a hard task. Instead, if you use a nice simple lattice your job is simplified to moving just a couple of vertices.
- It's nicer. The deformation you get looks a lot better!
- It's fast! You can use the same lattice to deform several meshes. Just give each object a lattice modifier, all pointing to the same lattice.
- It's a good practice. A lattice can be used to get different versions of a mesh with minimal extra work and consumption of resources. This leads to an optimal scene design, minimizing the amount of modeling work. A lattice does not affect the texture coordinates of a mesh's surface. Subtle changes to mesh objects are easily facilitated in this way, and do not change the mesh itself.


Example/Tutorial(s)
===================

There are example tutorials for 2.4 versions in the :doc:`Tutorials </ls>` section. A 2.6 tutorial shows how to :doc:`shape a fork </ls/modifiers/lattice/shaping_a_fork>`.


Particles and Lattices
======================

.. figure:: /images/Blender3D-ParticlesAndLattices-2.56.jpg

   Particles following a lattice.


Particles follow a Lattice if the modifier sequence is right. First the particles,
then the lattice!


