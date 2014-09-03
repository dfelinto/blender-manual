
..    TODO/Review: {{review|}} .


Loop Subdivide
**************

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Panel:    :guilabel:`Editing` context → :guilabel:`Mesh Tools`
   | Hotkey:   :kbd:`ctrl-R`


:guilabel:`Loop Cut` splits a loop of faces by inserting a new edge loop intersecting the chosen edge. The tool is interactive and has two steps:


Usage
=====

Pre-visualizing the cut
   After the tool is activated, move the cursor over a desired edge. The cut to be made is marked with a magenta colored line as you move the mouse over the various edges. The to-be-created edge loop stops at the poles (tris and ngons) where the existing face loop terminates.

Sliding the new edge loop
   Once an edge is chosen via :kbd:`lmb`, you can move the mouse along the edge to determine where the new edge loop will be placed. This is identical to the :doc:`Edge Slide tool </modeling/meshes/editing/edges#edge_slide>`. Clicking :kbd:`lmb` again confirms and makes the cut at the pre-visualized location, or clicking :kbd:`rmb` forces the cut to exactly 50%. This step is skipped when using multiple edge loops (see below)


.. figure:: /images/Doc26-loopCut-before.jpg
   :width: 200px
   :figwidth: 200px

   mesh before inserting edge loop


.. figure:: /images/Doc26-loopCut-preview.jpg
   :width: 200px
   :figwidth: 200px

   Preview of edge loop location


.. figure:: /images/Doc26-loopCut-placement.jpg
   :width: 200px
   :figwidth: 200px

   Interactive placement of edge loop between adjacent loops


Options
=======

Options are only available while the tool is in use, and are displayed in the 3d view header

Even :kbd:`E`
   Only available for single edge loops. This matches the shape of the edge loop to one of the adjacent edge loops. (See :doc:`Edge Slide tool </modeling/meshes/editing/edges#edge_slide>` for details)
Flip :kbd:`F`
   When Even is enabled, this flips the target edge loop to match. (See :doc:`Edge Slide tool </modeling/meshes/editing/edges#edge_slide>` for details)

Number of Cuts :kbd:`wheel` or :kbd:`pad+` / :kbd:`pad-`
   After activating the tool, but before confirming initial loop location, you can increase and decrease the number of cuts to create, by entering a number with the keyboard, scrolling :kbd:`wheel` or using :kbd:`pad+` and :kbd:`pad-`.
   Note that when creating multiple loops, these cuts are uniformly distributed in the original face loop, and *you will not be able to control their positions*.


.. figure:: /images/Doc26-loopCut-multicut.jpg
   :width: 250px
   :figwidth: 250px

   Preview of multiple edge loops


.. figure:: /images/Doc26-loopCut-multicut-after.jpg
   :width: 250px
   :figwidth: 250px

   Result of using multiple cuts


Smoothing  :kbd:`Alt-Wheel`
   Smoothing causes edge loops to be placed in an interpolated position, relative to the face it is added to,
   causing them to be shifted outwards or inwards by a given percentage,
   similar to the :guilabel:`Subdivide Smooth` command. When not using smoothing,
   new vertices for the new edge loop are placed exactly on the pre-existing edges. This keeps subdivided faces flat,
   but can distort geometry, particularly when using :doc:`Subdivision Surfaces </modifiers/generate/subsurf>`.
   Smoothing can help maintain the curvature of a surface once it is subdivided.




.. figure:: /images/Doc26-loopCut-unsmooth.jpg
   :width: 250px
   :figwidth: 250px

   Added edge loops without smoothing


.. figure:: /images/Doc26-loopCut-smooth.jpg
   :width: 250px
   :figwidth: 250px

   Same edge loops, but with smoothing value

