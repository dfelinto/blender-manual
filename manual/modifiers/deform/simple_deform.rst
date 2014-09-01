
Simple Deform Modifier
**********************

.. admonition:: Reference
   :class: refbox

   | Mode:     All modes
   | Panel:    :guilabel:`Modifiers`


Description
===========

.. figure:: /images/25-Manual-Modifiers-Simpledeform.jpg

   Simple Deform


The :guilabel:`Simple Deform` modifier allows easy application of a simple deformation to an
object (meshes, lattices, curves, surfaces and texts are supported).

Like most of the deform modifiers,
the deform functions are applied to the "computed vertices", i.e.
to the real geometry of the object at the time the modifier is calculated,
and not to the original *vertices* /control points. This means you can increase the level of
detail of the deform effect by first inserting a :guilabel:`Subdivision Surface` modifier
(for meshes), or raising the :guilabel:`Preview Resolution` settings
(for curves/surfaces/texts).

Using another object, it's possible to define the axis and origin of the deformation,
allowing application of very different effects.


Options
=======

:guilabel:`Mode`
   This drop-down list defines the deform function applied, among four available:

   - :guilabel:`Twist` - Rotates around the Z axis.
   - :guilabel:`Bend` - Bends the mesh over the Z axis.
   - :guilabel:`Taper` - Linearly scales along Z axis.
   - :guilabel:`Stretch` - Stretches the object along the Z axis (negative :guilabel:`Factor` leads to squash).

:guilabel:`Vertex Group`
   The name of the vertex group that indicates whether and how much each vertex is influenced by the deformation.

:guilabel:`Origin`
   The name of an object that defines the origin of deformation (usually an empty). This object can be:

   - Rotated to control the axis (as it is its Z axis that is now used as "guide").
   - Translated to control the origin of deformation.
   - Scaled to change the deform factor.

.. admonition:: Note
   :class: note

   When the object controlling the origin (the one in the :guilabel:`Origin` field) is a child of the deformed object, this creates a cyclic dependency in Blender's data system (the DAG - "dependency graph"?). The workaround is to create a new empty and attach both objects to it.


:guilabel:`Factor`
   The amount of deformation.  Can be set to negative.

:guilabel:`Limits`
   These settings allow you to set the lower and upper limits of the deformation (they are proportional values, from ``0.0`` to ``1.0``). Obviously, the upper limit can't be lower than lower limit.

:guilabel:`Lock X Axis` / :guilabel:`Lock Y Axis` (:guilabel:`Taper` and :guilabel:`Stretch` modes only)
   These controls whether the X and/or Y coordinates are allowed to change or not. Thus it is possible to squash the X coordinates of an object and keep the Y coordinates intact.


