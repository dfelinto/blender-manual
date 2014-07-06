
..    TODO/Review: {{review|im=needs example}} .


Duplicate
*********

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`Mesh --> Duplicate`
   | Hotkey:   :kbd:`shift-D`


This tool simply duplicates the selected elements,
without creating any links with the rest of the mesh (unlike extrude, for example),
and places the duplicate at the location of the original. Once the duplication is done,
*only the new duplicated elements are selected*,
and you are automatically placed in grab/move mode, so you can translate your copy elsewhere...

In the :guilabel:`Tool Shelf` are settings for :guilabel:`Vector` offset,
:guilabel:`Proportional Editing`, :guilabel:`Duplication Mode` (non-functional?),
and :guilabel:`Axis Constraints`.

Note that duplicated elements belong to the same :doc:`vertex groups <modeling/meshes/vertex_groups>` as the "original" ones. The same goes for the :doc:`material indices <materials/multiple_materials>`, the edge's :guilabel:`Sharp` and :guilabel:`Seam` flags, and probably for the other vertex/edge/face properties...
