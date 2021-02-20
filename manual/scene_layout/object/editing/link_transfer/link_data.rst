.. _bpy.ops.object.make_links_data:

*********
Link Data
*********

.. admonition:: Reference
   :class: refbox

   :Mode:      Object Mode
   :Menu:      :menuselection:`Object --> Link/Transfer Data...`

Links objects between scenes or data-blocks of the active object to all selected objects.
In some case (i.e. Object Data, Modifier) the target objects must be
of the same type as the active one or capable of receiving the data.
If targets already have data linked to them, it will be unlinked first.

Type
   Data-block type to link.

   - `Link Object Data`_
   - `Link Materials`_
   - `Link Animation Data`_
   - `Link Collections`_
   - `Link Instance Collection`_
   - `Link Fonts to Text`_
   - `Copy Modifiers`_
   - `Copy Grease Pencil Effects`_

.. seealso::

   :ref:`data-system-datablock-make-single-user` for unlinking data-blocks.


Link Object Data
================

Replace assigned Object Data.


Link Materials
==============

Replace assigned Materials.


Link Animation Data
===================

Replace assigned Animation Data.


Link Collections
================

Replace assigned Collections.


Link Instance Collection
========================

Replace assigned Collection Instance.


Link Fonts to Text
==================

Replace Text object Fonts.


Copy Modifiers
==============

Replace Modifiers.


Copy Grease Pencil Effects
==========================

Replace Grease Pencil Effects.
