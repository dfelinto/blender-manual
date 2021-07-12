.. _sculpt-mask-menu:
.. _bpy.ops.paint.mask:

****
Mask
****

Masking to control which areas of the mesh are influenced by sculpting.

.. figure:: /images/sculpt-paint_sculpting_editing_mask_example.jpg

   Black part is masked.


Brush
=====

To edit the mask, select the *Mask Brush* from the Brush panel.


Editing
=======

.. reference::

   :Mode:      Sculpt Mode
   :Menu:      :menuselection:`Mask`

Masks can be edited across the entire model.
Using :kbd:`A` opens a pie menu to choose different operations.


Invert Mask
-----------

.. reference::

   :Mode:      Sculpt Mode
   :Menu:      :menuselection:`Mask --> Invert Mask`
   :Shortcut:  :kbd:`Ctrl-I`

Inverts an existing mask.


.. _bpy.ops.paint.mask_flood_fill:

Fill Mask
---------

.. reference::

   :Mode:      Sculpt Mode
   :Menu:      :menuselection:`Mask --> Invert Mask`

Fills the whole mask with a value of 1.


Clear Mask
----------

.. reference::

   :Mode:      Sculpt Mode
   :Menu:      :menuselection:`Mask --> Invert Mask`
   :Shortcut:  :kbd:`Alt-M`

Fills the mask with a value of 0. To completely remove the mask data, see `Clear Sculpt-Mask Data`_.


.. _bpy.ops.paint.mask_box_gesture:

Box Mask
--------

.. reference::

   :Mode:      Sculpt Mode
   :Menu:      :menuselection:`Mask --> Box Mask`
   :Shortcut:  :kbd:`B`

Works like the *Box Select* tool, it creates a rectangular mask region.
Hold :kbd:`Shift` to clear the mask of the selected region.


.. _bpy.ops.paint.mask_lasso_gesture:

Lasso Mask
----------

.. reference::

   :Mode:      Sculpt Mode
   :Menu:      :menuselection:`Mask --> Lasso Mask`
   :Shortcut:  :kbd:`Shift-Ctrl-LMB`

Can be used to create a free-form mask, similar to the *Lasso Select* tool.

.. tip::

   To clear the mask of areas with the *Lasso Mask* tool, first invert the mask,
   apply the *Lasso Mask*, and then invert the mask back.


.. _bpy.ops.sculpt.mask_filter:

Mask Filters
------------

.. reference::

   :Mode:      Sculpt Mode
   :Menu:      :menuselection:`Mask --> Mask Filters`

Mask filters are operations that are applied to the whole paint mask.

Type
   Smooth/Sharpen Mask
      Changes the crispness of the mask edge.
   Grow/Shrink Mask
      Changes the size of the mask.
   Increase/Decrease Contrast
      Changes the contrast of the mask.

Iterations
   The number of times that the filter is going to be applied.

Auto Iteration Count
   Use an automatic number of iterations based on the number of vertices of the sculpt.


.. _bpy.ops.sculpt.mask_expand:
.. _bpy.ops.sculpt.expand:

Expand Mask by Topology
-----------------------

.. reference::

   :Mode:      Sculpt Mode
   :Menu:      :menuselection:`Mask --> Expand Mask by Topology`
   :Shortcut:  :kbd:`Shift-A`

Creates a mask radiating outwards from the active vertex in a uniform manner.

.. note::

   This operator is meant to be used interactively through the shortcut.


.. rubric:: Shortcuts

:Invert: :kbd:`F`
   Flips between expanding a positive mask (value of one) or a negative mask (value of zero).
   In the case of face sets, this option flips between including areas inside the masked area
   or areas outside the masked area.
:Toggle Preserve State: :kbd:`E`
   Accumulates the new mask on top of the previous one instead of replacing it.
   For Face Sets, this creates Face Sets boundaries instead of replacing the existing Face Set.
:Toggle Gradient: :kbd:`G`
   Enables linear gradient, creates a linear gradient of values from the origin to the current active vertex.
:Geodesic Recursive Step: :kbd:`R`
   Generate a new :term:`Geodesic` falloff from the boundary of the enabled vertices of the current falloff.
:Topology Recursive Step: :kbd:`Alt-R`
   Generate a new topology flood fill falloff from the boundary of the enabled vertices of the current falloff.
:Move Origin: :kbd:`Spacebar`
   Moves the initial vertex used for calculating the falloff.
:Geodesic Falloff: :kbd:`1`
   Uses a falloff based on the :term:`Geodesic` distances from the edge boundary to the active vertex.
:Topology Falloff: :kbd:`2`
   Uses a falloff based on a flood fill using edges.
:Diagonals Falloff: :kbd:`3`
   Uses a falloff based on a flood fill using polygon diagonals and edges.
:Spherical Falloff: :kbd:`4`
   Uses a falloff based on the Euclidean distances from the edge boundary to the active vertex.
:Snap Expanded to Face Sets: :kbd:`Ctrl`
   Isolates the expanded region to the boundary of the face set under the cursor.
