
Mesh Deform Modifier
********************

.. admonition:: Reference
   :class: refbox

   | Mode:     All modes
   | Panel:    :guilabel:`Modifiers`


Description
===========

The :guilabel:`Mesh Deform` modifier allows an arbitrary closed mesh (of any closed shape,
not just the cuboid shape of a :guilabel:`Lattice` modifier)
to act as a deformation cage around another mesh.


Options
=======

.. figure:: /images/25-Manual-Modifiers-MeshDeform.jpg

   Mesh Deform modifier


The :guilabel:`Mesh Deform` modifier is reasonably easy to use but it can be very slow to do
the calculations it needs, to properly map the deform mesh cage to the deformed object.

:guilabel:`Object`
   The name of the mesh object to be used as a deforming mesh cage.

:guilabel:`Vertex Group`
   An optional vertex group that will be affected by the deforming mesh cage.

:guilabel:`Invert`
   Inverts the influence set by the vertex group defined in previous setting (i.e. reverts the weight values of this group).

:guilabel:`Bind`
   The :guilabel:`Bind` button is what tells the :guilabel:`Mesh Deform` modifier to actually link the deform mesh cage to the deformed object, so that altering the shape of the deform mesh cage actually alters the shape of the deformed object.
   Be aware that depending on the settings of the :guilabel:`Mesh Deform` modifier and complexity of the deform mesh cage and/or deformed object, it can take a long time for this operation to complete.  This can result in Blender not responding to user's actions until it has completed, it is even possible that Blender will run out of memory and crash.

:guilabel:`Unbind`
   When a deformed object has been associated to a deform mesh cage, it can later be disassociated by selecting the :guilabel:`Unbind` button which replaced the :guilabel:`Bind` one.
   When :guilabel:`Unbind` is clicked, the *deform mesh cage* will keep its current shape; it will not reset itself back to its original start shape. If you need its original shape, you will have to save a copy of it before you alter it. The deformed object will, however, reset back to its original shape that it had before it was bound to the deform mesh cage.

:guilabel:`Precision`
   The :guilabel:`Precision` numeric slider field controls the accuracy with which the deform mesh cage alters the
   deformed object, when the points on the cage are moved.
   The range of values for the :guilabel:`Precision` field can range from **2** to **10**,
   the default being **5**. Raising this value higher can greatly increase the time it takes the :guilabel:`Mesh
   Deform` modifier to complete its binding calculations,
   but it will get more accurate cage mapping to the deformed object.
   This rise in calculation time can make Blender stop responding until it has calculated what it needs to.
   As well as making Blender not respond, raising the :guilabel:`Precision` value high and then trying to
   :guilabel:`Bind` on a very complex deform mesh cage and/or deformed object can use large amounts of memory and in
   extreme cases crash Blender.  To be safe, save your blend file before proceeding!
   This setting becomes unavailable once a cage has been bound.


:guilabel:`Dynamic`
   The :guilabel:`Dynamic` button indicates to the :guilabel:`Mesh Deform` modifier that it should also take into account deformations and changes to the underlying deformed object which were not a direct result of deform mesh cage alteration.
   With the :guilabel:`Dynamic` button activated, other mesh altering features (such as other modifiers and shape keys) are taken into account when binding a deform mesh cage to the deformed object, increasing deformation quality. It is deactivated by default to save memory and processing time when binding...
   Like with :guilabel:`Precision`, this setting is unavailable once a cage has been bound.


Hints
=====

- Ensure that the normals on the cage mesh point to the outside; they are used to determine the inside and outside of the cage.
- Besides the outer cage, more faces within the cage, either loose or forming another smaller cage, can be used for extra control. Such smaller cages may also overlap with the main cage; for example, to get extra control over eyes, two small sphere cages could be added around them.


See Also
========

- The :doc:`Lattice modifier <modifiers/deform/lattice>`.
- [http://graphics.pixar.com/library/HarmonicCoordinatesB/ (original paper)


