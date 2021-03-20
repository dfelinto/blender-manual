
*****
Usage
*****

Relations Management
====================

.. figure:: /images/editors_outliner_usage_relations.png
   :align: right

   Linking objects to a collection.

Data-blocks can be dragged and dropped to manage data relations in the Outliner.
To begin a drag and drop, :kbd:`LMB` click and drag from the name or icon of a data-block.

Objects can be moved to collections by dropping on the name or contents of a collection.
To link an object to a collection, hold :kbd:`Ctrl` while dropping.
To set parent-child relations between objects, drop an object onto another object
while holding :kbd:`Shift`.

.. note::

   Drag and drop will attempt to operate on the entire selection. Selected data-blocks
   that are incompatible with the operation will remain unmodified.


Modifiers, Constraints, & Visual Effects
========================================

You can manage :doc:`Modifiers </modeling/modifiers/index>`, :doc:`Constraints </animation/constraints/index>`, and
:doc:`Visual Effects </grease_pencil/visual_effects/index>` from the Outliner in a couple ways:

- To change the order with in the :ref:`stack <modifier-stack>`
  select the desired modifier and move it above or below other modifiers.
- To copy a single modifier to another select the modifier and drag it on top of the desired object.
- To copy the whole modifier stack to another object select the modifier icon and drag in to the desired object.


Drag & Dropping to 3D Viewport
==============================

Objects & Object Data
---------------------

Dragging object data-blocks from the Outliner to the :doc:`3D Viewport </editors/3dview/index>`
creates a :doc:`duplicate </scene_layout/object/editing/duplicate>` of the object.
Dragging *object data* data-blocks from the Outliner to the 3D Viewport
creates a :doc:`linked duplicate </scene_layout/object/editing/duplicate_linked>` of the object.
