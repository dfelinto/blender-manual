.. index:: Grease Pencil Modifiers; Subdivide Modifier
.. _bpy.types.SubdivideGpencilModifier:

******************
Subdivide Modifier
******************

The *Subdivide* modifier subdivide the strokes by
inserting points between other points to the lines.


Options
=======

.. figure:: /images/grease-pencil_modifiers_generate_subdivide_panel.png
   :align: right

   The Subdivide modifier.

Subdivision Type
   Catmull-Clark
      The default option, subdivides and smooths the surfaces.

   Simple
      Only subdivides the surfaces, without any smoothing.

Subdivisions
   Recursively adds more points.


Influence
---------

See :ref:`grease-pencil-modifier-influence-filters`.
