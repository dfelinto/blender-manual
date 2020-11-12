.. _bpy.ops.mesh.knife:
.. _tool-mesh-knife:

*****
Knife
*****

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Tool:      :menuselection:`Toolbar --> Knife`
   :Hotkey:    :kbd:`K`

The Knife tool can be used to interactively subdivide (cut up)
geometry by drawing lines or closed loops to create holes.


Usage
=====

When using *Knife*, the cursor changes to an icon of a scalpel
and the header changes to display options for the tool.
You can draw connected straight lines by clicking :kbd:`LMB`,
marked with small green squares. Red squares are already defined cuts.
Surrounding red squares mean that there is a cut already in that position,
so no additional vertex will be created (besides the first one).

.. list-table::

   * - .. figure:: /images/modeling_meshes_tools_knife_line-before.png

          Mesh before knife cut.

     - .. figure:: /images/modeling_meshes_tools_knife_line-active.png

          Knife cut active.

     - .. figure:: /images/modeling_meshes_tools_knife_line-after.png

          After confirming knife cut.


Tool Settings
=============

Occlude Geometry
   Only cut geometry visible on screen.

Only Selected :kbd:`Shift-K`
   Only cuts through selected geometry.


Controls
========

Confirm :kbd:`LMB` or :kbd:`Return`
   Confirms the cut.
   :kbd:`Return` will leave selected every edge except the new edges created from the cut.

Cancel
   Cancels the tool.

Draw a Continuous Line :kbd:`LMB` drag.
   So you can draw a free-hand line over a surface,
   points will be created at edge intersections.

Close Loop double-click :kbd:`LMB`
   This is a quick way to close the loop you are currently cutting.

New Cut :kbd:`E`
   Begins a new cut. This allows you to define multiple distinct cut lines.
   If multiple cuts have been defined, they are recognized as new snapping points.

   .. list-table::

      * - .. figure:: /images/modeling_meshes_tools_knife_multiple-before.png

             Creating multiple cuts.

        - .. figure:: /images/modeling_meshes_tools_knife_multiple-after.png

             Result of starting new cuts while in the tool.

Midpoint Snap :kbd:`Ctrl`
   Hold to snap the cursor to the midpoint of edges,
   meaning that all cuts will be performed at the exact center of each cut edge.

Ignore Snap :kbd:`Shift`
   Hold to make the tool ignore snapping,
   unlike the default where mouse cursor snaps to near edges.

Cut Through: :kbd:`Z`
   Allow the Cut tool to cut through to obscured faces, instead of only the visible ones.

Angle Constrain :kbd:`C`
   Constrains the cut to 45 degree increments.

   .. list-table::

      * - .. figure:: /images/modeling_meshes_tools_knife_angle-before.png
             :width: 320px

             Constraining cut angle.

        - .. figure:: /images/modeling_meshes_tools_knife_angle-after.png
             :width: 320px

             Result of constraining cut angle.


Known Limitations
=================

Duplicate Vertices
------------------

If you experience problems where duplicate vertices are being created by cuts,
this is often caused by too large a near/far clipping range.

Try increasing the *Clip Start* to avoid this problem,
see :ref:`Depth Troubleshooting <troubleshooting-depth>` for details.


Unconnected Cuts
----------------

Cuts that begin or end in the middle of a face, will be ignored.

*This is constrained by the kinds of geometry Blender can represent.*
