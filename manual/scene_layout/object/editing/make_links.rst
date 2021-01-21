.. _data-system-linked-libraries-make-link:
.. _bpy.ops.object.make_links:

**********
Make Links
**********

.. admonition:: Reference
   :class: refbox

   :Mode:      Object Mode
   :Menu:      :menuselection:`Object --> Make Links`
   :Hotkey:    :kbd:`Ctrl-L`

Links objects between scenes or data-blocks of the active object to all selected objects.
In some case (i.e. Object Data, Modifier) the target objects must be
of the same type as the active one or capable of receiving the data.
If targets already have data linked to them, it will be unlinked first.

Objects to Scene
   Links the selected objects into a different scene than the current one.
   The *Link Objects to Scene* in the :ref:`ui-undo-redo-adjust-last-operation` panel lets you choose between scenes.

   This makes the same object exist in more than one scene at once,
   including its position and animation data.
   The object's origin will change its color to reflect that.
Type
   Data-block type to link.

   Object Data, Materials, Animation Data, Collection, Instance Collection,
   Modifiers, Fonts, :doc:`Effects </grease_pencil/visual_effects/index>`.

   Transfer UV Maps
      The active UV map of the selected objects will be replaced by a copy of
      the active UV map of the active object. If the selected object doesn't
      have any UV maps, it is created. Objects must be of type mesh and
      must have a matching topology.

.. seealso::

   :ref:`data-system-datablock-make-single-user` for unlinking data-blocks.
