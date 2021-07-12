
********
Boundary
********

.. reference::

   :Mode:      Sculpt Mode
   :Tool:      :menuselection:`Toolbar --> Boundary`

This tool is used to transform and deform the boundaries i.e. the unconnected edges of a mesh.
The tool detects the mesh boundary closest to the active vertex and
propagates the deformation using the brush :doc:`Falloff </sculpt_paint/brush/falloff>` into the mesh.

.. note::

   Even if this brush can produce deformations in triangle meshes and meshes with a non-regular quad grid,
   the more regular and clean the topology is, the better the result.


Brush Settings
==============

Deformation Target
   How the deformation of the brush will affect the object.

   Geometry
      Brush deformation displaces the vertices of the mesh.
   Cloth Simulation
      Brush deforms the mesh by deforming the constraints of
      a :doc:`cloth simulation </sculpt_paint/sculpting/tools/cloth>`.

.. _bpy.types.Brush.boundary_deform_type:

Deformation
   Deformation type that is used by the brush.

   Bend
      Rotates the active boundary around the local Y axis.
   Expand
      Moves/extends the mesh boundary in the local X direction.
   Inflate
      Works similar to the :doc:`Inflate </sculpt_paint/sculpting/tools/inflate>` tool but,
      the vertices that are inflated are constrained to the mesh boundary.
   Grab
      Works similar to the :doc:`Grab </sculpt_paint/sculpting/tools/grab>` tool but,
      the vertices that are grabbed are constrained to the mesh boundary.
   Twist
      Rotates the active boundary around the local Z axis.
   Smooth
      Works similar to the :doc:`Grab </sculpt_paint/sculpting/tools/smooth>` tool but,
      the vertices that are smoothed are constrained to the the mesh boundary.

.. _bpy.types.Brush.boundary_falloff_type:

Boundary Falloff
   How the brush :doc:`Falloff </sculpt_paint/brush/falloff>` is applied across the boundary.

.. _bpy.types.Brush.boundary_offset:

Boundary Origin Offset
   Offset of the boundary origin in relation to the brush radius.

   Constant
      Applies the same deformation in the entire boundary.
   Brush Radius
      Applies the deformation in a localized area limited by the brush radius.
   Loop
      Applies the brush falloff in a loop pattern.
   Loop and Invert
      Applies the falloff radius in a loop pattern,
      inverting the displacement direction in each pattern repetition.


Usage
=====

The main use cases of this brush are the *Bend* and *Expand* deformation modes,
which depend on a grid topology to create the best results.
In order to do further adjustments and tweaks to the result of these deformations,
use the Inflate, Grab, Twist, and Smooth deformation modes, which do not depend that much on the topology.
