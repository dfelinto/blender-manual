.. _bpy.ops.gpencil.trace_image:

****************************
Trace Image to Grease Pencil
****************************

.. reference::

   :Mode:      Object Mode
   :Menu:      :menuselection:`Object --> Convert --> Trace Image to Grease Pencil`

The *Trace Image to Grease Pencil* tool traces a black and white image and generates Grease Pencil strokes.
If the image is not black and white, it will be internally converted.
For better results, convert the images manually to black and white.
Also try to keep the resolution of the image small; high resolutions can produce very dense strokes.


Usage
=====

#. Add an :ref:`Image Empty <bpy.types.Object.empty_image>` to the scene.
#. Run *Trace Image to Grease Pencil*.


Options
=======

Target Object
   The Grease Pencil object name. If left empty, a new Grease Pencil object will be created.

Thickness
   The thickness of the generated Grease Pencil strokes.

Resolution
   Resolution of the generated Grease Pencil strokes i.e. how many control points the stroke will have.
   A higher resolution will preserve more detail from the original image.

Scale
   The object scale applied to the generated Grease Pencil object.

Sample
   Recreates the stroke geometry with a predefined length between points.
   Smaller values will require more points to recreate the stroke,
   while larger values will result in fewer points needed to recreate the curve.
   A value of 0 disables stroke sampling.

Color Threshold
   Determine the :term:`Luminance` threshold above which strokes are generated.

Turn Policy
   Determines how to resolve ambiguities during decomposition of an image into paths.

   :Black:    Prioritizes to connect black (foreground) components.
   :White:    Prioritizes to connect white (background) components.
   :Left:     Always take a left turn.
   :Right:    Always take a right turn.
   :Minority: Prioritizes to connect the color (black or white) that occurs
              least frequently in the local neighborhood of the current position.
   :Majority: Prioritizes to connect the color (black or white) that occurs
              most frequently in the local neighborhood of the current position.
   :Random:   Choose pseudo-randomly.

Mode
   Determines if the image being traced is a single image or image sequence.

   :Single:   The image empty is a single image or the current frame of an image sequence.
   :Sequence: The image empty is an :ref:`Image Sequence <image-sequence>`.

Start at Current Frame
   When enabled, start the tracing process at the current image frame.

Trace Frame
   Used to trace only one frame of the image sequence, set to zero to trace all.
