
Curve Editing
=============

This page covers the basics of curve editing. Curve basics,
selecting and advanced editing are covered in the following pages:


- :doc:`Curve basics <modeling/curves>`
- :doc:`Curve Selecting <modeling/curves/selecting>`
- :doc:`Advanced Curve Editing <modeling/curves/editing/advanced>`


Curve Display
-------------

Display Options
~~~~~~~~~~~~~~~

.. figure:: /images/Editing_Curves_curve-display-panel.jpg

   Curve Display panel


When in Edit mode, the Properties Shelf (:kbd:`N`) contains options in the
:guilabel:`Curve Display` panel for how curves are displayed in the 3D viewport.

:guilabel:`Handles`
   Toggles the display of Bezier handles while in edit mode. This does not affect the appearance of the curve itself.
:guilabel:`Normals`
   Toggles the display of Curve Normals.
:guilabel:`Normal Size`
   Sets the display scale of curve normals.


Hiding Elements
~~~~~~~~~~~~~~~

When in :guilabel:`Edit` mode, you can hide and reveal elements from the display.
This can be useful in complex models with many elements on the Screen.

:guilabel:`Hide Selected elements`
   Use :kbd:`H`, or the :menuselection:`Curve --> Show/Hide --> Hide Selected` menu option from the 3D window header.

:guilabel:`Show Hidden elements`
   Use :kbd:`alt-H`, or the :menuselection:`Curve --> Show/Hide --> Show Hidden` menu option from the 3D window header.

:guilabel:`Hide Unselected elements`
   Use :kbd:`shift-H`, or the :menuselection:`Curve --> Show/Hide --> Hide Unselected` menu option from the 3D window header.


----


Basic Curve Editing (translation, rotation, scale)
--------------------------------------------------

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`Curve --> Transform --> Grab/Move, Rotate, Scale, ...`
   | Hotkey:   :kbd:`G` / :kbd:`R` / :kbd:`S`


Like other elements in Blender, Curve control points can be grabbed/moved (:kbd:`G`), rotated (:kbd:`R`) or scaled (:kbd:`S`) as described in the :doc:`Basic Transformations <3d_interaction/transformations/basics>` section. When in :guilabel:`Edit` mode, :doc:`proportional editing <3d_interaction/transform_control/proportional_edit>` is also available for transformation actions.


Snapping
--------

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Panel:    :guilabel:`Curve Tools` (:guilabel:`Editing` context)


:doc:`Mesh snapping <modeling/meshes/snapping>` also works with curve components. Both control points and their handles will be affected by snapping, except for within itself (other components of the active curve). Snapping works with 2D curves but points will be constrained to the local XY axes.


Deforming Tools
---------------

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`Curve --> Transform`


The :guilabel:`To Sphere`, :guilabel:`Shear`, :guilabel:`Wrap` and :guilabel:`Push/Pull` transform tools are described in the :doc:`Transformations <3d_interaction/transformations>` sections. The two other tools, :guilabel:`Tilt` and :guilabel:`Shrink/Fatten Radius` are related to :doc:`Curve Extrusion <modeling/curves/editing/advanced>`.


Smoothing
~~~~~~~~~

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Hotkey:   :menuselection:`[W][] --> smooth`


Curve smoothing is available through the specials menu. For Bézier curves, this smoothing
operation currently only smooths the positions of control points and not their tangents.
End points are also constrained when smoothing.


Mirror
------

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`Curve --> Mirror`
   | Hotkey:   :kbd:`ctrl-M`


The :guilabel:`Mirror` tool is also available, behaving exactly as with :doc:`mesh vertices <modeling/meshes/editing/deforming/mirror>`,


----


Set Bézier Handle Type
----------------------

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Panel:    :menuselection:`Curve Tools --> Handles`
   | Menu:     :menuselection:`Curve --> Control Points --> Set Handle Type`
   | Hotkey:   :kbd:`V`


