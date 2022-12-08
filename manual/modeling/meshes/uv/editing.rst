
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

.. reference::

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

Randomize
=========

.. reference::

   :Editor:    UV Editor
   :Mode:      Edit Mode
   :Menu:      :menuselection:`UV --> Transform --> Randomize`

Randomize the scale, rotation and offset of selected UV islands.
The *Randomize Transform* tool in the UV editor works
similar to *Randomize Transform* tool in the 3d view.

Random Seed
   Changes the random :term:`seed` used by the pseudo-random number generator,
   producing a different transform result for each seed value.

Location
   Amount to randomize location.

Rotation
   Amount to randomize rotation.

Scale Even
   Apply the same scale to the U coordinate and V coordinate.

Scale
   Amount to randomize scale in U and V coordinates.


Mirror
======

.. reference::

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

.. reference::

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

.. reference::

   :Editor:    UV Editor
   :Mode:      Edit Mode
   :Menu:      :menuselection:`UV --> Snap`
   :Shortcut:  :kbd:`Shift-S`

Snapping in the UV Editor is similar to
:doc:`Snapping in 3D </editors/3dview/controls/snapping>`.
For the snap to pixel options to work an image has to be loaded.

Selected to Pixels
   Moves selection to nearest pixel. See also *Round to Pixels* below.
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
Cursor to Origin
   Places the cursor to the location (0, 0, 0).

.. _bpy.ops.uv.weld:

Merge
=====

.. reference::

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

.. reference::

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

.. reference::

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

.. reference::

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

The sculpting tools, *Pinch* and *Relax*, will not move any pinned UVs. This allows
you to pin the borders, or around interior holes, and gives even more control to the
sculpt tools.

Pinning also works great with the *Live Unwrap* tool. If you pin two or more UVs,
with *Live Unwrap* on, moving or scaling the pinned UVs will interactively unwrap the model.
You can even use the *Grab* sculpting tool to move the pinned UVs.
This helps with fitting a UV island to a certain shape or region.


Mark/Clear Seams
================

.. reference::

   :Editor:    UV Editor
   :Mode:      Edit Mode
   :Menu:      :menuselection:`UV --> Mark/Clear Seam`

See :doc:`/modeling/meshes/uv/unwrapping/seams`.


.. _bpy.ops.uv.seams_from_islands:

Seams from Islands
==================

.. reference::

   :Mode:      View mode
   :Menu:      :menuselection:`UV --> Seams from Islands`

Adds seams at the boundaries of existing UV islands.
This is useful when modifying the UVs of already unwrapped meshes.


.. _bpy.ops.uv.pack_islands:

Pack Islands
============

.. reference::

   :Editor:    UV Editor
   :Mode:      Edit Mode
   :Menu:      :menuselection:`UV --> Pack Islands`

The *Pack Islands* tool generates an optimized UV layout with non-overlapping islands
that tries to efficiently fill the :term:`Texture Space`.

First it will uniformly scale the selected islands,
then individually translate each island so that they maximize the usage of the UV space.

 Pack To
   The :doc:`UDIM </modeling/meshes/uv/workflows/udims>` grid to pack UV islands into.

   :Closest UDIM: Pack islands to the UDIM closest to the center of the selection.
   :Active UDIM: Pack islands to active UDIM image tile or, if no image is available, the UDIM grid tile where the 2D cursor is located.
 Rotate
   Allow islands to be rotated as well as translated to maximize texture usage.
 Margin Method
   The method to use when calculating the empty space between islands.

   :Scaled: Use scale of existing UVs to multiply margin. (The default from Blender 3.3 and later.)
   :Add: Simple method, just add the margin. (This is the default margin scale from Blender 2.8 and earlier.)
   :Fraction: Precisely specify the fraction of the UV unit square for margin. (Slower than other two methods.)
 Margin
   The scale for the empty space between islands.

.. _bpy.ops.uv.average_islands_scale:

Average Island Scale
====================

.. reference::

   :Editor:    UV Editor
   :Mode:      Edit Mode
   :Menu:      :menuselection:`UV --> Average Island Scale`

Using the *Average Island Scale* tool, will scale each
UV island so that they are all approximately the same scale.

Non-Uniform
   Reduces average texture stretching within islands by scaling the U and V axes independently.
Shear
   Reduces average texture shearing within islands by shearing the U axis.


.. _bpy.ops.uv.minimize_stretch:

Minimize Stretch
================

.. reference::

   :Editor:    UV Editor
   :Mode:      Edit Mode
   :Menu:      :menuselection:`UV --> Minimize Stretch`

The *Minimize Stretch* tool, reduces UV stretch by minimizing the difference between
the angles in 3D and the angles in UV space.
This tool is similar to the Relax brush sculpt tool with the *Geometry Relaxation Method*,
but uses a different algorithm.

Fill Holes
   Just during *minimize stretch*, internal holes will be filled with temporary polygons
   to prevent stretching and overlaps of the surrounding UVs.
Blend
   The fraction between 0 and 1 of the original UVs to blend in once the stretch is minimized.
   A blend of 0 is the fully minimized stretch. Blend of 0.5 is halfway between the original UVs
   and the minimize stretch UVs.
Iterations
   More iterations result in smoother UVs, but take longer to process.

.. _bpy.ops.uv.stitch:

Stitch
======

.. reference::

   :Editor:    UV Editor
   :Mode:      Edit Mode
   :Menu:      :menuselection:`UV --> Stitch`
   :Shortcut:  :kbd:`Alt-V`

The *Stitch* tool, will join selected UVs that share vertices.
You set the tool to limit stitching by distance in the :ref:`bpy.ops.screen.redo_last` panel,
by activating *Use Limit* and adjusting the *Limit Distance*.


.. _bpy.ops.uv.align:

