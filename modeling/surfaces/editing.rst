
..    TODO/Review: {{review|split=X|text=split selection and editing}} .


Surface Selection
=================

Surface selection in :guilabel:`Edit` mode is very similar to :doc:`NURBS curve selection <modeling/curves/editing>`. The basic tools are the same as with :doc:`meshes <modeling/meshes/selecting>`, so you can select a simple control point with a :kbd:`lmb` -click, add to current selection with :kbd:`shift-lmb` -clicks, :kbd:`B` order-select, and so on.

:kbd:`L` (or :kbd:`ctrl-L`) will add to the selection the mouse cursor's nearest control point, and all the linked ones, i.e. all points belonging to the same surface.


Select Menu
===========

The :guilabel:`Select` menu (3D view headers) is even simpler than for curves…

   All these options have the same meaning and behavior as in :doc:`Object mode <modeling/objects/selecting>` (and the specificities of :guilabel:`Border Select` in :guilabel:`Edit` mode have already been discussed :doc:`here <modeling/meshes/selecting>`).


.. figure:: /images/NurbsSelectMenu.jpg

   frame[left].


Every Nth
---------

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`Select --> Every Nth`
   | Hotkey:   None


This is the same option as for :doc:`curve selection <modeling/curves/editing#every_nth>`. However, the behavior of the :guilabel:`N` ("selection step") parameter in the 2D of a NURBS surface "cage" seems quite difficult to understand…


Control Point Row
-----------------

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`Select --> Control Point Row`
   | Hotkey:   :kbd:`shift-R`


This option works a bit like :doc:`edge loop selection <modeling/meshes/selecting#edge_loop_selection>` for meshes, inasmuch it selects a whole :doc:`row <modeling/surfaces#control_points,_rows_and_grid>` of control points, based on the active (the last selected) one. The first time you hit :kbd:`shift-R`, the V-row passing through (containing) the active point will be *added to the current selection*. If you use again this shortcut, you will toggle between the U- and V-row of this point, *removing everything else from the selection*.


More and Less
-------------

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`Select --> More/Less`
   | Hotkey:   :kbd:`ctrl-pad+` / :kbd:`ctrl-pad-`


These two options are complementary and very similar to :doc:`those for meshes <modeling/meshes/selecting>`. Their purpose, based on current selected control points, is to reduce or enlarge this selection.

The algorithm is the same as with meshes:

- :guilabel:`More`: for each selected control point, select **all** its linked points (i.e. two, three or four).
- :guilabel:`Less`: for each selected control point, if **all** points linked to this point are selected, keep it selected. For all other selected control points, de-select them.

This implies two points:

