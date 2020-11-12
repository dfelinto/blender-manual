.. _bpy.ops.gpencil.trace_image:

*****************************
Trace Images to Grease Pencil
*****************************

.. admonition:: Reference
   :class: refbox

   :Mode:      Object Mode
   :Menu:      :menuselection:`Object --> Trace Images to Grease Pencil`

The *Trace Images to Grease Pencil* operator traces a black and white image and generates grease pencil strokes.
If the image is not black and white, it will be internally converted.
For better results, use manually converted to black and white images.
Also try to keep the resolution of the image small; high resolutions could produce very dense strokes.


Usage
=====

#. Add an :ref:`Image Empty <bpy.types.Object.empty_image>` to the scene.
#. Run *Trace Images to Grease Pencil*.


Options
=======

Target Object
   The grease pencil object name. If empty, a new grease pencil object will be created.

Thickness
   The thickness of the generated grease pencil strokes.

Resolution
   Resolution of the generated  grease pencil strokes i.e. how many control points the stroke will have.
   A higher resolution will preserve more detail from the original image.

Scale
   The object scale applied to the generated grease pencil object.

Sample
   Recreates the stroke geometry with a predefined length between points.
   Smaller values will require more points to recreate the stroke,
   while larger values will result in fewer points needed to recreate the curve.
   A value of 0 disables stroke sampling.

Color Threshold
   Determines what is considered white and what black.

Turn Policy
   Determines how to resolve ambiguities during decomposition of bitmaps into paths.

   :Black: Prefers to connect black (foreground) components.
   :White: Prefers to connect white (background) components.
   :Left: Always take a left turn.
   :Right: Always take a right turn.
   :Minority: Prefers to connect the color (black or white) that occurs least
      frequently in the local neighborhood of the current position.
   :Majority: Prefers to connect the color (black or white) that occurs most
      frequently in the local neighborhood of the current position.
   :Random: Choose pseudo-randomly.

Mode
   Determines if the image being traced is an single image or image sequence.

   :Single: The image empty is a single image or the current frame of an image sequence.
   :Sequence: The image empty is a :ref:`Image Sequence <image-sequence>`.
