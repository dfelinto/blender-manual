
**********
Snake Hook
**********

.. reference::

   :Mode:      Sculpt Mode
   :Tool:      :menuselection:`Toolbar --> Snake Hook`
   :Shortcut:  :kbd:`K`

Pulls vertices along with the movement of the brush to create long, snake-like forms.


Brush Settings
==============

.. _bpy.types.Brush.crease_pinch_factor:

Magnify
   The *Snake Hook* brush tends to lose volume along the stroke,
   with *Magnify* value greater than 0.5 it's possible to sculpt shapes without losing volume.

.. _bpy.types.Brush.rake_factor:

Rake
   A factor to support moving the mesh with rotation following the cursor's motion.

.. _bpy.types.Brush.snake_hook_deform_type:

Deformation
   Deformation type that is used by the brush.

   Radius Falloff
      Applies the brush falloff to the tip of the brush.
   Elastic
      Modifies the entire mesh using an :term:`Elastic` deformation,
      see also the :doc:`Elastic Deform </sculpt_paint/sculpting/tools/elastic_deform>` tool.
