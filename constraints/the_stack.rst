
..    TODO/Review: {{review|}} .

The Constraints Stack
=====================


.. figure:: /images/25-Manual-Constraints-Example-Stack.jpg
   :width: 200px
   :figwidth: 200px

   A constraint stack example


Constraints are evaluated from top to bottom of the constraint stack,
shown in the :guilabel:`Constraints` panel.


- In (\ *A constraint stack example*\ ), first the location of the lamp is copied to the owner object.
- The copy rotation constraint is ignored (red name, see below).
- So the next constraint evaluated is the :guilabel:`Child Of` one, which is currently reduced.
- Finally, the size of our cube is bounded by the :guilabel:`Limit Scale` last constraint.

    So here, the size of the cube is first controlled by the target of the :guilabel:`Child Of` constraint, within the limits allowed by the next :guilabel:`Limit Scale` constraint… As with modifiers, order is crucial!

You can move a constraint up and down the stack by using the small up/down arrow buttons that
are drawn in its header, to the right of the constraint name.
These buttons are only visible when needed, i.e.
the top constraint has only the "down" button, the bottom constraint,
only the "up" one - and when there is only one constraint in the stack,
both buttons are hidden.


Adding/Removing a Constraint
----------------------------

To add a constraint, you can, in the :guilabel:`Constraints` panel,
click on the… :guilabel:`Add Constraint` button! A menu shows up,
listing all available constraints for the current active object
(or bone in :guilabel:`Pose` mode
(in which case the constraint will show up in the bone constraints menu).
The new constraint is *always* added at the bottom of the stack.

You can also, in a 3D view, either:

- Select only the future owner, hit :kbd:`ctrl-shift-C`\ , and in the :guilabel:`Add Constraint to New Empty Object` menu that pops up, select the constraint you want to add. If the chosen constraint needs it, a new :guilabel:`Empty` object will be automatically added as target, positioned at the owner's center, and with null rotation.
- Select first the future target, and then the future owner, hit :kbd:`ctrl-shift-C`\ , and in the :guilabel:`Add Constraint to Active Object` (or :guilabel:`Add Constraint to Active Bone`\ ) menu that pops up, select the constraint you want to add. If the chosen constraint needs it, the other selected object/bone will be used as target.

Note that these pop-up menus do not display all the available constraints.

To remove a constraint,
click on the "X" button of the header of the constraint you want to delete,
in the :guilabel:`Constraints` panel.
You can also remove all constraints from the selected object(s),
using the :menuselection:`Object --> Constraints --> Clear Object Constraints`
(or :menuselection:`Pose --> Constraints --> Clear Pose Constraints…` or hit :kbd:`ctrl-alt-C`\ ).


