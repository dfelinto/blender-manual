
..    TODO/Review: {{review|im=normals, quads to tris}} .


Face Tools
**********

These are tools that manipulate faces.

Creating Faces
**************

Make Edge/Face
==============

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`Mesh --> Faces --> Make Edge/Face`
   | Hotkey:   :kbd:`F`


This will create an edge or some faces, depending on your selection. It is detailed in the :doc:`Basic Editing page </modeling/meshes/editing/basics#edge_and_face_creation>`.


Fill

----


.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`Mesh --> Faces --> Fill/Beautify Fill`
   | Hotkey:   :kbd:`alt-F`


The :guilabel:`Fill` option will create *triangular* faces from any group of selected edges
or vertices, *as long as they form one or more complete perimeters*.


.. figure:: /images/Fill1.jpg
   :width: 200px
   :figwidth: 200px

   A closed perimeter of edges


.. figure:: /images/Fill2.jpg
   :width: 200px
   :figwidth: 200px

   Filled using shortcut [F]. Created an n-gon


.. figure:: /images/Fill3.jpg
   :width: 200px
   :figwidth: 200px

   Filled using fill[Alt][F]


note, unlike creating n-gons, fill supports holes.


.. figure:: /images/Fill1_holes.jpg
   :width: 200px
   :figwidth: 200px

   A closed perimeter of edges with holes


.. figure:: /images/Fill2_holes.jpg
   :width: 200px
   :figwidth: 200px

   Filled using fill[Alt][F]


Beauty Fill
===========

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`Mesh --> Faces --> Fill/Beautify Fill`
   | Hotkey:   :kbd:`Alt-Shift-F`


:guilabel:`Beautify Fill` works only on selected existing faces. It rearrange selected triangles to obtain more "balanced" ones (i.e. less long thin triangles).


.. figure:: /images/mesh_beauty_fill_before.jpg
   :width: 200px
   :figwidth: 200px

   Text converted to a mesh


.. figure:: /images/mesh_beauty_fill_after.jpg
   :width: 200px
   :figwidth: 200px

   Result of Beauty Fill, :kbd:`Alt-Shift-F`


Grid Fill
=========

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`Mesh --> Faces --> Fill/Grid Fill`


:guilabel:`Grid Fill` uses a pair of connected edge-loops to fill in a grid that follows the surrounding geometry.


.. figure:: /images/mesh_fill_grid_simple_before.jpg
   :width: 200px
   :figwidth: 200px

   Input


.. figure:: /images/mesh_fill_grid_simple_after.jpg
   :width: 200px
   :figwidth: 200px

   Grid fill result


.. figure:: /images/mesh_fill_grid_surface_before.jpg
   :width: 200px
   :figwidth: 200px

   Input


.. figure:: /images/mesh_fill_grid_surface_after.jpg
   :width: 200px
   :figwidth: 200px

   Grid fill result


Convert Quads to Triangles
==========================

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`Mesh --> Faces --> Convert Quads to Triangles` or :menuselection:`Face Specials --> Triangulate`
   | Hotkey:   :kbd:`ctrl-T`


As its name intimates, this tool converts each selected quadrangle into two triangles.
Remember that quads are just a set of two triangles.


Convert Triangles to Quads
==========================

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Panel:    :guilabel:`Mesh Tools` (:guilabel:`Editing` context)
   | Menu:     :menuselection:`Mesh --> Faces --> Convert Triangles to Quads`
   | Hotkey:   :kbd:`alt-J`


This tool converts the selected triangles into quads by taking adjacent tris and removes the
shared edge to create a quad, based on a threshold.
This tool can be performed on a selection of multiple triangles.

This same action can be done on a selection of 2 tris,
by selecting them and using the shortcut :kbd:`F`, to create a face, or by selecting the
shared edge and dissolving it with the shortcut :menuselection:`[X] --> Dissolve`.

To create a quad, this tool needs at least two adjacent triangles.
If you have an even number of selected triangles,
it is also possible not to obtain only quads. In fact,
this tool tries to create "squarishest" quads as possible from the given triangles,
which means some triangles could remain.


