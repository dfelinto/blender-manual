
OpenEXR
=======

`ILM's OpenEXR <http://www.openexr.com>`__ has become a software industry standard for HDR image files, especially because of its flexible and expandable structure.

OpenEXR files can store values in the entire floating point space,
positive as well as negative numbers.

Apart from reading all OpenEXR file types, with RGBA and optional Z saved,
Blender supports OpenEXR in two ways:


-

FIXME(TODO: Internal Link;
[[#Render Output|Render Output]]
)

-

FIXME(TODO: Internal Link;
[[#Multi-layer, Multi-pass, tile-based files|Multi-layer, Multi-pass, tile-based files]]
)


Render Output
-------------

Available options for OpenEXR render output are:

**Half**
    Saves images in a custom 16 bits per channel floating point format. This reduces the actual "bit depth" to 10 bits, with a 5 bits power value and 1 bit sign.

**Zbuf**
    Save the depth information. In Blender this now is written in floats too, denoting the exact distance from the camera in "Blender unit" values.

**Preview**
    On rendering animations (or single frames via command line), Blender saves the same image also as a JPEG, for quick preview or download.

**Compression** (this button is below the Image menu button, default set to "None")


- PIZ, lossless wavelet compression. Compresses images with grain well.
- ZIP, standard lossless compression using zlib
- RLE, runlength encoded, lossless, works well when scanlines have same values.
- PXR24. lossy algorithm from Pixar, converting 32 bits floats to 24 bits floats.


Multi-layer, Multi-pass, tile-based files
-----------------------------------------

An OpenEXR file can hold unlimited layers and passes, stored hierarchically.
This feature now is in use for the "Save Buffers" render option.
This option doesn't allocate the entire final Render Result before render
(which can have many layers and passes), but saves for each tile the intermediate result to a
single OpenEXR file in the default Blender 'temp' directory.

When rendering is finished, after all render data has been freed,
this then is read back entirely in memory.