:Loop Count Increase: :kbd:`W`
   Increase the number of loops or iterations the operator is run;
   using four loops will split the mask into four parts.
:Loop Count Decrease: :kbd:`Q`
   Decrease the number of loops or iterations the operator is run;
   using four loops will split the mask into four parts.
:Toggle Brush Gradient: :kbd:`B`
   Similar to linear gradient but uses the current brush :doc:`Falloff </sculpt_paint/brush/falloff>`
   to define the shape of the falloff.
:Texture Distortion Increase: :kbd:`Y`
   Increases the falloff distance when using a texture to distort the mask shape.
:Texture Distortion Decrease: :kbd:`T`
   Decreases the falloff distance when using a texture to distort the mask shape.


Usage
^^^^^

.. rubric:: Textures

Textures can be used to affect the "strength" of the mask.
This feature can be combined with loops and recursion to create really unique looking masks.
To enable textures, you first need to create/select a texture to use,
this is done by in the Properties editor's :doc:`Texture Properties </render/materials/legacy_textures/index>`.
Next select the texture in the :doc:`Texture </sculpt_paint/brush/texture>` Brush Settings,
while there **make sure** to enable *3D* :ref:`Mapping <bpy.types.BrushTextureSlot.map_mode>`.
Now, you can use :kbd:`Y` and :kbd:`T` to increase or decrease the affect the texture has on the edge of the mask.


Expand Mask by Normals
----------------------

.. reference::

   :Mode:      Sculpt Mode
   :Menu:      :menuselection:`Mask --> Expand Mask by Normals`
   :Shortcut:  :kbd:`Shift-Alt-A`

Creates a mask radiating outwards from the active vertex while following the curvature of the mesh.
This operator uses the same internal operator as :ref:`bpy.ops.sculpt.expand`
meaning all the shortcuts and functionality works the same as that tool.

.. note::

   This operator is meant to be used interactively through the shortcut.


.. _bpy.ops.mesh.paint_mask_extract:

Mask Extract
------------

.. reference::

   :Mode:      Sculpt Mode
   :Menu:      :menuselection:`Mask --> Mask Extract`

Creates a duplicate mesh object based on masked geometry.

Threshold
   Minimum mask value to consider the vertex valid to extract a face from the original mesh.

Add Boundary Loop
   Creates and extra boundary loop on the edges of the geometry,
   making it ready for adding a Subdivision Surface modifier later.

Smooth Iterations
   Smooth iterations applied to the extracted mesh.

Project to Sculpt
   Project the extracted mesh on to the original sculpt object.

Extract as Solid
   Adds a :doc:`Solidify Modifier </modeling/modifiers/generate/solidify>` to the newly created mesh object.


.. _bpy.ops.mesh.paint_mask_slice:

Mask Slice
----------

.. reference::

   :Mode:      Sculpt Mode
   :Menu:      :menuselection:`Mask --> Mask Slice`

Removes the masked vertices from the mesh.

Threshold
   Minimum mask value to consider the vertex valid to extract a face from the original mesh.

Fill Holes
   Fills concave holes with geometry that might have resulted from the *Mask Slice* operation.

Slice to New Object
   Create a new object from the masked geometry.


.. _bpy.ops.sculpt.dirty_mask:

Dirty Mask
----------

.. reference::

   :Mode:      Sculpt Mode
   :Menu:      :menuselection:`Mask --> Dirty Mask`

Generates a mask based on the geometry cavity and pointiness.


.. _bpy.ops.sculpt.mask_init:

Random Mask
-----------

.. reference::

   :Mode:      Sculpt Mode
   :Menu:      :menuselection:`Mask --> Random Mask`

Generates a mask with random values for the entire object based on different mesh data.

Per Vertex
   Assigns a random mask value for each vertex.
Per Face Set
   Assigns a random mask value for each :doc:`Face Set </sculpt_paint/sculpting/editing/face_sets>`.
Per Loose Mask
   Assigns a random mask value for each disjoint part of the mesh.


.. _bpy.types.Sculpt.show_mask:
.. _bpy.types.View3DOverlay.sculpt_mode_mask_opacity:

Display Settings
================

.. reference::

   :Mode:      Sculpt Mode
   :Popover:   :menuselection:`Viewport Overlays -- Sculpt --> Mask`

The mask display can be toggled as a :doc:`viewport overlay </editors/3dview/display/overlays>`.
In the overlay popover, the opacity of the mask overlay can be adjusted to make it more or less visible on the mesh.


.. _bpy.ops.mesh.customdata_mask_clear:
.. _sculpt_mask_clear-data:

Clear Sculpt-Mask Data
======================

.. reference::

   :Mode:      Object/Edit Mode
   :Menu:      :menuselection:`Properties --> Object Data --> Geometry Data --> Clear Sculpt-Mask Data`

Completely frees the mask data layer from the mesh. While not a huge benefit,
this can speed-up sculpting if the mask is no longer being used.
