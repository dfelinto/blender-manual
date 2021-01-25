
***********
Mesh Filter
***********

.. admonition:: Reference
   :class: refbox

   :Mode:      Sculpt Mode
   :Tool:      :menuselection:`Toolbar --> Mesh Filter`

Applies a deformation to all vertices in the mesh at the same time.
To use this tool, click and drag away from the object to have a positive effect
and click and drag towards the mesh to have a negative effect.


Tool Settings
=============

Filter Type
   Smooth
      Eliminates irregularities of the mesh by making the positions of the vertices more uniform.
      This filter works similar to the *Smooth Brush*.
   Scale
      Increases the size of the mesh.
      This filter works similar to the :ref:`Scale Transform <bpy.ops.transform.resize>`.
   Inflate
      Displaces vertices uniformly along their normal.
      This filter works similar to the *Inflate Brush*.
   Sphere
      Morphs the mesh progressively into a sphere.
      This filter works similar to the :ref:`To Sphere Transform <bpy.ops.transform.tosphere>`.
   Random
      Randomly moves vertices along the vertex normal.
      This filter works similar to the :ref:`Randomize Transform <bpy.ops.object.randomize_transform>`.
   Relax
      Tries to create an even distribution of quads without deforming the volume of the mesh.
      This filter works the same as the *Relax* mode of the *Slide Relax* brush.
   Relax Face Sets
      Smooths the edges of the face sets by modifying the underlying
      topology so edges flow along the perimeter of the face sets.
      This will remove the jagged lines visible after drawing or creating a face set.
   Surface Smooth
      Eliminates irregularities of the mesh by making the positions
      of the vertices more uniform while preserving the volume of the object.

      Shape Preservation
         How much of the original shape is preserved when smoothing.
      Per-Vertex Displacement
         How much the position of each individual vertex influences the final result.
   Sharpen
      Sharpens and smooths the mesh based on its curvature,
      resulting in pinching hard edges and polishing flat surfaces.
      It fixes most of the artifacts of the voxel remesher and those produced when
      sculpting hard surfaces and stylized models with creasing and flattening brushes.

      Smooth Ratio
         How much smoothing is applied to polished surfaces.
      Intensify Details
         Increases the high frequency surface details of the mesh
         by intensifying the difference between creases and valleys.
      Curvature Smooth Iterations
         The number of times the smoothing operation is applied per brush step.
         Controls how much smooth the resulting shape is, ignoring high-frequency details.
   Enhance Details
      Increases the high frequency surface details of the mesh
      by intensifying the difference between creases and valleys.
   Erase Displacement
      Deletes displacement information of
      the :doc:`Multires Modifier </modeling/modifiers/generate/multiresolution>`,
      resetting the mesh to the subdivision limit surface.
      This can be used to delete parts of the sculpt or to fix reprojection artifacts
      after applying a :doc:`Shrinkwrap Modifier </modeling/modifiers/deform/shrinkwrap>`.

      Negative strokes will intensify the displacement details,
      this method works similar to *Enhance Details* and can give better results in some circumstances.

Strength
   The amount of effect the filter has on the mesh.

Deformation Axis
   Apply the deformation only on the selected axis.

Orientation
   :doc:`Orientation </editors/3dview/controls/orientation>` of the axis to limit the filter displacement.

   Local
      Use the local axis to limit the displacement.
   World
      Use the global axis to limit the displacement.
   View
      Use the view axis to limit the displacement.
