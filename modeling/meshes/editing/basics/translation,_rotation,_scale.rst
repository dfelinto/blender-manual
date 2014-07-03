
..    TODO/Review: {{review|}} .

Translation, Rotation, Scale
============================


.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Panel:    :guilabel:`Mesh Tools` (\ :guilabel:`Editing` context)
   | Menu:     :menuselection:`Mesh --> Transform --> Grab/Move, Rotate, Scale, …`
   | Hotkey:   :kbd:`G`\ /\ :kbd:`R`\ /\ :kbd:`S`


Once you have a selection of one or more elements, you can grab/move (\ :kbd:`G`\ ), rotate (\ :kbd:`R`\ ) or scale (\ :kbd:`S`\ ) them, like many other things in Blender, as described in the :doc:`Manipulation in 3D Space <3d_interaction/transformations/basics>` section.

To move, rotate and scale selected components, either use the :guilabel:`Translate`\ , :guilabel:`Rotate`\ , and :guilabel:`Scale` buttons, the :doc:`transform manipulators <3d_interaction/transform_control/manipulators>`\ , or the shortcuts:

:kbd:`G`\ , :kbd:`R`\ , and :kbd:`S` respectively.
After moving a selection, the options in the Tool Shelf allow you to fine-tune your changes,
limit the effect to certain axes, turn proportional editing on and off, etc.

Of course, when you move an element of a given type (e.g. an edge),
you also modify the implicitly related elements of other kinds (e.g. vertices and faces).

You also have in :guilabel:`Edit` mode an extra option when using these basic manipulations: the :doc:`proportional editing <3d_interaction/transform_control/proportional_edit>`\ .
