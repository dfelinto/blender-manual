
..    TODO/Review: {{review|partial=X|im=examples}} .

Randomize Transform
*******************

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object` mode
   | Menu:     :menuselection:`Object --> Transform --> Randomize Transform`


.. figure:: /images/Doc26-transform-randomize.jpg

   Randomize transform options


The randomize transform tool allows you to apply random translate, rotate,
and scale values to an object or multiple objects. When applied on multiple objects,
each object gets its own seed value, and will get different transform results from the rest.


Options
=======

Random Seed
   The random seed is an offset to the random transformation. A different seed will produce a new result.

Transform Delta
   Randomize Delta Transform values instead of regular transform. See :doc:`Delta Transforms </3d_interaction/transform_control/transform_properties#delta_transform>`.

Randomize Location
   Randomize Location vales

Location
   The maximum distances the objects can move along each axis.

Randomize Rotation
   Randomize rotation values.

Rotation
   The maximum angle the objects can rotate on each axis

Randomize Scale
   Randomize scale values.

Scale Even
   Use the same scale for each axis.

Scale
   The maximum scale randomization over each axis.