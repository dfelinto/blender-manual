.. the title should be remeshing since retopology (feature based) is a subtype of remeshing.
   remeshing vs. retopology by dev Pablo Dobarro bcon19: https://www.youtube.com/watch?v=lxkyA4Xslzs&t=9m34s

**********
Retopology
**********

Retopology is the process of simplifying the topology of a mesh to make it cleaner and easier to work with.
Retopology is need for mangled topology resulting from sculpting or generated topology, for example from a 3D scan.
Meshes often need to be retopologized if the mesh is going to be deformed in some way.
Deformations can include rigging or physics simulations such as cloth or soft body.
Retopology can be done by hand by manipulating geometry in Edit Mode or through automated methods.


Using the Poly Build Tool
=========================

Todo 2.81.


.. _bpy.types.Mesh.remesh:
.. _bpy.ops.object.voxel_remesh:

Remeshing
=========

.. reference::

   :Mode:      Object Mode, Sculpt Mode
   :Panel:     :menuselection:`Properties --> Object Data --> Remesh`

Remeshing is a technique that automatically rebuilds the geometry with a more uniform topology.
Remeshing can either add or remove the amount of topology depending on a defined resolution.
This technique is especially useful for :doc:`sculpting </sculpt_paint/sculpting/index>`,
to generate better topology after blocking out the initial shape.

.. note:: Limitations:

   - Remeshing only works on the original mesh data and
     ignores generated geometry from modifiers, shape keys, rigging, etc.
   - Remeshing will not work with the :doc:`/modeling/modifiers/generate/multiresolution`.

.. seealso::

   :doc:`Remesh modifier </modeling/modifiers/generate/remesh>`


Voxel
-----

The Voxel Remesher uses OpenVDB to generate a new manifold mesh from the current geometry.
It produces a mesh with perfectly even distributed topology and
it does not have any performance penalty once the new mesh is calculated.
This makes the voxel remesher great for sculpting as it is possible to
sculpt at a much higher level of detail than using other features
like dyntopo which often adds more performance overhead.

Voxel Size
   The resolution or the amount of detail the remeshed mesh will have.
   The value is used to define the size, in object space, of the :term:`Voxel`.
   These voxels are assembled around the mesh and are used to determine the new geometry.
   For example a value of 0.5 m will create topological patches that are about 0.5 m
   (assuming *Preserve Volume* is enabled).
   Lower values preserve finer details but will result in a mesh with a much more dense topology.

Adaptivity
   Reduces the final face count by simplifying geometry where detail is not needed.
   This introduce triangulation to faces that do not need as much detail.
   Note, an *Adaptivity* value greater than zero disables *Fix Poles*.

Fix Poles
   Tries to produce less :term:`Poles <Pole>` at the cost of some performance to produce a better topological flow.

Preserve
   Volume
      Tells the algorithm to try to preserve the original volume of the mesh.
      Enabling this could make the operator slower depending on the complexity of the mesh.
   Paint Mask
      Reprojects the :ref:`paint mask <sculpt-mask-menu>` onto the new mesh.
   Face Sets
      Reprojects :ref:`Face Sets <sculpting-editing-facesets>` onto the new mesh.
   Color Attributes
      Reprojects the :ref:`Color Attributes <modeling-meshes-properties-object_data-color-attributes>` onto
      the new mesh.

Voxel Remesh
   Performs the remeshing operation to create a new manifold mesh based on the volume of the current mesh.
   Performing this will lose all mesh object data layers associated with the original mesh.


.. _bpy.ops.object.quadriflow_remesh:

Quad
----

The Quad remesh uses the Quadriflow algorithm to create a :term:`Quad`
based mesh with few poles and edge loops following the curvature of the surface.
This method is relatively slow but generates a higher quality output for final topology.

.. warning::

   Performing *Quadriflow Remesh* will lose all mesh object data layers associated with the original mesh.

Quadriflow Remesh
   Opens a pop-up used to set parameters for the remesh operation.

Use Paint Symmetry
   Generates a symmetrical mesh using the :ref:`Mesh Symmetry <modeling_meshes_tools-settings_mirror>` options.

Preserve Sharp
   Tells the algorithm to try to preserve sharp features of the mesh.
   Enabling this could make the operator slower depending on the complexity of the mesh.

Preserve Mesh Boundary
   Tells the algorithm to try to preserve the original volume of the mesh.
   Enabling this could make the operator slower depending on the complexity of the mesh.

.. Use Mesh Curvature
..    Take the mesh curvature into account when remeshing.

Preserve Paint Mask
   Reprojects the :ref:`Paint Mask <sculpt-mask-menu>` onto the new mesh.

Smooth Normals
   Applies the :ref:`Smooth Normals <bpy.ops.object.shade_smooth>` operator to the resulting mesh.

Mode
   How to specify the amount of detail for the new mesh.

   :Ratio: Specify target number of faces relative to the current mesh.
   :Edge Length: Input target edge length in the new mesh.
   :Faces: Input target number of faces in the new mesh.

Seed
   Random :term:`Seed` to use with the solver;
   different seeds will cause the remesher to generate different quad layouts on the mesh.
