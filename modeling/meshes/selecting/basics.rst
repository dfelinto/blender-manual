
..    TODO/Review: {{review|im=examples|partial=X|text = expand basic selection tools}} .


Basic Selection
===============

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Hotkey:   :kbd:`rmb` and :kbd:`shift-rmb`


The most common way to select an element is to :kbd:`rmb` on that item;
this will replace the existing selection with the new item.


Adding to a Selection
---------------------

To add to the existing selection, hold down :kbd:`shift` while right clicking.
Clicking again on a selected item will deselect it.

As in :guilabel:`Object` mode, there is a unique *active* element,
displayed in a lighter shade (in general, the last element selected).
Depending on the tools used, this element might be very important!

Note that there is no option to choose what element to select between overlapping ones
(like the :kbd:`alt-rmb` click in :guilabel:`Object` mode). However,
if you are in solid, shaded, or textured viewport shading mode
(not bounding box or wireframe),
you will have a fourth button in the header that looks like a cube,
just right of the select mode ones.

When enabled, this limits your ability to select based on visible elements
(as if the object was solid), and prevents you from accidentally selecting, moving,
deleting or otherwise working on backside or hidden items.


Selecting Elements in a Region
------------------------------

.. admonition:: Reference
   :class: refbox

   | Mode:     :guilabel:`Edit` mode
   | Hotkey:   :kbd:`B`, :kbd:`C`, and :kbd:`ctrl-lmb` click and drag


Region selection allows you to select groups of elements within a 2D region in your 3D view.
The region can be either a circle or rectangle.
The circular region is only available in :guilabel:`Edit mode`. The rectangular region,
or "\ *Border Select* ",
is available in both :guilabel:`Edit mode` and :guilabel:`Object` mode.


.. admonition:: Note
   :class: note

   What is selected using both these tools is affected by the :guilabel:`Limit Selection to visible` feature (available under the 3D viewport) in :guilabel:`Solid Viewport Shading Mode`.

   For example,

   - in solid shading mode and face selection mode, all faces *within* the selection area will be selected;
   - whilst in the wireframe shading mode and face selection mode, only faces whose handle are within the selection area will be selected.


Rectangular region (Border select)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`Border Select` is available in either :guilabel:`Edit mode` or :guilabel:`Object` mode. To activate the tool use the :kbd:`B`. Use :guilabel:`Border Select` to select a group of objects by drawing a rectangle while holding down :kbd:`lmb`. In doing this you will select all objects that lie within or touch this rectangle. If any object that was last active appears in the group it will become selected *and* active.


+-------------------------------------------------------------------------+-------------------------------------------------------------------------+-------------------------------------------------------------------------+
+.. figure:: /images/25-Manual-Modeling-Meshes-Selection-Borderselect1.jpg|.. figure:: /images/25-Manual-Modeling-Meshes-Selection-Borderselect2.jpg|.. figure:: /images/25-Manual-Modeling-Meshes-Selection-Borderselect3.jpg+
+   :width: 200px                                                         |   :width: 200px                                                         |   :width: 200px                                                         +
+   :figwidth: 200px                                                      |   :figwidth: 200px                                                      |   :figwidth: 200px                                                      +
+                                                                         |                                                                         |                                                                         +
+   Start                                                                 |   Selecting                                                             |   Complete                                                              +
+-------------------------------------------------------------------------+-------------------------------------------------------------------------+-------------------------------------------------------------------------+


In (*Start*), :guilabel:`Border Select` has been activated and is indicated by showing a
dotted cross-hair cursor. In (*Selecting*),
the *selection region* is being chosen by drawing a rectangle with the :kbd:`lmb`.
The selection area is only covering the selection handles of three faces. Finally,
by releasing :kbd:`lmb` the selection is complete; see (*Complete*).


.. admonition:: Note
   :class: note

   Border select adds to the previous selection, so in order to select only the contents of the rectangle, deselect all with :kbd:`A` first. In addition, you can use :kbd:`mmb` while you draw the border to deselect all objects within the rectangle.


Circular region
~~~~~~~~~~~~~~~

