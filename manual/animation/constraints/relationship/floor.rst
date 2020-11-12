.. index:: Object Constraints; Floor Constraint
.. _bpy.types.FloorConstraint:

****************
Floor Constraint
****************

The *Floor* constraint allows you to use its target position
(and optionally rotation) to specify a plane with a "forbidden side",
where the owner cannot go. This plane can have any orientation you like.
In other words, it creates a floor (or a ceiling, or a wall)!
Note that it is only capable of simulating entirely flat planes,
even if you use the *Vertex Group* option.
It cannot be used for uneven floors or walls.


Options
=======

.. figure:: /images/animation_constraints_relationship_floor_panel.png

   Floor panel.

Target
   :ref:`ui-data-id` used to select the constraints target, and is not functional (red state) when it has none.
   See :ref:`common constraint properties <rigging-constraints-interface-common-target>` for more information.

Offset
   Allows you to offset the "floor" plane from the target's origin,
   by the given number of units. Use it e.g.
   to account for the distance from a foot bone to the surface of the foot's mesh.

Max/Min
   Controls which plane will be the "floor".
   The names of the buttons correspond, indeed, to the *normal* to this plane
   (e.g. enabling Z means "XY plane", etc.).
   By default, these normals are aligned with the *global* axes.
   However, if you enable *Use Rotation* (see above), they will be aligned with the *local target's axes*.
   As the constraint does not only define an uncrossable plane,
   but also a side of it which is forbidden to the owner,
   you can choose which side by enabling either the positive or negative normal axis...
   e.g. by default Z, the owner is stuck in the positive Z coordinates.

Use Rotation
   Forces the constraint to take the target's rotation into account.
   This allows you to have a "floor" plane of any orientation you like, not just the global XY, XZ and YZ ones...

Target/Owner
   Standard conversion between spaces.
   See :ref:`common constraint properties <rigging-constraints-interface-common-space>` for more information.

Influence
   Controls the percentage of affect the constraint has on the object.
   See :ref:`common constraint properties <bpy.types.constraint.influence>` for more information.


Example
=======

.. vimeo:: 171554207
