
*******
Editing
*******

.. _bpy.ops.image.new:

New
===

.. reference::

   :Mode:      All Modes
   :Menu:      :menuselection:`Image --> New`
   :Shortcut:  :kbd:`Alt-N`

Creates a new :ref:`image-generated` Image.


.. _bpy.ops.image.open:

Open
====

.. reference::

   :Mode:      All Modes
   :Menu:      :menuselection:`Image --> Open`
   :Shortcut:  :kbd:`Alt-O`

Load image from a file.


.. _bpy.ops.image.read_viewlayers:

Open Cache Render
=================

.. reference::

   :Mode:      All Modes
   :Menu:      :menuselection:`Image --> Open Cache Render`
   :Shortcut:  :kbd:`Ctrl-R`

Load the current scene's render layers from disk cache, if available.
This can be used to save RAM while rendering because the render layers do not have to be saved in RAM.
And also for recovering some information from a fail render.
For this to work, :ref:`Cache Result <bpy.types.RenderSettings.use_render_cache>` must be enabled.


.. _bpy.ops.image.replace:

Replace
=======

.. reference::

   :Mode:      All Modes
   :Menu:      :menuselection:`Image --> Replace`
   :Shortcut:  :kbd:`Ctrl-R`

Replaces the current image throughout the blend-file with another image.


.. _bpy.ops.image.reload:

Reload
======

.. reference::

   :Mode:      All Modes
   :Menu:      :menuselection:`Image --> Reload`
   :Shortcut:  :kbd:`Alt-R`

Reload the image from the file on drive.


.. _bpy.ops.image.external_edit:

Edit Externally
===============

.. reference::

   :Mode:      All Modes
   :Menu:      :menuselection:`Image --> Edit Externally`

Using the *Edit Externally* tool Blender will open an external image editor,
as specified in the *Preferences* and load in the image to be edited.


.. _bpy.ops.image.save:

Save
====

.. reference::

   :Mode:      All Modes
   :Menu:      :menuselection:`Image --> Save`
   :Shortcut:  :kbd:`Alt-S`

Save the image, if the image is already a file.

.. important::

   Rendered images are not automatically saved, they have to be saved to drive manually.


.. _bpy.ops.image.save_as:

Save As
=======

.. reference::

   :Mode:      All Modes
   :Menu:      :menuselection:`Image --> Save As`
   :Shortcut:  :kbd:`Shift-Alt-S`

Save the (rendered) image in a separate file.


Save a Copy
===========

.. reference::

   :Mode:      All Modes
   :Menu:      :menuselection:`Image --> Save a Copy`

Using *Save as Copy* will save the file to a specified name,
but will keep the old one open in the Image editor.


.. _bpy.ops.image.save_all_modified:

Save All Images
===============

.. reference::

   :Mode:      All Modes
   :Menu:      :menuselection:`Image --> Save All Images`

Save all modified images. Packed images will be repacked.


.. _bpy.ops.image.invert:

Invert
======

.. reference::

   :Mode:      All Modes
   :Menu:      :menuselection:`Image --> Invert`

Invert Image Colors
   Invert the colors of an image.
Invert Channel
   Red, Green, Blue, Alpha


.. _bpy.ops.image.resize:

Resize
======

.. reference::

   :Mode:      All Modes
   :Menu:      :menuselection:`Image --> Resize`

Adjust the image size in pixels.


.. _bpy.ops.image.flip:

Flip
====

.. reference::

   :Mode:      All Modes
   :Menu:      :menuselection:`Image --> Flip`

This operator mirrors the image across a specified axis.
Use this to alter the perspective of an image giving an alternative viewpoint;
this can make an image more visually appealing or highlight some visual flaw.

Horizontally
   Mirrors the image so the left side becomes the right side.
Vertically
   Mirrors the image so the top becomes the bottom.


.. _bpy.ops.image.pack:

Pack
====

.. reference::

   :Mode:      All Modes
   :Menu:      :menuselection:`Image --> Pack`

Packs the image into the blend-file.
See :ref:`pack-unpack-data`.


.. _bpy.ops.image.unpack:

Unpack
======

.. reference::

   :Mode:      All Modes
   :Menu:      :menuselection:`Image --> Unpack`

Unpack the image to a drive.


.. _bpy.ops.palette.extract_from_image:

Extract Palette
===============

.. reference::

   :Mode:      All Modes
   :Menu:      :menuselection:`Image --> Extract Palette`

Extracts a :ref:`Color Palette <ui-color-palette>` from the image for use by other tools.


.. _bpy.ops.gpencil.image_to_grease_pencil:

Generate Grease Pencil
======================

.. reference::

   :Mode:      All Modes
   :Menu:      :menuselection:`Image --> Generate Grease Pencil`

Creates a :doc:`Grease Pencil </grease_pencil/index>` object using the currently selected image as a source.
