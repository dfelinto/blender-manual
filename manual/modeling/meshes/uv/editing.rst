
*******
Editing
*******

After unwrap, you will likely need to arrange the UV maps,
so that they can be used in texturing or painting. Your goals for editing are:

- Stitch pieces (of UV maps) back together.
- Minimize wasted space in the image.
- Enlarge the faces where you want more detail.
- Re-size/enlarge the faces that are stretched.
- Shrink the faces that are too grainy and have too much detail.

With a minimum of dead space,
the most pixels can be dedicated to giving the maximum detail and fineness to the UV texture.
A UV face can be as small as a pixel (the little dots that make up an image)
or as large as an entire image. You probably want to make major adjustments first,
and then tweak the layout.


Transform
=========

.. admonition:: Reference
   :class: refbox

   :Editor:    UV Editor
   :Mode:      Edit Mode
   :Tool:      :menuselection:`Toolbar --> Move, Rotate, Scale, Transform`
   :Menu:      :menuselection:`UV --> Transform`

- Move :kbd:`G`
- Rotate :kbd:`R`
- Scale :kbd:`S`
- Shear :kbd:`Shift-Ctrl-Alt-S`


Axis Locking
------------

Transformations can be locked to an axis by pressing :kbd:`X` or :kbd:`Y` after one of the transform tools.
Also, holding the :kbd:`MMB` will constrain movement to the X or Y axis.


Mirror
======

.. admonition:: Reference
   :class: refbox

   :Editor:    UV Editor
   :Mode:      Edit Mode
   :Menu:      :menuselection:`UV --> Mirror`
   :Shortcut:  :kbd:`Ctrl-M`

UVs can be mirrored on the Y axis or the X axis:

- Mirror X
- Mirror Y

You can also use the hotkeys :kbd:`X` or :kbd:`Y`,
or hold the :kbd:`MMB` and drag in the mirror direction.


Copy Mirrored UV Coordinates
----------------------------

.. admonition:: Reference
   :class: refbox

   :Editor:    UV Editor
   :Mode:      Edit Mode
   :Menu:      :menuselection:`UV --> Copy Mirrored UV Coordinates`

Copies UVs from one side of the mirrored mesh to the other.
Affects only selected vertices (on both sides).

Axis Direction
   Positive/Negative
Precision
   Tolerance for finding vertex duplicates.


.. _bpy.ops.uv.snap_selected:
.. _bpy.ops.uv.snap_cursor:

Snap
====

.. admonition:: Reference
   :class: refbox

   :Editor:    UV Editor
   :Mode:      Edit Mode
   :Menu:      :menuselection:`UV --> Snap`
   :Shortcut:  :kbd:`Shift-S`

Snapping in the UV Editor is similar to
:doc:`Snapping in 3D </editors/3dview/controls/snapping>`.
For the snap to pixel options to work an image has to be loaded.

Selected to Pixels
   Moves selection to nearest pixel. See also *Snap to pixel* above.
Selected to Cursor
   Moves selection to 2D cursor location.
Selected to Cursor (Offset)
   Moves selection center to 2D cursor location, while preserving the offset of the vertices from the center.
Selected to Adjacent Unselected
   Moves selection to adjacent unselected element.

Cursor to Pixels
   Snaps the cursor to the nearest pixels.
Cursor to Selected
   Moves the Cursor to the center of the selection.


.. _bpy.ops.uv.weld:

Merge
=====

.. admonition:: Reference
   :class: refbox

   :Editor:    UV Editor
   :Mode:      Edit Mode
   :Menu:      :menuselection:`UV --> Merge`
   :Shortcut:  :kbd:`M`

At Center
   Moves selected UVs to their average position.
At Cursor
   Moves selection UVs to 2D cursor location.

.. _bpy.ops.uv.remove_doubles:

By Distance
   Merges selected UVs within the specified *Merge Distance*.


.. _bpy.ops.uv.select_split:

Split
=====

.. admonition:: Reference
   :class: refbox

   :Editor:    UV Editor
   :Mode:      Edit Mode
   :Menu:      :menuselection:`UV --> Split`
   :Shortcut:  :kbd:`Alt-M`

Selection :kbd:`Y`
   Splits (disconnects) the selection from the rest of the UV.
   The border edge to any non-selected elements are duplicated.

   Note that the "copy" is left exactly at the same position as the original,
   so you must move it to see it clearly.


