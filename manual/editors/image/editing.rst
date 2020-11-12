
*******
Editing
*******

.. admonition:: Reference
   :class: refbox

   :Mode:      All Modes
   :Menu:      :menuselection:`Image`

New
   Creates a new :ref:`image-generated` Image.
Open
   Load image from a file.
Open Cache Render
   Load the current scene's render layers from disk cache, if available.
   This can be used to save RAM while rendering because the render layers do not have to be saved in RAM.
   This can also be used to recover some information from a fail render.
   For this to work, :ref:`Save Buffers <render_properties_save-buffers>` must be enabled.

Replace
   Replaces the current image throughout the blend-file with another image.
Reload
   Reload the image from the file on drive.
Edit Externally
   Using the *Edit Externally* tool Blender will open an external image editor,
   as specified in the *Preferences* and load in the image to be edited.

Save
   Save the image, if the image is already a file :kbd:`Alt-S`.
Save As
   Save the (rendered) image in a separate file :kbd:`Shift-Alt-S` or
   you want to save it under a different name.
Save a Copy
   Using *Save as Copy* will save the file to a specified name,
   but will keep the old one open in the Image editor.
Save All Images
   Save all modified images. Packed images will be repacked.

Invert
   Invert Image Colors
      Invert the colors of an image.
   Invert Channel
      Red, Green, Blue, Alpha

Resize
   Adjust the image size in pixels.
Pack
   Packs the image into the blend-file.
   See :ref:`pack-unpack-data`.
Unpack
   Unpack the image to a drive.
Extract Palette
   Extracts a :ref:`Color Palette <ui-color-palette>` from the image for use by other tools.
Generate Grease Pencil
   Creates a :doc:`Grease Pencil </grease_pencil/index>` object using the currently selected image as a source.

.. important::

   Rendered images are not automatically saved, they have to be saved to drive manually.