- First, when **all** control points of a surface are selected, nothing will happen (as for :guilabel:`Less`, all linked points are always selected, and of course, :guilabel:`More` can't add any). Conversely, the same goes when no control point is selected.
- Second, these tools will never "go outside" of a surface (they will never "jump" to another surface in the same object).


Surface Editing
===============

Surface editing has even fewer tools and options than its curve counterpart - and has many
common points with it… So this page covers (or tries to cover) all the subjects,
from the basics of surface editing to more advanced topics, like retopology.


Basic Surface Editing (translation, rotation, scale)
----------------------------------------------------

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`Surface --> Transform --> Grab/Move, Rotate, Scale, …`
   | Hotkey:   :kbd:`G` / :kbd:`R` / :kbd:`S`


Once you have a selection of one or more control points, you can grab/move (:kbd:`G`), rotate (:kbd:`R`) or scale (:kbd:`S`) them, like many other things in Blender, as described in the :doc:`Manipulation in 3D Space <3d_interaction/transformations/basics>` section.

You also have in :guilabel:`Edit` mode an extra option when using these basic manipulations: the :doc:`proportional editing <3d_interaction/transform_control/proportional_edit>`.


Advanced Transform Tools
------------------------

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`Surface --> Transform`


The :guilabel:`To Sphere`, :guilabel:`Shear`, :guilabel:`Wrap` and :guilabel:`Push/Pull` transform tools are described in the :doc:`Mesh Editing <modeling/meshes/tools#advanced_transform_tools>` chapter. Surfaces have no specific transform tools.


NURBS Control Points Settings
-----------------------------

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Panel:    :guilabel:`Curve Tools` (:guilabel:`Editing` context, :kbd:`F9`), and :guilabel:`Transform Properties`


We saw in a :doc:`previous page <modeling/surfaces#weight>` that NURBS control points have a weight, which is the influence of this point on the surface. You set it either using the big :guilabel:`Set Weight` button in the :guilabel:`Curve Tools` panel (after having defined the weight in the numeric field to the right), or by directly typing a value in the :guilabel:`W` numeric field of the :guilabel:`Transform Properties` panel.


Adding or Extruding
-------------------

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`Surface --> Extrude`
   | Hotkey:   :kbd:`E` (or :kbd:`ctrl-lmb`)


Unlike meshes or curves, you cannot generally directly add new control points to a surface (with :kbd:`ctrl-lmb` clicks), as you can only extend a surface by adding a whole U- or V-row at once. The only exception is when working on a NURBS surface curve, i.e. a surface with only one control point on each U- or V-row. In this special case, all works exactly as with :doc:`curves <modeling/curves/editing#adding_new_segments>`.

Most of the time, only extrusion is available. As usual, once the tool is activated the
extrusion happens immediately and you are placed into :guilabel:`Grab mode`,
ready to drag the new extruded surface to its destination.

There are two things very important to understand:

- Surfaces are **2D** objects - so you can't extrude anything *inside* a surface (e.g. "inner" row); it wouldn't make any sense!
- The control "grid" *must remain "squarish"*, which means that you can only extrude a whole row, not parts of rows here and there…

To summarize, the :guilabel:`Extrude` tool will only work when one and only one whole border
row is selected - otherwise nothing happens.

As for curves, you cannot create a new surface in your object out of nowhere, by just :kbd:`ctrl-lmb` -clicking with nothing selected. However, unlike for curves, there is no "cut" option allowing you to separate a surface into several parts, so you only can create a new surface by
FIXME(TODO: Internal Link;
[[#Duplication|copying]]
) an existing one (:kbd:`shift-D`), or adding a new one (:guilabel:`Add` menu…).


Examples
~~~~~~~~

Images (*Selecting control-point*) to (*Complete*)
show a typical extrusion along the side of a surface.

In (*Selecting control-point*) and (:kbd:`shift-R`),
a border row of control points were highlighted by selecting a single control point,
labeled "\ ``C`` ", and then using the handy row select tool (:kbd:`shift-R`)
to select the rest of the control points.


+----------------------------------------------+
+.. figure:: /images/NurbsSurfaceSelectEdge.jpg+
+   :width: 500px                              +
+   :figwidth: 500px                           +
+----------------------------------------------+


The edge is then extruded using :kbd:`E` as shown in (*Extruding*).
Notice how the mesh has bunched up next to the highlighted edge;
the area in question is highlighted in a light-gray circular area.
That is because the *new* extruded surface section is bunched up there as well.


+------------------------------------+
+.. figure:: /images/NurbsExtrude.jpg+
+   :width: 500px                    +
+   :figwidth: 500px                 +
+------------------------------------+


By moving the new section away from the area, the surface begins to "unbunch".
The direction of movement is marked with a white arrow, labeled "\ ``E`` ",
and the new section is labeled "\ ``S`` ".

You can continue this process of extruding - or adding - new surface sections until you have
reached the final shape for your model.


Opening or Closing a Surface
----------------------------

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`Surface --> Toggle Cyclic`
   | Hotkey:   :kbd:`C`


As in :doc:`curves <modeling/curves/editing#opening_and_closing_a_curve>`, surfaces can be closed (cyclic) or open. However, as surfaces are 2D, you can control this property independently along the U and V axes.

To toggle the cyclic property of a surface along one axis, use :kbd:`C` and choose either :guilabel:`cyclic U` or :guilabel:`cyclic V` from the :doc:`Toggle pop-up menu <modeling/surfaces>`. The corresponding surface's outer edges will join together to form a "closed" surface.


.. admonition:: Inner and Outer
   :class: note

   Surfaces have an "inner" and "outer" face, the first being black whereas the latter is correctly shaded - there does not seem to be any "double sided" shading option for surfaces…). When you close a surface in one or two directions, you might get an entirely black object! In this case, just
   FIXME(TODO: Internal Link;
   [[#Switch Direction|switch the "direction"]]
   ) of your surface…


Duplication
-----------

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`Curve --> Duplicate`
   | Hotkey:   :kbd:`shift-D`


Well, as with meshes and curves, this command just duplicates the selection. As usual,
the copy is selected and placed in :guilabel:`Grab` mode, so you can move it to another place.

However, with surfaces there are some selections that can't be duplicated,
in which case they will just be placed in :guilabel:`Grab` mode… In fact,
only selections forming *a single valid sub-grid* are copyable; let's see this in practice:

- You can copy a single control point. From it, you will be able to "extrude" a "surface curve" along the U axis, and then extrude this unique U-row along the V axis to create a real new surface.
- You can copy a single continuous part of a row (or a whole row, of course). This will give you a new **U-row**, even if you selected (part of) a V-row!
- You can copy a single whole sub-grid.

Note that trying to duplicate several valid "sub-grids" (even being single points)
at once won't work; you'll have to do it one after the other…


Deleting Elements
-----------------

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`Curve --> Delete...`
   | Hotkey:   :kbd:`X` or :kbd:`Del`


The :guilabel:`Erase` pop-up menu of surfaces offers you two options:

:guilabel:`Selected`
   This will delete the selected rows, *without* breaking the surface (i.e. the adjacent rows will be directly linked, joined, once the intermediary ones are deleted). The selection must abide by the following rules:

   - Whole rows, and only whole rows must be selected.
   - Only rows along the same axis must be selected (i.e. you can't delete both U- and V-rows at the same time).

   Also remember that NURBS order cannot be higher than its number of control points in a given axis, so it might decrease when you delete some control points… Of course, when only one row remains, the surface becomes a "surface curve"; when only one point remains, there is no more visible surface; and when all points are deleted, the surface itself is deleted.

:guilabel:`All`
   As with meshes or curves, this deletes everything in the object!


Example
~~~~~~~

+---------------------------------------------+
+.. figure:: /images/NurbsDeletingSegments.jpg+
+   :width: 600px                             +
+   :figwidth: 600px                          +
+                                             +
+   Before and after                          +
+---------------------------------------------+


In (*Before*) a row of control points has been selected by initially selecting the control point labeled "\ ``A`` " and using :kbd:`shift-R` to select the remaining control points. Then, using the :doc:`Erase menu <ce/menus/erase#edit_mode>` (:kbd:`X`), the *selected* row of control points is erased, resulting in (*After*).


Joining or Merging Surfaces
---------------------------

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`Surface --> Make Segment`
   | Hotkey:   :kbd:`F`


Just like :doc:`curves <modeling/curves/editing#joining_or_merging_curves>`, merging two surfaces requires that a single edge, a border row of control points, from two separate surfaces are selected. This means that the surfaces must be part of the same object. For example, you can't join two surfaces while in :guilabel:`Object` mode - but you can of course, as with any objects of the same type,
FIXME(TODO: Internal Link;
[[#Joining Objects|join two or more {{Literal|Surface}} objects]]
) into one object (:kbd:`ctrl-J`) - they just won't be "linked" or merged in a single one… Yes, it's a bit confusing!

This command is equivalent to creating edges or :kbd:`F` aces for meshes
(hence its shortcut), and so it only works in :guilabel:`Edit` mode.
The selection must contains only border rows of the same resolution
(with the same number of control points),
else Blender will try to do its best to guess what to merge with what, or the merge will fail
(either silently, or stating that "\ ``Resolution doesn't match`` " if rows with
different number of points are selected, or that there is "\ ``Too few selections to
merge`` " if you only selected points in one surface…).

So to avoid problems, you should always only select border rows with the same number of
points… Note that you can join a border U-row of one surface with a border V-row of another
one, Blender will automatically "invert" the axis of one surface for them to match correctly.

NURBS surface curves are often used to create objects like hulls, as they define cross sections all along the object, and you just have to "skin" them as described above to get a nice, smooth and harmonious shape. See :doc:`this tutorial <ls/modeling/surfaces/skinning>` for a detailed workflow.


Examples
~~~~~~~~

(*Joining ready*) is an example of two NURBS surface curves, **not** NURBS curves, in :guilabel:`Edit` mode, ready to be joined. (*Joining complete*) is the result of joining the two curves.


+---------------------------------+
+.. figure:: /images/NurbsJoin.jpg+
+   :width: 350px                 +
+   :figwidth: 350px              +
+                                 +
+   Joining ready.                +
+---------------------------------+


Subdivision
-----------

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Panel:    :guilabel:`Curve Tools1` (:guilabel:`Editing` context, :kbd:`F9`)
   | Menu:     :menuselection:`Surface --> Segments --> Subdivide`, :menuselection:`Specials --> Subdivide`
   | Hotkey:   :menuselection:`[W] --> [pad1]`


Surface subdivision is most simple:
using either the :guilabel:`Subdivide` entry in the :guilabel:`Specials` menu
(:kbd:`W`), or the :guilabel:`Subdivide` button of the :guilabel:`Curve Tools1` panel,
you will subdivide once all *completely selected grids* by subdividing each "quad" into four
smaller ones.

If you apply it to a 1D surface (a "surface curve"), this tool works exactly as with :doc:`curves <modeling/curves/editing#subdivision>`.


Spin

----


.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Panel:    :guilabel:`Curve Tools1` (:guilabel:`Editing` context, :kbd:`F9`)


This tool is a bit similar to its :doc:`mesh counterpart <modeling/meshes/tools#spin>` - but with less control and options (in fact, there's none!).

It only works on selected "surfaces" made of *one U-row* (and not with one V-row),
so-called "surface curves", by "extruding" this "cross section" in a square pattern,
automatically adjusting the weights of control points to get a perfect circular extrusion
(this also implies closing the surface along the V axis), following exactly the same principle
as for the :guilabel:`NURBS Tube` or :guilabel:`NURBS Donut` primitives.


Switch Direction
----------------

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`Surface --> Segments --> Switch Direction`, :menuselection:`Specials --> Switch Direction`
   | Hotkey:   :menuselection:`[W] --> [pad2]`


This command will "reverse" the direction of any curve with at least one selected element (i.
e. the start point will become the end one, and *vice versa*).
Mainly useful when using a curve as path, or the bevel and taper options…


Other Specials Options
----------------------

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :guilabel:`Specials`
   | Hotkey:   :kbd:`W`


The :guilabel:`Specials` menu contains exactly the same additional options as for :doc:`curves <modeling/curves/editing#other_specials_options>` - but I suppose :guilabel:`Set Radius` and :guilabel:`Smooth Radius` have nothing to do here…


Conversion
----------

As there are only NURBS surfaces, there is no "internal" conversion here.

However, there is an "external" conversion available, from surface to mesh,
that only works in :guilabel:`Object` mode.
It transforms a :guilabel:`Surface` object into a :guilabel:`Mesh` one,
using the surface resolutions in both directions to create faces, edges and vertices.


Retopology
----------

Snapping surface components is the same as is with meshes and curves. See :doc:`Retopology <modeling/meshes/editing/retopo>` for more information.


Misc Editing
------------

You have some of the same options as with meshes, or in :guilabel:`Object` mode. You can :doc:`separate <modeling/objects/groups_and_parenting#separating_objects>` a given surface (:kbd:`P`), make other selected objects :doc:`children <modeling/objects/groups_and_parenting#parenting_objects>` of one or three control points (:kbd:`ctrl-P` - note however that parenting to three control points has a strange behavior with curves…), or :doc:`add hooks <modifiers/deform/hooks>` to control some points with other objects.

The :guilabel:`Mirror` tool is also available, behaving exactly as with :doc:`mesh vertices <modeling/meshes/tools#mirror>`.


