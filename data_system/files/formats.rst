
Supported Formats
=================

Image Formats
-------------

This is the list of image file formats supported internally by Blender:


High Dynamic Range Graphics
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Blender's image input/output system transparently support regular 32 bits graphics
(4 x 8 bits) or floating point images storing 128 bits per pixel (4 x 32 bits).

On reading High Dynamic Range Images (\ `HDRI <http://http://en.wikipedia.org/wiki/HDRI>`__\ ),
even when they're for example 3 x 10 bits,
the pixels are always converted internally to RGBA float values. Optionally,
like while displaying the image in the UV Image editor,
this then gets converted to regular 32 bits for faster display.

When an image has float colors, all imaging functions in Blender default to use that.
This includes the Video Sequence Editor, texture mapping, background images,
and the Compositor.

For hints how to manipulate or view HDR images, please check the Curves UI page.


- :doc:`OpenEXR (Multilayer) <data_system/files/formats/openexr>`
- :doc:`DPX, Cineon and Radiance HDR <data_system/files/formats/dpx,_cineon,_hdr>`


Others Formats
~~~~~~~~~~~~~~

Here's a list of other supported image formats:

- BMP
- DDS
- SGI IRIS (old!)
- PNG
- JPEG
- JPEG 2000
- Targa
- Targa Raw (uncompressed Targa)
- TIFF


Movie Formats
-------------

- AVI (Windows)
- AVI JPEG
- AVI Raw
- Frame Server
- H.264
- MPEG
- Ogg Theora
- QuickTime
- Xvid


Color Modes
-----------

- BW, Images get saved in 8 bits grayscale (only PNG, JPEG, TGA, TIF)
- RGB, Images are saved with RGB (color)
- RGBA, Images are saved with RGB and Alpha data (if supported)


Color Depths
------------

- 8 bit color channels
- 12 bit color channels
- 16 bit color channels
- 32 bit color channels


Reference
---------

- `Formats <http://projects.blender.org/scm/viewvc.php/trunk/blender/source/blender/makesrna/intern/rna_scene.c?view=markup&root=bf-blender>`__