This selection tool is only available in :guilabel:`Edit mode` and can be activated with
:kbd:`C`.
Once in this mode the cursor changes to a dashed cross-hair with a 2D circle surrounding it.
The tool will operate on whatever the current select mode is.
Clicking or dragging with the :kbd:`lmb`,
causing elements to be inside the circle will cause those elements to be selected.

You can enlarge or shrink the circle region using :kbd:`pad+` and :kbd:`pad-`,
or the :kbd:`wheel`.


+---------------------------------------------------------------------------+---------------------------------------------------------------------------+
+.. figure:: /images/25-Manual-Modeling-Meshes-Selection-Circularselect1.jpg|.. figure:: /images/25-Manual-Modeling-Meshes-Selection-Circularselect2.jpg+
+   :width: 300px                                                           |   :width: 300px                                                           +
+   :figwidth: 300px                                                        |   :figwidth: 300px                                                        +
+                                                                           |                                                                           +
+   Before                                                                  |   After                                                                   +
+---------------------------------------------------------------------------+---------------------------------------------------------------------------+
+Circle Region Select                                                                                                                                   +
+---------------------------------------------------------------------------+---------------------------------------------------------------------------+

(*Circle Region Select*) is an example of selecting edges while in :guilabel:`Edge Select Mode`. As soon as an edge intersects the circle the edge becomes selected. The tool is interactive such that edges are selected while the circle region is being dragged with the :kbd:`lmb`.

If you want to deselect elements,
either hold :kbd:`mmb` or :kbd:`alt-lmb` and begin clicking or dragging again.

For :guilabel:`Faces` select mode,
the circle must intersect the face indicators usually represented by small pixel squares;
one at the center of each face.

To exit from this tool, click :kbd:`rmb`, or hit the :kbd:`Esc` key.


Lasso region
~~~~~~~~~~~~

:guilabel:`Lasso` select is similar to :guilabel:`Border` select in that you select objects based on a region, except :guilabel:`Lasso` is a hand-drawn region that generally forms a circular/round-shaped form; kind of like a lasso.

:guilabel:`Lasso` is available in either :guilabel:`Edit Mode` or :guilabel:`Object Mode`. To activate the tool use the :kbd:`ctrl-lmb` while dragging. The one difference between :guilabel:`Lasso` and :guilabel:`Border` select is that in :guilabel:`Object mode`, :guilabel:`Lasso` only selects objects where the lasso region intersects the objects' center.

To deselect, use :kbd:`ctrl-shift-lmb` while dragging.


+------------------------------------------------------------------------+------------------------------------------------------------------------+------------------------------------------------------------------------+
+.. figure:: /images/25-Manual-Modeling-Meshes-Selection-Lassoselect1.jpg|.. figure:: /images/25-Manual-Modeling-Meshes-Selection-Lassoselect2.jpg|.. figure:: /images/25-Manual-Modeling-Meshes-Selection-Lassoselect3.jpg+
+   :width: 200px                                                        |   :width: 200px                                                        |   :width: 200px                                                        +
+   :figwidth: 200px                                                     |   :figwidth: 200px                                                     |   :figwidth: 200px                                                     +
+                                                                        |                                                                        |                                                                        +
+   Start                                                                |   Selecting                                                            |   Complete                                                             +
+------------------------------------------------------------------------+------------------------------------------------------------------------+------------------------------------------------------------------------+
+Lasso selection                                                                                                                                                                                                           +
+------------------------------------------------------------------------+------------------------------------------------------------------------+------------------------------------------------------------------------+

(*Lasso selection*) is an example of using the :guilabel:`Lasso` select tool in :guilabel:`Vertex Select Mode`.


Additional Selection Tools
--------------------------

The select menu in edit mode contains additional tool for selecting components:

:guilabel:`(De)select All` :kbd:`A`
   Select all or none of the mesh components.
:guilabel:`Invert Selection` :kbd:`ctrl-I`
   Selects all components that are not selected, and deselect currently selected components.
:guilabel:`More` :kbd:`ctrl-num+`
   Propagates selection by adding components that are adjacent to selected elements.
:guilabel:`Less` :kbd:`ctrl-num-`
   Deselects components that form the bounds of the current selection