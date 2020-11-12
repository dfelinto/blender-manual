.. _bpy.types.SceneSequence:

************
Scene Strips
************

Scene strips are a way to insert the render output of another scene into your sequence.
Instead of rendering out a video, then inserting the video file, you can insert the scene directly.

The strip length will be determined based on the animation settings in that scene.

.. note::

   Scene strips cannot be used to reference the sequence's own scene; a secondary scene must be used instead.


Options
=======

Use Sequence
   Expand the scenes sequence strips, allowing one scene to reuse another scene's edit
   (instead of taking the render output from the scene).

   This is similar to how :doc:`Meta Strips </video_editing/sequencer/meta>` work,
   with the added advantage of supporting multiple instances of the same data.
Volume
   Volume of the audio taken from the chosen scene.
Camera
   This can be used to override the scene's camera with any other object.

   It is useful to support switching views within a single scene.
Show Grease Pencil
   Shows :doc:`Grease Pencil </grease_pencil/introduction>`
   in non render preview i.e. *Solid* mode.
Transparent
   Creates a transparent background.
   This is useful for doing overlays like rendering out Grease Pencil films via the Sequencer.
