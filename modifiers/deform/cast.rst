
..    TODO/Review: {{review|}} .


Cast Modifier
=============


.. admonition:: Reference
   :class: refbox

   | Mode:     Any mode
   | Panel:    :guilabel:`Modifiers`


This modifier shifts the shape of a mesh, curve,
surface or lattice to any of a few pre-defined shapes (sphere, cylinder, cuboid).

It is equivalent to the :guilabel:`To Sphere` tool in the :guilabel:`Editing` context
(\ :guilabel:`Mesh` ? :guilabel:`Transform` ? :guilabel:`To Sphere` :kbd:`Alt-Shift-S`\ )
and what other programs call "Spherify" or "Spherize", but, as written above,
it is not limited to casting to a sphere.


.. admonition:: Hint
   :class: note

   The :doc:`Smooth modifier <modifiers/deform/smooth>` is a good companion to :guilabel:`Cast`\ , since the cast shape sometimes needs smoothing to look nicer or even to fix shading artifacts.


.. admonition:: Important
   :class: note

   For performance, this modifier works only with local coordinates. If the modified object looks wrong, you may need to apply the object's rotation (\ :kbd:`ctrl-A`\ ), especially when casting to a cylinder.


Options
-------


.. figure:: /images/25-Manual-Modifiers-cast.jpg

   cast modifier


:guilabel:`Cast Type`
   Menu to choose cast type (target shape): :guilabel:`Sphere`\ , :guilabel:`Cylinder` or :guilabel:`Cuboid`\ .

:guilabel:`X`\ , :guilabel:`Y`\ , :guilabel:`Z`
   Toggle buttons to enable/disable the modifier in the X, Y, Z axes directions (X and Y only for :guilabel:`Cylinder` cast type).

:guilabel:`Factor`
   The factor to control blending between original and cast vertex positions. It's a linear interpolation: **0.0** gives original coordinates (i.e. modifier has no effect), **1.0** casts to the target shape. Values below or above ``[0.0, 1.0]`` deform the mesh, sometimes in interesting ways.

:guilabel:`Radius`
   If non-zero, this radius defines a sphere of influence. Vertices outside it are not affected by the modifier.

:guilabel:`Size`
   Alternative size for the projected shape. If zero, it is defined by the initial shape and the control object, if any.

:guilabel:`From radius`
   If activated, calculate :guilabel:`Size` from :guilabel:`Radius`\ , for smoother results.

:guilabel:`Vertex Group`
   A vertex group name, to restrict the effect to the vertices in it only. This allows for selective, real-time casting, by painting vertex weights.

:guilabel:`Control Object`
   The name of an object to control the effect. The location of this object's center defines the center of the projection. Also, its size and rotation transform the projected vertices. Hint: animating (keyframing) this control object also animates the modified object.


Example
-------


.. figure:: /images/263-Manual-Modifiers-Cast-Example.jpg
   :width: 400px
   :figwidth: 400px

   Top: Suzanne without modifiers. Middle: Suzanne with each type of Cast Modifier (Sphere, Cylinder and Cuboid). Bottom: Same as above, but now only X axis is enabled. `Sample blend file <http://wiki.blender.org/index.php/Media:263-Cast-Modifier.blend>`__


