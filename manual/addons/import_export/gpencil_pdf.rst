
************************************************
Portable Document Fromat (PDF) as Grease Pencil
************************************************

.. admonition:: Reference
   :class: refbox

   :Category:  Import-Export
   :Menu:      :menuselection:`File --> Export --> Grease Pencil as PDF`

.. warning:: .. warning:: This script only works in Object Mode.

Properties
==========

Object
   Determine wich objects include in the export

   :Active: Export only the active Grease Pencil object.
   :Selected: Export all selected Grease Pencil objects.
   :Visible: Export all visible Grease Pencil object in the scene.

Frame
   :Active: Export only the active keyframe.
   :Selected: Export all selected keyframes as different PDF pages.

.. note:: To enable multi-keyframe selection you must enable Multiframe Edition.
   See :doc:`Multiframe Edition </grease_pencil/multiframe>` for more information.

Sampling
   Precision for the stroke sampling. Low values mean a more accurate result.

Fill
   When enabled, Export the Grease Pencil strokes fill.

Normalize
   When enabled, Export strokes with constant thickness.


Usage
=====

This format is use for interchanging PDF between applications,
it support the export of Grease Pencil animation creating one page in the PDF document for each keyframe selected.
