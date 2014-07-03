


Smooth Modifier
===============


 .. admonition:: Reference
   :class: refbox

   | Mode:     Any mode
   | Panel:    :guilabel:`Modifiers`


Description
-----------


.. figure:: /images/25-Manual-Modifiers-Mesh-Smooth-example01.jpg

   Smooth modifier applied to a subdivided cube


.. figure:: /images/25-Manual-Modifiers-Mesh-Smooth-example02.jpg

   As above, with a vertex group selected


This modifier smooths a mesh by flattening the angles between adjacent faces in it,
just like :guilabel:`Smooth` in the :guilabel:`Editing` context.
It smooths without subdividing the mesh - the number of vertices remains the same.

This modifier is not limited to smoothing, though.
Its control factor can be configured outside the [\ **0.0**\ , **1.0**\ ] range
(including negative values), which can result in interesting deformations,
depending on the affected mesh.


Options
-------

:guilabel:`X`\ , :guilabel:`Y`\ , :guilabel:`Z`
   Toggle buttons to enable/disable the modifier in the X, Y and/or Z axes directions.

:guilabel:`Factor`
   The factor to control the smoothing amount. The smoothing ranges from **0.0** to **1.0** (\ **0.0**\ : disabled, **0.5**\ : same as the :guilabel:`Smooth` button, **1.0**\ : maximum). Alternatively, values outside this range (above **1.0** or below **0.0**\ ) distort the mesh.

:guilabel:`Repeat`
   The number of smoothing iterations, equivalent to pressing the :doc:`Smooth <ling/meshes/editing/deforming#smooth>` button multiple times.

:guilabel:`Vertex Group`
   A vertex group name, to restrict the effect to the vertices in it only. This allows for selective, real-time smoothing, by painting vertex weights.