Unwrap
======

.. admonition:: Reference
   :class: refbox

   :Editor:    UV Editor
   :Mode:      Edit Mode
   :Menu:      :menuselection:`UV --> Unwrap`
   :Shortcut:  :kbd:`U`

Blender offers several ways of mapping UVs.
The simpler projection methods use formulas that map 3D space onto 2D space,
by interpolating the position of points toward a point, axis or plane through a surface.
The more advanced methods can be used with more complex models, and have more specific uses.

- :ref:`bpy.ops.uv.unwrap`
- :ref:`bpy.ops.uv.smart_project`
- :ref:`bpy.ops.uv.lightmap_pack`
- :ref:`bpy.ops.uv.follow_active_quads`
- :ref:`bpy.ops.uv.cube_project`
- :ref:`bpy.ops.uv.cylinder_project`
- :ref:`bpy.ops.uv.sphere_project`


.. _bpy.ops.uv.pin:

Pin & Unpin
===========

.. admonition:: Reference
   :class: refbox

   :Editor:    UV Editor
   :Mode:      Edit Mode
   :Menu:      :menuselection:`UV --> Pin/Unpin`
   :Shortcut:  :kbd:`P`, :kbd:`Alt-P`

You can pin UVs so they do not move between multiple unwrap operations.
When Unwrapping a model it is sometimes useful to "Lock" certain UVs,
so that parts of a UV layout stay the same shape, and/or in the same place.
Pinning is done by selecting a UV, then selecting *Pin* from the *UVs* menu,
or the shortcut :kbd:`P`. You can *Unpin a UV* with the shortcut :kbd:`Alt-P`.

Pinning is most effective when using the Unwrap method of UV mapping, for organic objects.
An example is when you are modeling a symmetrical object using
the :doc:`Mirror Modifier </modeling/modifiers/generate/mirror>`.
Some of the UVs on the mirror axis may be shared across the mirrored counterparts.
You could pin the UVs that correspond to the midline, then align them on the X axis,
and they will stay in that location.

Pinning also work great with the Live Unwrap tool. If you pin two or more UVs,
with Live Unwrap on, dragging pinned UVs will interactively unwrap the model.
This helps with fitting a UV island to a certain shape or region.


Mark/Clear Seams
================

.. admonition:: Reference
   :class: refbox

   :Editor:    UV Editor
   :Mode:      Edit Mode
   :Menu:      :menuselection:`UV --> Mark/Clear Seam`

See :doc:`/modeling/meshes/uv/unwrapping/seams`.


.. _bpy.ops.uv.seams_from_islands:

Seams from Islands
==================

.. admonition:: Reference
   :class: refbox

   :Mode:      View mode
   :Menu:      :menuselection:`UV --> Seams from Islands`

Adds seams at the boundaries of existing UV islands.
This is useful when modifying the UVs of already unwrapped meshes.


.. _bpy.ops.uv.pack_islands:
.. _editors-uv-editing-layout-pack_islands:

Pack Islands
============

.. admonition:: Reference
   :class: refbox

   :Editor:    UV Editor
   :Mode:      Edit Mode
   :Menu:      :menuselection:`UV --> Pack Islands`
   :Shortcut:  :kbd:`Ctrl-P`

The *Pack Islands* tool generates an optimized UV layout with non-overlapping islands
that tries to efficiently fill the :term:`Texture Space`.

First it will uniformly scale the selected island,
then individually transform each island so that they fill up the UV space as much as possible.


.. _bpy.ops.uv.average_islands_scale:

Average Island Scale
====================

.. admonition:: Reference
   :class: refbox

   :Editor:    UV Editor
   :Mode:      Edit Mode
   :Menu:      :menuselection:`UV --> Average Island Scale`
   :Shortcut:  :kbd:`Ctrl-A`

Using the *Average Island Scale* tool, will scale each
UV island so that they are all approximately the same scale.


.. _bpy.ops.uv.minimize_stretch:

Minimize Stretch
================

.. admonition:: Reference
   :class: refbox

   :Editor:    UV Editor
   :Mode:      Edit Mode
   :Menu:      :menuselection:`UV --> Minimize Stretch`
   :Shortcut:  :kbd:`Ctrl-V`

The *Minimize Stretch* tool, reduces UV stretch by minimizing angles. This essentially relaxes the UVs.


