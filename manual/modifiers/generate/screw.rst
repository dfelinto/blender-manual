
Screw Modifier
**************

.. admonition:: Reference
   :class: refbox

   | Mode:     Any mode
   | Panel:    :guilabel:`Modifiers`


Description
===========

The :guilabel:`Screw` modifier is similar to the :guilabel:`Screw` tool in the :guilabel:`Tool
Shelf` in that it takes a profile object, a :guilabel:`Mesh` or a :guilabel:`Curve`,
to create a helix-like shape.


.. figure:: /images/25-Manual-Modifiers-Screw-align.jpg
   :width: 600px
   :figwidth: 600px

   Properly aligning the profile object is important


The profile should be two dimensional and properly aligned to the cardinal direction of the
object rather than to the screw axis.


Options
=======

.. figure:: /images/25-Manual-Modifiers-Screw.jpg

   Screw modifier


Axis
   The axis along which the helix will be built.

   Screw
      The height of one helix iteration.
AxisOb
   The name of an object to define the axis direction.

   Object Screw
      Use the :guilabel:`Axis Object` to define the value of :guilabel:`Screw`.
Angle
   Degrees for a single helix revolution.
Steps
   Number of steps used for a single revolution (displayed in the 3D view.)
Render Steps
   As above, used during render time.  Increase to improve quality.
Calc Order
   Order of edges is calculated to avoid problems with normals.  Only needed for meshes, not curves.
Flip
   Flip normals direction.
Iterations
   Number of revolutions.


