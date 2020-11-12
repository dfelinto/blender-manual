.. _bpy.types.MetaSequence:

***********
Meta Strips
***********

A Meta Strip is a strip which contain multiple strips treated as if it was one strip.
It allows you to reduce the vertical space used in the Sequencer.
You can edit it the same way as any other strips.

It is organization tool. For example, if you are using a lot of strips with
complicated arrangement, you can group them together using Meta strips.

Make Meta Strip :kbd:`Ctrl-G`
   To create a Meta strip, select all the strips you want to group, and :kbd:`Ctrl-G` to group them.
   The Meta strips will span from the beginning of the first strip to the end of the last one,
   and condenses all channels into a single strip.
UnMeta Strip :kbd:`Ctrl-Alt-G`
   Separating (ungrouping) the Meta strip restores the strips to their relative positions and channels.
   This can be used if you choose to delete a Meta strip and want to keep the strips inside.

.. figure:: /images/video-editing_sequencer_meta_example.png
   :align: center

   Example of Meta strips.

You can edit the content inside a Meta strip by pressing :kbd:`Tab`.
It will expand the strip to the whole view and hide any other strips.
To exit the Meta strip press :kbd:`Tab` again.
Meta strips can also be nested, which make editing them a little confusing.
To exit out one level of Meta Strip make sure you do not have a Meta strips selected when you press :kbd:`Tab`.

.. note::

   The default blend mode for a Meta strip is Replace. There are many cases where this alters
   the results of the animation so be sure to check the results and adjust the blend mode if necessary.

One convenient use for Meta strips is when you want to apply the same effect to multiple strips.
For example: if you have a video that was recorded in different files and want to add an effect strip.
It is much more convenient to apply a single set of effects
to one Meta strip than applying it to each individual strip.

.. seealso::

   It is also possible to do the similar task described above with
   an :doc:`Adjustment Layer </video_editing/sequencer/strips/adjustment>` effect strip.
