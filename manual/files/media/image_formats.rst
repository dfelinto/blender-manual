.. _bpy.types.Image:
.. _bpy.ops.image:
.. _files-media-image_formats:

**************************
Supported Graphics Formats
**************************

Image Formats
=============

This is the list of image file formats supported internally by Blender:

.. |tick|  unicode:: U+2713
.. |cross| unicode:: U+2717

.. list-table::
   :header-rows: 1
   :class: valign
   :widths: 25 25 10 10 10 20

   * - Format
     - Channel Depth
     - Alpha
     - :doc:`Metadata </render/output/properties/metadata>`
     - DPI
     - Extensions
   * - BMP
     - 8bit
     - |cross|
     - |cross|
     - |tick|
     - ``.bmp``
   * - Iris
     - 8, 16bit
     - |tick|
     - |cross|
     - |cross|
     - ``.sgi`` ``.rgb`` ``.bw``
   * - PNG
     - 8, 16bit
     - |tick|
     - |tick|
     - |tick|
     - ``.png``
   * - JPEG
     - 8bit
     - |cross|
     - |tick|
     - |tick|
     - ``.jpg`` ``.jpeg``
   * - JPEG 2000
     - 8, 12, 16bit
     - |tick|
     - |cross|
     - |cross|
     - ``.jp2`` ``.jp2`` ``.j2c``
   * - Targa
     - 8bit
     - |tick|
     - |cross|
     - |cross|
     - ``.tga``
   * - `Cineon & DPX`_
     - 8, 10, 12, 16bit
     - |tick|
     - |cross|
     - |cross|
     - ``.cin`` ``.dpx``
   * - `OpenEXR`_
     - float 16, 32bit
     - |tick|
     - |tick|
     - |tick|
     - ``.exr``
   * - `Radiance HDR`_
     - float
     - |tick|
     - |cross|
     - |cross|
     - ``.hdr``
   * - TIFF
     - 8, 16bit
     - |tick|
     - |cross|
     - |tick|
     - ``.tif`` ``.tiff``

.. hint::

   If you are not interested in technical details,
   a good rule of thumb for selecting output formats for your project is:

   Use OpenEXR
      if you intend to do compositing or color grading on these images.
   Use PNG
      if you intend on-screen output or encoding into multiple video formats.
   Use JPEG
      for on-screen output where file size is a concern and quality loss is acceptable.

   *All these formats support compression which can be important when rendering out animations.*

.. hint::

   Bit depths for image formats represent the following numbers of tonal levels per channel:

   :8: 256 levels
   :10: 1024 levels
   :12: 4096 levels
   :16: 65536 levels


Opening Images
==============

Relative Path
   Sets the file path to be relative to the currently opened blend-file.

   See :ref:`files-blend-relative_paths`.
Detect Sequences
   Automatically looks for image sequences in the selected images (based on the file name).
   Disable this when you do want to get single images that are part of a sequence.
Detect UDIMs
   Automatically looks for :doc:`UDIM </modeling/meshes/uv/workflows/udims>`
   tiles in the directory of the selected image; if matches are found they are loaded into Blender as UDIMs.
   This works by detecting if the filename has a ``.xxxx`` (four digit number) before the file extension.


.. _image-formats-open-sequence:

Opening an Image Sequence
-------------------------

The filename of the images must contain a digit, indicating the frame.
The sequence could be opened by the selection of the images and
by the confirmation with the *Open Image* button or :kbd:`Return`.

.. (alt) To load image sequence in any of the supported image
   file formats, first click on the first frame and then Accept.
   Then change the Source to Image Sequence, and enter the ending frame number of this sequence.


.. _bpy.types.ImageFormatSettings:

Saving Images
=============

File Format
   Choose what format to save the image as.
Color Mode
   Choose the color format to save the image (or video) to.
   Note that *RGBA* is not available for all image formats, check the list above for details.

   BW, RGB, RGBA
Color Depth
   Some image file formats support a varying number of bits per pixel.
   This affects the color quality and file size. Commonly used depths:

   8-bit (256 levels)
      Most common for on-screen graphics and video.
   10, 12, 16-bit
      Used for some formats focusing on photography and digital films
      (such as DPX and JPEG 2000).
   16-bit Half Float
      Since full 32bit float is often more than enough precision,
      half float can save drive space while still providing a high dynamic range.
   32-bit Float
      Highest quality color depth.

   .. note::

      Internally Blender's image system supports either:

      - 8 bits per channel (4 × 8 bits).
      - 32 bits float per channel (4 × 32 bits) -- *using 4 times as much memory.*

      Images higher than 8 bits per channel will be converted into a float on loading into Blender.
Compression
   Used to reduce the size of the image file.
   How this is done may vary depending on the file format and settings used.
Quality
   Similar to *Compression* but is used for JPEG based file formats.
   The quality is a percentage, 0% being the maximum amount of compression and 100% is no compression.
Save As Render
   Applies :doc:`color transform </render/color_management>` to the saved image.
Copy
   The Copy checkbox will define if the data-block will reference the newly created file
   or the reference will be unchanged, maintaining it with the original one.


Format Details
==============

Cineon & DPX
------------

Cineon is Kodak's standard for film scanning, 10 bits per channel and logarithmic.
DPX has been derived from Cineon as the ANSI/SMPTE industry standard.
DPX supports 16-bit colors/channels, linear as well as logarithmic.
DPX is currently a widely adopted standard used in the film hardware/software industry.

DPX as well as Cineon only stores and converts the "visible" color range of values between 0.0
and 1.0 (as a result of rendering or composite).


OpenEXR
-------

`ILM's OpenEXR <https://www.openexr.com/>`__ has become a software industry standard
for HDR image files, especially because of its flexible and expandable structure.

An OpenEXR file can store multiple layers and passes.
This means OpenEXR images can be loaded into a Compositor keeping render layers and passes intact.


Output Options
^^^^^^^^^^^^^^

Available options for OpenEXR render output are:

Color Depth
   *Half* saves images in a custom 16 bits per channel floating-point format.
   This reduces the actual "bit depth" to 10-bit, with a 5-bit power value and 1-bit sign.

   Float (Half), Float (Full)
Codec
   ``PXR24``
      Lossy algorithm from Pixar, converting 32-bit floats to 24-bit floats.
   ``ZIP``
      Standard lossless compression using Zlib, operating on 16 scanlines at a time.
   ``PIZ``
      Lossless wavelet compression. Compresses images with grain well.
   ``RLE``
      Run-length encoded, lossless, works well when scanlines have same values.
   ``ZIPS``
      Standard lossless compression using Zlib, operating on a single scanline at a time.
   ``DWAA``
      JPEG-like lossy algorithm from DreamWorks.
Z Buffer
   Save the depth information.
   In Blender, this now is written in floats too,
   denoting the exact distance from the camera.
Preview
   On rendering animations (or single frames via command line),
   Blender saves the same image also as a JPEG, for quick preview or download.


Radiance HDR
------------

Radiance is a suite of tools for lighting simulation.
Since Radiance had the first (and for a long time the only) HDR image format,
this format is supported by many other software packages.

Radiance ``.hdr`` files store colors still in 8 bits per component,
but with an additional (shared) 8-bit exponent value, making it 32 bits per pixel.