.. _bpy.ops.uv.stitch:

Stitch
======

.. admonition:: Reference
   :class: refbox

   :Editor:    UV Editor
   :Mode:      Edit Mode
   :Menu:      :menuselection:`UV --> Stitch`
   :Shortcut:  :kbd:`V`

The *Stitch* tool, will join selected UVs that share vertices.
You set the tool to limit stitching by distance in the :ref:`bpy.ops.screen.redo_last` panel,
by activating *Use Limit* and adjusting the *Limit Distance*.


.. _bpy.ops.uv.align:

Align
=====

.. admonition:: Reference
   :class: refbox

   :Editor:    UV Editor
   :Mode:      Edit Mode
   :Menu:      :menuselection:`UV --> Align`
   :Shortcut:  :kbd:`Shift-W`

Straighten
   Auto, X, Y
Align
   Will line up the selected UVs on the X axis, Y axis, or automatically chosen axis.

   Auto, X, Y


Show/Hide Faces
===============

.. admonition:: Reference
   :class: refbox

   :Editor:    UV Editor
   :Mode:      Edit Mode
   :Menu:      :menuselection:`UV --> Show/Hide Faces`

- Reveal Hidden :kbd:`Alt-H`
- Hide Select :kbd:`H`
- Hide Unselect :kbd:`Shift-H`


Export UV Layout
================

.. admonition:: Reference
   :class: refbox

   :Editor:    UV Editor
   :Mode:      Edit Mode
   :Menu:      :menuselection:`UV --> Export UV Layout`

If you are using an external application, you need to know where on the mesh you are painting.

.. note::

   This is an :doc:`add-on </addons/import_export/mesh_uv_layout>` activated by default.


Proportional Editing
====================

.. admonition:: Reference
   :class: refbox

   :Editor:    UV Editor
   :Mode:      Edit Mode
   :Header:    :menuselection:`Proportional Editing`
   :Menu:      :menuselection:`UV --> Proportional Editing`
   :Shortcut:  :kbd:`O`

Proportional Editing is available in UV editing. The controls are the same as in the 3D Viewport.
See :doc:`Proportional Editing in 3D </editors/3dview/controls/proportional_editing>`
for a full reference.


UV Options
==========

.. admonition:: Reference
   :class: refbox

   :Editor:    UV Editor
   :Mode:      Edit Mode
   :Menu:      :menuselection:`UVs`

.. _bpy.types.SpaceUVEditor.use_live_unwrap:

Live Unwrap
   Continuously unwraps the selected UV islands while transforming pinned vertices.
   Note, this is different than the :ref:`Live Unwrap <bpy.types.ToolSettings.use_edge_path_live_unwrap>`
   option in the 3D Viewport.

.. _bpy.types.SpaceUVEditor.pixel_snap_mode:

Snap to Pixels
   Disabled
      UVs will not be snapped.
   Corner
      Will force the UVs to snap to the corners of the nearest pixels of an image if loaded.
   Center
      Will force the UVs to snap to the center of the nearest pixels of an image if loaded.

.. _bpy.types.SpaceUVEditor.lock_bounds:

Constraining to Image Bounds
   For standard textures, this option prevents UVs from being moved outside the 0 to 1 UV range.
   For :doc:`UDIMs </modeling/meshes/uv/workflows/udims>` textures,
   this option prevents UVs from being moved outside the nearest UDIM tile.


3D Viewport
===========

.. _bpy.ops.mesh.uvs_rotate:

Rotate UVs
----------

.. admonition:: Reference
   :class: refbox

   :Editor:    3D Viewport
   :Mode:      Edit Mode
   :Menu:      :menuselection:`Face --> Face Data --> Rotate UVs`

The orientation of the UV texture is defined by each face.
If the image is, for example, upside down or laying on its side,
use the :menuselection:`Face --> Rotate UVs` (in the 3D Viewport in Face Select mode)
menu to rotate the UVs per face in 90-degree turns.


.. _bpy.ops.mesh.uvs_reverse:

Reverse UVs
-----------

.. admonition:: Reference
   :class: refbox

   :Editor:    3D Viewport
   :Mode:      Edit Mode
   :Menu:      :menuselection:`Face --> Face Data --> Reverse UVs`

The :menuselection:`Face --> Reverse UVs` tool mirrors the UVs per face,
which flips the image over, showing you the image reversed.
