.. _bpy.ops.mesh.sort_elements:
.. _mesh-edit-sort-elements:

*************
Sort Elements
*************

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Sort Elements...`

This tool (available from the context menu, *Vertices*, *Edges* and *Faces* menus)
allows you to reorder the matching selected mesh elements, following various methods.
Note that when called from the context menu,
the affected element types are the same as the active select modes.

View Z Axis
   Sort along the active view's Z axis, from farthest to nearest by default
   (use *Reverse* if you want it the other way).
View X Axis
   Sort along the active view's X axis, from left to right by default (again, there is the *Reverse* option).
Cursor Distance
   Sort from nearest to farthest away from the 3D cursor position (*Reverse* also available).
Material
   Sort faces, and faces only, from those having the lowest material's index to those having the highest.
   Order of faces inside each of those "material groups" remains unchanged.
   Note that the *Reverse* option only reverses the order of the materials,
   *not* the order of the faces inside them.
Selected
   Move all selected elements to the beginning (or end, if *Reverse* enabled),
   without affecting their relative orders.
   Warning: This option will also affect **unselected** elements' indices!
Randomize
   Randomizes indices of selected elements (*without* affecting those of unselected ones).
   The seed option allows you to get another randomization --
   the same seed over the same mesh or set of selected elements will always give the same result!
Reverse
   Simply reverse the order of the selected elements.

.. hint:: Enabling the Display Indices Option

   Enable the *Developer Extras* Option in :menuselection:`Preferences --> Interface --> Display` panel,
   a checkbox will appear in :menuselection:`Display & Shading Menu --> Viewport Overlay --> Developer --> Indices`.
