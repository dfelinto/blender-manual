.. _bpy.ops.mesh.bevel:
.. _tool-mesh-bevel:

***********
Bevel Edges
***********

.. admonition:: Reference
   :class: refbox

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Edge --> Bevel Edges`
   :Shortcut:  :kbd:`Ctrl-B`
   :Menu:      :menuselection:`Vertex --> Bevel Vertices` (vertex bevel)
   :Shortcut:  :kbd:`Shift-Ctrl-B` (vertex bevel)

The *Bevel* tool allows you to create chamfered or rounded corners on geometry.
A bevel is an effect that smooths out edges and corners.

Real world edges are very seldom exactly sharp.
Not even a knife blade edge can be considered perfectly sharp.
Most edges are intentionally beveled for mechanical and practical reasons.

Bevels are also useful for giving realism to non-organic models. In the real world,
the blunt edges on objects catch the light and change the shading around the edges.
This gives a solid, realistic look,
as opposed to un-beveled objects which can look too perfect.

.. figure:: /images/modeling_meshes_editing_edge_bevel_cubes.jpg

   Cubes with and without bevel.


Usage
=====

The *Bevel Edges* tool works only on selected edges with exactly two adjacent faces.
It will recognize any edges included in a vertex or face selection as well,
and perform the bevel the same as if those edges were explicitly selected.
In "vertex only" mode, the *Bevel Vertices* tool works on selected vertices instead of edges,
and there is no requirement about having any adjacent faces.
The *Bevel* tool smooths the edges and/or "corners" (vertices)
by replacing them with faces making smooth profiles with a specified number of *segments*
(see the options below for details about the bevel algorithm).

Use :kbd:`Ctrl-B` or a method listed above to run the tool.
Move the mouse to interactively or type a number to specify the bevel offset,
and scroll the :kbd:`Wheel` to increase or decrease the number of segments (see below).

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_edge_bevel_example-1.png
          :width: 320px

          Selected edge before beveling.

     - .. figure:: /images/modeling_meshes_editing_edge_bevel_example-2.png
          :width: 320px

          Result of bevel (one segment).

     - .. figure:: /images/modeling_meshes_editing_edge_bevel_example-3.png
          :width: 320px

          Result of bevel (vertex only).

.. note::

   Normal (edge) beveling only works on edges that have exactly two faces
   attached to them. Vertex beveling has no such restriction.


Options
=======

Affect :kbd:`V`
   Vertices
      Only the areas near vertices are beveled, the edges remain unchanged.
   Edges
      Bevel the edges, creating intersections at vertices.

Width Type :kbd:`M`
   Selects how the *Width* value controls the size of the bevel. According to the selection, the width is:

   Offset
      The distance from the new edge to the original.
   Width
      The distance between the two new edges formed by the bevel
      (or the edges on either side of the bevel if there is more than one segment).
   Percent
      The percentage of the length of adjacent edges that the new edges slide.
   Absolute
      The exact distance along edges adjacent to the beveled edge. A difference from **Offset** is visible
      when the unbeveled edges attached to beveled edges meet at an angle besides a right angle.

   For vertex-only bevels, the Offset and Depth types measure from the original vertex.
   The Width type is measured from a new vertex to the center of the new face (as half the *Width*).

Width :kbd:`A`
   You can change the bevel width by moving the mouse towards and away from the object,
   a bit like with transform tools.
   The exact meaning of the value depends on the *Width Type* option (see above).
   As usual, the scaling can be controlled to a finer degree by holding :kbd:`Shift` to scale in 0.001 steps.
   :kbd:`LMB` finalizes the operation, :kbd:`RMB` or :kbd:`Esc` aborts the action.

   .. note::

      When multiple edges are beveled at the same time,
      it is sometimes impossible to make the width match the above definition on all edges simultaneously.
      Bevel tries to compromise in such cases.
      Sometimes turning off Loop Slide (see below) can make it easier for Bevel to make the widths as specified.

Segments :kbd:`S`
   The number of segments in the bevel can be defined by
   scrolling the mouse :kbd:`Wheel` to increase or decrease this value.
   The greater the number of segments, the smoother the bevel.
   Or press :kbd:`S` to change the number with mouse movements, as well as numeric input.

   Alternatively, you can manually enter a segment number value while using the tool,
   or in the Mesh Tool options panel after using the tool.

   .. figure:: /images/modeling_meshes_editing_edge_bevel_example-4.png
      :width: 320px

      Bevel with four segments.

Shape :kbd:`P`
   This is a number between 0 and 1 that controls the shape of the profile (side view of a beveled edge).
   The default value, 0.5, gives a circular arc (if the faces meet at right angles).
   Values less than that give a flatter profile, with 0.25 being exactly flat,
   and values less than that giving a concave bevel. Values more than 0.5 give a more convex profile.
   Similarly as *Segments* it can be set with mouse movements and numeric input after toggling :kbd:`P`.

Material Index
   The *Material* number specifies which material is assigned to the new faces created by the *Bevel* tool.
   With the default, -1, the material is inherited from the closest existing face ("closest" can be a bit ambiguous).
   Otherwise, the number is the slot index of the material to use for all newly created faces.

Harden Normals :kbd:`H`
   When enabled, the per-vertex face normals of the bevel faces are adjusted to
   match the surrounding faces, and the normals of the surrounding faces are not affected.
   This will keep the surrounding faces flat (if they were before),
   with the bevel faces shading smoothly into them. For this effect to work,
   custom split normals need to be enabled, which requires Auto Smooth to be enabled
   (see :doc:`Normals </modeling/meshes/editing/mesh/normals>`).
   As a convenience, that option will be enabled for you if it is not already when you enable Harden Normals here.

Clamp Overlap :kbd:`C`
   Limits the width of each beveled edge so that edges cannot cause
   overlapping intersections with other geometry.

Loop Slide
   If there are un-beveled edges along with beveled edges into a vertex,
   the bevel tries to slide along those edges when possible.
   Turning the option off can lead to more even bevel widths.

Mark
   Seams :kbd:`U`
      If a seam edge crosses a non-seam one and you bevel all of them,
      this option will maintain the expected propagation of seams.
   Sharp :kbd:`K`
      Similar to Mark Seams, but for sharp edges.

Miter Outer :kbd:`O`
   A *miter* is formed when two beveled edges meet at an angle.
   On the side where the angle is greater than 180 degrees, if any, it is called an *outer miter*.
   This option specifies the pattern that Blender uses at an outer miter.

   Sharp
      Edges meet at a sharp point, with no extra vertices introduced on the edges.
   Patch
      Edges meet at a sharp point but in addition, two extra vertices are introduced near the point
      so that the edges and faces at the vertex may be less pinched together than
      what occurs in the *Sharp* case.
      The *Spread* slider controls how far the new vertices are from the intersection.
   Arc
      Two vertices are introduced near the intersection, and a curved arc joins them together.
      The *Spread* slider controls how far the new vertices are from the intersection.
      The *Profile* slider controls the shape of the arc.

   The current choices are shown in this diagram, where the outer miter is along the horizontal surface.

   .. list-table::

      * - .. figure:: /images/modeling_meshes_editing_edge_bevel_miter-2.png
             :width: 320px

             Sharp outer miter.

        - .. figure:: /images/modeling_meshes_editing_edge_bevel_miter-3.png
             :width: 320px

             Patch outer miter.

        - .. figure:: /images/modeling_meshes_editing_edge_bevel_miter-4.png
             :width: 320px

             Arc outer miter.

Inner :kbd:`I`
   An *Inner Miter* is formed when the angle between two beveled edges is less than 180 degrees.
   This option specifies the pattern Blender uses at an inner miter.
   The options are the same as for Outer Miter, except that *Patch* makes no sense and is therefore omitted.
   Inner miters are shown in the following diagram, where two inner miters are on the vertical surfaces.

   .. list-table::

      * - .. figure:: /images/modeling_meshes_editing_edge_bevel_miter-5.png
             :width: 200px

             Sharp inner miter.

        - .. figure:: /images/modeling_meshes_editing_edge_bevel_miter-6.png
             :width: 200px

             Arc inner miter.

Spread
   The value used to spread extra vertices apart for *Outer* and *Inner Miters*.

Intersection Type :kbd:`N`
   When more than two beveled edges meet at a vertex, a mesh is created as
   a way to complete the intersection between the generated geometry.
   This option controls the method used to create that mesh.

   Grid Fill
      The default method for building intersections, useful when a smooth continuation of
      the bevel profile is desired. Without *Custom Profile* enabled, the curve of the profile
      continues through the intersection, but with a custom profile it just creates a smooth grid within
      the intersection's boundary.
   Cutoff
      Creates a cutoff face at the end of each beveled edge coming into the vertex. This is most
      useful for custom profiles when the new intersection is too complex for a smooth grid fill.

      With a three way intersection, when the inner corners of the cutoff profiles faces meet at
      the same location, no center face is created.

      The direction of the cutoff faces depends on the original vertex's normal.

   .. list-table:: Intersection method options.

      * - .. figure:: /images/modeling_meshes_editing_edge_bevel_vmesh-1.png
             :width: 200px

             Grid fill intersection method.

        - .. figure:: /images/modeling_meshes_editing_edge_bevel_vmesh-2.png
             :width: 200px

             Three way cutoff intersection where the inner vertices are merged.

        - .. figure:: /images/modeling_meshes_editing_edge_bevel_vmesh-3.png
             :width: 200px

             Cutoff intersection method with a center face.

Face Strength
   Set *Face Strength* on the faces involved in the bevel, according to the specified mode.
   This can be used in conjunction with
   a :doc:`Weight Normals Modifier </modeling/modifiers/modify/weighted_normal>`
   (with the *Face Influence* option checked).

   None
      Do not set face strength.
   New
      Set the face strength of new faces along edges to *Medium*,
      and the face strength of new faces at vertices to *Weak*.
   Affected
      In addition to those set for the *New* case,
      also set the faces adjacent to new faces to have strength *Strong*.
   All
      In addition to those set for the *Affected* option,
      also set all the rest of the faces of the model to have strength *Strong*.

Profile Type :kbd:`Z`
   Superellipse
      Creates a bevel with a uniform concave or convex curve.

   Custom
      .. figure:: /images/modeling_modifiers_generate_bevel_profile-widget.png
         :align: right
         :width: 300px

         The custom profile widget.

      This widget allows the creation of a user-defined profile with more complexity than
      with the single profile parameter. The modal tool allows toggling the custom profile,
      but the shape of the profile is only editable in the options panel after the operation is confirmed.

      The profile starts at the bottom right of the widget and ends at the top left, as if it
      were between two edges intersecting at a right angle. Control points are created in the widget and
      then the path is sampled with the number of segments from the Bevel modifier.

      .. note::

         The *Profile* slider stays active when miters are enabled
         because it still controls the shape of the miter profiles.

      Presets
         The *Support Loops* and *Steps* presets are built dynamically depending on
         the number of segments in the bevel. If the number of segments is changed,
         the preset will have to be re-applied.

      Sampling
         Samples will first be added to each control point, then if there are enough samples,
         they will be divided evenly between the edges. The *Sample Straight Edges* option toggles whether
         the samples are added to edges with sharp control points on either side. If there aren't enough samples
         to give each edge the same number of samples, they will just be added to the most curved edges.
         So it is recommended to use at least as many segments as there are control points.


Examples
========

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_edge_bevel_example-5.png
          :width: 320px

          Result of beveling multiple edges.

     - .. figure:: /images/modeling_meshes_editing_edge_bevel_example-6.png
          :width: 320px

          Another example of beveling multiple edges.

     - .. figure:: /images/modeling_meshes_editing_edge_bevel_example-7.png
          :width: 320px

          An example using Profile=0.150.

.. seealso:: Bevel Modifier

   The :doc:`Bevel Modifier </modeling/modifiers/generate/bevel>`
   is a non-destructive alternative to the Bevel tool.
