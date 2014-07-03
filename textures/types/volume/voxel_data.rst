

..    TODO/Review: {{review|partial=X|text=elaborate|im=needs images}} .


Voxel Data
==========

Voxel data renders a voxel source, working very similarly to an image texture, but in 3d.
Various input data source types are available (such as smoke voxel data, or external files),
as well as various interpolation methods.

The voxels are stored in a flat z/y/x grid of floats.
Functions for sampling this based on location within the (0,1) bounds are available in:

- source/blender/blenlib/intern/voxel.c

The default voxel data source, Smoke,
is used for rendering Blender's internal smoke simulations.
Other sources include binary raw formats, and Image Sequence,
which can be used to stack a sequence of images into a 3D representation,
which is a common format for medical volume data such as CT scans.


Settings
--------


:guilabel:`File Format`
   :guilabel:`Blender Voxel`
       Default binary voxel file format.
   :guilabel:`8 bit RAW`
       8 bit grayscale binary data.
   :guilabel:`Image Sequence`
       Generate voxels from a sequence of image slices.
   :guilabel:`Smoke`
       Render voxels from a Blender smoke simulation.

:guilabel:`Source Path`\ :The external source data file to use for 8 bit Raw data and Blender Voxel formats

:guilabel:`Domain Object (Smoke)`
   Object used as the smoke simulation domain

:guilabel:`Source`
   :guilabel:`Smoke`
      Use smoke density and color as texture data.
   :guilabel:`Flame`
      Use flame temperature as texture data.
   :guilabel:`Heat`
      Use smoke heat as texture data. Values from -2.0 to 2.0 are used.
   :guilabel:`Velocity`
      Use smoke velocity as texture data.

:guilabel:`Resolution`\ :Resolution of the voxel grid when using 8 bit Raw data.

:guilabel:`Interpolation`
   :guilabel:`Nearest Neighbor`
       No interpolation, fast but blocky and low quality.
   :guilabel:`Linear`
       Good smoothness and speed.
   :guilabel:`Quadratic`
       Mid-range quality and speed.
   :guilabel:`Cubic Catmull-Rom`
       Smoothed high quality interpolation, but slower.


:guilabel:`Extension`
   :guilabel:`Extend`
       Extend by repeating edge pixels of the image.
   :guilabel:`Clip`
       Clip to image size and set exterior pixels as transparent.
   :guilabel:`Repeat`
       Cause the image to repeat horizontally and vertically.

:guilabel:`Intensity`
   Multiplier for intensity values

