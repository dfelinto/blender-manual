
..    TODO/Review: {{review|partial=x|fixes=[] }} .


Layers
======

Grease Pencil sketches are organized in layers,
much like those you could find in the GIMP or Photoshop.
These layers are not related to any of the other layer systems in Blender,
and also do not have an upper limit on the maximum number of layers that can be used.
Like the layers in the aforementioned applications, these layers can also be renamed, locked,
hidden, and deleted.

Their main purpose is to collect together a bunch of sketches that belong together in some
meaningful way (i.e. "blocking notes", "director's comments on blocking", or "guidelines").
For this reason, all the strokes on a layer (not just those made after a particular change)
are affected by that layer's color, opacity, and stroke thickness settings.

By default, most operations occur only on the *active* layer.
The active layer can be identified as the one with the different panel color
(in the default set, a light orangy-brown color). Clicking on a layer,
or changing any of its settings will make it the new active layer.

The active layer can also be identified by looking at the status indicator
(in the top right-hand corner of every view with Grease Pencil data being shown).


Animation of the Sketches
=========================

Grease Pencil can be used to do basic pencil tests (i.e. 2D animation in flipbook style).
Sketches are stored on the frame that they were drawn on, as a separate drawing
(only on the layer that they exist on).
Each drawing is visible until the next drawing for that layer is encountered.
The only exception to this is the first drawing for a layer,
which will also be visible before the frame it was drawn on.

Therefore, it is simple to make a pencil-test/series of animated sketches:

- Go to first relevant frame. Draw.
- Jump to next relevant frame. Draw some more.
- Keep repeating process, and drawing until satisfied. Voila! Animated sketches.


Onion Skinning
--------------

Onion-skinning (also known as ghosting), is a useful tool for animators, as neighboring frame
(s) are lightly drawn by Blender. It allows animators to make judgments about movements,
by comparing movement from different frames.

Usage Notes:

- Onion-skinning is enabled per layer by clicking on the :guilabel:`Onion Skin` button in the grease pencil properties panel.
- The :guilabel:`Frames` field, directly under the :guilabel:`Onion Skin` button, controls how many frames will be drawn. When :guilabel:`Frames` is **0**, only the drawing on either side of the current frame will be visible. Otherwise, this field specifies the maximum number of frames on either side of the current frame that will result in a neighboring drawing.


Adjusting Timing of Sketches
----------------------------

It is possible to set a Grease-Pencil block to be loaded up in the :guilabel:`DopeSheet` for
editing of the timings of the drawings.
This is especially useful for animators blocking out shots,
where the ability to re-time blocking is one of the main purposes of the whole exercise.

- In an :guilabel:`Dope Sheet` window, change the mode selector (found beside the menus) to :guilabel:`Grease Pencil` (by default, it should be set to :guilabel:`DopeSheet`).
- At this point, the :guilabel:`DopeSheet` should now display a few "channels" with some "keyframes" on them. These "channels" are the layers, and the "keyframes" are the frames at which the layer has a sketch defined. They can be manipulated like any other data in the :guilabel:`DopeSheet` can be.


.. figure:: /images/DopeSheetGreasePencil.jpg
   :width: 598px
   :figwidth: 598px


All the available Grease-Pencil blocks for the current screen layout will be shown.
The Area/Grease-Pencil datablocks are drawn as green channels,
and are named with relevant info from the views. They are also labeled with the area (i.e.
window) index (which is currently not shown anywhere else though).


Copying Sketches
----------------

It is possible to copy sketches from a layer/layers to other layers in the :guilabel:`Action
Editor`, using the "Copy"/"Paste" buttons in the header. This works in a similar way as the
copy/paste tools for keyframes in the :guilabel:`Action Editor`.

Sketches can also be copied from one screen (or view) to another using these tools.
It is important to keep in mind that keyframes will only be pasted into selected layers,
so layers will need to be created for the destination areas too.