.. figure:: /images/Fill5.jpg
   :width: 200px
   :figwidth: 200px

   Before converting tris to quads


.. figure:: /images/QuadToTris.jpg
   :width: 200px
   :figwidth: 200px

   After converting tris to quads, with a max angle of 30


All the menu entries and hotkey use the settings defined in the :guilabel:`Mesh Tools` panel:

Max Angle
   This values (between **0** and **180**) controls the threshold for this tool to work on adjacent triangles. With a threshold of **0.0**, it will only join adjacent triangles that form a perfect rectangle (i.e. right-angled triangles sharing their hypotenuses). Larger values are required for triangles with a shared edge that is small, relative to the size of the other edges of the triangles.

Compare UVs
   When enabled, it will prevent union of triangles that are not also adjacent in the active UV map. Note that this seems to be the only option working...
Compare Vcol
   When enabled, it will prevent union of triangles that have no matching vertex color. I'm not sure how this option works - or even if it really works...
Compare Sharp
   When enabled, it will prevent union of triangles that share a "sharp" edge. I'm not sure either if this option works, and what is the "sharp" criteria - neither the :guilabel:`Sharp` flag nor the angle between triangles seem to have an influence here...
Compare Materials
   When enabled, it will prevent union of triangles that do not use the same material index. This option does not seem to work neither...


Solidify
********

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`Mesh --> Faces --> Solidify`
   | Hotkey:   :menuselection:`[ctrl][F] --> Solidify`


This takes a selection of faces and solidifies them by extruding them uniformly to give volume to a non-manifold surface. This is also available as a :doc:`Modifier </modifiers/generate/solidify>`. After using the tool, you can set the offset distance in the Tool Palette.

Thickness
   Amount to offset the newly created surface. Positive values offset the surface inward relative to the normals. Negative values offset outward.


.. figure:: /images/Doc26-solidify-before.jpg
   :width: 200px
   :figwidth: 200px

   Mesh before solidify operation


.. figure:: /images/Doc26-solidify-after.jpg
   :width: 200px
   :figwidth: 200px

   Solidify with a positive thickness


.. figure:: /images/Doc26-solidify-after2.jpg
   :width: 200px
   :figwidth: 200px

   Solidify with a negative thickness


Rotate Edges
************

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`Mesh --> Faces --> Rotate Edge CW`


This command functions the same edge rotation in edge mode.

It works on the shared edge between two faces and rotates that edge if the edge was selected.


.. figure:: /images/RotateEdgeFaceMode1.jpg
   :width: 300px
   :figwidth: 300px

   Two faces selected


.. figure:: /images/RotateEdgeFaceMode2.jpg
   :width: 300px
   :figwidth: 300px

   After rotating edge


See :doc:`Rotate Edge CW / Rotate Edge CCW </modeling/meshes/editing/edges#rotate_edge_cw_/_rotate_edge_ccw>` for more information.


Normals
*******

As normals are mainly a face "sub-product", we describe their few options here also.

See :doc:`Smoothing </modeling/meshes/smoothing>` for additional information on working with face normals.


Flip Direction
==============

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`Mesh --> Normals --> Flip` or :menuselection:`Specials --> Flip Normals`
   | Hotkey:   :menuselection:`[W] --> Flip Normals` }


Well, it will just reverse the normals direction of all selected faces.
Note that this allows you to precisely control the direction (**not the orientation**,
which is always perpendicular to the face) of your normals, as only selected ones are flipped.


Recalculate Normals
===================

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`Mesh --> Normals --> Recalculate Outside` and :menuselection:`Mesh --> Normals --> RecalculateInside`
   | Hotkey:   :kbd:`ctrl-N` and :guilabel:`ctrl`


These commands will recalculate the normals of selected faces so that they point outside
(respectively inside) the volume that the face belongs to.
This volume do not need to be closed. In fact, this means that the face of interest must be
adjacent with at least one non-coplanar other face. For example,
with a :guilabel:`Grid` primitive, neither :guilabel:`Recalculate Outside` nor
:guilabel:`Recalculate Inside` will never modify its normals...


