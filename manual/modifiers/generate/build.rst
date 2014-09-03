
..    TODO/Review: {{review|}} .


Build Modifier
**************

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object` mode
   | Panel:    :guilabel:`Modifiers`


The :guilabel:`Build` modifier causes the faces of the mesh object to appear,
one after the other, over time.
If the material of the mesh is a halo rather than a standard one,
then the vertices of the mesh, not the faces, appear one after another.

By default, faces (or vertices) appear in the order in which they are stored in memory
(by default, the order of creation). The face/vertex order can be altered in :guilabel:`Edit
mode` by selecting :guilabel:`Sort Faces` from the :guilabel:`Search Menu`
:kbd:`Space`.


Options
=======

.. figure:: /images/build_modifier_animated.gif
   :width: 285px
   :figwidth: 285px

   Build modifier in action


Start
   The start frame of the building process.

Length
   The number of frames over which to rebuild the object.

Randomize
   Randomizes the order in which the faces are built.

Seed
   The random seed. Changing this value gives a different "random" order when :guilabel:`"Randomize"` is checked - this order being always the same for a given seed/object set.


