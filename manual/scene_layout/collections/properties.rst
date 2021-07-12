
*********************
Collection Properties
*********************

.. reference::

   :Mode:      Object Mode
   :Panel:     :menuselection:`Properties --> Collection Properties`

Collection properties tab allows convenient access to properties for the active collection.

.. figure:: /images/scene-layout_collections_property_panel.png

   Collection properties.


Restrictions
============

Selectable
   Collection is selectable in the scene.

Disable in Renders
   Collection is globally disabled in renders.

Holdout
   Mask objects in collection from view layer.

Indirect Only
   Objects in this collection only contribute indirectly (through shadows and reflections)
   in the view layer.


Instancing
==========

Instance Offset
   Offset from the origin when instancing.


.. _scene_layout-collections-line-art:

Line Art
========

.. _bpy.types.Collection.lineart_usage:

Usage
   How the collection is loaded into line art.
   Child objects of the collection can override this setting
   if they wish in :ref:`Object Properties <bpy.types.ObjectLineArt.usage>`.

   :Include:
      Include all objects in this collection into line art calculation.
   :Intersection Only:
      Objects in the collection will only produce intersection lines in
      the scene and their own geometry stay invisible.
   :Occlusion Only:
      Objects in the collection will only cause occlusion to existing feature lines
      and their geometry stay invisible.
   :Exclude:
      Objects in this collection will not be loaded into line art at all.
   :No Intersection:
      Objects in this collection will not generate intersection lines on
      themselves or with other objects in scene.
