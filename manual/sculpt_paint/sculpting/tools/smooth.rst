
******
Smooth
******

.. admonition:: Reference
   :class: refbox

   :Mode:      Sculpt Mode
   :Tool:      :menuselection:`Toolbar --> Smooth`
   :Shortcut:  :kbd:`Shift-S`

Eliminates irregularities in the area of the mesh within the brush's
influence by smoothing the positions of the vertices.
The inverse of this tool is to sharpen the details in a mesh
by applying a Laplacian smooth in the opposite direction.


Brush Settings
==============

Direction
   The operation to apply to the mesh.
   This setting can be toggled with :kbd:`Ctrl` while sculpting.

   Smooth
      Smooths the surface of the mesh by decreasing the difference between creases and valleys.
   Enhance Details
      Sharpens details on the surface of the mesh by intensifying the difference between creases and valleys.

.. _bpy.types.Brush.smooth_deform_type:

Deformation
   Deformation type that is used in the brush.

   Laplacian
      Smooths the surface and the volume.
   Surface
      Smooths the surface of the mesh, while preserving the volume.

      .. _bpy.types.Brush.surface_smooth_shape_preservation:

      Shape Preservation
         How much of the original shape is preserved when smoothing. Increasing the value
         reduces the effect of having multiple iterations on the strength of smoothing.

      .. _bpy.types.Brush.surface_smooth_current_vertex:

      Per-Vertex Displacement
         How much the position of each individual vertex influences the final result.
         Increasing the value reduces the overall strength of smoothing.

      .. _bpy.types.Brush.surface_smooth_iterations:

      Iterations
         Number of smoothing iterations per brush step.

      .. note::

         This method works by applying regular smoothing, computing the difference between
         the original (blended between start of iteration and fully original based on *Shape Preservation*)
         and the smoothed mesh, smoothing these offsets, pushing vertices back using the smoothed offsets,
         and finally blending in the original mesh based on *Per-Vertex Displacement*.
