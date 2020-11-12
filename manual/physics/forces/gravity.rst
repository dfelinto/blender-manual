.. _bpy.types.Scene.gravity:

*******
Gravity
*******

.. admonition:: Reference
   :class: refbox

   :Panel:     :menuselection:`Scene --> Gravity`

Gravity is a global setting that is applied to all physics systems in a scene.
It can be found in the scene tab.
This value is generally fine left at its default, -9.810 on the Z axis,
which is the force of gravity in the real world.
Changing this value would simulate a lower or higher force of gravity.
Gravity denoted g, measurement *m* × *s*\ :sup:`-2`.

Gravity is applied in the same way to all physics systems.

Gravity is practically the same around the entirety of planet *Earth*.
For rendering scenes from the *Moon*, use a value six times smaller, i.e. 1.622 *m* × *s*\ :sup:`-2`.
The planet *Mars* has a gravity value of 3.69.

.. note::

   The gravity value per physics system can be scaled down in the *Field Weights* tab.
