.. _bpy.ops.mesh.knife:
.. _tool-mesh-knife:

*****
Knife
*****

.. reference::

   :Mode:      Edit Mode
   :Tool:      :menuselection:`Toolbar --> Knife`
   :Shortcut:  :kbd:`K`

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

If multiple objects are selected before entering Edit Mode,
then knife cuts will affect all of those objects.

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

X-Ray
   Show cut points on non-visible geometry too, when *Occlude Geometry* is deactivated.

Measurement
   Which visible measurements to show.

   Distance, Angle, None, Both

Angle Snapping
   Whether or not dragged lines should be constrained to particular angles, and if so,
   which coordinate system the angle is relative to.

   None, Screen, Relative

Angle Snapping Increment
   When angle snapping is on, the angle will be constrained to a multiple of this angle.


Controls
========

Confirm :kbd:`Spacebar` or :kbd:`Return`
   Confirms the cut.
   :kbd:`Return` will leave selected every edge except the new edges created from the cut.

Cancel :kbd:`Esc`
   Cancels the cut.

Draw a Continuous Line :kbd:`LMB` drag.
   So you can draw a free-hand line over a surface,
   points will be created at edge intersections.

Close Loop double-click :kbd:`LMB`
   This is a quick way to close the loop you are currently cutting.

New Cut :kbd:`RMB`
   Begins a new cut. This allows you to define multiple distinct cut lines.
   If multiple cuts have been defined, they are recognized as new snapping points.

   .. list-table::

      * - .. figure:: /images/modeling_meshes_tools_knife_multiple-before.png

             Creating multiple cuts.

        - .. figure:: /images/modeling_meshes_tools_knife_multiple-after.png

             Result of starting new cuts while in the tool.

Midpoint Snap :kbd:`Shift`
   Hold to snap the cursor to the midpoint of edges,
   meaning that all cuts will be performed at the exact center of each cut edge.

Ignore Snap :kbd:`Ctrl`
   Hold to make the tool ignore snapping,
   unlike the default where mouse cursor snaps to near edges.

Cut Through: :kbd:`C`
   Allow the Cut tool to cut through to occluded faces, instead of only the visible ones.

Angle Constrain :kbd:`A`
   Constrains the cut line to certain degree increments.
   The increment can be specified in the Tool Settings (see above), or can be typed
   when angle constraining is active.
   The default angles are in the plane of the screen, but typing :kbd:`A` again
   makes it relative to the last cut edge.
   If the last cut edge is ambiguous (because the cut was on a vertex),
   typing :kbd:`R` cycles through the possible reference edges.

   .. list-table::

      * - .. figure:: /images/modeling_meshes_tools_knife_angle-before.png
             :width: 320px

             Constraining cut angle.

        - .. figure:: /images/modeling_meshes_tools_knife_angle-after.png
             :width: 320px

             Result of constraining cut angle.

Axis Constrain :kbd:`X`, :kbd:`Y`, or :kbd:`Z`
   Constrains the cut line to one of the coordinate system axes.
   Initially it will be the global axis with the given name,
   but pressing the same key again switches to the object's local axis system.
   Additionally, if the scene transformation orientation is set to
   a custom orientation (e.g. from a face), the constraints will be in that coordinate system.

Visible Measurements :kbd:`S`
   Shows measurements of the cuts being made: angles with respect to a mesh edge, lengths, or both.
   Pressing :kbd:`S` repeatedly cycles between what can be shown.

   Only Distance, Only Angles, Both, None

   .. list-table::

     * - .. figure:: /images/modeling_meshes_tools_knife-measurement-distance.png
            :width: 640px

            Only Distance.

       - .. figure:: /images/modeling_meshes_tools_knife-measurement-angles.png
            :width: 640px

            Only Angles.

       - .. figure:: /images/modeling_meshes_tools_knife-measurement-both.png
            :width: 640px

            Both angles and distance.

Undo :kbd:`Ctrl-Z`
   Undoes the previous cut segment. The starting point for the next cut is adjusted accordingly.
   If a cut is a drag cut, the entire drag cut is undone.

X-Ray Mode :kbd:`V`
   Toggles whether or not cuts to segments behind the visible geometry are shown.


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