Align
=====

.. reference::

   :Editor:    UV Editor
   :Mode:      Edit Mode
   :Menu:      :menuselection:`UV --> Align`
   :Shortcut:  :kbd:`Shift-W`

The *Align* tool will move the selected UVs to a line, where that line is specified in different ways by *Axis*.

The *Straighten* option will calculate a line segment between two endpoints and move all selected UVs onto that line.

The *Align X* and *Align Y* options will axis-align all selected UVs to the midpoint of the current selection.

Axis
   :Straighten: Move UV to closest point on line segment.
   :Straighten X: Move *U* co-ordinates onto the line.
   :Straighten Y: Move *V* co-ordinates onto the line.
   :Align X: Move *U* co-ordinates to the midpoint of the selection.
   :Align Y: Move *V* co-ordinates to the midpoint of the selection.
   :Align Auto: Choose between *Align X* or *Align Y* automatically.

.. _bpy.ops.uv.align_rotation:

Align Rotation
==============

.. reference::

   :Editor:    UV Editor
   :Mode:      Edit Mode
   :Menu:      :menuselection:`UV --> Align Rotation`

The *Align Rotation* tool aligns entire islands to either the U or V axis.

The tool has three different methods of operation.
The different methods specify the source for the alignment,
and also whether to align with both the U and V axes,
or just the V axis alone.

When using the *Auto* method, islands are aligned so that UV edges are aligned
to either the U axis or the V axis. This method works best with quads
and meshes representing organic subjects.

When using the *Edge* method, only the selected edges are considered,
and the islands will be aligned such that the selected edges are aligned
with the V axis. This method works with the selection, so it works best
when a particular edge, or edge loop, needs to be aligned in UV coordinates.

When using the *Geometry* method, the geometry is taken into consideration.
Either the *X* axis, the *Y* axis, or the *Z* axis can be used. Suppose
the *X* axis is chosen. Using this method, edges which have a positive extent
in the *X* axis will be rotated in the UV map so that the edge
extends upwards in the *V* axis.
This method works best to align multiple islands which share some common
geometric property, either in the X, Y or Z axis.

Note that in the *Auto* method, edges can end up aligned either up or down or left or right
depending on the orientation of the island prior to activating the tool.
In the *Edge* method, the alignment of selected edges can be either up
or down in the V axis, whatever is closest to the current orientation of the UV island.
By comparison, in the *Geometry* method, the alignment will always be pointing up in the V axis,
ignoring any previous orientation.

.. _bpy.ops.uv.copy:

Copy UVs
========

.. reference::

   :Editor:    UV Editor
   :Mode:      Edit Mode
   :Menu:      :menuselection:`UV --> Copy UVs`

For each selected UV island, the *Copy UVs* tool will copy it's topology and UV coordinates into a temporary clipboard for later use with the *Paste UVs* tool.

.. note::

   The *Copy UVs* tool currently uses an internal clipboard which is not shared between instances of blender.

.. _bpy.ops.uv.paste:

Paste UVs
=========

.. reference::

   :Editor:    UV Editor
   :Mode:      Edit Mode
   :Menu:      :menuselection:`UV --> Paste UVs`

For each selected UV island, the *Paste UVs* tool will attempt to match the topology of an island stored in the internal clipboard.
If a match is found, the UVs stored in the clipboard for the original island will be pasted onto the currently selected island.

For example, if a triangle attached to a quad attached to a quad is in the clipboard, then a different triangle<=>quad<=>quad is selected,
then the topologies match, and the UVs will be pasted over the current selection.

For best results, you may want to use the Rip tool, or :menuselection:`UV > Split > Selection`, prior to using *Paste UVs*.

.. _bpy.ops.uv.hide:
.. _bpy.ops.uv.reveal:

Show/Hide Faces
===============

.. reference::

   :Editor:    UV Editor
   :Mode:      Edit Mode
   :Menu:      :menuselection:`UV --> Show/Hide Faces`

- Reveal Hidden :kbd:`Alt-H`
- Hide Selected :kbd:`H`
- Hide Unselected :kbd:`Shift-H`


Export UV Layout
================

.. reference::

   :Editor:    UV Editor
   :Mode:      Edit Mode
   :Menu:      :menuselection:`UV --> Export UV Layout`

If you are using an external application, you need to know where on the mesh you are painting.

.. note::

   This is an :doc:`add-on </addons/import_export/mesh_uv_layout>` activated by default.


Proportional Editing
====================

.. reference::

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

.. reference::

   :Editor:    UV Editor
   :Mode:      Edit Mode
   :Menu:      :menuselection:`UVs`

.. _bpy.types.SpaceUVEditor.use_live_unwrap:

Live Unwrap
   Continuously unwraps the selected UV islands while transforming pinned vertices.
   Note, this is different than the :ref:`Live Unwrap <bpy.types.ToolSettings.use_edge_path_live_unwrap>`
   option in the 3D Viewport.

.. _bpy.types.SpaceUVEditor.pixel_round_mode:

Round to Pixels
   During UV transforms, you can use Round to Pixels to help with matching features in the image
   or ensure your UVs have precise horizontal, vertical or diagonal alignment.

   Note that Round to Pixels is applied after any snapping modes.

   :Disabled: UVs will not be rounded.
   :Corner:
      Will force the UVs to round to the corner of the nearest pixel of an image if loaded.
   :Center:
      Will force the UVs to round to the center of the nearest pixel of an image if loaded.

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

.. reference::

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

.. reference::

   :Editor:    3D Viewport
   :Mode:      Edit Mode
   :Menu:      :menuselection:`Face --> Face Data --> Reverse UVs`

The :menuselection:`Face --> Reverse UVs` tool mirrors the UVs per face,
which flips the image over, showing you the image reversed.
