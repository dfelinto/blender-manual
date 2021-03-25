
************************************************
Scalable Vector Graphics (SVG) as Grease Pencil
************************************************

This format is use for interchanging vector based illustrations between applications and is supported by applications such as Inkscape, 
Illustrator, Corel Draw, and modern browsers among others.

.. warning:: The exporter only works in Object Mode.

Import
======

Options
--------

Resolution
   Resolution for generated strokes.

Scale
   Generated strokes scale.

Export
======

Options
--------

Object
   Determine wich objects include in the export

   :Active: Export only the active Grease Pencil object.
   :Selected: Export all selected Grease Pencil objects.
   :Visible: Export all visible Grease Pencil object in the scene.

Sampling
   Precision for the stroke sampling. Low values mean a more accurate result.

Fill
   When enabled, Export the Grease Pencil strokes fill.

Normalize
   When enabled, Export strokes with constant thickness.

Clip Camera
   When enabled, and camera view is active export only the strokes clipped from camera view.