Handle types are a property of :doc:`Bézier curves. <modeling/curves>` and can be used to alter features of the curve. For example, switching to :guilabel:`Vector handles` can be used to create curves with sharp corners. Read the :doc:`Bézier curves <modeling/curves>` page for more details.


Extending Curves
----------------

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`Curve --> Extrude`
   | Hotkey:   :kbd:`ctrl-lmb` or :kbd:`E`


Once a curve is created you can add new segments (in fact,
new control points defining new segments), either by extruding,
or placing new handles with :kbd:`ctrl-lmb` clicks.
Each new segment is added to one end of the curve.
A new segment will only be added if a single vertex, or handle,
at one end of the curve is selected. If two or more control points are selected,
a new Bézier closed curve is started.

Unlike mesh editing, you cannot create a new curve inside the edited object by :kbd:`ctrl-lmb` -clicking without any control points selected. to do so, you can cut an existing curve in two parts (by
FIXME(TODO: Internal Link;
[[#Deleting Elements|deleting a segment]]
)),
FIXME(TODO: Internal Link;
[[#Duplication|copying]]
) an existing one (:kbd:`shift-D`), or add a new one through the menu.


Subdivision
-----------

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Panel:    :guilabel:`Curve Tools` (:guilabel:`Editing` context)
   | Menu:     :menuselection:`Curve --> Segments --> Subdivide`
   | Hotkey:   :kbd:`w`


Curve subdivision simply subdivides all selected segments by adding one or more control points
between the selected segments. To control the number of cuts,
press :kbd:`W` to make a single subdivision.
Then press :kbd:`F6` to bring up the :guilabel:`Number of Cuts` menu.


Duplication
-----------

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`Curve --> Duplicate`
   | Hotkey:   :kbd:`shift-D`


This command duplicates the selected control points,
along with the curve segments implicitly selected (if any).
The copy is selected and placed in :guilabel:`Grab` mode, so you can move it to another place.


Joining Curve Segments
----------------------

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`Curve --> Make Segment`
   | Hotkey:   :kbd:`F`


Two open curves can be combined into one by creating a segment between the two curves.
To join two separated curves,
select one end control point from each curve then press :kbd:`F`.
The two curves are joined by a segment to become a single curve.


.. figure:: /images/Editing_Curves_two-curves-joined.jpg
   :width: 600px
   :figwidth: 600px

   Curves before and after joining


Additionally, you can close a curve by joining the endpoints but note that you can only join
curves of the same type (i.e. Bézier with Bézier, NURBS with NURBS)


Separating Curves
-----------------

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`Curve --> Separate`
   | Hotkey:   :kbd:`P`


Curve objects that are made of multiple distinct curves can be separated into their own
objects by selecting the desired segments and pressing :kbd:`P`. Note,
if there is only one curve in a Curve object,
pressing :kbd:`P` will create a new Curve object with no control points.


Deleting Elements
-----------------

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`Curve --> Delete...`
   | Hotkey:   :kbd:`X` or :kbd:`Del`


The :guilabel:`Erase` pop-up menu of curves offers you three options:


:guilabel:`Selected`
   This will delete the selected control points, *without* breaking the curve (i.e. the adjacent points will be directly linked, joined, once the intermediary ones are deleted). Remember that NURBS order cannot be higher than its number of control points, so it might decrease when you delete some control point. Of course, when only one point remains, there is no more visible curve, and when all points are deleted, the curve itself is deleted.

:guilabel:`Segment`
   This option is somewhat the opposite to the preceding one, as it will cut the curve, without removing any control points, by erasing one selected segment.
   This option always removes *only one segment* (the last "selected" one), even when several are in the selection. So to delete all segments in your selection, you'll have to repetitively use the same erase option...

:guilabel:`All`
   As with meshes, this deletes everything in the object!


+------------------------------------------------------+-----------------------------------------------------+
+.. figure:: /images/Editing_Curves_delete-selected.jpg|.. figure:: /images/Editing_Curves_delete-segment.jpg+
+   :width: 300px                                      |   :width: 300px                                     +
+   :figwidth: 300px                                   |   :figwidth: 300px                                  +
+                                                      |                                                     +
+   Deleting Curve Selected                            |   Deleting Curve segments                           +
+------------------------------------------------------+-----------------------------------------------------+


Opening and Closing a Curve
---------------------------

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`Curve --> Toggle Cyclic`
   | Hotkey:   :kbd:`Alt-C`


This toggles between an open curve and closed curve (Cyclic).
Only curves with at least one selected control point will be closed/open.
The shape of the closing segment is based on the start and end handles for Bézier curves,
and as usual on adjacent control points for NURBS.
The only time a handle is adjusted after closing is if the handle is an :guilabel:`Auto` one.
(*Open curve*) and (*Closed curve*) is the same Bézier curve open and closed.

This action only works on the original starting control-point or the last control-point added.
Deleting a segment(s) doesn't change how the action applies;
it still operates only on the starting and last control-points. This means that
:kbd:`Alt-C` may actually join two curves instead of closing a single curve! Remember
that when a 2D curve is closed, it creates a renderable flat face.


.. figure:: /images/Editing_Curves_open-closed-cyclic.jpg
   :width: 400px
   :figwidth: 400px

   Open and Closed curves.


Switch Direction
----------------

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`Curve --> Segments --> Switch Direction`, :menuselection:`Specials --> Switch Direction`
   | Hotkey:   :menuselection:`[W] --> [pad2]`


This command will "reverse" the direction of any curve with at least one selected element (i.
e. the start point will become the end one, and *vice versa*).
This is mainly useful when using a curve as path, or using the bevel and taper options.


----


Converting Tools
----------------

Converting Curve Type
~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Panel:    :guilabel:`Curve Tools»Set Spline type`


.. figure:: /images/Editing_Curves_set-spline-type.jpg
   :width: 150px
   :figwidth: 150px

   Set Spline Type button


You can convert splines in a curve object between Bézier, NURBS, and Poly curves.
Press :kbd:`T` to bring up the Toolshelf.
Clicking on the :guilabel:`Set Spline Type` button will allow you to select the Spline type
(Poly, Bézier or NURBS).

Note, this is not a "smart" conversion, i.e. Blender does not try to keep the same shape,
nor the same number of control points. For example, when converting a NURBS to a Bézier,
each group of three NURBS control points become a unique Bézier one
(center point and two handles).


Convert Curve to Mesh
~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object` mode
   | Menu:     :menuselection:`Object --> Convert to`
   | Hotkey:   :kbd:`alt-c`


There is also an "external" conversion, from curve to mesh,
that only works in :guilabel:`Object` mode.
It transforms a :guilabel:`Curve` object in a :guilabel:`Mesh` one,
using the curve resolution to create edges and vertices.
Note that it also keeps the faces and volumes created by closed and extruded curves.


Convert Mesh to Curve
~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Object` mode
   | Menu:     :menuselection:`Object --> Convert to`
   | Hotkey:   :kbd:`alt-c`


Mesh objects that consist of a series of connected vertices can be converted into curve
objects. The resulting curve will be a Poly curve type,
but can be converted to have smooth segments as described above.


Curve Parenting
---------------

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Hotkey:   :kbd:`Ctrl-P`


You can make other selected objects :doc:`children <modeling/objects/groups_and_parenting#parenting_objects>` of one or three control points :kbd:`ctrl-P`, as with mesh objects.

Select either 1 or 3 control points,
then :kbd:`Ctrl-rmb` another object and use :kbd:`Ctrl-P` to make a vertex parent.


Hooks
-----

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`Curve --> control points --> hooks`
   | Hotkey:   :kbd:`Ctrl-H`


:doc:`Hooks <modifiers/deform/hooks>` can be added to control one or more points with other objects.


Set Goal Weight
---------------

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Menu:     :menuselection:`W --> Set Goal Weight`


:guilabel:`Set Goal Weight`
   This sets the "goal weight" of selected control points, which is used when a curve has Soft Body physics, forcing the curve to "stick" to their original positions, based on the weight.

