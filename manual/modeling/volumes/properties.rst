
**********
Properties
**********

.. _bpy.types.VolumeGrids:

Grids
=====

OpenVDB can contain multiple grids which represent different "layers" of volume.
The :ref:`ui-list-view` shows all the grids in the OpenVDB-file along with its name and data type.


OpenVDB File
============

.. _bpy.types.Volume.filepath:

File Path
   Volume sample file used by the volume data-block.

.. _bpy.types.Volume.is_sequence:

Sequence
   Loads the OpenVDB-file as an animation loading separate files for individual frames.

   .. _bpy.types.Volume.frame_duration:

   Frames
      Number of frames of the sequence to use.

   .. _bpy.types.Volume.frame_start:

   Start
      Global starting frame of the sequence, assuming the first frame has a 1 in the file name.

   .. _bpy.types.Volume.frame_offset:

   Offset
      Offset the number of the frame to use in the animation.

   .. _bpy.types.Volume.sequence_mode:

   Mode
      Animation setting of the volume sequence before the start frame and after the end frame.

      :Clip:
         Hides frames outside the specified frame range.
      :Extend:
         Repeats the start frame before, and the end frame after the frame range.
      :Repeat:
         Cycles the frames in the sequence; restarting at frame one.
      :Ping-Pong:
         Repeats the frames, reversing the playback direction on every other cycle.


.. _bpy.types.VolumeDisplay:

Viewport Display
================

.. _bpy.types.VolumeDisplay.wireframe_type:

Wireframe
   Method used to represent volumes in :ref:`wireframe <3dview-shading-rendered>` shading mode.
   For heavy volume data sets, it can be useful to set the object to always display as wireframe.
   This way the 3D Viewport remains responsive but the volume still appears in the final render.

   :None:
      The volume is not displayed in wireframe mode.
   :Bounds:
      Displays the volume as :term:`Bounding Box` for the entire volume grid.
   :Boxes:
      Displays a bounding boxes for nodes in the volume tree.
   :Points:
      Displays points for nodes in the volume tree.

.. _bpy.types.VolumeDisplay.wireframe_detail:

Detail
   The amount of detail to display for *Boxes* or *Points* wireframe mode.

   :Coarse:
      Display one box or point for each intermediate tree node.
   :Fine:
      Display a box or point for each leaf node containing 8×8 voxels.

.. _bpy.types.VolumeDisplay.density:

Density
   Thickness of the volume in the 3D Viewport.
   The density of the volume in the render is adjusted via
   :doc:`Volume Shading </render/shader_nodes/shader/volume_principled>`.

.. _bpy.types.VolumeDisplay.interpolation_method:

Interpolation
   Interpolation method to use for the visualization of the fluid grid.

   :Linear:
      Linear interpolation between voxels. Gives good smoothness and speed.
   :Cubic:
      Cubic interpolation between voxels. Gives smoothed high quality interpolation, but is slower.
   :Closest:
      No interpolation between voxels. Gives raw voxels.


.. _bpy.types.VolumeDisplay.use_slice:

Slice
-----

Renders only a single 2D section of the domain object.

.. _bpy.types.VolumeDisplay.slice_axis:

Axis
   :Auto:
      Adjust slice direction according to the view direction.
   :X/Y/Z:
      Slice along the X, Y, or Z axis.

.. _bpy.types.VolumeDisplay.slice_depth:

Position
   Position of the slice relative to the length of the respective domain side.


.. _bpy.types.VolumeRender:

Render
======

.. _bpy.types.VolumeRender.space:

Space
   Specifies how volume density and step size are computed relative either to the object or world.

   :Object:
      Keeps volume *Density* and *Detail* the same regardless of object scale.
   :World:
      Specify *Step Size* and *Density* in world space.

.. _bpy.types.VolumeRender.step_size:

Step Size :guilabel:`Cycles Only`
   Distance between volume samples. Lower values render more detail at the cost of performance.
   If set to zero, the step size is automatically determined based on voxel size.

.. _bpy.types.VolumeRender.clipping:

Clipping :guilabel:`Cycles Only`
   Value under which voxels are considered empty space to optimize rendering.

.. _bpy.types.VolumeRender.precision:

Precision :guilabel:`Cycles Only`
   Specifies volume data precision, lower values reduce memory consumption at the cost of detail.

   :Full: Full float (Use 32 bit for all data).
   :Half: Half float (Use 16 bit for all data).
   :Variable: Automatically vary the precision and use less precision for less noticeable areas.
