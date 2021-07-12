
****************************
Adding/Removing a Constraint
****************************

What is described on this page about Object Constraints can be also be applied on Bone Constraints.


Tab
===

.. reference::

   :Mode:      Object Mode
   :Menu:      :menuselection:`Properties --> Constraint tab`

To add a constraint click on the *Add Object Constraint* menu in the Constraints tab.

.. figure:: /images/animation_constraints_interface_adding-removing_add-menu.png

To remove a constraint click on the "X" button
in the :doc:`header </animation/constraints/interface/header>`.


Menu
====

.. _bpy.ops.object.constraint_add_with_targets:

Add Constraint (with Targets)
-----------------------------

.. reference::

   :Mode:      Object Mode and Pose Mode
   :Menu:      :menuselection:`Object --> Constraint --> Add Constraint (with Targets)`

Adds a constraint to the active object.
The type of constraint must be chosen from a pop-up menu,
though it can be changed later from the *Add Constraint (with Targets)*
:ref:`bpy.ops.screen.redo_last` panel.
If there is an other object selected besides the active one,
that object will be the constraint target (if the chosen constraint accepts targets).

When using a bone from another armature as the target for a constraint, the tool
will look inside the non-active armature and use its active bone,
provided that armature is in Pose Mode.


.. _bpy.ops.object.constraints_copy:

Copy Constraints to Selected Objects
------------------------------------

.. reference::

   :Mode:      Object Mode and Pose Mode
   :Menu:      :menuselection:`Object --> Constraint --> Copy Constraints to Selected Objects`

Copies the active object Constraints to the rest of the selected objects.


.. _bpy.ops.object.constraints_clear:

Clear Object Constraints
------------------------

.. reference::

   :Mode:      Object Mode and Pose Mode
   :Panel:     :menuselection:`Object --> Constraint --> Clear Object Constraints`

Removes all Constraints of the selected object(s).


.. _bpy.ops.object.track_set:
.. _bpy.ops.object.track_clear:

Track
=====

.. reference::

   :Mode:      Object Mode
   :Panel:     :menuselection:`Object --> Track`

These tools add a tracking constraint to the selected objects;
the target object of the constraint will be the active object, which won't have a constraint added.

- :doc:`Damped Track Constraint </animation/constraints/tracking/damped_track>`
- :doc:`Track To Constraint </animation/constraints/tracking/track_to>`
- :doc:`Lock Track Constraint </animation/constraints/tracking/locked_track>`

Clear Track
   Removes all Damped Track, Track To and Lock Track Constraints from the selected objects.
Clear and Keep Transformation (Clear Track)
   Removes all Track Constraint from the selected objects, while keeping the final transform caused by them.
