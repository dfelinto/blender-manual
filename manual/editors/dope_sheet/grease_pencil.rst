
*************
Grease Pencil
*************

This Mode allows you adjust the timing of the :doc:`Grease Pencil object's </grease_pencil/index>`
animation frames. It is especially useful for animators blocking out shots,
where the ability to re-time blocking is one of the main purposes of the whole exercise.

This mode can be accessed by changing the Dope Sheet editor's *Mode* selector (found in the header to the far left)
to Grease Pencil.

To use this editor mode, make sure you have a :doc:`Grease Pencil object </grease_pencil/index>` selected.

.. figure:: /images/editors_dope-sheet_grease-pencil_view.png


Channels Region
===============

Grease Pencil (light blue)
   The channels' region shows the Grease Pencil data-blocks containing the layers.
   Multiple blocks are used for each area (e.g. one for the 3D Viewport and the Image editor).
Layers (gray)
   These channels contain the keyframes to which
   the :doc:`layers </grease_pencil/properties/layers>` are bound.

   Opacity
      Controls the layers :ref:`Opacity <bpy.types.GPencilLayer.opacity>`.
   Mask (mask icon)
      Toggle the :doc:`Masks </grease_pencil/properties/masks>` visibility.
   Onion Skinning (onion skin icon)
      Toggle the use the layer for :doc:`Onion Skinning </grease_pencil/properties/onion_skinning>`.
   Viewport/Render Visibility (eye icon)
      Toggle layer visibility in the viewport and in render.
   Lock Animation (checkbox icon)
      Toggles playback of animation or keep the channel static.
   Lock (padlock icon)
      Toggle layer from being editable.


Header
======

Layer Move
   Moves the selected layer/channel up or down in the evaluation stack.
Layer Add/Remove
   Adds/removes Grease Pencil layers/channels.

Insert Keyframe
---------------

Insert Keyframe :kbd:`I` can be used for creating blank Grease Pencil frames at a particular frame.
It will create blank frames if *Additive Drawing* is disabled, otherwise
it will make a copy of the active frame on that layer, and use that.


Copying Frames
--------------

It is possible to copy frames from one layer to another,
or from object to object, using the *Copy* and *Paste* tools in the *Key* menu.
Note that keyframes will be pasted into selected layers, so make sure you have a destination layer selected.


Main View
=========

The keyframes can be manipulated like any other data in the *Dope Sheet*.
Interpolated keyframes (alias breakdowns) are visualized as smaller light blue points.


Sidebar
=======

The Sidebar contains a copy of the Grease Pencil :doc:`Layer Properties </grease_pencil/properties/layers>`.
