
******
Remesh
******

.. admonition:: Reference
   :class: refbox

   :Mode:      All Paint Modes
   :Header:    :menuselection:`Tool Settings --> Remesh`
   :Panel:     :menuselection:`Sidebar --> Tool --> Remesh`
   :Shortcut:  :kbd:`Ctrl-R` (Voxel), :kbd:`Ctrl-Alt-R` (Quadriflow)

Remeshing is a technique that automatically rebuilds the geometry with a more uniform topology.
Remeshing can either add or remove the amount of topology depending on a defined resolution.
This technique is especially useful for :doc:`sculpting </sculpt_paint/sculpting/index>`,
to generate better topology after blocking out the initial shape.

The Voxel Remesher uses an OpenVDB to generate a new manifold mesh from the current geometry.
It produces a mesh with perfectly even distributed topology and
it does not have any performance penalty once the new mesh is calculated.
This makes the voxel remesher great for sculpting has it is possible to
sculpt at a much higher level of detail than using other features
like dyntopo which often adds more performance overhead.

Voxel Size
   The resolution or the amount of detail the remeshed mesh will have.
   The value is used to define the size, in object space, of the :term:`Voxel`.
   These voxels are assembled around the mesh and are used to determine the new geometry.
   For example a value of 0.5m will create topological patches that are about 0.5m
   (assuming *Preserve Volume* is enabled).
   Lower values preserve finer details but will result in a mesh with a much more dense topology.

   The voxel size also be adjusted from the 3D Viewport using :kbd:`Shift-R`.
   Using this shortcut shows a grid that has the real size of the resulting voxel size.
   Holding :kbd:`Shift` while adjusting the size allows better pressing
   while holding :kbd:`Ctrl` adjusts the size linearly.

   Sample Voxel Size
      Used to adjust the *Voxel Size* by picking an area of the mesh
      to match the denseness of polygons after the remesh operation.

Adaptivity
   Reduces the final face count by simplifying geometry where detail is not needed.
   This introduce triangulation to faces that do not need as much detail.
   Note, an *Adaptivity* value greater than zero disables *Fix Poles*.

Fix Poles
   Tries to produce less :term:`poles <Pole>` at the cost of some performance to produce a better topological flow.

Preserve
   Volume
      Tells the algorithm to try to preserve the original volume of the mesh.
      Enabling this could make the operator slower depending on the complexity of the mesh.
   Paint Mask
      Reprojects the :ref:`paint mask <sculpt-mask-menu>` onto the new mesh.
   Face Sets
      Reprojects :ref:`Face Sets <sculpting-editing-facesets>` onto the new mesh.

Voxel Remesh
   Performs the remeshing operation to create a new manifold mesh based on the volume of the current mesh.
   Performing this will lose all mesh object data layers associated with the original mesh.

.. seealso::

   :doc:`Remesh modifier </modeling/modifiers/generate/remesh>`


Known Limitations
=================

- Remeshing only works on the original mesh data and
  ignores generated geometry from modifiers, shape keys, rigging, etc.
- Remeshing will not work with the :doc:`/modeling/modifiers/generate/multiresolution`.
